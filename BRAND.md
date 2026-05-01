# Bill of Behavior — brand kit (this repo)

Visual identity for <https://billofbehavior.com>.

The **canonical source of truth** for the FusionCore brand family lives at
`biz/talks/_assets/logos/` (see `biz/talks/BRAND.md`). This file documents
the BoB sub-brand and the assets shipped with this site.

---

## Position in the FusionCore family

```
FusionCore  ─── deep-purple house brand, primary accent #DE5AFF
   │
   └── Bill of Behavior (sub-brand) ─── same purple palette,
       open standard                    + gold #C3A50D as the
                                        "verified" accent in the logomark
```

A visitor arriving from fusioncore.ai sees the same purple-on-deep-purple
palette here. The single distinguishing detail is the gold dot inside the
BoB logomark — visual shorthand for "this is the verified, standardised
piece of the FusionCore work".

---

## Palette (tokens)

| Role | Hex | CSS variable |
|------|-----|--------------|
| Primary background (dark) | `#400049` | `--bg-deep` |
| Gradient stop (lighter) | `#5a1a66` | `--bg-deep-3` |
| Gradient stop (deeper) | `#28002e` | `--bg-deep-2` |
| Accent (purple) | `#DE5AFF` | `--accent` |
| Accent dark (hover) | `#a82fc7` | `--accent-dk` |
| Accent light (washes) | `#f4dcff` | `--accent-lt` |
| **Verified mark (gold)** | `#C3A50D` | `--gold` |
| Caution (reserved) | `#D43F5B` | `--coral` |
| Muted on dark | `#C9A5CF` | `--muted-dark` |
| Body text | `#1c2030` | `--ink` |
| Soft section background | `#f6f4ee` | `--bg-soft` |

All canonical from `biz/talks/BRAND.md`. Do not introduce new hex values
without updating the canonical doc first.

---

## Typography

System sans-serif stack:

```
-apple-system, BlinkMacSystemFont, "Segoe UI", Helvetica, Arial, sans-serif
```

No Google Fonts, no `@font-face`, no JS — privacy-friendly by default.
For decks and print, the canonical stack is Tahoma / Avenir (see canonical
BRAND.md); the web stack approximates this with system fonts.

---

## Asset inventory (what ships in this repo)

### Site favicon set (used by the live site)

```
static/
├── favicon.svg              ← root favicon (modern, scales freely)
├── favicon.ico              ← multi-size legacy fallback (16/32/48)
├── apple-touch-icon.png     ← 180×180 for iOS home-screen
├── manifest.webmanifest     ← PWA manifest (theme-color, icons)
└── brand/
    ├── logomark.svg         ← icon-only mark (geometric: rules + gold dot)
    ├── wordmark.svg         ← typographic "Bill of Behavior"
    ├── lockup.svg           ← logomark + wordmark (dark on light)
    ├── lockup-light.svg     ← lockup variant (light on dark — used in topnav)
    ├── favicon.svg          ← optimised for tiny rendering
    ├── favicon-16/32/48.png ← raster fallbacks (rolled into favicon.ico)
    ├── apple-touch-icon.png
    ├── icon-192.png         ← Android / PWA medium
    ├── icon-512.png         ← Android / PWA large
    ├── og-image.svg         ← canonical 1200×630 OpenGraph card
    └── og-image.png         ← rendered raster (used in <meta og:image>)
```

### Logo suites (one folder per brand)

Source PNGs are dropped into `static/brand/<slug>/source.png`; the icon suite
is generated from there.

```
static/brand/
├── bob-registered/          ← canonical "bob §®" registered logo (3D bee)
│   ├── source.png
│   ├── icon.svg             ← SVG wrapper around 512px master
│   ├── icon-{16,32,48,180,192,512}.png
│   ├── favicon-{16,32,48}.png
│   ├── favicon.ico
│   └── apple-touch-icon.png
├── fusioncore/              ← FusionCore battery + leaves master logo
│   └── (same layout)
└── k8sstormcenter/          ← Kubernetes Storm Center tree-of-life seal
    └── (same layout)
```

Canonical sources also live in `biz/talks/_assets/logos/` and are mirrored
here so the site is self-contained for CI builds:

| Canonical | Mirrored to |
|---|---|
| `biz/talks/_assets/logos/billofbehavior/bob-registered.png` | `static/brand/bob-registered/source.png` |
| `biz/talks/_assets/logos/fusioncore-logo-master.png` | `static/brand/fusioncore/source.png` |
| `biz/talks/_assets/logos/k8sstormcenter/storm-center-tree.png` | `static/brand/k8sstormcenter/source.png` |

