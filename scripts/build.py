"""Rebuild public/index.html from design/portfolio.dc.html.

The shipped bundle = design/bundle-base.html (loader + inlined React, support.js
and fonts) with its __bundler/template swapped for the current source.
Usage:  python -I scripts/build.py
"""
import json, re, pathlib

root = pathlib.Path(__file__).resolve().parent.parent
base = (root / 'design/bundle-base.html').read_text(encoding='utf8')
src = (root / 'design/portfolio.dc.html').read_text(encoding='utf8')
fonts = (root / 'design/fonts.css').read_text(encoding='utf8')

RUNTIME_UUID = 'd9993dcc-72d7-4b38-bd3a-d192dbb52b5c'  # support.js in the manifest
tpl = src.replace('<script src="./support.js"></script>', f'<script src="{RUNTIME_UUID}"></script>')
# Google Fonts <link> -> the fonts already embedded in the bundle
tpl, n = re.subn(r'<link rel="stylesheet" href="https://fonts\.googleapis\.com[^>]*>', lambda m: f'<style>{fonts}</style>', tpl)
assert n == 1 and RUNTIME_UUID in tpl, 'source markers not found'

enc = json.dumps(tpl, ensure_ascii=False).replace('</script', '<' + chr(92) + 'u002Fscript')
out, k = re.subn(r'(<script type="__bundler/template">).*?(</script>)', lambda m: m.group(1) + enc + m.group(2), base, count=1, flags=re.S)
assert k == 1
(root / 'public/index.html').write_text(out, encoding='utf8', newline='\n')
print('built public/index.html', len(out), 'bytes')
