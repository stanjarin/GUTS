# BABY’S FIRST GUTS

## What the hell is where?

This is the **Stanley-level map**, not the engineering manual. Read this when you have forgotten which site does what, where to go, or which phone is talking to whom.

There are **three places Stanley may need to get into** and **five players in the performance**.

---

# PART ONE — THE THREE PLACES YOU CONTROL

## 1. P PHONE — the Performer phone

**What it is:** Stanley’s phone running the existing **NoBo NoFo PWA**.

**What it does:** This is where the secret work begins. Before performance the ARM PIN can be prepared. During performance, the H2G2 covert input is used to enter the chosen force word without obvious “magic app” business.

**What happens next:** The P phone sends the word securely to Cloudflare. It does **not** send anything directly to the spectator’s phone.

Think:

> **P PHONE = SECRET CONTROL PANEL**

Normal performer route:

**NoBo NoFo → H2G2 covert input → word → Cloudflare**

The NoBo code itself lives in the separate GitHub repository:

`stanjarin/NoBoNoFo`

---

## 2. GITHUB — the workshop / filing cabinet

**What it is:** Where the project files and source code live.

Main GUTS repository:

`stanjarin/GUTS`

Performer/NoBo repository:

`stanjarin/NoBoNoFo`

**What is in GUTS:**

- the spectator website code
- the nine-book corpus
- Pre-Page artwork
- Gutenberg Landing artwork
- Carousel artwork
- Suggestions overlay
- full-size book covers
- Cloudflare Worker code
- README/specification/recovery documents
- version history through Git commits

**What GitHub does NOT do during the trick:** It does not shuttle the secret word between the two phones. It is the workshop/source archive, not the live messenger.

Think:

> **GITHUB = WHERE WE BUILD AND STORE THE MACHINE**

When a change is committed to GUTS, Cloudflare deployment machinery can publish that new version to the live site.

---

## 3. CLOUDFLARE — the theatre machinery

**What it is:** The live production host and tiny state store behind `gutenbrg.com`.

Cloudflare does two important jobs:

1. **HOST WEBSITE** — serves the live GUTS spectator site and its artwork/code.
2. **REMEMBER WORD** — receives the force word from the P phone and temporarily stores the performance state in KV so the spectator site can retrieve it.

Think:

> **CLOUDFLARE = HOST WEBSITE + REMEMBER WORD**

The basic secret traffic is:

**P PHONE → Cloudflare → SP PHONE**

There is no direct P-phone-to-SP-phone connection.

Production domain:

`https://gutenbrg.com`

Cloudflare Worker: `guts`

KV binding: `GUTS_STATE`

The actual secret/PIN values belong in Cloudflare/private configuration, **never in public GitHub files**.

---

# PART TWO — THE FIVE PLAYERS THE AUDIENCE ENCOUNTERS

## 1. P PHONE

**P = Performer.**

Stanley’s phone. Secretly supplies the force word through NoBo/H2G2.

The spectator does not need to know it has communicated with anything.

---

## 2. GUTENBRG

This is **our** live site:

`gutenbrg.com`

Notice the missing second **e**. It is deliberately not `gutenberg.org`.

GUTENBRG contains the performance machinery and fake/constructed Gutenberg-like journey:

**Pre-Page → Landing → Carousel → selected cover → Contents → chapter → reader**

This is where the `$$$` sockets, force-word substitution and reader state machinery live.

Think:

> **GUTENBRG = OUR SECRET STAGE SET**

The spectator should experience it as ordinary web wandering, not as “the trick website.”

---

## 3. REAL GUTENBERG

This is the genuine **Project Gutenberg** website:

`https://www.gutenberg.org`

It is not ours and contains no force machinery.

Its job in the performance architecture is reality/camouflage. The constructed route borrows the visual/world context of Project Gutenberg and can ultimately hand the spectator into the genuine site so the fake machinery disappears behind them.

Think:

> **REAL GUTENBERG = THE REAL WORLD**

Do not confuse:

**gutenbrg.com = ours**

**gutenberg.org = real Project Gutenberg**

---

## 4. PRE-PAGE

The Pre-Page is the **Resources** page the spectator encounters first.

It looks like an old, mildly institutional resources portal. It says the books are **from Project Gutenberg**; it does not claim that the Resources page itself *is* Project Gutenberg.

It has four ordinary-looking links:

- Recent additions
- Popular titles
- Reader recommendations
- Staff picks

All four are supposed to work independently, although they ultimately lead into the same GUTS book environment.

Performance reason:

Stanley apparently remembers an old Gutenberg shortcut and gives it to the spectator. Instead of landing exactly where expected, it produces this slightly wrong old Resources page.

Possible beat:

> “Oh. … OK, that’ll do. Tap any of those.”

That small imperfection is camouflage, not a mistake in the premise.

The current short route used to reach it is:

`https://tinyurl.com/ebooks-0`

Think:

> **PRE-PAGE = THE ACCIDENTAL-LOOKING FRONT DOOR**

---

## 5. SP PHONE — the Spectator phone

**Sp = Spectator.**

This is the crucial object: **their own phone**.

The spectator opens the route, reaches the Pre-Page, wanders into the Gutenberg-style book collection, chooses a book, chooses a chapter and stops on a page.

Meanwhile their browser quietly asks Cloudflare for the current performance state. If the P phone has armed a word, the GUTS reader knows it and can substitute that word into the appropriate `$$$` socket.

Think:

> **SP PHONE = WHERE THE IMPOSSIBILITY APPEARS**

No app install. No direct connection to Stanley’s phone. No visible control interface.

---

# THE WHOLE THING IN ONE PICTURE

```text
                    BUILD / MAINTAIN

             GitHub: stanjarin/GUTS
                      |
                      | deploys
                      v
              CLOUDFLARE / GUTENBRG
              host site + remember word
                      ^
                      |
            secret word/state push
                      |
              P PHONE / NoBo H2G2


                    PERFORMANCE

P PHONE
   |
   | secretly sends WORD
   v
CLOUDFLARE  <----------------------+
   |                               |
   | stores WORD                   | SP browser quietly pulls state
   |                               |
   +----------------------------> SP PHONE
                                    |
                                    v
                              PRE-PAGE
                                    |
                                    v
                           GUTENBRG LANDING
                                    |
                                    v
                         CAROUSEL / CHOOSE BOOK
                                    |
                                    v
                       COVER → CONTENTS → READER
                                    |
                                    v
                              WORD APPEARS
                                    |
                           eventually / as needed
                                    v
                            REAL GUTENBERG
```

---

# THE SIX THINGS TO REMEMBER

1. **P phone controls secretly.**
2. **GitHub stores/builds the project.**
3. **Cloudflare hosts GUTENBRG and remembers the word.**
4. **GUTENBRG is ours; Gutenberg.org is real.**
5. **Pre-Page is the accidental-looking front door.**
6. **The miracle happens on Sp’s own phone.**

And the engineering mantra remains:

> **H2 PUSHES — GUT PULLS.**

For actual repair/development work, graduate from Baby’s First Lesson to:

`IF_CHATGPT_DIES_READ_THIS.md`

then:

`README.md`
