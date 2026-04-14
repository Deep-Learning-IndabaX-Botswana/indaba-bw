"""
freeze.py — Build a static version of the site for GitHub Pages.

Usage:
    python freeze.py

Output goes to the  docs/  folder.
Enable GitHub Pages in your repo settings:
    Settings → Pages → Source: Deploy from branch → main / docs
"""

import os
from flask_frozen import Freezer
from app import app

# ── Output directory ────────────────────────────────────────────────────────
app.config['FREEZER_DESTINATION']       = 'docs'
app.config['FREEZER_RELATIVE_URLS']     = True   # works on any GitHub Pages base URL
app.config['FREEZER_REMOVE_EXTRA_FILES'] = False  # keep existing files (images, etc.)

freezer = Freezer(app)

if __name__ == '__main__':
    freezer.freeze()
    # GitHub Pages ignores folders starting with _ unless a .nojekyll file exists
    nojekyll = os.path.join('docs', '.nojekyll')
    if not os.path.exists(nojekyll):
        open(nojekyll, 'w').close()
    print("✅  Site frozen to /docs — ready for GitHub Pages.")
    print("    Commit and push, then enable Pages from  main / docs  in repo settings.")
