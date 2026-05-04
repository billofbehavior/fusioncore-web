# Private content via Git submodules

This site is intentionally public. When some content needs to be more tightly
held than the parent repo allows — a draft spec, an unreleased prospectus,
client-confidential FusionCore material — it lives in a **separate private
repo**, mounted into the Hugo `content/` tree as a Git submodule.

The pattern is reusable: today it's used (or about to be) for
`content/bob/docs/drafts/`. Tomorrow the same recipe applies to
`content/fusioncore/private/` or any other path.

---

## Why submodules instead of branches or marketing-shortcode tricks?

| Approach | Why we didn't pick it |
|----------|----------------------|
| Branches | Sensitive material is still in the parent repo's git history. Anyone with read access to the repo (now or later — including a leaked clone or an old contractor) can recover it. |
| Markdown front-matter `draft: true` | Hugo skips drafts on production build, but the source is still in the repo. Same problem as branches. |
| Build-time fetch from a non-Git source | Adds a second deploy mechanism, complicates rollbacks. |
| **Submodule pointing at a private repo** | Source lives in a *different* repo with its *own* access list. Public clones of the parent never see it. CI fetches via a scoped read-only deploy key. |

The submodule pattern also keeps the public repo honest: a casual reader
can see exactly which paths are private (the gitlinks in
`.gitmodules`) without learning anything about their contents.

---

## Recipe (~10 minutes once)

### 0. Decide the layout

| Field | Example for the bob-drafts case | For a future fusioncore case |
|-------|--------------------------------|-----------------------------|
| Slug | `bob-drafts` | `fusioncore-private` |
| Private repo URL | `git@github.com:billofbehavior/private-bob-drafts.git` | `git@github.com:billofbehavior/fusioncore-private.git` |
| Mount path | `content/bob/docs/drafts` | `content/fusioncore/private` |

### 1. Create the private repo on GitHub

```sh
gh repo create billofbehavior/private-bob-drafts --private \
  --description "Bill of Behavior draft specs — private"
```

### 2. Generate the deploy keypair

From this repo's root:

```sh
scripts/setup-private-submodule.sh --keys bob-drafts
```

The script:

- generates `~/.ssh/submodule-bob-drafts{,.pub}`
- prints both halves with paste instructions

### 3. Wire the keys

- **Public key** → private repo → Settings → Deploy keys → Add deploy key.
  **Leave "Allow write access" UNCHECKED** (read-only is enough; minimum
  privilege).
- **Private key** → THIS repo (`billofbehavior/fusioncore-web`) → Settings
  → Secrets and variables → Actions → New repository secret named
  **`SUBMODULE_DEPLOY_KEY`**. If the secret already exists from a previous
  submodule, REPLACE its value with the new private key concatenated with
  the previous one — `ssh-agent` loads every key in the multi-line value
  and tries them in order.

### 4. Move existing private content into the new private repo

If the content already exists somewhere in this repo (e.g.,
`content/bob/docs/drafts/spec-stackprofile-v0.0.1.md`):

```sh
mkdir /tmp/private-bob-drafts && cd $_
git init -b main
# Copy or `git mv` the existing files INTO this fresh repo
cp ~/fusioncore-web/content/bob/docs/drafts/spec-*.md .
git add .
git commit -m "initial private bob drafts"
git remote add origin git@github.com:billofbehavior/private-bob-drafts.git
git push -u origin main

# Now remove the originals from the parent repo
cd ~/fusioncore-web
git rm content/bob/docs/drafts/*.md
# Don't commit yet — the git submodule add will replace this dir
```

### 5. Add the submodule

```sh
scripts/setup-private-submodule.sh --add bob-drafts \
  git@github.com:billofbehavior/private-bob-drafts.git \
  content/bob/docs/drafts

git add .gitmodules content/bob/docs/drafts
git commit -m "add private submodule: bob-drafts"
git push
```

### 6. Verify CI

Push a commit. The `.github/workflows/deploy.yml` workflow:

- loads `SUBMODULE_DEPLOY_KEY` into `ssh-agent` (only if the secret is
  set — no-op for forks / first-time setups)
- runs `actions/checkout` with `submodules: recursive`, which uses the
  loaded SSH key to clone the private submodule
- builds Hugo as normal, with the private content materialized at the
  mount path

If the build fails with `Permission denied (publickey)`:

- the deploy key isn't accepted by the private repo (re-paste the public
  key, check "Allow read access")
- or the private key in `SUBMODULE_DEPLOY_KEY` doesn't match
- or there's a stray indentation in the multi-line secret (paste the key
  block exactly, including `-----BEGIN OPENSSH PRIVATE KEY-----` and
  `-----END OPENSSH PRIVATE KEY-----`)

---

## Day-to-day

### Editing private content

```sh
cd content/bob/docs/drafts        # this is now its own git repo
$EDITOR spec-stackprofile-v0.0.2.md
git add . && git commit -m "v0.0.2 draft"
git push                          # pushes to the PRIVATE repo

cd $REPO_ROOT
git add content/bob/docs/drafts   # bumps the gitlink in the parent
git commit -m "bump bob-drafts submodule"
git push                          # parent CI rebuilds, picks up new content
```

### Pulling someone else's update

```sh
git submodule update --remote --merge
```

### Inspecting a fresh clone

A new contributor cloning the parent without the deploy key sees
`content/bob/docs/drafts/` as an empty directory. Hugo will skip the
content. The site still builds locally — they just won't render the
private pages.

---

## Layered access gating

A submodule keeps the **source** private but the **rendered output** is
still public on whatever host serves the site. For the rendered side,
two layers stack:

1. **Client-side gate (already in use)** — the `passwordgate` Hugo
   shortcode hides the content body behind a hashed password until the
   reader enters it. Source-of-truth: `layouts/shortcodes/passwordgate.html`.
   Real obfuscation, not server-side enforcement; sufficient for "casual"
   gating.
2. **Server-side gate** — once the site is hosted on Apache/LiteSpeed
   (Namecheap shared hosting, post-cutover), drop an `.htaccess` +
   `.htpasswd` pair into `static/bob/docs/drafts/` and the host will
   refuse the directory without HTTP Basic auth. GitHub Pages and
   Cloudflare Pages don't honor `.htaccess` — for those, use Cloudflare
   Access (zero-trust auth at the edge) instead.

Server-side gate template (Apache) lives at
`static/bob/docs/drafts/.htaccess` (kept in repo, public — points at a
`.htpasswd` file generated separately and uploaded to the host out-of-
band).

---

## Reusing this pattern for `fusioncore.ai` private content

Same recipe, different slug + path:

```sh
scripts/setup-private-submodule.sh --keys fusioncore-private
# wire deploy key + secret (append new private key to SUBMODULE_DEPLOY_KEY)
scripts/setup-private-submodule.sh --add fusioncore-private \
  git@github.com:billofbehavior/fusioncore-private.git \
  content/fusioncore/private
```

The workflow already supports multiple keys via the multi-line secret;
no CI changes needed.

---

## Don'ts

- ❌ Do not put the private SSH key into the parent repo — only into the
  `SUBMODULE_DEPLOY_KEY` secret.
- ❌ Do not check "Allow write access" on the deploy key — read-only is
  enough and limits blast radius if the key leaks.
- ❌ Do not `git rm --cached` the gitlink without also removing the
  `.gitmodules` entry — leaves the parent confused.
- ❌ Do not assume client-side `passwordgate` is real security. If the
  content is genuinely sensitive, gate it server-side too.
