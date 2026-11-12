#!/usr/bin/env python3
"""Build the Phantoms site.

Reads the text in content/ and writes finished pages to _site/.
No dependencies beyond Python 3.

    python3 build.py             build once
    python3 build.py --serve     build, then serve at http://localhost:8000
    python3 build.py --artifact  build a self-contained copy in _artifact/
                                 for a private preview page on claude.ai
"""
import html
import re
import shutil
import sys
from pathlib import Path

ROOT = Path(__file__).parent
CONTENT = ROOT / "content"
STATIC = ROOT / "static"
OUT = ROOT / "_site"

SITE_TITLE = "Phantoms"
SITE_TAGLINE = "Ghost stories by ten forgotten writers, 1880–1925"


# ---------------------------------------------------------------- content

def read_page(path):
    """Split a content file into its header fields and its body text."""
    text = path.read_text(encoding="utf-8")
    meta, body = {}, text
    if text.startswith("---\n"):
        head, body = text[4:].split("\n---\n", 1)
        for line in head.splitlines():
            if not line.strip() or line.startswith("#"):
                continue
            key, _, value = line.partition(":")
            meta[key.strip()] = value.strip()
    return meta, body.strip()


def inline(text):
    """Turn *italic*, **bold** and [links](url) into HTML."""
    text = html.escape(text, quote=False)
    text = re.sub(r"\[([^\]]+)\]\(([^)]+)\)", r'<a href="\2">\1</a>', text)
    text = re.sub(r"\*\*([^*]+)\*\*", r"<strong>\1</strong>", text)
    text = re.sub(r"\*([^*]+)\*", r"<em>\1</em>", text)
    return text


def slugify(text):
    return re.sub(r"[^a-z0-9]+", "-", text.lower()).strip("-")


def markdown(body):
    """A small Markdown reader: headings, paragraphs, lists, tables of
    two or more columns, and quoted extracts with a caption."""
    out, blocks = [], re.split(r"\n\s*\n", body)
    first_para_done = False
    for block in blocks:
        lines = block.strip().splitlines()
        if not lines:
            continue
        first = lines[0]
        if block.strip() == "* * *":
            out.append('<p class="break" role="separator" aria-label="Break">* &nbsp; * &nbsp; *</p>')
            first_para_done = True
        elif first.startswith("## "):
            title = first[3:].strip()
            out.append(f'<h2 id="{slugify(title)}">{inline(title)}</h2>')
            # A heading may be followed directly by a paragraph.
            rest = " ".join(l.strip() for l in lines[1:])
            if rest:
                out.append(f"<p>{inline(rest)}</p>")
        elif first.startswith("> "):
            quote = [l[2:] for l in lines if l.startswith("> ")]
            caption = [l[2:] for l in lines if l.startswith("^ ")]
            fig = ['<figure class="extract">', "<blockquote>"]
            fig.append(f"<p>{inline(' '.join(quote))}</p>")
            fig.append("</blockquote>")
            if caption:
                fig.append(f"<figcaption>{inline(' '.join(caption))}</figcaption>")
            fig.append("</figure>")
            out.append("\n".join(fig))
        elif first.startswith("- "):
            items, current = [], ""
            for l in lines:
                if l.startswith("- "):
                    if current:
                        items.append(current)
                    current = l[2:].strip()
                else:
                    current += " " + l.strip()
            items.append(current)
            lis = "\n".join(f"<li>{inline(i)}</li>" for i in items)
            out.append(f"<ul>\n{lis}\n</ul>")
        elif first.startswith("| "):
            rows = [[c.strip() for c in l.strip().strip("|").split("|")] for l in lines]
            rows = [r for r in rows if not set("".join(r)) <= set("-: ")]
            head, rest = rows[0], rows[1:]
            th = "".join(f'<th scope="col">{inline(c)}</th>' for c in head)
            trs = "\n".join(
                "<tr>" + "".join(f"<td>{inline(c)}</td>" for c in r) + "</tr>"
                for r in rest
            )
            out.append(
                '<div class="table-wrap" tabindex="0" role="region" '
                'aria-label="Table">'
                f"<table><thead><tr>{th}</tr></thead>\n<tbody>\n{trs}\n</tbody></table></div>"
            )
        else:
            text = " ".join(l.strip() for l in lines)
            cls = "" if first_para_done else ' class="opening"'
            first_para_done = True
            out.append(f"<p{cls}>{inline(text)}</p>")
    return "\n".join(out)


# -------------------------------------------------------------- templates

