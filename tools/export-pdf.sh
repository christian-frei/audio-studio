#!/usr/bin/env bash
# Render studio-signal-chain.drawio to a single-page A3 PDF.
# No drawio CLI needed — drawio2html.py rasterises the pages to HTML and Chrome prints them.
set -euo pipefail
cd "$(dirname "$0")/.."
SRC=studio-signal-chain.drawio
OUT=studio-signal-chain.pdf
TMP=$(mktemp -d)
trap 'rm -rf "$TMP"' EXIT
CHROME="/Applications/Google Chrome.app/Contents/MacOS/Google Chrome"
[ -x "$CHROME" ] || { echo "Google Chrome not found at $CHROME" >&2; exit 1; }
python3 tools/drawio2html.py "$SRC" "$TMP/chain.html"
"$CHROME" --headless --disable-gpu --no-sandbox --no-pdf-header-footer \
          --print-to-pdf="$TMP/chain.pdf" "file://$TMP/chain.html" 2>/dev/null
cp "$TMP/chain.pdf" "$OUT"
echo "wrote $OUT (A3 portrait, both pages on one sheet)"
