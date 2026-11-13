# Prompts for the biography pictures

One prompt for each picture named in a biography's caption, written for
ChatGPT's image maker. Each is complete on its own: paste it as it is.

The idea to protect: no picture gives a writer a clear face. They are
hidden, or turned away, or missing, or one small figure among many. If a
result gives one figure pride of place, ask for it again.

Each caption gets there by a different road. Chris said on 12 November
2026 that too many rested on "nobody knows which one he is", and that
the site can carry that once. Trembath's verandah has it. The others:

| Writer | How the caption handles it |
|---|---|
| Staniforth | He said the sketch was made up |
| Tugwell | Not in the picture |
| Lovegrove | Found by the dash in his own list of names |
| Charlton | Her own hat brim over her eyes |
| Kenworthy | Pointed out plainly, behind the drum |
| Tobin | The portrait is lost |
| Dalgleish | Drawn from behind, because he would not sit |
| Protheroe | At the edge, turned to the children |
| Gadd | Her own hand in front of her face |
| Trembath | One of nine, and he never said which |
| Ormiston | Only his handwriting |

A new caption must not repeat one of these.

When pictures go on the site, the About page must say they were made by
an AI image model. They are invented pictures of invented people.

## Where the pictures go

Finished pictures live in `static/images/`, named after the writer
(`harriet-tugwell.webp`), at 1,400 pixels on the long side. Each
biography names its picture in its header, with a description for
people who cannot see it. A wide picture sits above the text and a tall
one in the side column. A biography with no picture keeps the empty
oval.

After adding or changing a picture, run `python3 images/make_faint.py`.
It makes the small grey copy that the home page shows, very pale, behind
the title and the writer's name. If the picture is a drawing on white
paper, add `image_kind: drawing` to the header, so that in dark mode it
is shown as a negative and the paper does not glare.

The sub-editors' room came out with ten men, not eleven, so the caption
was changed to match the picture.

## Things to check in each result

- The number of people, which image models often get wrong.
- Modern faces: even white teeth, groomed eyebrows, present-day
  haircuts. Before about 1910 nobody grins at a camera.
- Tone. Old prints are purple-brown or grey, not orange.
- Any writing. It should be absent or unreadable, except the initials in
  the last prompt.
- Too clean. If it looks new, ask for "more fading, foxing and wear, as
  on a print that has been handled for a century".

## 1. Alfred Staniforth: the sub-editors' room, 1904

```
A pen-and-ink illustration from a British newspaper of 1904, of the kind a staff artist drew for an article on how the paper is made. It shows the sub-editors' room of a London evening paper late at night: one long table under green-shaded hanging lamps, with exactly eleven men in shirtsleeves and waistcoats bent over proofs. Paste-pots, long scissors, spikes of copy, a speaking-tube on the wall, a clock showing a late hour. Quick, confident cross-hatching. The faces are only a few strokes each, so that no man can be told from another and none is the centre of the picture. Black ink on off-white newsprint that has yellowed, with faint show-through from the other side and a soft fold line. It is a drawing, not a photograph: line only, no grey wash. No caption and no lettering. Landscape format, 3:2.
```

## 2. Harriet Tugwell: the cathedral choir, 1889

```
An albumen photograph of 1889 on a cream cabinet-card mount: an English cathedral choir posed outdoors. About twenty men and boys in dark cassocks and white surplices stand in three rows on worn stone steps, in front of a medieval doorway and a row of grey stone houses with tall chimneys. The men are bearded or moustached, the boys stiff and unsmiling; one small boy has moved and is slightly blurred. There are no women anywhere in the group. In an upper window behind them a lace curtain is half drawn back, and there may or may not be a pale shape behind the glass. Purple-brown albumen tone, faded towards the edges, with foxing and slight silvering in the dark areas. Show the whole print on its mount, photographed flat from directly above in soft even light. Period-true in every detail, nothing modern, no legible writing. Landscape format, 3:2.
```