def layout(title, body, root, description, page_class="", style=""):
    full_title = SITE_TITLE if title == SITE_TITLE else f"{title} · {SITE_TITLE}"
    return f"""<!doctype html>
<html lang="en-GB">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{html.escape(full_title)}</title>
<meta name="description" content="{html.escape(description)}">
<meta name="color-scheme" content="light dark">
<link rel="preload" href="{root}static/fonts/libre-caslon-text-latin-400-normal.woff2" as="font" type="font/woff2" crossorigin>
<link rel="preload" href="{root}static/fonts/libre-caslon-display-latin-400-normal.woff2" as="font" type="font/woff2" crossorigin>
<link rel="stylesheet" href="{root}static/style.css">
<link rel="icon" href="{root}static/favicon.svg" type="image/svg+xml">
</head>
<body class="{page_class}"{style}>
<a class="skip" href="#main">Skip to the text</a>
<header class="masthead">
  <a class="masthead-name" href="{root}">Phantoms</a>
  <nav aria-label="Main">
    <ul>
      <li><a href="{root}#writers">The writers</a></li>
      <li><a href="{root}editor/">The editor</a></li>
      <li><a href="{root}about/">About</a></li>
    </ul>
  </nav>
</header>
<main id="main">
{body}
</main>
<footer class="colophon">
  <p>The writers on these pages are invented. The history around them is
  real. <a href="{root}about/">About this project</a>.</p>
</footer>
<script src="{root}static/site.js" defer></script>
</body>
</html>
"""


PLATE = """<figure class="plate">
  <svg viewBox="0 0 200 250" role="img" aria-label="An empty oval portrait frame">
    <rect class="plate-card" x="1" y="1" width="198" height="248" rx="3"/>
    <rect class="plate-line" x="12" y="12" width="176" height="226" rx="1"/>
    <ellipse class="plate-well" cx="100" cy="116" rx="62" ry="80"/>
    <ellipse class="plate-mist" cx="100" cy="124" rx="40" ry="54"/>
    <ellipse class="plate-rim" cx="100" cy="116" rx="62" ry="80"/>
  </svg>
  <figcaption>{caption}</figcaption>
</figure>"""


def picture(meta, root):
    """The picture for a biography. Returns two pieces: one to sit above
    the text (a wide picture) and one for the side column (a tall picture,
    or the empty oval frame when there is no picture yet)."""
    caption = inline(meta["plate"])
    if not meta.get("image"):
        return "", PLATE.format(caption=caption)
    src = f'{root}static/images/{meta["image"]}'
    w, h = meta.get("image_size", "1400x933").split("x")
    img = (
        f'<a href="{src}" aria-label="Open the picture at full size">'
        f'<img src="{src}" width="{w}" height="{h}" loading="lazy" decoding="async" '
        f'alt="{html.escape(meta.get("image_alt", ""))}"></a>'
    )
    if int(w) >= int(h):
        return f'<figure class="photo photo-wide">{img}<figcaption>{caption}</figcaption></figure>', ""
    return "", f'<figure class="photo photo-tall">{img}<figcaption>{caption}</figcaption></figure>'


def facts_list(meta, keys):
    rows = []
    for label, key in keys:
        if meta.get(key):
            rows.append(f"<div><dt>{label}</dt><dd>{inline(meta[key])}</dd></div>")
    return '<dl class="facts">\n' + "\n".join(rows) + "\n</dl>"


FACT_KEYS = [
    ("Born", "born"), ("Died", "died"), ("Work", "work"),
    ("Wrote", "wrote"), ("Signed", "signed"), ("Published in", "sold"),
]


def accent_style(meta):
    if not meta.get("accent"):
        return ""
    return f' style="--accent:{meta["accent"]};--accent-night:{meta["accent_night"]}"'


