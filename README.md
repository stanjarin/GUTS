# GUTS

GUTS is the spectator-phone development branch of the NoBo NoFo concept.

## Current state

**FORMAT 1 — six new books**

The new-book corpus has completed source cleaning and first-stage reader formatting. The working set is:

- James Joyce — *Ulysses*
- Agatha Christie — *The Murder at the Vicarage*
- A. A. Milne — *The House at Pooh Corner*
- Damon Runyon — *On Broadway*
- Dorothy Parker — *Men I’m Not Married To*
- James Thurber — *My Life and Hard Times*

Three books will later be inherited from the existing NoBo NoFo corpus:

- P. G. Wodehouse — *Right Ho, Jeeves!*
- Ernest Hemingway — *A Farewell to Arms*
- Mark Twain — *Huckleberry Finn*

That gives the final nine-book GUTS library.

## Formatting doctrine

FORMAT 1 converts the cleaned source into deterministic, phone-oriented reader pages.

- Preserve wording and order.
- Preserve genuine verse and dialogue structure.
- Make chapter/story/episode boundaries unmistakable in the reader.
- Runyon: 47 story openings are structural divisions; the three collection titles remain distinct from story titles.
- Joyce: 18 episode names are GUTS navigation structure, not represented as Joyce's printed chapter headings.
- Exceptionally long authorial paragraphs may be divided into comfortable screen-reading paragraphs without changing wording or order.
- Pagination is for the eventual spectator-phone reading experience.
- Checker PDFs are desktop proofing representations of that pagination, not the final UI.

## Force doctrine

The canonical marker is `$$$`.

The force target is **paragraph-based**. Performance instruction: “Now read the first paragraph. No, sorry, the first new paragraph.”

No sockets or force paragraphs are added during FORMAT 1.

## Next production stage

1. QA FORMAT 1.
2. Bring in the three inherited NoBo NoFo books.
3. Normalize the complete nine-book corpus.
4. Generate socket / force-paragraph machinery.
5. Build the GUTS spectator-phone reader and performance-state architecture.

## Engineering relationship

GUTS is a separate product/repository. It may reuse proven NoBo NoFo engineering principles and code, but spectator possession of the phone imposes a higher standard of camouflage and clean behaviour.
