"""Check the generated visitor journey, links, metadata and content boundaries."""
from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import urlsplit, unquote
import json
import re
import xml.etree.ElementTree as ET

ROOT = Path(__file__).resolve().parents[1]
errors = []


class Page(HTMLParser):
    def __init__(self, path):
        super().__init__(convert_charrefs=True)
        self.path = path
        self.ids = set()
        self.refs = []
        self.h1 = 0
        self.canonical = False
        self.description = False
        self.title = False
        self.og = False
        self.active_routes = []

    def handle_starttag(self, tag, attributes):
        attrs = dict(attributes)
        if 'id' in attrs:
            if attrs['id'] in self.ids:
                errors.append(f'{self.path}: duplicate ID {attrs["id"]}')
            self.ids.add(attrs['id'])
        self.h1 += tag == 'h1'
        self.title = self.title or tag == 'title'
        if tag == 'meta':
            self.description = self.description or (attrs.get('name') == 'description' and bool(attrs.get('content')))
            self.og = self.og or attrs.get('property') == 'og:image'
            if attrs.get('property') == 'og:image':
                self.refs.append(attrs.get('content', '').removeprefix('https://sangambaral.com.np'))
        if tag == 'link' and attrs.get('rel') == 'canonical':
            self.canonical = attrs.get('href', '').startswith('https://sangambaral.com.np/')
        if tag == 'img':
            if not attrs.get('alt') or not attrs.get('width') or not attrs.get('height'):
                errors.append(f'{self.path}: image lacks alternative text or dimensions')
        if tag == 'a' and attrs.get('target') == '_blank':
            if 'noopener' not in attrs.get('rel', ''):
                errors.append(f'{self.path}: external window lacks noopener')
        if tag == 'a' and 'route-link' in attrs.get('class', '') and attrs.get('aria-current') == 'page':
            self.active_routes.append(attrs.get('href'))
        for attr in ('src', 'href'):
            if attrs.get(attr):
                self.refs.append(attrs[attr])


catalog = json.loads((ROOT / 'content/projects.json').read_text(encoding='utf-8'))
projects = catalog['projects']
apps = json.loads((ROOT / 'content/apps.json').read_text(encoding='utf-8'))['apps']
assert len(apps) == 6 and len({a['id'] for a in apps}) == len(apps), 'Expected six unique curated apps'
assert sum(a['kind'] == 'live' for a in apps) == 1, 'Unexpected public app status'
for app in apps:
    assert app['projectUrl'].startswith('/projects/'), 'App must lead to a reviewed case study'
    assert (app['kind'] == 'live') == bool(app['launchUrl']), 'Never advertise an unverified public app'
    if app['launchUrl']:
        assert app['launchUrl'] == 'https://walsong-personal-trainer.vercel.app/', 'Public app destination requires review'
assert len(projects) == 7, 'Expected seven curated projects'
assert len({p['id'] for p in projects}) == len(projects), 'Duplicate project IDs'
assert sum(p['featured'] for p in projects) == 4, 'Expected four featured projects'
for project in projects:
    if project['sourceVisibility'] == 'private':
        assert not project['sourceUrl'] and not project['demoUrl'], 'Private project has an unreviewed public destination'
assert (ROOT / 'CNAME').read_text().strip() == 'sangambaral.com.np', 'Custom domain changed'

paths = [ROOT / 'index.html', ROOT / 'professional/index.html', ROOT / 'personal/index.html', ROOT / 'apps/index.html'] + sorted((ROOT / 'projects').glob('*.html'))
assert len(paths) == 11, 'Expected four top-level routes and seven stories'
pages = {}
for path in paths:
    source = path.read_text(encoding='utf-8')
    page = Page(path.relative_to(ROOT))
    page.feed(source)
    pages[path.resolve()] = page
    if page.h1 != 1 or not all([page.title, page.description, page.canonical, page.og]):
        errors.append(f'{page.path}: incomplete headings or discovery metadata')
    expected_route = '/' if path == ROOT / 'index.html' else '/personal/' if path == ROOT / 'personal/index.html' else '/apps/' if path == ROOT / 'apps/index.html' else '/professional/'
    if page.active_routes != [expected_route]:
        errors.append(f'{page.path}: wrong current navigation route')
    if path.parent.name == 'projects' and 'href="/professional/#work"' not in source:
        errors.append(f'{page.path}: project backlink does not lead to professional work')
    if '@@' in source or 'pre-entry' in source or 'cdn.jsdelivr.net/three' in source:
        errors.append(f'{page.path}: unresolved template or legacy entry gate')
    for ld in re.findall(r'<script type="application/ld\+json">(.*?)</script>', source, re.S):
        json.loads(ld)

local_refs = 0
for path, page in pages.items():
    for ref in page.refs:
        parsed = urlsplit(ref)
        if parsed.scheme or parsed.netloc:
            continue
        target = (ROOT / unquote(parsed.path.lstrip('/'))) if parsed.path.startswith('/') else (path.parent / unquote(parsed.path))
        if not parsed.path:
            target = path
        if target.is_dir():
            target = target / 'index.html'
        target = target.resolve()
        local_refs += 1
        if not target.is_relative_to(ROOT):
            errors.append(f'{page.path}: link escapes website root: {ref}')
        elif not target.exists():
            errors.append(f'{page.path}: missing local target: {ref}')
        elif parsed.fragment and target in pages and parsed.fragment not in pages[target].ids:
            errors.append(f'{page.path}: missing fragment: {ref}')

for svg in (ROOT / 'assets').glob('*.svg'):
    ET.parse(svg)
ET.parse(ROOT / 'sitemap.xml')
assert (ROOT / 'assets/social-card.png').read_bytes()[:8] == b'\x89PNG\r\n\x1a\n', 'Missing PNG social card'
if errors:
    raise SystemExit('\n'.join(errors))
print(f'PASS: {len(paths)} pages, {local_refs} local references, 7 curated stories, 6 curated apps, image/SVG metadata and private-project link boundaries.')