## 3. Thomas Lovegrove: the sergeants' mess, Athlone, 1886

```
An albumen cabinet photograph of 1886: the sergeants of a British infantry battalion, posed outside a grey stone barrack block in Ireland. About eighteen men in three rows, the front row seated on a bench with two more reclining on the gravel in front. Dark tunics with pale piping, sergeants' chevrons, sashes, and small round undress caps. Every man has a heavy moustache, cropped hair and the same upright, guarded stare, so that they look like brothers and no one stands out. A small terrier sits between two of them. Flat white sky, focus a little soft at the edges. Purple-brown tone, faded, with foxing and one corner of the card mount worn. Show the whole print on its mount, photographed flat from directly above in soft even light. Period-true in every detail, nothing modern, no legible writing. Landscape format, 3:2.
```

## 4. Hester Charlton: the college staff, 1904

```
A gelatin silver photograph of 1904 on a grey card mount: the teaching staff of an English women's college, posed outdoors on a terrace in front of an ornate red-brick building with pale stone dressings. About fourteen women aged thirty to sixty, in dark academic gowns over high-collared blouses, in two rows, the front row seated. Several wear large Edwardian hats. In the back row, second from one end, one woman is almost entirely hidden by the wide hat-brim of the colleague in front of her: only a shoulder, one hand and a narrow slice of forehead can be seen. Nobody smiles. Cool neutral black-and-white tone, slightly faded, with a few spots and a faint crease. Show the whole print on its mount, photographed flat from directly above in soft even light. Period-true in every detail, nothing modern, no legible writing. Landscape format, 3:2.
```

## 5. Eli Kenworthy: the brass band, Whit Friday, 1899

```
A photograph of 1899 on a buff card mount: a village brass band on Whit Friday in a Pennine mill town in the north of England. About twenty-four bandsmen in dark braided uniforms and peaked caps stand in three rows in a steep cobbled street, holding cornets, tenor horns, euphoniums and basses, with a bass drum on the ground in front. Soot-black stone terraces and a mill chimney behind them; women in shawls and children in their best clothes look on from the pavement. The bandsmen are working men, some young and some grey. The players with tenor horns stand in the middle row among the others, no different from the rest, and nobody is the centre of the picture. Overcast light. Warm brown tone, a little faded, a crease across one corner. Show the whole print on its mount, photographed flat from directly above in soft even light. Period-true in every detail, nothing modern, no legible writing. Landscape format, 3:2.
```

## 6. Nora Tobin: the lost wedding portrait

```
A page from a family photograph album of about 1900, photographed flat from directly above in soft daylight from one side. A heavy dark-green card page with gilt-edged window mounts for four cabinet portraits. Three of the windows hold faded Irish studio portraits of the 1890s, only partly in frame at the edges of the picture and slightly out of focus: a man with a watch-chain, an old woman in a shawl, two children. The fourth window, in the centre of the picture and in sharp focus, is empty. Inside it is a clean rectangle of paler, unfaded card where a photograph sat for fifty years, with a faint ghost of its outline and a torn scrap of the old mount still stuck in one corner. Worn page edges, a little foxing. Nothing modern, no legible writing. Portrait format, 2:3.
```

## 7. Andrew Dalgleish: the caricature, 1902

```
A full-page pen-and-ink caricature from a Scottish legal periodical of 1902, in the manner of the "men of the day" drawings of the time. A lean, stooping Edinburgh solicitor of about fifty, in a top hat and a long dark overcoat, hurries up a flight of stone steps with a black tin deed-box under one arm and a rolled umbrella under the other. He is drawn from behind and a little to one side, so that the hat-brim and a turned-up collar hide nearly all of his face: the tip of a nose and the rim of a pair of spectacles are all that show. Exaggerated but affectionate, with fine cross-hatching and a plain background that only suggests classical columns. Black ink on cream paper that has yellowed, with foxing. It is a drawing, not a photograph. No caption and no lettering. Portrait format, 2:3.
```

