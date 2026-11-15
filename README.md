# Sangam Baral — portfolio

A responsive, static portfolio published on GitHub Pages at
[sangambaral.com.np](https://sangambaral.com.np/).

## Edit and preview

Requires Python 3.12+; no package installation or application backend is needed.

```sh
python scripts/build.py
python scripts/check.py
python -m http.server 4173 --bind 127.0.0.1
```

Open `http://127.0.0.1:4173`.

- `content/profile.json`: profile, professional links and experience.
- `content/projects.json`: curated selection, project order, stacks and source links.
- `content/stories.json`: case-study copy and implementation boundaries.
- `templates/`: homepage and project-page HTML templates.
- `assets/`: CSS, progressive JavaScript enhancements and original SVG illustrations.
- `scripts/build.py`: generates `index.html`, project pages, sitemap and illustrations.
- `scripts/check.py`: verifies content, generated pages, local links and privacy boundaries.

Run the build after content/template changes and commit the generated files with
the source. Root `index.html` is the GitHub Pages entry point. Preserve `CNAME`.
The three PNG sharing cards can be regenerated on Windows with
`powershell -File scripts/social-previews.ps1`.

The homepage introduces both sides of Sangam. `/professional/` contains selected
work, engineering experience and approach; `/personal/` presents owner-supplied
interests in travel, gaming, AI and nature filmmaking. Cross-page navigation uses
real directory routes compatible with GitHub Pages. Existing project URLs remain
available, with backlinks leading to the professional collection.

Project visuals are original **concept illustrations**, not product screenshots.
They contain no customer, traveler, health or plant records. Private projects have
no repository or internal demo links. Do not automatically publish private GitHub
activity or treat planned capabilities as released features.

Public GitHub metadata can inform future editorial updates, but project summaries
remain curated. Add a public demo or resume action only when its destination has
been verified. Review current employment and project statuses when updating content.
