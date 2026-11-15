# Portfolio redesign — 15 November 2026

The portfolio now presents Sangam Baral through a bright editorial homepage,
original system illustrations, four featured projects, three shorter project
entries and seven dedicated project stories. LinkedIn, GitHub and email are
available throughout. Project status and implementation boundaries remain explicit.

The static site uses no application backend, tracking scripts or browser-stored
credentials. Public-source links are provided only for public repositories.
Project illustrations use no operational or personal data. Internal research
notes are excluded from Git.

## Validation before release

- Generated all eight pages from curated JSON and HTML templates.
- Validated 124 local asset/page/fragment references, metadata, image dimensions,
  SVG/XML structure and private-project link boundaries.
- Checked JavaScript syntax with Node.
- Measured the homepage at 320, 390, 768, 1024 and 1440 px: no horizontal overflow.
- Measured each of the seven project pages at 390 and 1440 px: no horizontal overflow
  or failed images in the sampled state.
- Tested project filters and mobile menu open/close with Escape focus restoration.
- Inspected desktop and mobile screenshots; sampled browser logs contained no errors.

This is focused browser/source validation, not a full assistive-technology audit
or a field Core Web Vitals assessment. Real device review and approved product
screenshots can inform future refinements.