## 8. Rachel Protheroe: the school photograph

```
A school photograph of about 1905, a gelatin silver print on a dark card mount: the pupils of a small village school in rural west Wales, posed in the yard in front of a low stone schoolhouse with a slate roof. About thirty children aged five to twelve in four rows, the boys in jackets and heavy boots, the girls in white pinafores, all staring solemnly at the camera. A child in the front row holds a blank slate. At the far right-hand edge of the group stands the schoolmistress, a woman of about forty in a plain dark dress with her hair pinned up. She turned her head towards the children at the moment of exposure, so her face is in profile and slightly blurred. Grey light, wet ground, bare hills behind. Neutral tone, faded, with spots and a worn corner. Show the whole print on its mount, photographed flat from directly above in soft even light. Period-true in every detail, nothing modern, no legible writing. Landscape format, 3:2.
```

## 9. Winifred Gadd: the works outing, 1926

```
An amateur snapshot of 1926, a small gelatin silver print with a white border: the office staff of a factory on their annual outing to an English seaside town. About twenty-five people, mostly young women in cloche hats, drop-waisted coats and bar shoes, with a few men in flat caps and trilbies, crowd together beside an open motor charabanc on a promenade. They are laughing, squinting into the sun and turning to talk; nobody has posed them. No one is at the centre. Two faces are cut off by the edge of the frame, one is hidden behind a raised hand and one is blurred. The picture is slightly tilted and slightly overexposed, with a light leak in one corner. Neutral grey tone, a glossy surface with fine scratches and a bent corner. Show the whole print, photographed flat from directly above in soft even light. Period-true in every detail, nothing modern, no legible writing. Landscape format, 3:2.
```

## 10. John Trembath: the verandah at Ascension, about 1903

```
A photograph of about 1903, a gelatin silver print on a card mount that has been kept for years in the tropics: exactly nine men on the verandah of a wooden bungalow at a British telegraph station on a barren volcanic island. They wear white drill suits or shirtsleeves. Some sit in cane chairs, some lean against the verandah posts, and one sits on the steps with a dog. Sun helmets rest on knees or on the boards. They are moustached, sunburnt, aged from twenty-five to fifty, squinting, and all much alike. Hard overhead light and deep shade under the roof, so that several faces are half lost in shadow. Bare dark cinder ground and a flagstaff beyond. The print is faded and yellowed, with brown mould spots, and one corner of the mount is broken off. Show the whole print on its mount, photographed flat from directly above in soft even light. Period-true in every detail, nothing modern, no legible writing. Landscape format, 3:2.
```

## 11. George Ormiston: the initials in the margin

```
A close photograph, taken from above in low raking daylight, of part of a handwritten manuscript page from about 1900: a contributor's story in black ink, in a neat sloping hand, on cream foolscap paper with a ruled left margin. The handwriting looks real but is too small and cursive to read. Down the left margin, in a different, upright hand in soft pencil, run an editor's marks: a vertical stroke beside one paragraph, a word struck through, a small query mark, and at the foot of the margin the initials "G. O." with a short line under them. Those initials are the only writing in the picture that can be read. A rusty pin-hole and the stain of a paper-clip at the top corner, a faint ring left by a cup, slight foxing. Shallow depth of field, with the initials in sharp focus. Nothing modern. Portrait format, 2:3.
```

# The ghost pictures

Ten dark pictures for the plate at the top of the home page, one for
each writer's idea of a ghost. Each shows behind the title while that
writer's line is up. Chris makes them in one ChatGPT thread, in a style
he worked out there (dense, dark, engraved, nearly all black with one
small light). So these give only the subject, the date and where things
go. The style is his and is not written down here.

The originals go in `images/ghosts/`, named after the writer
(`harriet-tugwell.webp`). Then run `python3 images/make_faint.py`,
`python3 build.py` and `node images/check_plate.js`.

