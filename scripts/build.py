"""Generate the static portfolio and original, data-free SVG illustrations."""
from pathlib import Path
import html
import json

ROOT = Path(__file__).resolve().parents[1]
BASE = 'https://sangambaral.com.np'
ASSET_VERSION = '20261118-apps'
PROJECTS = json.loads((ROOT / 'content/projects.json').read_text(encoding='utf-8'))['projects']
STORIES = json.loads((ROOT / 'content/stories.json').read_text(encoding='utf-8'))
PROFILE = json.loads((ROOT / 'content/profile.json').read_text(encoding='utf-8'))
APPS = json.loads((ROOT / 'content/apps.json').read_text(encoding='utf-8'))['apps']


def esc(value):
    return html.escape(str(value), quote=True)


GITHUB = '<svg viewBox="0 0 24 24" fill="currentColor" aria-hidden="true"><path d="M12 .9A11.1 11.1 0 0 0 8.5 22.5c.6.1.8-.2.8-.5v-2.1c-3.4.7-4.1-1.4-4.1-1.4-.5-1.3-1.3-1.6-1.3-1.6-1.1-.8.1-.8.1-.8 1.2.1 1.8 1.2 1.8 1.2 1.1 1.8 2.8 1.3 3.5 1 .1-.8.4-1.3.8-1.6-2.7-.3-5.5-1.4-5.5-6.1 0-1.3.5-2.4 1.2-3.2-.1-.3-.5-1.6.2-3.2 0 0 1-.3 3.3 1.2a11.5 11.5 0 0 1 6 0c2.3-1.5 3.3-1.2 3.3-1.2.7 1.6.3 2.9.2 3.2.8.8 1.2 1.9 1.2 3.2 0 4.7-2.8 5.8-5.5 6.1.4.4.8 1.1.8 2.2V22c0 .3.2.6.8.5A11.1 11.1 0 0 0 12 .9Z"/></svg>'
LINKEDIN = '<svg viewBox="0 0 24 24" fill="currentColor" aria-hidden="true"><path d="M5.3 3a2.2 2.2 0 1 1 0 4.4 2.2 2.2 0 0 1 0-4.4ZM3.5 9h3.6v12H3.5V9Zm5.9 0h3.5v1.6h.1c.5-.9 1.6-1.9 3.4-1.9 3.6 0 4.2 2.3 4.2 5.4V21H17v-6.1c0-1.5 0-3.4-2.1-3.4s-2.4 1.6-2.4 3.3V21H9.4V9Z"/></svg>'


def header(mode='professional'):
    routes = [('/', 'Overview', 'overview'), ('/professional/', 'Professional', 'professional'), ('/personal/', 'Personal', 'personal'), ('/apps/', 'Apps', 'apps')]
    route_links = ''.join(f'<a class="route-link" href="{url}"' + (' aria-current="page"' if mode == key else '') + f'>{label}</a>' for url, label, key in routes)
    return f'''<header class="site-header" id="top"><div class="wrap header-inner">
<a class="brand" href="/" aria-label="Sangam Baral — home"><span class="brand-symbol" aria-hidden="true">SB</span><span>Sangam Baral<span class="sr-only"> — home</span></span></a>
<button class="menu-toggle" type="button" aria-expanded="false" aria-controls="site-navigation" aria-label="Open navigation"><span>MENU</span><span class="menu-icon" aria-hidden="true"></span></button>
<nav class="site-nav" id="site-navigation" aria-label="Main navigation">{route_links}<div class="nav-social"><a href="{PROFILE['linkedin']}" target="_blank" rel="noopener noreferrer" aria-label="LinkedIn (opens in a new tab)">{LINKEDIN}</a><a href="{PROFILE['github']}" target="_blank" rel="noopener noreferrer" aria-label="GitHub (opens in a new tab)">{GITHUB}</a></div><a class="nav-contact" href="#contact">Let's talk <span aria-hidden="true">↗</span></a></nav></div></header>'''


