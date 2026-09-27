# NoBo socket anomaly forensic

- bloomfield: pages=1482 sockets=1482 distribution={1: 1482}
- farewell: pages=464 sockets=464 distribution={1: 464}
- h2g2: pages=254 sockets=254 distribution={1: 254}
- hst: pages=125 sockets=124 distribution={0: 1, 1: 124}
- huck: pages=586 sockets=586 distribution={1: 586}
- jeeves: pages=379 sockets=379 distribution={1: 379}
- jobs: pages=1046 sockets=1046 distribution={1: 1046}
- keef: pages=988 sockets=988 distribution={1: 988}
- sotweed: pages=1833 sockets=5301 distribution={0: 66, 3: 1767}

**TOTAL current book pages: 7157**
**TOTAL current $$$ tokens in force_paragraphs: 10624**

## HST abnormal pages
### chapter 1 / page 1 — I
- marker count: 0
- genuine paragraphs: ['We were somewhere around Barstow on the edge of the desert when the drugs began to take hold. I remember saying something like “I feel a bit lightheaded; maybe you should drive. …” And suddenly there was a terrible roar all around us and the sky was full of what looked like huge bats, all swooping and screeching and diving around the car, which was going about 100 miles an hour with the top down to Las Vegas. And a voice was screaming: “Holy Jesus! What are these goddamn animals?” Then it was quiet again. My attorney had taken his shirt off and was pouring beer on his chest, to facilitate the tanning process. “What the hell are you yelling about?” he muttered, staring up at the sun with his eyes closed and covered with wraparound Spanish sunglasses. “Never mind,” I said. “It’s your turn to drive.” I hit the brakes and aimed the Great Red Shark toward the shoulder of the highway.']
- force paragraphs: ['We were somewhere around Barstow on the edge of the desert when the drugs began to take hold. I remember saying something like “I feel a bit lightheaded; maybe you should drive. …” And suddenly there was a terrible roar all around us and the sky was full of what looked like huge bats, all swooping and screeching and diving around the car, which was going about 100 miles an hour with the top down to Las Vegas. And a voice was screaming: “Holy Jesus! What are these goddamn animals?” Then it was quiet again. My attorney had taken his shirt off and was pouring beer on his chest, to facilitate the tanning process. “What the hell are you yelling about?” he muttered, staring up at the sun with his eyes closed and covered with wraparound Spanish sunglasses. “Never mind,” I said. “It’s your turn to drive.” I hit the brakes and aimed the Great Red Shark toward the shoulder of the highway.']

## Sot-Weed marker pattern
- total marker-count distribution: {0: 66, 3: 1767}
- marker paragraph-index patterns: {(0,): 896, (1,): 871, (): 66}
### sample with 0 markers — chapter 1 page 1 — Chapter 1
- per-force-paragraph marker counts: [0]
- genuine: ['IN THE LAST YEARS OF THE SEVENTEENTH CENTURY THERE WAS TO BE found among the fops and fools of the London coffee-houses one rangy, gangling flitch called Ebenezer Cooke, more ambitious than talented, and yet more talented than prudent, who, like his friends-in-folly, all of whom were supposed to be educating at Oxford or Cambridge, had found the sound of Mother English more fun to game with than her sense to labor over, and so rather than applying himself to the pains of scholarship, had learned the knack of versifying, and ground out quires of couplets after the fashion of the day, afroth with Joves and Jupiters, aclang with jarring rhymes, and string-taut with similes stretched to the snapping-point. As poet, this Ebenezer was not better nor worse than his fellows, none of whom left behind him anything nobler than his own posterity; but four things marked him off from them.']
- force: ['IN THE LAST YEARS OF THE SEVENTEENTH CENTURY THERE WAS TO BE found among the fops and fools of the London coffee-houses one rangy, gangling flitch called Ebenezer Cooke, more ambitious than talented, and yet more talented than prudent, who, like his friends-in-folly, all of whom were supposed to be educating at Oxford or Cambridge, had found the sound of Mother English more fun to game with than her sense to labor over, and so rather than applying himself to the pains of scholarship, had learned the knack of versifying, and ground out quires of couplets after the fashion of the day, afroth with Joves and Jupiters, aclang with jarring rhymes, and string-taut with similes stretched to the snapping-point. As poet, this Ebenezer was not better nor worse than his fellows, none of whom left behind him anything nobler than his own posterity; but four things marked him off from them.']

### sample with 3 markers — chapter 1 page 2 — Chapter 1
- per-force-paragraph marker counts: [3, 0, 0, 0]
- genuine: ['The first was his appearance: pale-haired and pale-eyed, raw-boned and gaunt-cheeked, he stood— nay, angled— nineteen hands high. His clothes were good stuff well tailored, but they hung on his frame like luffed sails on long spars.', "Heron of a man, lean-limbed and long-billed, he walked and sat with loose-jointed poise; his every stance was angular surprise, his each gesture half flail. Moreover there was a discomposure about his face, as though his features got on ill together: heron's beak, wolf-hound's forehead, pointed chin, lantern jaw, wash-blue eyes, and bony blond brows had minds of their own, went their own ways, and took up odd stances. They moved each independent of the rest and fell into new configurations, which often as not had no relation to what one took as his mood of the moment. And these configurations were shortlived, for like restless mallards the features of his face no sooner were settled than ha! they'd be flushed, and hi! how they'd flutter, every man for himself, and no man could say what lay behind them.", 'The second was his age: whereas most of his accomplices were scarce']
- force: ['At this point it’s useful to remember the thing that Ebenezer kept scribbling over and over late that night so long ago. ‘$$$, $$$, $$$’. But what he meant by it could not then be divined.', 'The first was his appearance: pale-haired and pale-eyed, raw-boned and gaunt-cheeked, he stood— nay, angled— nineteen hands high. His clothes were good stuff well tailored, but they hung on his frame like luffed sails on long spars.', "Heron of a man, lean-limbed and long-billed, he walked and sat with loose-jointed poise; his every stance was angular surprise, his each gesture half flail. Moreover there was a discomposure about his face, as though his features got on ill together: heron's beak, wolf-hound's forehead, pointed chin, lantern jaw, wash-blue eyes, and bony blond brows had minds of their own, went their own ways, and took up odd stances. They moved each independent of the rest and fell into new configurations, which often as not had no relation to what one took as his mood of the moment. And these configurations were shortlived, for like restless mallards the features of his face no sooner were settled than ha! they'd be flushed, and hi! how they'd flutter, every man for himself, and no man could say what lay behind them.", 'The second was his age: whereas most of his accomplices were scarce']

## README-vs-current-corpus check
- README text: # NoBo NoFo — v.5M

W3 DATA FIX — prepared socket on every page.

- Removes the bad v.5L runtime repeated-graft approach by returning to the v.5K engine.
- Every one of the 9,761 shipped logical pages now has its own force_paragraphs.
- Each prepared page is based on that page's own genuine prose; the socket is inserted into a sentence already on that page.
- Existing hand-authored Pass 4 sockets are preserved.
- Genuine paragraphs are untouched underneath.
- PAID / CLEAN machinery is unchanged.
- Keyboard fix retained.
- W1 cover slide remains deferred.

VERIFIED:
- pages checked: 9,761
- pages missing a $$$ socket: 0
- total $$$ sockets: 9,762

BOOKS CHANGED.
- current corpus pages counted directly: 7157
- current force-paragraph $$$ tokens counted directly: 10624