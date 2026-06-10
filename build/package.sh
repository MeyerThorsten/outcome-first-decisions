#!/usr/bin/env bash
# Rebuild outcome-first-decisions.zip deterministically from the working tree.
# Ships only skill content — website, docs, tests, and build tooling stay out.
set -euo pipefail

ROOT="$(cd "$(dirname "$0")/.." && pwd)"
ZIP="$ROOT/outcome-first-decisions.zip"

cd "$ROOT"
rm -f "$ZIP"

zip -q -X -r "$ZIP" \
  SKILL.md README.md LICENSE PROVENANCE.md \
  references templates examples subskills workflows \
  industry-overlays operations outreach decision-journal \
  agents commands \
  -x '*/.DS_Store' -x '.DS_Store'

unzip -l "$ZIP" | tail -1
echo "Built: $ZIP"