## Placement, the same for all ten

On a wide screen the title and the line sit on the left of the plate,
over the picture. On a phone the whole picture sits above the words. So:

- Landscape, 3:2.
- One small bright thing, in the right-hand third, between a quarter
  and two-thirds of the way down. Nothing else bright.
- The left two-thirds dark and quiet: no highlights, no pale shapes.
- Nothing that matters in the top or bottom tenth, which wide screens
  cut off.
- Nobody in it, and no reflection or shadow of anybody.
- No lettering that can be read.

## The ten

Seven of these stories are not written yet. Their pictures are drawn
from the writer's idea of a ghost and from the titles and one-line
summaries already on the biography pages, and they should not be taken
as fixing anything in a story.

### 1. Alfred Staniforth: a device for one clean fright (done)

The far corner of an empty horse tram at night, Sheffield, 1886. An oil
lamp above the corner seat, upper right. Two pennies on the seat under
it. From "The Last Car but One".

### 2. Harriet Tugwell: what a household will not say

```
Same style. Subject: the drawing-room of an English country house in Somerset on a winter evening, about 1895. A low upholstered chair stands empty beside a small round table. On the table is a little oil reading-lamp with a shade, lit, and it is the only light in the picture. A small thick book lies closed on the seat of the low chair. Facing the chair across a hearth-rug, and almost lost in the dark, is a large high-backed armchair, also empty, with a shawl over one arm. Heavy curtains, a glimpse of a bookcase. Nobody in the room.
Placement: the little lamp and the low chair in the right-hand third of the picture, about halfway down. The lamp is the one bright thing and it is small. The left two-thirds, with the big armchair, stays very dark and quiet. Landscape, 3:2. No people, no lettering.
```

### 3. Thomas Lovegrove: a man still on the strength

```
Same style. Subject: a corner of a British Army barrack yard at night, in the 1880s. A wooden sentry-box stands empty beside the barred and padlocked door of a low brick store. A single lantern hangs from an iron bracket over the door, lit, and it is the only light. Wet cobbles, a high brick wall, a water-butt. The sentry-box is empty: no soldier, no rifle, no shadow of anyone.
Placement: the lantern, the door and the sentry-box in the right-hand third, with the lantern about a third of the way down. The lantern is the one bright thing and it is small. The left two-thirds is the dark yard and wall, with nothing bright in it. Landscape, 3:2. No people, no lettering.
```

### 4. Hester Charlton: an ancient debt, unpaid

```
Same style. Subject: an archaeological dig on Hadrian's Wall in Northumberland at dusk, in 1903. The round mouth of a stone-lined Roman well, newly cleared, in a trench cut through turf. A workman's lantern has been left on the stone rim, lit, and it is the only light. Beside it on the wet rim lie three or four penny coins. A rope goes down into the well from a simple wooden windlass, and a bucket and a spade lie by it. Behind, a few courses of squared Roman stones and bare moor. Nobody there.
Placement: the well, the lantern and the coins in the right-hand third, with the lantern about halfway down. The lantern is the one bright thing and it is small. The left two-thirds is dark trench, turf and sky with nothing bright in it. Landscape, 3:2. No people, no lettering.
```

### 5. Eli Kenworthy: a wage owing

```
Same style. Subject: the spinning room of a Lancashire cotton mill, about 1895, empty, with the machines stopped. A long spinning mule runs away into the dark: hundreds of upright spindles in a row on a low wheeled carriage, over bare oily floorboards, with iron pillars holding up the ceiling. One gas jet burns on a wall bracket, and it is the only light. Under it, set neatly against the wall, is a small pair of child's wooden-soled clogs, and on the floor beside the machine lies a short hand-brush. Nobody in the room.
Placement: the gas jet, the clogs and the brush in the right-hand third, with the gas jet about a third of the way down. The gas jet is the one bright thing and it is small. The long row of spindles runs off to the left into darkness, with nothing bright in it. Landscape, 3:2. No people, no lettering.
```

