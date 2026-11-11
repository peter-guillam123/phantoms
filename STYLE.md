# How the stories are written

The one place for everything learned about the style of the stories.
Read it before writing or changing a story. Add to it every time Chris
reacts to one, in his words where possible, with the date.

There are two layers, and a story needs both:

1. **General: this file.** What every story of the period does, what the
   magazines' house styles were, and the modern habits to keep out.
2. **Author-specific: the writer's file in `personas/`.** That writer's
   voice rules, plus a "Period notes" section written after reading real
   stories from their own magazines. Tugwell and Trembath have theirs.
   The other eight do not, and must before they write.

The evidence behind the general rules (what was read, the counts, the
gaps) is in `research/period-style.md`.

## Who decides

- Inside a story, the writer and the period decide. Chris's general
  rules for writing (short words, no em dashes, Orwell) do not apply.
  "I don't really want my general md affecting these." (11 Nov 2026)
- "These need to be believable as historical objects." (11 Nov 2026)
- Everything written in the present day still follows his house style:
  biographies, About page, notes, commit messages.

## Before writing

1. Read the writer's file in `personas/` and the comparison in
   `personas/README.md`.
2. Read real stories from the magazine the story is meant to have
   appeared in. `research/period-style.md` says how, and which magazines
   are still unread.
3. Check any fact marked unverified before leaning on it.

## Set it as the magazine would

House style belongs to the magazine, not the writer.

- ***Chambers's Journal*, 1899–1900:** single quotation marks, double
  inside; "Mr", "Mrs", "Dr" with no full point; "gray"; "-ise";
  "to-day", "to-night", "any one", "every one", "for ever";
  "drawing-room", "arm-chair", "cocoa-nut"; but "bedroom", "upstairs",
  "bookcase", "firelight". Long unspaced dashes. Stories signed, 3,200 to
  4,300 words, complete in one number. First word or two in capitals.
- ***Temple Bar*, 1890–91:** double quotation marks; "Mrs." with a point.
- Other magazines: not read yet. Read them first.

## What the prose of the time does

- Sentences are not especially long: the middle one in *Chambers's* is
  13 or 14 words, in *Temple Bar* 18.
- About one semicolon and one dash to every hundred words.
- Feelings are stated. The author may speak to the reader.
- Stories open on scenery or on someone's circumstances, are heavily
  plotted, and close by saying what became of everyone.
- They carry slack: a description of the town, a digression, a foolish
  opinion, a pious remark.

## Tells to keep out

Chris found "The Reader" "a little modern or classic Claude" and
confirmed this list ("that's pretty much the list", 11 Nov 2026).

- **The one-line kicker.** A short paragraph that lands a point and
  stops. Fold it into its neighbour.
- **The aphorism**, as a habit. See below for the exception.
- **Lists of three.**
- **"Not this, but that."**
- **Motifs that all pay off.** Leave some details doing nothing.
- **Unbroken restraint.** Let someone be foolish, sentimental or devout.
- **Modern idiom.** "A kind of statement."

Quick check: no paragraph of narration under nine words.

## What Chris has liked

- The structure and the idea of "The Reader": "well structured and a
  lovely idea." (11 Nov 2026)
- **One good aphorism can stay.** He asked for "a vicarage belongs to
  the vicar" back after the rewrite cut it. My reading: a line like that
  is welcome once, where it is the writer's own subject. It is the habit
  he objects to.
- **The period ending over the modern one.** The rewrite of "The Reader"
  swapped a dry joke of a last line for a reflection on mercy to the
  very old. "Keep the new ending - I like it!" My reading: when the
  period's way and the modern way differ at the close, choose the
  period's, sentiment included.
- He said yes when asked whether narration (first or third person) was
  being thought about. It is fixed per writer: see `CLAUDE.md`.

## Measured so far

| Story | Words | Words per sentence (mean / middle) | Semicolons per 1,000 | Dashes per 1,000 |
|---|---|---|---|---|
| Real: "A Just Sentence", Chambers's, 1900 | 3,202 | 17 / 13 | 8 | 8 |
| Real: "The Chaperon", Chambers's, 1900 | 4,286 | 17 / 14 | 13 | 11 |
| Real: "A New Sensation", Temple Bar, 1891 | 6,179 | 23 / 18 | 12 | 7 |
| "The Reader" (Tugwell), as published | 3,961 | 21 / 16 | 12 | 4 |
| "The Diary at Direction Island" (Trembath) | 3,317 | 22 / 17 | 12 | 4 |

Both of ours are light on dashes. Tugwell's and Trembath's middle
sentences are now nearly the same length, so what separates them is
person, paragraph length and how much speech there is. Watch that the
next writer differs on more than one count.

## What a detector made of them

On 11 November 2026 Chris ran the opening of each published story
through Pangram, a tool that guesses whether text was written by a
machine. It is a smoke alarm, not a judge, and 180 words is a small
sample. The target is still a believable object of 1900, not a score.

- "The Diary at Direction Island" (Trembath): 100% human.
- "The Reader" (Tugwell), the opening as first published, before the
  rewrite: 100% AI. The rewritten opening has not been tested.
- A real passage, the opening of "The Chaperon" by R. Ramsay
  (*Chambers's Journal*, January 1900): 100% human. So the tool does
  recognise the genuine article, at least once.

Chris's view, in his words: "my aim is NOT to explicitly trick Pangram",
and "I don't fully trust Pangram, but I do see it as a positive sign
that a persona combined with attention to historic writing styles might
outfox something like Pangram." He is not concerned about the result for
"The Reader". So: never write to the detector. Note what it says when he
offers it, and no more.

My guesses at why, to be tested and not yet rules:

- Trembath is a plain man giving evidence. He hedges, interrupts himself
  and tacks on afterthoughts ("is thought, I know, to be a poor thing").
  His sentences trail. Tugwell's narrator is poised and ironic, with
  balanced clauses that each close neatly, and that poise is what a
  model produces by default when asked for good prose.
- Every detail in the opening of "The Reader" is well chosen and a
  little funny (the perambulator, the foot-rule). Trembath's opening
  has throat-clearing in it that does no work.
- First person in a working voice may simply be further from a model's
  habits than polished third person.

If these hold, the general lesson is to allow clumsiness: afterthoughts,
hedges, a sentence that says a thing twice. And Tugwell's irony, which
is her whole voice, is the hardest of the ten to make sound unmachined.

One thing the two tests suggest: the story written after reading the
real magazines passed, and the opening written before the rewrite did
not. That is two samples, and proves little, but it points the same way
as everything else in this file.

## Showing and publishing

- A new story is marked `draft: yes` and shown in the private preview.
  It goes public when Chris has read it and said so.
- A change to a published story goes to the preview first too.
