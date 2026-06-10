#!/usr/bin/env python3
"""Structural validation for the outcome-first-decisions skill package.

Run from anywhere: python3 tests/validate_package.py
Exits 0 when every invariant holds; prints each failure with the offending file.
Stdlib only — no dependencies.
"""

import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
FAILURES: list[str] = []


def fail(msg: str) -> None:
    FAILURES.append(msg)


def check(cond: bool, msg: str) -> None:
    if not cond:
        fail(msg)


def read(rel: str) -> str:
    return (ROOT / rel).read_text(encoding="utf-8")


# ---------------------------------------------------------------- frontmatter
def check_frontmatter() -> None:
    text = read("SKILL.md")
    m = re.match(r"\A---\n(.*?)\n---\n", text, re.DOTALL)
    check(bool(m), "SKILL.md: missing YAML frontmatter block")
    if m:
        fm = m.group(1)
        for field in ("name:", "description:"):
            check(field in fm, f"SKILL.md frontmatter: missing `{field}` field")


# ------------------------------------------------- referenced paths must exist
def check_referenced_paths() -> None:
    """Every backtick path in SKILL.md and README.md must exist on disk."""
    for rel in ("SKILL.md", "README.md"):
        text = read(rel)
        for ref in re.findall(r"`([\w./-]+(?:\.md|\.yaml|/))`", text):
            check((ROOT / ref).exists(), f"{rel}: referenced path does not exist: {ref}")


def check_readme_file_structure() -> None:
    """Paths drawn in the README file-structure tree must exist."""
    text = read("README.md")
    m = re.search(r"```text\noutcome-first-decisions/\n(.*?)```", text, re.DOTALL)
    check(bool(m), "README.md: file-structure block not found")
    if not m:
        return
    stack: list[str] = []
    for line in m.group(1).splitlines():
        entry = re.match(r"^([│ ]*)(?:├──|└──)\s+(\S+)", line)
        if not entry:
            continue
        depth = len(entry.group(1)) // 4
        name = entry.group(2)
        stack = stack[:depth]
        path = "/".join(stack + [name])
        if name.endswith("/"):
            stack = stack[:depth] + [name.rstrip("/")]
            check((ROOT / path).is_dir(), f"README.md tree: missing directory {path}")
        else:
            check((ROOT / path).is_file(), f"README.md tree: missing file {path}")


# ----------------------------------------------------------- overlay structure
OVERLAY_SECTIONS = [
    "## Unit of Value",
    "## Most-Believed-But-Wrong Narrative",
    "## Buyer-Behavior Signals (rung 6+)",
    "## Hardest-to-Fake Proof Test",
    "Anti-Patterns",          # heading text varies: "Common X Anti-Patterns to Watch"
    "Scoreboard Defaults",    # heading text varies: "Scoreboard Defaults for X Users"
]


def check_overlays() -> None:
    overlays = sorted((ROOT / "industry-overlays").glob("*.md"))
    check(len(overlays) > 0, "industry-overlays/: no overlay files found")
    for f in overlays:
        if f.name == "overlay-builder.md":
            continue
        text = f.read_text(encoding="utf-8")
        for section in OVERLAY_SECTIONS:
            check(
                section in text,
                f"industry-overlays/{f.name}: missing required section: {section}",
            )
        # every overlay must anchor at least one rung-6+ signal block
        check(
            "rung 6+" in text,
            f"industry-overlays/{f.name}: no rung-6+ evidence anchoring",
        )


# ------------------------------------------------------- slash-command parity
DOC_PAGES = [
    "README.md",
    "website/skills/outcome-first-decisions.md",
    "website/skills/outcome-first-decisions.html",
]


def command_stems() -> set[str]:
    return {f.stem for f in (ROOT / "commands").glob("*.md")}


def check_commands_mentioned() -> None:
    stems = command_stems()
    check(len(stems) > 0, "commands/: no command files found")
    for page in DOC_PAGES:
        text = read(page)
        for stem in stems:
            check(
                f"/{stem}" in text,
                f"{page}: does not mention slash command /{stem}",
            )


