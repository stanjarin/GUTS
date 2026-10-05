# Virtual Reader Renderer

A general-purpose fixed-layout Reader probe for NoBo/GUTS-style pages.

It renders one page in a real browser engine and reports **exact rendered line breaks**, line boxes, paragraph positions, and the `$$$` marker position. It also emits a screenshot. The point is to replace inferred typography with measurable browser geometry.

## Inputs
A small JSON file containing `viewport`, `paragraphs`, and optional CSS overrides. The renderer is not tied to any title or corpus.

## Outputs
- `page.png` — rendered page
- `metrics.json` — exact line-by-line text and geometry
- marker coordinates and line number for `$$$`

## Use

```bash
python render_reader.py fixtures/bloomfield-ch1-p6.json --out out --executable /usr/bin/chromium
```

Where Playwright browser bundles are installed, omit `--executable` and choose `--engine chromium|webkit|firefox`.

## Calibration rule
Do **not** trust placement classification until the renderer reproduces a real-device control specimen line-for-line. Bloomfield Ch 1 p6 is the first control. Once it matches, verify at least two additional pages before using the renderer for HIGH/LOW/RETENTION judgements.

## Important limitation
Browser engine and font metrics matter. Linux Chromium with a Georgia substitute is useful for mechanics but is not automatically equivalent to iOS Safari. The tool therefore treats real-device line breaks as calibration truth. A Safari/WebKit run, or a calibrated equivalent profile, is preferred for production judgments.

This tool is read-only: it does not mutate corpus or Reader state.
