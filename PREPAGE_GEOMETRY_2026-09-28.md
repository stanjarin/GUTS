# PRE-PAGE / ARTWORK GEOMETRY

**Updated 29 September 2026**

The former 1242 × 2208 measurement described an implementation/export instance, not the governing artwork system.

## Governing fixed-page master

- MASTER: **2048 × 4210 px**
- ESSENTIAL / SAFE: **1804 × 3640 px**

The blue guides in Stanley's artwork templates mark the essential area that must survive device variation.

Design rule:
- bring meaningful composition close to the safe guides;
- canvas outside the safe guides is sacrificial crop allowance;
- do not add huge internal margins inside the safe zone.

## Long landing art

The landing page uses the same 2048-wide system but extends vertically for deliberate overscroll camouflage.

Known long landing master:
- **2048 × 8000 px**

## Pre-Page pilot result

The Pre-Page is a long scrolling page and should **not** use `object-fit: cover` against a viewport-height box.

Passing branch implementation:
- `width:112%`
- `max-width:none`
- `height:auto`
- `margin-left:-6%`
- normal vertical scrolling

This produces a modest horizontal crop while retaining the full vertical document.

One transparent hotspot covers the entire four-link block:
- Recent additions
- Popular titles
- Reader recommendations
- Staff picks

Stanley phone QA: **PASS & PASS**.

Next geometry test: apply the same principle to one cleaned-up book cover before standardising the whole cover set.