### Note on the BoB favicon

The current site favicon (`static/favicon.svg`) is the **geometric
logomark** (purple frame, white rules, gold dot) — designed to read at 16px.
The **registered "bob §®" logo** (with bee and "Bill of Behavior" subtitle)
is preserved in `brand/bob-registered/` for use as a brand badge / OG card /
deck title slide, but doesn't survive the 16×16 favicon rendering test.
Switch the site favicon to bob-registered only if you accept reduced
legibility at small sizes.

---

## Logomark concept

The mark depicts an **application profile** — three rules of decreasing
prominence (representing entries in a behavior bill), with a single gold
dot signalling the verified runtime state on the active rule.

This is *not* a profile silhouette, *not* a generic "secure" padlock, and
*not* a wordmark monogram. The semantic meaning matches the standard:
declarative rules + verification.

### When to use which

| Situation | Use |
|-----------|-----|
| Browser tab / favicon | `favicon.svg` (auto), `favicon.ico` (legacy) |
| iOS home-screen | `apple-touch-icon.png` |
| Android home-screen / PWA | manifest icons (192/512) |
| Top nav of the website | `lockup-light.svg` |
| Page hero, decks, slides | `lockup.svg` (on light) or `lockup-light.svg` (on dark) |
| Avatar / GitHub org | `logomark.svg` |
| Social card preview (LinkedIn / X / OG) | `og-image.png` |
| Print / deck title slide | `lockup.svg` at minimum 18 mm width |

---

## Regenerating raster assets

### From SVG sources (the geometric logomark / wordmark / OG card)

```sh
cd biz/talks/_assets/logos/billofbehavior
OUT=fusioncore-web/static/brand
rsvg-convert -w 16  bob-favicon.svg  -o "$OUT/favicon-16.png"
rsvg-convert -w 32  bob-favicon.svg  -o "$OUT/favicon-32.png"
rsvg-convert -w 48  bob-favicon.svg  -o "$OUT/favicon-48.png"
rsvg-convert -w 180 bob-logomark.svg -o "$OUT/apple-touch-icon.png"
rsvg-convert -w 192 bob-logomark.svg -o "$OUT/icon-192.png"
rsvg-convert -w 512 bob-logomark.svg -o "$OUT/icon-512.png"
rsvg-convert -w 1200 -h 630 bob-og-image.svg -o "$OUT/og-image.png"
convert "$OUT/favicon-16.png" "$OUT/favicon-32.png" "$OUT/favicon-48.png" \
        "$OUT/favicon.ico"
cp bob-*.svg "$OUT/"
cp bob-favicon.svg fusioncore-web/static/favicon.svg
cp "$OUT/apple-touch-icon.png" fusioncore-web/static/apple-touch-icon.png
```

### From PNG source (FusionCore logo, BoB-registered, Storm Center tree)

Drop the source PNG into `static/brand/<slug>/source.png`, then:

```sh
gen_suite() {
  src="$1"; slug="$2"
  out="static/brand/$slug"
  mkdir -p "$out"
  # Trim transparent borders, center on transparent 1024 square, ~10% padding
  convert "$src" -trim +repage \
    -background none -gravity center \
    -resize 832x832 -extent 1024x1024 \
    "$out/master-1024.png"
  for size in 16 32 48 180 192 512; do
    convert "$out/master-1024.png" -resize ${size}x${size} "$out/icon-${size}.png"
  done
  cp "$out/icon-180.png" "$out/apple-touch-icon.png"
  cp "$out/icon-16.png"  "$out/favicon-16.png"
  cp "$out/icon-32.png"  "$out/favicon-32.png"
  cp "$out/icon-48.png"  "$out/favicon-48.png"
  convert "$out/favicon-16.png" "$out/favicon-32.png" "$out/favicon-48.png" \
          "$out/favicon.ico"
  rm "$out/master-1024.png"
}

gen_suite static/brand/fusioncore/source.png      fusioncore
gen_suite static/brand/bob-registered/source.png  bob-registered
gen_suite static/brand/k8sstormcenter/source.png  k8sstormcenter
```

Both `rsvg-convert` (librsvg2-bin) and `convert` (ImageMagick) are in apt.

---

## Don'ts

- Do not introduce alternative palettes ("BoB green" etc.) without updating
  `biz/talks/BRAND.md` first — consistent messaging is a named pain point.
- Do not stretch, recolour, or add drop-shadows to the logomark.
- Do not place the dark logomark on coral or pink. It belongs on white,
  cream, or FusionCore deep purple.
- Do not load Google Fonts or external fonts. The site is privacy-clean.