def writer_page(meta, body, prev, nxt, stories=()):
    n = int(meta["order"])
    numerals = ["I", "II", "III", "IV", "V", "VI", "VII", "VIII", "IX", "X"]
    ghost = (
        '<p class="creed"><span class="creed-lead">A ghost is</span> '
        f'{inline(meta["theme"])}.</p>'
    )
    content = markdown(body)
    # Put the big theme line under the "What a ghost was" heading.
    content = re.sub(
        r'(<h2 id="what-a-ghost-was-to-(?:him|her)">.*?</h2>)',
        r"\1\n" + ghost.replace("\\", r"\\"),
        content, count=1,
    )

    def pager(w, label, cls):
        if not w:
            return f'<span class="{cls}"></span>'
        return (
            f'<a class="{cls}" href="../{w["slug"]}/">'
            f'<span class="pager-label">{label}</span>'
            f'<span class="pager-name">{html.escape(w["name"])}</span></a>'
        )

    if stories:
        block = '<h2 id="read">Read</h2>\n' + story_links(stories, "../../")
        content = content.replace('<h2 id="further-reading">', block + '\n<h2 id="further-reading">')

    wide, side_pic = picture(meta, "../../")
    return f"""<article class="entry">
  <header class="entry-head">
    <p class="eyebrow"><a href="../../#writers">The writers</a> <span aria-hidden="true">·</span> No. {numerals[n-1]} of ten</p>
    <h1>{html.escape(meta["name"])}</h1>
    <p class="dates">{meta["dates"]} <span aria-hidden="true">·</span> {inline(meta["trade"])}, {inline(meta["place"])}</p>
    <p class="standfirst">{inline(meta["summary"])}</p>
  </header>
  {wide}
  <div class="entry-body">
    <aside class="entry-side{' entry-side-plain' if wide else ''}" aria-label="At a glance">
      {side_pic}
      {facts_list(meta, FACT_KEYS)}
    </aside>
    <div class="prose">
{content}
    </div>
  </div>
  <nav class="pager" aria-label="More writers">
    {pager(prev, "Previous", "pager-prev")}
    {pager(nxt, "Next", "pager-next")}
  </nav>
</article>"""


def story_page(meta, body, author):
    content = markdown(body)
    # Set the first word or two in capitals, as the magazines did.
    content = re.sub(
        r'<p class="opening">([A-Z][A-Z’\' ]+)\b',
        lambda m: f'<p class="opening"><span class="lead-in">{m.group(1).title()}</span>',
        content, count=1,
    )
    draft = '<p class="draft-flag">Preview. Not yet published.</p>' if meta.get("draft") else ""
    return f"""<article class="story">
  <header class="story-head">
    {draft}
    <p class="eyebrow"><a href="../../#writers">The writers</a> <span aria-hidden="true">·</span> {inline(meta["venue"])}, {meta["year"]}</p>
    <h1>{html.escape(meta["title"])}</h1>
    <p class="byline">{inline(meta["byline"])}</p>
  </header>
  <div class="prose story-text">
{content}
  </div>
  <footer class="story-foot">
    <p>{inline(meta["note"])}</p>
    <p>“{html.escape(meta["byline"].replace("By ", ""))}” was <a href="../../writers/{author["slug"]}/">{html.escape(author["name"])}</a> ({author["dates"]}).</p>
  </footer>
</article>"""


def story_links(stories, prefix):
    items = []
    for st in stories:
        flag = ' <span class="draft-flag">Preview</span>' if st.get("draft") else ""
        items.append(
            f'<li><a href="{prefix}stories/{st["slug"]}/">{html.escape(st["title"])}</a>'
            f' <span class="row-meta">{inline(st["venue"])}, {st["year"]}</span>{flag}</li>'
        )
    return '<ul class="story-list">\n' + "\n".join(items) + "\n</ul>"


def simple_page(meta, body, side=""):
    eyebrow = f'<p class="eyebrow">{inline(meta["eyebrow"])}</p>' if meta.get("eyebrow") else ""
    dates = f'<p class="dates">{inline(meta["dates"])}</p>' if meta.get("dates") else ""
    return f"""<article class="entry">
  <header class="entry-head">
    {eyebrow}
    <h1>{html.escape(meta["title"])}</h1>
    {dates}
    <p class="standfirst">{inline(meta["summary"])}</p>
  </header>
  <div class="entry-body{'' if side else ' entry-body-single'}">
    {side}
    <div class="prose">
{markdown(body)}
    </div>
  </div>
</article>"""


def faint(meta, slug):
    """The pale copy of a picture that sits behind a row on the home page.
    It is decoration, so it has no description and is hidden from screen
    readers. A drawing is marked, because in the dark it is shown as a
    negative: otherwise its white paper would glare."""
    if not (STATIC / "images" / "faint" / f"{slug}.webp").exists():
        return ""
    kind = " is-drawing" if meta.get("image_kind") == "drawing" else ""
    return (f'<img class="row-faint{kind}" src="static/images/faint/{slug}.webp" alt="" '
            f'aria-hidden="true" loading="lazy" decoding="async">')


