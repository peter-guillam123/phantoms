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
- `STYLE.md` - how the stories are written: the period's habits, the
  magazine house styles, the modern tells to keep out, and what Chris has
  said he likes. Read it before touching a story. Add to it whenever he
  reacts to one.
- `research/` - the real history the personas rest on, with sources, and
  a list of gaps.
- `content/` - what readers see: a biography per writer in
  `content/writers/`, the editor, the home page text and the About page.
  Plain text with a short header. Curly quotes are typed in by hand.
- `content/stories/` - the stories. One marked `draft: yes` appears only
  in the private preview, never on the public site. Remove that line to
  publish it, and only when Chris has read it and said so.
- `images/PROMPTS.md` - a prompt for each picture named in a biography's
  caption, for an AI image maker. No pictures are on the site yet.
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
- The site is public at https://peter-guillam123.github.io/phantoms/.
  Anything merged to `main` is built and published by
  `.github/workflows/pages.yml`.
- Chris views the site through a private preview page on claude.ai:
  https://claude.ai/artifact/URcMQYgf26vUQDk712TmPx. After a change he
  should see, run `python3 build.py --artifact` and republish
  `_artifact/index.html` with the other twelve pages to that address.
- Each writer has one colour, light and dark, set in the header of their
  content file. Any new colour must pass 4.5:1 contrast on both papers.
- The About page diary is in Chris's voice, newest first. Add an entry
  with each significant change.

## Rules for this project

- The writers are invented. The world around them is real. Every persona
  file ends with a "What is real" list. Keep the two apart: never present
  an invented writer, story or magazine as historical fact in research
  notes, and never invent a quote, figure or source for the real history.
- Chris's general instructions on writing (Orwell's rules, British house
  style, no em dashes) do not apply to the stories, or to lines quoted
  from them. He said so on 11 November 2026. Inside a story the only
  authorities are the writer's brief and the practice of the time and the
  magazine. Em dashes, long sentences, semicolons, dialect, sentiment and
  stated feelings are all in. The house style still governs everything
  written in the present day: the biographies, the About page, notes and
  commit messages.
- A story must be believable as an object of its time. Before writing
  one, read real stories from the magazine it is meant to have appeared
  in (see `research/period-style.md` for how, and what is still unread),
  set it in that magazine's house style, and check it against the
  measurements in that file.
- Chris finds some story prose "a little modern or classic Claude". The
  habits he means, and the things he has said he likes, are in
  `STYLE.md`. Check every story against it before showing it to him.
- A change to a story that is already public is shown to Chris in the
  preview first, and merged only when he says so.
- Narration is fixed per writer and is part of what tells them apart:
  first person for Lovegrove, Charlton, Tobin, Trembath and Staniforth
  (a newspaper man talking straight to the reader); close third for
  Tugwell, Protheroe and Gadd; a teller with listeners for Kenworthy; a file of documents for
  Dalgleish. Do not change it without saying so.
- Before writing a story, read the persona's file in full, and the
  comparison table in `personas/README.md`, so the voice stays distinct
  from the other nine.
- A fact marked "unverified" in `research/` must be checked before a story
  leans on it.
- A story that could be moved from one writer to another is not
  finished. That is George Ormiston's test, and the project's.