def footer(mode='professional'):
    heading = "Let's build <em>what's next.</em>" if mode == 'professional' else "Good things <em>start here.</em>"
    introduction = "A role, a collaboration, or a problem worth solving. I'd love to hear about it." if mode != 'personal' else "A travel story, a game recommendation or a curious idea. Let's start a conversation."
    return f'''<footer class="contact-section" id="contact"><div class="wrap"><div class="contact-top"><span class="eyebrow">HAVE SOMETHING IN MIND?</span><p>{introduction}</p></div><div class="contact-heading"><h2>{heading}</h2><a class="contact-arrow" href="mailto:{PROFILE['email']}" aria-label="Email Sangam Baral"><span aria-hidden="true">↗</span></a></div><div class="contact-actions"><div><div class="email-group"><a class="email-link" href="mailto:{PROFILE['email']}">{PROFILE['email']}</a><button class="copy-email" type="button" data-enhancement>Copy email <span aria-hidden="true">⧉</span></button></div><p class="copy-status" role="status" aria-live="polite"></p></div><div class="social-links"><a href="{PROFILE['linkedin']}" target="_blank" rel="noopener noreferrer">LinkedIn <span aria-hidden="true">↗</span><span class="sr-only"> (opens in a new tab)</span></a><a href="{PROFILE['github']}" target="_blank" rel="noopener noreferrer">GitHub <span aria-hidden="true">↗</span><span class="sr-only"> (opens in a new tab)</span></a><button type="button" class="share-page" data-enhancement>Copy page link <span aria-hidden="true">↗</span></button></div></div><p class="share-status mono" role="status" aria-live="polite"></p><div class="footer-bottom"><span class="mono">© 2026 SANGAM BARAL</span><div class="mono"><i class="status-dot" aria-hidden="true"></i> KATHMANDU, NEPAL <span data-local-time>UTC +05:45</span></div><a href="#top" class="mono">BACK TO TOP <span aria-hidden="true">↑</span></a></div></div></footer>'''


def head(title, description, path='/', social_image='social-card.png'):
    structured = {'@context': 'https://schema.org', '@type': 'Person', 'name': PROFILE['name'], 'jobTitle': PROFILE['role'], 'url': BASE + '/', 'sameAs': [PROFILE['linkedin'], PROFILE['github']]}
    theme = '#f4eee5' if path == '/personal/' else '#f6f5f0'
    return f'''<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{esc(title)}</title>
<meta name="description" content="{esc(description)}">
<meta name="theme-color" content="{theme}">
<meta name="color-scheme" content="light">
<link rel="canonical" href="{BASE}{path}">
<link rel="icon" href="/assets/favicon.svg" type="image/svg+xml">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=DM+Sans:wght@400;450;500;550;600;650;700&amp;family=IBM+Plex+Mono:wght@400;500&amp;display=swap">
<link rel="stylesheet" href="/assets/styles.css?v={ASSET_VERSION}">
<link rel="stylesheet" href="/assets/worlds.css?v={ASSET_VERSION}">
<link rel="stylesheet" href="/assets/apps.css?v={ASSET_VERSION}">
<meta property="og:type" content="website">
<meta property="og:site_name" content="Sangam Baral">
<meta property="og:title" content="{esc(title)}">
<meta property="og:description" content="{esc(description)}">
<meta property="og:url" content="{BASE}{path}">
<meta property="og:image" content="{BASE}/assets/{social_image}?v={ASSET_VERSION}">
<meta property="og:image:width" content="1200">
<meta property="og:image:height" content="630">
<meta property="og:image:alt" content="{esc(title)}">
<meta name="twitter:card" content="summary_large_image">
<meta name="twitter:title" content="{esc(title)}">
<meta name="twitter:description" content="{esc(description)}">
<meta name="twitter:image" content="{BASE}/assets/{social_image}?v={ASSET_VERSION}">
<script type="application/ld+json">{json.dumps(structured, ensure_ascii=False)}</script>'''


def render(template, values):
    result = template
    for key, value in values.items():
        result = result.replace(f'@@{key}@@', str(value))
    if '@@' in result:
        raise ValueError('Unresolved template variable')
    return result


def svg_canvas(content, background='#e8edf9', definitions=''):
    return f'''<svg xmlns="http://www.w3.org/2000/svg" width="1000" height="650" viewBox="0 0 1000 650"><defs><filter id="shadow" x="-40%" y="-40%" width="180%" height="190%"><feDropShadow dx="0" dy="18" stdDeviation="22" flood-color="#172b43" flood-opacity=".13"/></filter>{definitions}</defs><rect width="1000" height="650" fill="{background}"/>{content}</svg>'''


