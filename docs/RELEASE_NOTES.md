# Portfolio redesign — 15 November 2026

## Personal and professional release

The homepage now introduces two distinct perspectives with direct navigation to
`/professional/` and `/personal/`. The professional page keeps the curated work
and experience collection, with clearer engineering positioning and employer
context near the introduction. Existing project URLs remain valid.

The personal page uses owner-supplied interests in travel, video games, AI and
nature filmmaking. Warm editorial typography, original interest illustrations and
a labeled AI landscape create a distinct visual treatment. Quiet view can hide
the landscape's headline; it does not pretend a still image is a playable video.
Each main route has its own canonical URL and social preview. Page-link copying
uses the canonical URL, without query parameters or tracking identifiers.

Release checks: ten generated pages and 179 local references pass the source
validator, including current-route navigation, social images and professional
project backlinks. Browser layout checks at 320, 390, 768, 1024 and 1440 px found
no horizontal overflow or failed images on the three main routes. Quiet-view
toggle and page-link copying worked in the sampled browser. Sampled logs had no
errors. This is focused browser verification, not a full accessibility audit or
proof of audience reach.

The optimized, 197 KB landscape is described in [visual provenance](VISUAL_ASSETS.md).

## Original editorial release

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
