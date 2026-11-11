# Phantoms

Kind: Personal

A compendium of short ghost stories, to be published as a webpage. Each
story is written in the voice of an invented writer of roughly 1880–1925:
the kind of little-known contributor who sent work to magazines and
periodicals, not the famous names. The test is whether a set of personas
can produce styles a reader can tell apart, and stories worth reading.
It may grow into a meta narrative or ARG later. Nothing is decided.

## Where things are

- `personas/` - working briefs, one per invented writer, plus the editor
  (`00-george-ormiston.md`) and `README.md`, which compares them side by
  side. These hold the voice rules and the checks on what is real.
- `research/` - the real history the personas rest on, with sources, and
  a list of gaps.
- `content/` - what readers see: a biography per writer in
  `content/writers/`, the editor, the home page text and the About page.
  Plain text with a short header. Curly quotes are typed in by hand.
- `static/` - the stylesheet, one small script and the fonts.
- `build.py` - turns `content/` into web pages in `_site/` (not kept in
  git). `python3 build.py --serve` builds and serves at localhost:8000.

## The site

- Each biography is written in-world, as a present-day researcher would
  write it. Invented and real are woven together on purpose.
- Honesty lives in three places, and all three stay unless Chris says
  otherwise: the About page says plainly that the writers and the editor
  are invented; every page footer says so in one line; "Further reading"
  links go only to real sources about real things. Never invent an
  archive reference, a shelfmark or a citation.
- Pages carry `noindex` until Chris decides to launch. Nothing is
  deployed yet.
- Each writer has one colour, light and dark, set in the header of their
  content file. Any new colour must pass 4.5:1 contrast on both papers.
- The About page diary is in Chris's voice, newest first. Add an entry
  with each significant change.

## Rules for this project

- The writers are invented. The world around them is real. Every persona
  file ends with a "What is real" list. Keep the two apart: never present
  an invented writer, story or magazine as historical fact in research
  notes, and never invent a quote, figure or source for the real history.
- A persona's voice rules beat the house style inside that persona's
  stories: period spelling, long sentences and dialect are all allowed
  there if the persona would use them. The one exception is the em dash,
  which stays banned in stories too unless Chris lifts it. Everything else
  (notes, About page, UI copy, commit messages) follows Chris's house
  style.
- Before writing a story, read the persona's file in full, and the
  comparison table in `personas/README.md`, so the voice stays distinct
  from the other nine.
- A fact marked "unverified" in `research/` must be checked before a story
  leans on it.
- A story that could be moved from one writer to another is not
  finished. That is George Ormiston's test, and the project's.