def index_page(meta, body, writers, editor, stories=()):
    phrases = "\n".join(
        f'      <li data-by="{html.escape(w["name"])}, {html.escape(w["trade"].lower())}" '
        f'data-accent="{w["accent"]}" data-accent-night="{w["accent_night"]}" '
        f'data-faint="static/images/faint/{w["slug"]}.webp" data-kind="{w.get("image_kind", "photograph")}">'
        f'{inline(w["theme"])}</li>'
        for w in writers
    )
    first = writers[0]
    rows = [f"""    <li class="row row-editor" style="--accent:{editor['accent']};--accent-night:{editor['accent_night']}">
      {faint(editor, 'george-ormiston')}
      <span class="row-no" aria-hidden="true">Ed.</span>
      <div class="row-who">
        <h3><a href="editor/">{html.escape(editor['title'])}</a></h3>
        <p class="row-meta">{inline(editor['dates']).replace(" · ", "<br>")}</p>
      </div>
      <div class="row-ghost">
        <p class="row-theme"><span class="creed-lead">{inline(editor['creed_lead'])}</span> {inline(editor['creed'])}</p>
        <p class="row-nuance">{inline(editor['teaser'])}</p>
      </div>
    </li>"""]
    numerals = ["I", "II", "III", "IV", "V", "VI", "VII", "VIII", "IX", "X"]
    for w in writers:
        n = int(w["order"])
        mine = [st for st in stories if st["author"] == w["slug"]]
        links = ""
        if mine:
            label = "The story" if len(mine) == 1 else "The stories"
            items = "".join(
                f'<li><a href="stories/{st["slug"]}/"><span class="row-story-title">{html.escape(st["title"])}</span> '
                f'<span class="row-story-where">{inline(st["venue"])}, {st["year"]}</span></a>'
                + (' <span class="draft-flag">Preview</span>' if st.get("draft") else "")
                + "</li>"
                for st in mine
            )
            links = f"""
        <div class="row-stories">
          <p class="creed-lead">{label}</p>
          <ul>{items}</ul>
        </div>"""
        rows.append(f"""    <li class="row" style="--accent:{w['accent']};--accent-night:{w['accent_night']}">
      {faint(w, w['slug'])}
      <span class="row-no" aria-hidden="true">{numerals[n-1]}</span>
      <div class="row-who">
        <h3><a href="writers/{w['slug']}/">{html.escape(w['name'])}</a></h3>
        <p class="row-meta">{w['dates']}<br>{inline(w['trade'])}, {inline(w['place'])}</p>
      </div>
      <div class="row-ghost">
        <p class="row-theme"><span class="creed-lead">A ghost is</span> {inline(w['theme'])}.</p>
        <p class="row-nuance">{inline(w['nuance'])}</p>{links}
      </div>
    </li>""")
    return f"""<section class="hero" aria-labelledby="hero-title">
  <div class="hero-faint" data-turn-faint aria-hidden="true">
    <img src="static/images/faint/{first['slug']}.webp" alt="" class="is-shown{' is-drawing' if first.get('image_kind') == 'drawing' else ''}" decoding="async">
    <img alt="" decoding="async">
  </div>
  <p class="eyebrow">{SITE_TAGLINE}</p>
  <h1 id="hero-title">Phantoms</h1>
  <div class="turn" data-turn style="--accent:{first['accent']};--accent-night:{first['accent_night']}">
    <p class="turn-line" aria-hidden="true">
      <span class="turn-lead">A ghost is</span>
      <span class="turn-phrase" data-turn-phrase>{inline(first['theme'])}</span><span class="turn-stop">.</span>
    </p>
    <p class="turn-by" aria-hidden="true" data-turn-by>{html.escape(first['name'])}, {html.escape(first['trade'].lower())}</p>
    <ul class="turn-source" hidden>
{phrases}
    </ul>
    <p class="visually-hidden">Each of the ten writers had a different idea of what a ghost is. All ten are listed below.</p>
    <button class="turn-toggle" type="button" data-turn-toggle hidden aria-pressed="false">Pause</button>
  </div>
</section>
<section class="intro prose">
{markdown(body)}
</section>
<section class="writers" id="writers" aria-labelledby="writers-title">
  <h2 id="writers-title">The editor and the ten</h2>
  <ol class="rows">
{chr(10).join(rows)}
  </ol>
</section>"""


# ------------------------------------------------------------------ build

ARTIFACT = "--artifact" in sys.argv
GOOGLE_FONTS = (
    '<link rel="stylesheet" href="https://fonts.googleapis.com/css2?'
    "family=Libre+Caslon+Display&family=Libre+Caslon+Text:ital,wght@0,400;0,700;1,400"
    '&display=swap">'
)


