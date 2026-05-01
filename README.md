# fusioncore-web

Source for <https://fusioncore.ai>. Built with [Hugo](https://gohugo.io/) — a
single Go binary, no Node toolchain.

## Stack

- **Hugo extended** (≥ 0.123)
- Custom in-tree theme (templates live directly under `layouts/` — no theme
  module to track)
- System fonts only — no Google Fonts, no JS, no cookies

## Layout

```
fusioncore-web/
├── hugo.toml            site config + content params
├── content/
│   └── _index.md        homepage stub (body comes from layouts/index.html)
├── data/
│   ├── talks.yaml       upcoming + past talks (drives the speaking section)
│   └── trainings.yaml   workshop catalogue
├── layouts/
│   ├── _default/
│   │   └── baseof.html  base HTML shell (head, header, footer)
│   ├── partials/
│   │   ├── header.html  top nav
│   │   └── footer.html  footer + Impressum
│   └── index.html       homepage sections
└── static/
    ├── css/main.css     stylesheet (purple #ad72ff accent on dark hero)
    └── favicon.svg
```

## Local dev

```sh
hugo server -D       # http://localhost:1313/, hot-reload on save
```

## Build

```sh
hugo --gc --minify   # outputs to ./public/
```

## Deployment — GitHub Pages

CI lives in `.github/workflows/deploy.yml`. Every push to `main` builds the
site and deploys it to GitHub Pages.

`static/CNAME` carries `fusioncore.ai`, so Hugo copies it to the root of the
build output and Pages serves the site at the custom domain.

### One-time GitHub setup

1. **Repo → Settings → Pages**
   - **Source:** `GitHub Actions`
   - **Custom domain:** `fusioncore.ai`
   - Enable **Enforce HTTPS** (after the cert provisions, ~10 min)
2. **Repo → Settings → Actions → General**
   - Workflow permissions: `Read and write permissions` (so the deploy job
     can publish the Pages artifact)

### One-time DNS setup (Namecheap)

In the Namecheap dashboard for `fusioncore.ai`, replace any existing parking
or sitebuilder records with:

| Type  | Host | Value                           |
|-------|------|---------------------------------|
| A     | @    | 185.199.108.153                 |
| A     | @    | 185.199.109.153                 |
| A     | @    | 185.199.110.153                 |
| A     | @    | 185.199.111.153                 |
| AAAA  | @    | 2606:50c0:8000::153             |
| AAAA  | @    | 2606:50c0:8001::153             |
| AAAA  | @    | 2606:50c0:8002::153             |
| AAAA  | @    | 2606:50c0:8003::153             |
| CNAME | www  | billofbehavior.github.io.       |

Then **disable Namecheap's PHP sitebuilder** so it stops serving the old
page. After DNS propagates (5–30 min), the workflow's next push will be
live at <https://fusioncore.ai>.

## Editing content

- **Talks** → `data/talks.yaml`. Add / remove entries; the speaking section
  rebuilds.
- **Trainings** → `data/trainings.yaml`.
- **Hero copy / tagline** → `[params]` in `hugo.toml`.
- **Section bodies** → `layouts/index.html` (HTML; the homepage is templated,
  not markdown).
- **Impressum / footer** → `layouts/partials/footer.html`.

## Notes

- This project intentionally uses **no external Hugo theme**. Theme modules
  add maintenance overhead the size of this site does not justify.
- The visual language matches the existing live site (white-on-dark hero,
  purple accent) so the migration is invisible to returning visitors.
- Compatible with the planned billofbehavior.com design language: cream
  background + slate text on the open-standard side; dark hero + purple
  accent on the company side. Both share the same footer treatment and grid.