def svg_text(x, y, text, size=12, color='#17251f', extra=''):
    return f'<text x="{x}" y="{y}" font-family="Arial,sans-serif" font-size="{size}" fill="{color}" {extra}>{esc(text)}</text>'


def make_system():
    def cube(x, y, w, height, top, left, right, lines=False):
        shape = f'<polygon points="{x},{y} {x+w},{y+w*.5} {x},{y+w} {x-w},{y+w*.5}" fill="{top}" stroke="#8293b3" stroke-width=".6"/><polygon points="{x-w},{y+w*.5} {x},{y+w} {x},{y+w+height} {x-w},{y+w*.5+height}" fill="{left}" stroke="#8293b3" stroke-width=".6"/><polygon points="{x},{y+w} {x+w},{y+w*.5} {x+w},{y+w*.5+height} {x},{y+w+height}" fill="{right}" stroke="#8293b3" stroke-width=".6"/>'
        if lines:
            for i in range(1, 6):
                yy = y + w + height * i / 7
                shape += f'<path d="M {x+8} {yy} l {w-16} {-w*.5+8}" stroke="#9cb7ff" stroke-width=".8" opacity=".5"/>'
        return shape
    grid = ''.join(f'<path d="M {80+i*33} 470 l 240 -140 M {80+i*33} 470 l 240 140"/>' for i in range(11))
    parts = f'<g stroke="#ccd3c5" stroke-width=".65" opacity=".7">{grid}</g>'
    parts += '<ellipse cx="352" cy="470" rx="165" ry="49" fill="#526644" opacity=".08" filter="url(#soft)"/>'
    parts += '<g fill="none" stroke="#abb6a2" stroke-width=".8"><ellipse cx="344" cy="345" rx="245" ry="172" transform="rotate(-25 344 345)"/><path d="M102 367V235l94-54M535 443V288l-82-48" stroke-dasharray="3 5"/><path d="M145 433l195 110 183-105"/></g>'
    parts += cube(341, 420, 180, 18, '#e9ede4', '#cbd3c0', '#dfe6d5')
    parts += cube(409, 290, 78, 91, '#ffffff', '#dbe3f0', '#edf0f6')
    parts += cube(278, 226, 91, 156, 'url(#blueTop)', '#2449cb', '#163899', True)
    parts += cube(192, 342, 59, 69, '#fffefa', '#d8decf', '#ecede5')
    parts += '<path d="M279 382v83l-87-51M409 382v43l-68 40" stroke="#7c9de7" stroke-width="1" fill="none"/>'
    parts += cube(290, 130, 53, 58, '#7896f5', '#4269db', '#3058c9', True)
    parts += '<g fill="none" stroke="#6889dc" stroke-width="1"><path d="M290 241v-22" stroke-dasharray="2 4"/><path d="M278 226l91 45v156M409 290v-37h96"/><path d="M192 342v-35h-59"/><circle cx="505" cy="253" r="3" fill="#254bd8"/><circle cx="133" cy="307" r="3" fill="#254bd8"/></g>'
    parts += svg_text(109, 293, '01 / THE PROBLEM', 8, '#536555', 'letter-spacing="1"')
    parts += svg_text(462, 236, '02 / THE SYSTEM', 8, '#536555', 'letter-spacing="1"')
    parts += svg_text(315, 568, '03 / SOMETHING USEFUL', 8, '#536555', 'letter-spacing="1"')
    parts += '<g fill="#254bd8"><circle cx="112" cy="432" r="3"/><circle cx="538" cy="360" r="3"/><path d="M458 150v15m-7.5-7.5h15" stroke="#254bd8"/></g><g fill="none" stroke="#9aa99b" stroke-width=".8"><circle cx="344" cy="345" r="267" stroke-dasharray="1 9" opacity=".4"/><path d="M310 80h45M332 58v45" opacity=".6"/></g>'
    return f'<svg xmlns="http://www.w3.org/2000/svg" width="680" height="660" viewBox="0 0 680 660"><defs><linearGradient id="blueTop" x2="1" y2="1"><stop stop-color="#6f91ec"/><stop offset="1" stop-color="#3158d6"/></linearGradient><filter id="soft"><feGaussianBlur stdDeviation="12"/></filter></defs>{parts}</svg>'