def for_artifact(page, is_main):
    """The preview host has stricter rules than a normal web server: styles
    and scripts must sit inside each page, fonts come from Google, and
    links must name the file. The main page is given without its outer
    shell, which the host adds."""
    css = (STATIC / "style.css").read_text(encoding="utf-8")
    css = re.sub(r"@font-face\s*\{.*?\}\s*", "", css, flags=re.S)
    js = (STATIC / "site.js").read_text(encoding="utf-8")
    page = re.sub(r'<link rel="(?:preload|icon)"[^>]*>\n', "", page)
    page = re.sub(r'<meta name="robots"[^>]*>\n', "", page)
    page = re.sub(
        r'<link rel="stylesheet" href="[^"]*static/style.css">',
        lambda m: GOOGLE_FONTS + "\n<style>\n" + css + "</style>", page,
    )
    page = re.sub(
        r'<script src="[^"]*static/site.js" defer></script>',
        lambda m: "<script>\n" + js + "</script>", page,
    )

    def name_the_file(m):
        path, anchor = m.group(1), m.group(2) or ""
        if path == "" or path.endswith("/"):
            path += "index.html"
        return f'href="{path}{anchor}"'

    page = re.sub(r'href="(?!https?:|#)([^"#]*)(#[^"]*)?"', name_the_file, page)
    if is_main:
        title = re.search(r"<title>.*?</title>", page).group(0)
        head = re.search(r"(<link rel=\"stylesheet\".*?</style>)", page, flags=re.S).group(1)
        body = re.search(r"<body[^>]*>(.*)</body>", page, flags=re.S).group(1)
        page = f"{title}\n{head}\n{body}"
    return page


def write(path, text):
    if ARTIFACT:
        text = for_artifact(text, path == OUT / "index.html")
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(text, encoding="utf-8")


def build():
    global OUT
    if ARTIFACT:
        OUT = ROOT / "_artifact"
    if OUT.exists():
        shutil.rmtree(OUT)
    OUT.mkdir()
    if not ARTIFACT:
        shutil.copytree(STATIC, OUT / "static")
        (OUT / ".nojekyll").write_text("")
    elif (STATIC / "images").exists():
        shutil.copytree(STATIC / "images", OUT / "static" / "images")

    writers = []
    for path in sorted((CONTENT / "writers").glob("*.md")):
        meta, body = read_page(path)
        meta["body"] = body
        writers.append(meta)
    writers.sort(key=lambda w: int(w["order"]))

    # A story marked "draft: yes" is left out of the public site and shown
    # only in the private preview.
    stories = []
    for path in sorted((CONTENT / "stories").glob("*.md")):
        meta, body = read_page(path)
        if meta.get("draft") and not ARTIFACT:
            continue
        meta["body"] = body
        stories.append(meta)
    stories.sort(key=lambda st: int(st["order"]))
    by_slug = {w["slug"]: w for w in writers}
    for st in stories:
        author = by_slug[st["author"]]
        write(OUT / "stories" / st["slug"] / "index.html", layout(
            st["title"], story_page(st, st["body"], author), "../../",
            f'{st["title"]}, a ghost story. {st["summary"]}',
            "page-story", accent_style(author),
        ))

    for i, w in enumerate(writers):
        prev = writers[i - 1] if i > 0 else None
        nxt = writers[i + 1] if i < len(writers) - 1 else None
        page = layout(
            w["name"],
            writer_page(w, w["body"], prev, nxt, [st for st in stories if st["author"] == w["slug"]]),
            "../../",
            f'{w["name"]} ({w["dates"]}): {w["summary"]}',
            "page-writer", accent_style(w),
        )
        write(OUT / "writers" / w["slug"] / "index.html", page)

    editor, editor_body = read_page(CONTENT / "editor.md")
    side = (
        '<aside class="entry-side" aria-label="At a glance">'
        + picture(editor, "../")[1]
        + facts_list(editor, [("Born", "born"), ("Died", "died"), ("Work", "work"), ("Wrote", "wrote")])
        + "</aside>"
    )
    write(OUT / "editor" / "index.html", layout(
        editor["title"], simple_page(editor, editor_body, side), "../",
        editor["summary"], "page-writer", accent_style(editor),
    ))

    about, about_body = read_page(CONTENT / "about.md")
    write(OUT / "about" / "index.html", layout(
        about["title"], simple_page(about, about_body), "../",
        about["summary"], "page-about",
    ))

    home, home_body = read_page(CONTENT / "index.md")
    write(OUT / "index.html", layout(
        SITE_TITLE, index_page(home, home_body, writers, editor, stories), "",
        home["summary"], "page-home",
    ))
    print(f"Built {len(writers) + len(stories) + 3} pages in {OUT}")


if __name__ == "__main__":
    build()
    if "--serve" in sys.argv:
        import functools
        import http.server
        handler = functools.partial(http.server.SimpleHTTPRequestHandler, directory=str(OUT))
        print("Serving at http://localhost:8000 (Ctrl-C to stop)")
        http.server.ThreadingHTTPServer(("", 8000), handler).serve_forever()
