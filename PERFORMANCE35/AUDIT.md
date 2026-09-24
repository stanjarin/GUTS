# GUTS 0.35 PERFORMANCE PAGINATION AUDIT

Machine audit only: no live reader data changed.

## AAM
- source pages: 203
- source words/page: min 2; median 134; max 205
- pages under 220 words: 203
- proposed air-lock (30 words): Pooh stopped for a moment, because $$$ had come into his head. He wasn’t quite sure why it had, but there it was, so he thought he had better remember it.

## AC
- source pages: 176
- source words/page: min 8; median 143; max 210
- pages under 220 words: 176
- proposed air-lock (22 words): It was only then that $$$ occurred to me. At the time it seemed quite unimportant, and I thought no more about it.

## DP
- source pages: 28
- source words/page: min 5; median 133; max 214
- pages under 220 words: 28
- proposed air-lock (22 words): For no good reason I suddenly remembered $$$. There are thoughts which know perfectly well when they are not wanted, and come anyway.

## DR
- source pages: 1583
- source words/page: min 6; median 166; max 232
- pages under 220 words: 1577
- proposed air-lock (28 words): It comes to me at this point that $$$ is something worth remembering, although I cannot say why. So I remember it, and let the matter go at that.

## JJ
- source pages: 1878
- source words/page: min 0; median 137; max 231
- pages under 220 words: 1844
- proposed air-lock (21 words): Then $$$ came to him, suddenly and complete, a word out of nowhere. He held it there a moment and went on.

## JT
- source pages: 138
- source words/page: min 33; median 146; max 214
- pages under 220 words: 138
- proposed air-lock (25 words): For some reason I thought then of $$$, although it had nothing whatever to do with what was happening. This was probably why I remembered it.

## Right Ho, Jeeves
- chapters: 23; pages: 379
- words/page: min 0; median 202; max 378
- pages under 220 words: 304

## Adventures of Huckleberry Finn
- chapters: 43; pages: 586
- words/page: min 0; median 195; max 423
- pages under 220 words: 406

## A Farewell to Arms
- chapters: 41; pages: 464
- words/page: min 0; median 197; max 424
- pages under 220 words: 320

## 0.35 geometry to build
- Keep 15px / 1.45 reader typography.
- Retain genuine text only; cut unusably short chapters rather than pad/repeat.
- Target ~260–330 genuine words per displayed page before air-lock, with terminal-page balancing.
- Every prepared page: variable genuine carry-over -> one self-contained air-lock containing $$$ -> fresh genuine paragraph -> remaining genuine text.
- Vary carry-over length/paragraph position to stagger air-lock vertically.
- No selectable chapter survives unless it can support at least 3 performance-depth pages after balancing.
- Rebuild Contents and force coordinates only after pagination is frozen.