def make_covers():
    assets = ROOT / 'assets'
    # All charts, numbers and routes below are deliberately illustrative.
    p = '<circle cx="800" cy="100" r="260" fill="#254bd8" opacity=".055"/><g filter="url(#shadow)"><rect x="165" y="125" width="670" height="405" rx="10" fill="#f8fafc"/><rect x="165" y="125" width="670" height="46" rx="10" fill="#152c40"/><rect x="165" y="155" width="670" height="16" fill="#152c40"/>'
    p += svg_text(191, 154, 'P / PowerVeyra', 13, '#fff', 'font-weight="bold"') + svg_text(699, 153, 'REPORT REVIEW', 8, '#b8cee2', 'letter-spacing="1"')
    p += svg_text(194, 207, 'From records to a clearer picture.', 20, '#172e42', 'font-weight="bold"')
    p += '<rect x="191" y="230" width="180" height="72" rx="4" fill="#e6edf5"/><rect x="387" y="230" width="197" height="72" rx="4" fill="#edf1ea"/><rect x="600" y="230" width="207" height="72" rx="4" fill="#e6edf5"/>'
    for x, title, value in [(207, '01 / IMPORT', 'Retain the source'), (403, '02 / REVIEW', 'Make quality visible'), (616, '03 / EXPLORE', 'Connect the readings')]:
        p += svg_text(x, 251, title, 8, '#597087', 'letter-spacing="1"') + svg_text(x, 280, value, 12, '#213a4d')
    p += svg_text(200, 337, 'ILLUSTRATIVE TREND', 8, '#597087', 'letter-spacing="1"')
    p += ''.join(f'<path d="M199 {y}H799" stroke="#e1e7ed"/>' for y in [360, 393, 426, 459])
    p += '<path d="M200 443C240 451 250 390 290 405S350 445 392 393 440 410 480 373 530 385 565 355 610 392 650 350 710 377 750 330 780 351 800 328V473H200Z" fill="#3266cf" opacity=".09"/><path d="M200 443C240 451 250 390 290 405S350 445 392 393 440 410 480 373 530 385 565 355 610 392 650 350 710 377 750 330 780 351 800 328" fill="none" stroke="#3266cf" stroke-width="3"/><circle cx="650" cy="350" r="5" fill="#3266cf" stroke="white" stroke-width="3"/>'
    p += svg_text(200, 505, 'SOURCE → CHECK → UNDERSTAND', 8, '#597087', 'letter-spacing="1.3"') + '</g>'
    p += svg_text(500, 587, 'CONCEPT ILLUSTRATION · NO OPERATIONAL DATA', 8, '#586f87', 'text-anchor="middle" letter-spacing="1.2"')
    (assets / 'powerveyra.svg').write_text(svg_canvas(p, '#e2eafa'), encoding='utf-8')

    f = '<circle cx="500" cy="325" r="222" fill="none" stroke="#bec9ae"/><circle cx="500" cy="325" r="266" fill="none" stroke="#cbd4bd" stroke-dasharray="2 8"/><g transform="rotate(-9 402 323)" filter="url(#shadow)"><rect x="298" y="99" width="214" height="428" rx="31" fill="#1b2d23"/><rect x="306" y="107" width="198" height="412" rx="25" fill="#f4f5eb"/><rect x="370" y="116" width="68" height="16" rx="8" fill="#1b2d23"/>'
    f += svg_text(326, 162, 'W / WALSONG FIT', 9, '#254333', 'font-weight="bold"') + svg_text(326, 205, 'Your pace.', 28, '#1b2d23', 'font-weight="bold"') + svg_text(326, 236, 'Your progress.', 23, '#1b2d23')
    f += '<rect x="324" y="260" width="162" height="108" rx="9" fill="#d4e4bd"/><path d="M348 317h18l8-27 15 49 12-35 9 13h50" fill="none" stroke="#365c37" stroke-width="2"/>' + svg_text(338, 353, 'ONE DAY AT A TIME', 8, '#365c37')
    for y, label in [(399, 'Training'), (442, 'Nutrition'), (485, 'Recovery')]:
        f += f'<path d="M327 {y+11}H484" stroke="#d3d9ca"/>' + svg_text(329, y, label, 11, '#254333') + svg_text(469, y, '+', 15, '#254333')
    f += '</g><g transform="rotate(10 600 360)" filter="url(#shadow)"><rect x="518" y="218" width="202" height="280" rx="17" fill="#294635"/>' + svg_text(541, 255, 'SMALL STEPS.', 9, '#cce1bb', 'letter-spacing="1.3"') + svg_text(541, 285, 'Lasting habits.', 22, '#f2f5e8')
    f += '<circle cx="619" cy="370" r="57" fill="none" stroke="#48624b" stroke-width="11"/><path d="M619 313a57 57 0 1 1-54 75" fill="none" stroke="#d2e9a9" stroke-width="11" stroke-linecap="round"/>' + svg_text(619, 377, 'MOVE', 13, '#f2f5e8', 'text-anchor="middle" letter-spacing="2"') + svg_text(542, 465, 'TRAIN / FUEL / RECOVER', 8, '#cce1bb', 'letter-spacing=".5"') + '</g>'
    f += svg_text(500, 587, 'CONCEPT ILLUSTRATION · NOT PERSONAL HEALTH RECORDS', 8, '#52674b', 'text-anchor="middle" letter-spacing="1"')
    (assets / 'walsong-fit.svg').write_text(svg_canvas(f, '#dfe7d1'), encoding='utf-8')

    b = '<g stroke="#d6bea8" fill="none" opacity=".7">' + ''.join(f'<path d="M{x} 0V650M0 {x}H1000"/>' for x in range(0, 1001, 60)) + '</g><path d="M0 475Q180 275 330 400T650 290T1000 235V650H0Z" fill="#d8c5ad"/><path d="M0 565Q140 350 350 480T660 420T1000 330V650H0Z" fill="#bfbaa0"/>'
    b += '<g filter="url(#shadow)"><rect x="195" y="123" width="610" height="397" rx="8" fill="#f8f3e9"/><path d="M195 315L350 188l90 94 85-116 126 162 70-63 84 86v169H195Z" fill="#e7e4d3"/><path d="M195 396l120-74 103 53 147-83 95 114 145-64v178H195Z" fill="#c9d5bf"/><path d="M195 481l131-64 149 46 118-59 212 77v39H195Z" fill="#8ca48a"/>'
    b += svg_text(224, 158, 'B / BATOLEKHA', 12, '#2b4432', 'font-weight="bold"') + svg_text(224, 204, 'Begin with a little curiosity.', 22, '#2b4432', 'font-weight="bold"')
    b += '<path d="M342 455Q315 390 413 395T523 326T652 309" fill="none" stroke="#fdf8ea" stroke-width="3" stroke-dasharray="5 7"/><circle cx="342" cy="455" r="7" fill="#fdf8ea"/><circle cx="652" cy="309" r="7" fill="#fdf8ea"/><rect x="567" y="370" width="196" height="99" rx="5" fill="#fdfaf3"/>' + svg_text(583, 394, 'EXPLORE / PLAN / PREPARE', 7, '#64785f', 'letter-spacing=".8"') + svg_text(583, 422, 'A journey worth', 16, '#2b4432') + svg_text(583, 445, 'understanding.', 16, '#2b4432') + '</g>'
    b += svg_text(500, 587, 'CONCEPT ILLUSTRATION · NOT A NAVIGATION MAP', 8, '#725e48', 'text-anchor="middle" letter-spacing="1.2"')
    (assets / 'batolekha.svg').write_text(svg_canvas(b, '#e7d5c2'), encoding='utf-8')

    a = '<circle cx="500" cy="325" r="245" fill="none" stroke="#c9c6df"/><g filter="url(#shadow)" transform="rotate(-7 500 325)"><rect x="216" y="132" width="568" height="386" rx="10" fill="#fbfaff"/>' + svg_text(247, 174, 'A / AbroadMitra', 13, '#39316b', 'font-weight="bold"') + svg_text(247, 218, 'A world of possibilities.', 25, '#39316b', 'font-weight="bold"')
    a += '<rect x="247" y="244" width="506" height="39" rx="5" fill="#eceaf6"/><circle cx="266" cy="262" r="6" fill="none" stroke="#8b83ad"/><path d="M270 267l5 5" stroke="#8b83ad"/>' + svg_text(292, 268, 'Find the direction that fits you', 10, '#696086')
    for x, label, sub in [(247, 'DISCOVER', 'Explore options'), (422, 'COMPARE', 'See the context'), (597, 'DECIDE', 'Know the reasons')]:
        a += f'<rect x="{x}" y="305" width="156" height="170" rx="5" fill="#f1eff8"/><circle cx="{x+78}" cy="355" r="24" fill="#d9d3ee"/><path d="M{x+61} 360h34M{x+65} 360v-14l13-9 13 9v14M{x+73} 360v-12h10v12" fill="none" stroke="#67579f" stroke-width="1.6"/>' + svg_text(x+78, 412, label, 9, '#554786', 'text-anchor="middle" letter-spacing="1"') + svg_text(x+78, 443, sub, 9, '#696086', 'text-anchor="middle"')
    a += '</g>' + svg_text(500, 587, 'CONCEPT ILLUSTRATION · DISCOVERY, NOT ADMISSION PREDICTION', 8, '#696086', 'text-anchor="middle" letter-spacing=".9"')
    (assets / 'abroadmitra.svg').write_text(svg_canvas(a, '#e5e1f2'), encoding='utf-8')

    for identifier, color, accent, word, labels in [
        ('nepalkhata', '#e4e9df', '#345344', 'Every item. Every invoice.', ['INVENTORY', 'BILLING', 'INSIGHT']),
        ('jwelflow', '#eee4cf', '#78623a', 'Made for the details.', ['WEIGHT', 'CRAFT', 'VALUE']),
        ('documind', '#dce8e9', '#2d6369', 'Ask. Retrieve. Understand.', ['DOCUMENT', 'CONTEXT', 'ANSWER'])
    ]:
        s = '<g filter="url(#shadow)"><rect x="205" y="142" width="590" height="368" rx="8" fill="#fcfcf7"/>' + svg_text(240, 192, next(p['name'] for p in PROJECTS if p['id'] == identifier), 17, accent, 'font-weight="bold"') + svg_text(240, 247, word, 30, accent, 'font-weight="bold"')
        for i, label in enumerate(labels):
            x = 240+i*180
            s += f'<rect x="{x}" y="282" width="160" height="174" rx="4" fill="{color}"/><circle cx="{x+80}" cy="340" r="28" fill="none" stroke="{accent}" opacity=".5"/><path d="M{x+67} 340h26M{x+80} 327v26" stroke="{accent}" stroke-width="1.5"/>' + svg_text(x+80, 405, label, 9, accent, 'text-anchor="middle" letter-spacing="1.2"')
        s += '</g>' + svg_text(500, 587, 'CONCEPT ILLUSTRATION · NO CUSTOMER OR DOCUMENT DATA', 8, accent, 'text-anchor="middle" letter-spacing="1.1"')
        (assets / f'{identifier}.svg').write_text(svg_canvas(s, color), encoding='utf-8')