# ---------------------------------------------------------------- count claims
def h2_count(rel: str) -> int:
    return len(re.findall(r"^## ", read(rel), re.MULTILINE))


def claimed_counts(text: str) -> dict[str, int]:
    """Extract 'N <thing>' claims from a marketing page."""
    claims = {}
    patterns = {
        "core frameworks": r"(\d+)\s+core frameworks",
        "supporting frameworks": r"(\d+)\s+supporting frameworks",
        "anti-patterns": r"(\d+)\s+named anti-patterns",
        "principles": r"(\d+)\s+principles",
        "mental models": r"(\d+)\s+mental models",
        "industry overlays": r"(\d+)\s+industry overlays",
        "subskills": r"(\d+)\s+nested subskills",
        "slash commands": r"(\d+)\s+Claude Code slash commands",
    }
    for key, pat in patterns.items():
        m = re.search(pat, text)
        if m:
            claims[key] = int(m.group(1))
    return claims


def actual_counts() -> dict[str, int]:
    overlays = [
        f for f in (ROOT / "industry-overlays").glob("*.md")
        if f.name != "overlay-builder.md"
    ]
    return {
        "core frameworks": h2_count("references/frameworks-core.md"),
        "supporting frameworks": h2_count("references/frameworks-extended.md"),
        "anti-patterns": h2_count("references/anti-patterns.md"),
        "principles": h2_count("references/principles.md"),
        "mental models": h2_count("references/mental-models.md"),
        "industry overlays": len(overlays),
        "subskills": len(list((ROOT / "subskills").glob("*/SKILL.md"))),
        "slash commands": len(command_stems()),
    }


def check_marketing_counts() -> None:
    actual = actual_counts()
    for page in (
        "website/skills/outcome-first-decisions.md",
        "website/skills/outcome-first-decisions.html",
    ):
        claims = claimed_counts(read(page))
        check(len(claims) >= 5, f"{page}: expected count claims not found (page format changed?)")
        for key, claimed in claims.items():
            check(
                claimed == actual[key],
                f"{page}: claims {claimed} {key}, package has {actual[key]}",
            )


# ----------------------------------------------------- md/html marketing sync
def check_md_html_sync() -> None:
    md = read("website/skills/outcome-first-decisions.md")
    html = read("website/skills/outcome-first-decisions.html")
    md_claims = claimed_counts(md)
    html_claims = claimed_counts(html)
    for key in set(md_claims) | set(html_claims):
        check(
            md_claims.get(key) == html_claims.get(key),
            f"website pages out of sync on '{key}': md={md_claims.get(key)} html={html_claims.get(key)}",
        )
    for stem in command_stems():
        check(
            (f"/{stem}" in md) == (f"/{stem}" in html),
            f"website pages out of sync on command /{stem}",
        )


# ------------------------------------------------------------- relative links
def check_relative_links() -> None:
    for f in ROOT.rglob("*.md"):
        if any(part in (".git", "node_modules", "docs") for part in f.parts):
            continue
        text = f.read_text(encoding="utf-8")
        for target in re.findall(r"\[[^\]]*\]\(([^)#\s]+)\)", text):
            if target.startswith(("http://", "https://", "mailto:")):
                continue
            resolved = (f.parent / target).resolve()
            check(
                resolved.exists(),
                f"{f.relative_to(ROOT)}: broken relative link: {target}",
            )


# ------------------------------------------------------------------------ main
def main() -> int:
    check_frontmatter()
    check_referenced_paths()
    check_readme_file_structure()
    check_overlays()
    check_commands_mentioned()
    check_marketing_counts()
    check_md_html_sync()
    check_relative_links()

    if FAILURES:
        print(f"FAIL — {len(FAILURES)} problem(s):\n")
        for msg in FAILURES:
            print(f"  ✗ {msg}")
        return 1
    print("OK — all structural invariants hold.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