### 6. Nora Tobin: a neighbour in need of a favour

```
Same style. Subject: the inside of a draper's shop in a country town in Ireland, after closing, about 1893. A long wooden counter with a large account book lying open on it, a pen beside the book, and a single candle in a brass candlestick, lit, which is the only light. Bolts of cloth on shelves behind the counter. Beyond the end of the counter the back door of the shop stands a little way open on to complete darkness. Nobody in the shop.
Placement: the candle, the open book and the back door in the right-hand third, with the candle about halfway down. The candle is the one bright thing and it is small. The counter and the shelves run off to the left into the dark, with nothing bright there. The pages of the book are in shadow and nothing on them can be read. Landscape, 3:2. No people, no lettering.
```

### 7. Andrew Dalgleish: a witness nobody can cross-examine

```
Same style. Subject: a room in an Edinburgh house in 1897, being cleared after a death. The furniture has been pushed together and roped for the sale room, and the pictures are stacked against the wall. Apart from the rest, a tall looking-glass in a dark wooden frame leans against the bare wall, with a blank paper lot-ticket tied to it by a string. On a lawyer's black tin deed-box in front of it stands one candle, lit, which is the only light. The glass shows the candle flame and the empty room, and nobody.
Placement: the looking-glass and the candle in the right-hand third, with the flame about halfway down. The flame and its reflection are the only bright things and both are small. The left two-thirds is the roped furniture in deep shadow. Landscape, 3:2. No people, no reflection of anyone, no lettering.
```

### 8. Rachel Protheroe: a warning that comes first

```
Same style. Subject: a narrow sunken lane between high hedge-banks in the hills of west Wales, on a moonless night, about 1896. Some way down the lane, low over the mud and about the height of a hand, a single small pale flame is moving along by itself. Nobody is carrying it and it lights almost nothing. A field gate, bare thorn trees, and far off the dark shape of a farmhouse with no light in it.
Placement: the small flame in the right-hand third, a little below halfway down. It is the one bright thing and it is very small. The left two-thirds is hedge-bank and black sky with nothing bright in it. Landscape, 3:2. No people, no lettering.
```

### 9. Winifred Gadd: a wish with nowhere to go

```
Same style. Subject: a clerk's desk in the office of a factory in outer London, after hours, in 1923. A heavy upright typewriter with a sheet of paper in it, a candlestick telephone, a wire tray of letters, and the typist's chair pushed back from the desk. One electric desk-lamp with a metal shade is lit, and it is the only light: it falls in a small pool on the typewriter keys and the paper. Everything beyond the desk is dark: rows of other desks with covered typewriters, a tall window with night outside. Nobody in the office.
Placement: the lamp and the typewriter in the right-hand third, about halfway down. The pool of lamplight is the one bright thing and it is kept small. The left two-thirds is the dark office with nothing bright in it. Nothing on the paper can be read. Landscape, 3:2. No people, no lettering.
```

### 10. John Trembath: a message that outlived its sender

```
Same style. Subject: the instrument-room of a submarine cable station on a coral island in the Indian Ocean, at three in the morning, about 1910. A plain wooden room with open rafters. On a desk a large bound diary lies open with a pen across it, beside a brass telegraph instrument from which a narrow paper tape has run out and coiled on the floor. One oil lamp on the desk is lit, and it is the only light. The operator's chair is pushed back and empty. Through an open shuttered window, the black trunks of coconut palms. Nobody in the room.
Placement: the lamp, the open diary and the instrument in the right-hand third, with the lamp about halfway down. The lamp is the one bright thing and it is small. The left two-thirds is the dark room, the rafters and the window, with nothing bright there. The pages of the diary are in shadow and nothing on them can be read. Landscape, 3:2. No people, no lettering.
```