def app_cards():
    cards = []
    for p in APPS:
        featured = ' is-featured' if p['kind'] == 'live' else ''
        launch = (f'<a class="app-launch" href="{esc(p["launchUrl"])}" target="_blank" rel="noopener noreferrer">Open app <span aria-hidden="true">↗</span><span class="sr-only"> (opens in a new tab)</span></a>' if p['launchUrl'] else '')
        cards.append(f'''<article class="app-tile{featured}" data-app-category="{esc(p['category'])}">
<div class="app-tile-visual"><img src="/assets/{esc(p['image'])}" width="1000" height="650" alt="Original concept illustration for {esc(p['name'])}; not a product screenshot." loading="lazy"></div>
<div class="app-tile-copy"><div class="app-tile-top"><span class="eyebrow">{esc(p['eyebrow'])}</span><span class="app-status">{esc(p['status'])}</span></div>
<h3>{esc(p['name'])}</h3><p class="app-tile-summary">{esc(p['summary'])}</p><p class="app-tile-note">{esc(p['note'])}</p>
<div class="app-tile-actions">{launch}<a href="/apps/{esc(p['id'])}/">View details <span aria-hidden="true">↗</span></a></div></div></article>''')
    return '\n'.join(cards)


def build():
    (ROOT / 'assets').mkdir(exist_ok=True)
    (ROOT / 'projects').mkdir(exist_ok=True)
    (ROOT / 'professional').mkdir(exist_ok=True)
    (ROOT / 'personal').mkdir(exist_ok=True)
    (ROOT / 'apps').mkdir(exist_ok=True)
    (ROOT / 'assets/system.svg').write_text(make_system(), encoding='utf-8')
    make_covers()
    (ROOT / 'assets/favicon.svg').write_text('<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 64 64"><rect width="64" height="64" rx="8" fill="#18211e"/><text x="8" y="43" fill="#f6f5f0" font-family="Arial,sans-serif" font-size="34" font-weight="bold" letter-spacing="-4">SB</text><circle cx="54" cy="10" r="7" fill="#6282ef"/></svg>', encoding='utf-8')
    featured = []
    more = []
    for index, p in enumerate(PROJECTS):
        s = STORIES[p['id']]
        url = f'/projects/{p["id"]}.html'
        if p['featured']:
            tags = ''.join(f'<span>{esc(t)}</span>' for t in p['stack'])
            featured.append(f'''<article class="project-card" data-project-group="{s['group']}"><a class="project-cover" href="{url}" aria-label="Explore {esc(p['name'])}"><img src="/assets/{p['id']}.svg" width="1000" height="650" alt="Concept illustration for {esc(p['name'])}; not a product screenshot." loading="lazy"><span class="cover-label">{index+1:02d} / {esc(p['category']).upper()}</span></a><div class="project-info"><div class="project-title-row"><h3><a href="{url}">{esc(p['name'])}</a></h3><span class="project-status">{esc(p['status'])}</span></div><p>{esc(p['summary'])}</p><div class="project-tags">{tags}</div><a class="text-link project-small-link" href="{url}">Explore project <span aria-hidden="true">↗</span><span class="sr-only">: {esc(p['name'])}</span></a></div></article>''')
        else:
            more.append(f'''<a class="project-row" data-project-group="{s['group']}" href="{url}"><span class="row-number mono">{index+1:02d}</span><h4>{esc(p['name'])}</h4><span class="row-summary">{esc(p['summary'])}</span><span class="row-stack">{' / '.join(esc(t) for t in p['stack'][:3])}<br>{esc(p['status'])}</span><span class="row-arrow" aria-hidden="true">↗</span></a>''')
    experience = []
    for index, item in enumerate(PROFILE['experience']):
        experience.append(f'''<article class="experience-item"><span class="mono">{esc(item['period'])}</span><details{' open' if index == 0 else ''}><summary><div><h3>{esc(item['role'])}</h3><p class="company">{esc(item['company'])} · {esc(item['location'])}</p></div></summary><p>{esc(item['description'])}</p></details></article>''')
    template = (ROOT / 'templates/professional.html').read_text(encoding='utf-8')
    professional = render(template, {'HEAD': head('Sangam Baral — Software & Product Engineer', 'Good ideas. Built properly. Explore Sangam Baral’s engineering experience, selected software projects and work in automation, business products and AI.', '/professional/', 'professional-social.png'), 'HEADER': header('professional'), 'FOOTER': footer('professional'), 'FEATURED': '\n'.join(featured), 'MORE': '\n'.join(more), 'EXPERIENCE': '\n'.join(experience)})
    (ROOT / 'professional/index.html').write_text(professional, encoding='utf-8')
    template = (ROOT / 'templates/overview.html').read_text(encoding='utf-8')
    overview = render(template, {'HEAD': head('Sangam Baral — Engineer, Builder & Curious Human', 'Meet Sangam Baral, a software and product engineer from Nepal. Explore his professional work and his personal interests in travel, gaming, AI and nature filmmaking.'), 'HEADER': header('overview'), 'FOOTER': footer('overview')})
    (ROOT / 'index.html').write_text(overview, encoding='utf-8')
    template = (ROOT / 'templates/personal.html').read_text(encoding='utf-8')
    personal = render(template, {'HEAD': head('Sangam Baral — Curious, by Nature', 'The personal side of Sangam Baral: travel, video games, exploring AI and technology, and capturing the natural world through a lens.', '/personal/', 'personal-social.png'), 'HEADER': header('personal'), 'FOOTER': footer('personal')})
    (ROOT / 'personal/index.html').write_text(personal, encoding='utf-8')
    template = (ROOT / 'templates/apps.html').read_text(encoding='utf-8')
    apps_page = render(template, {'HEAD': head('Apps & Tools — Sangam Baral', 'Explore Walsong Fit and an evolving collection of thoughtfully built apps, experiments and products by Sangam Baral.', '/apps/'), 'HEADER': header('apps'), 'FOOTER': footer(), 'APP_CARDS': app_cards()})
    (ROOT / 'apps/index.html').write_text(apps_page, encoding='utf-8')
    template = (ROOT / 'templates/app.html').read_text(encoding='utf-8')
    for app in APPS:
        slug = app['id']
        (ROOT / 'apps' / slug).mkdir(parents=True, exist_ok=True)
        launch_action = (f'<a class="button button-dark" href="{esc(app["launchUrl"])}" target="_blank" rel="noopener noreferrer">Open application <span aria-hidden="true">↗</span><span class="sr-only"> (opens in a new tab)</span></a>' if app['launchUrl'] else '')
        values = {'HEAD': head(f'{app["name"]} — Apps — Sangam Baral', app['summary'], f'/apps/{slug}/'), 'HEADER': header('apps'), 'FOOTER': footer(), 'ID': esc(slug), 'EYEBROW': esc(app['eyebrow']), 'NAME': esc(app['name']), 'STATUS': esc(app['status']), 'SUMMARY': esc(app['summary']), 'NOTE': esc(app['note']), 'IMAGE': esc(app['image']), 'PROJECT_URL': esc(app['projectUrl']), 'LAUNCH_ACTION': launch_action}
        (ROOT / 'apps' / slug / 'index.html').write_text(render(template, values), encoding='utf-8')
    template = (ROOT / 'templates/project.html').read_text(encoding='utf-8')
    for i, p in enumerate(PROJECTS):
        s = STORIES[p['id']]
        source_action = f'<a class="button button-dark" href="{esc(p["sourceUrl"])}" target="_blank" rel="noopener noreferrer">View source on GitHub <span aria-hidden="true">↗</span><span class="sr-only"> (opens in a new tab)</span></a>' if p['sourceUrl'] else f'<a class="button button-dark" href="mailto:{PROFILE["email"]}?subject=Let%27s%20talk%20about%20{p["id"]}">Discuss this project <span aria-hidden="true">↗</span></a>'
        values = {key.upper(): esc(value) for key, value in s.items() if isinstance(value, str)}
        next_project = PROJECTS[(i+1) % len(PROJECTS)]
        values.update({'HEAD': head(f'{p["name"]} — Sangam Baral', p['summary'], f'/projects/{p["id"]}.html'), 'HEADER': header(), 'FOOTER': footer(), 'ID': p['id'], 'NAME': esc(p['name']), 'CATEGORY': esc(p['category']), 'STATUS': esc(p['status']), 'STACK': ' / '.join(esc(t) for t in p['stack']), 'SOURCE_ACTION': source_action, 'ILLUSTRATION_ALT': esc(f'Original concept illustration for {p["name"]}; no real customer or internal records.'), 'DETAILS': ''.join(f'<li>{esc(t)}</li>' for t in s['details']), 'NEXT_ID': next_project['id'], 'NEXT_NAME': esc(next_project['name'])})
        (ROOT / f'projects/{p["id"]}.html').write_text(render(template, values), encoding='utf-8')
    urls = [BASE + '/', BASE + '/professional/', BASE + '/personal/', BASE + '/apps/'] + [f'{BASE}/apps/{app["id"]}/' for app in APPS] + [f'{BASE}/projects/{p["id"]}.html' for p in PROJECTS]
    sitemap = '<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n' + '\n'.join(f'  <url><loc>{url}</loc><lastmod>2026-11-18</lastmod></url>' for url in urls) + '\n</urlset>\n'
    (ROOT / 'sitemap.xml').write_text(sitemap, encoding='utf-8')
    print(f'Built overview, professional, personal and apps routes, {len(PROJECTS)} project pages and sitemap.')


if __name__ == '__main__':
    build()
