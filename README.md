# Govind Prabhu — Portfolio (handoff for Claude Code)

## TL;DR for Claude Code
`public/index.html` is a **finished, self-contained, production-ready build** (all JS inlined; only Google Fonts load remotely). The primary task is to **deploy it to Vercel as a static site**. Porting to Next.js is optional (see "Optional: port to Next.js").

### Deploy (do this)
```bash
cd govind-portfolio-handoff
npx vercel login            # if not logged in
npx vercel --prod --yes     # vercel.json serves public/ as static output
```
Suggested project name: `govind-prabhu`. Report the production URL back to the user.

Recommended (auto-redeploys on push):
```bash
git init && git add -A && git commit -m "Portfolio v1"
gh repo create govindprabhu03/portfolio --public --source=. --push
npx vercel link --yes && npx vercel git connect --yes
```

Post-deploy checks: page loads with no console errors; ⌘K / Ctrl+K opens the command palette; Siemens Lab demos respond; KalaSphere tenant/role switcher works; Projects filter works; all external links open (GitHub, live demos, LinkedIn, mailto, tel).

## Files
- `public/index.html` — deployable bundle (do not hand-edit; it's compiled).
- `design/portfolio.dc.html` + `design/support.js` — editable source (open `portfolio.dc.html` in a browser via any static server to view). All content data lives in the `<script data-dc-script>` block: `TOOLS`, `PROJECTS`, `MODS`, `SKILLS`, `USES/PUSE`, leadership, contact.
- `vercel.json` — static config + security headers.

## Content rules (from the owner)
- Never mention "Ravindra Bhavan Sankhali" anywhere. KalaSphere-AI is described generically as "a multi-tenant ERP for cultural institutions".
- Demo data in Siemens Lab and KalaSphere tenants (Natya Academy, Sur School of Music, Rang Arts Centre) is illustrative and labelled as such.
- 13 repos exist on GitHub; 6 are featured. To add more, append to `PROJECTS` (fields: name, status, tags, kind, one, desc, live?, repo, steps[], decisions[{t,d}], stack[], role?, exIn?, exOut?).

## Optional: port to Next.js
If asked to rebuild in a framework: Next.js App Router + TypeScript, one page, client components per section. The HTML is a **high-fidelity** reference — match it exactly.

**Sections (in order):** sticky header (logo, nav, ⌘K button) → hero (headline + "system map" card) → stats strip → 01 Siemens Lab (6 tools, each with Before/Built/Result + interactive demo) → 02 KalaSphere-AI (light section; tenant + role switcher drives a mock app with RBAC-locked modules and a live RLS SQL snippet) → 03 Projects (filter chips, list + detail: how-it-works pipeline with cycling highlight every 1.4s, example, key decisions, stack, links) → 04 Stack (skill chips; selecting shows "Used in" links that jump to the tool/project) → 05 Education / 06 Leadership → 07 Contact (form builds a live JSON preview; submit opens mailto) → footer. Command palette: ⌘/Ctrl+K toggles, Esc closes, Enter runs first match.

**Responsive:** split panels are `flex-wrap` with `flex:1 1 280px` (list) and `flex:3 1 560px` (detail); header nav hides below 1000px.

### Design tokens
- Dark bg `#0f1012`, raised `#131417`, panel `#16171a`, panel-2 `#1d1f23`, inset `#121316`, lines `#22242a` / `#2a2c31` / `#3a3c42`
- Text `#ecebe6`, secondary `#b9b8b1`, muted `#9b9a94`, dim `#6c6b66`
- Accent lime `#c8f560` (hover `#ddff7a`, tint bg `#1f2614`, tint border `#3d4a1e`); warn `#ff7a59`; caution `#ffc861`
- Light section bg `#f2f0e9`, ink `#141416`, body `#3c3b38`, accent `#4d6b12`, borders `#d9d6cc`
- Fonts (Google): **Instrument Serif** (display headlines, italic accents), **Archivo** 400–800 (UI/body), **IBM Plex Mono** 400–600 (labels, code, metadata; 11–13px, letter-spacing .1–.14em uppercase for kickers)
- Display sizes: h1 `clamp(52px,7.4vw,112px)/.92`; section h2 `clamp(44px,6vw,84px)/.95`; card titles Archivo 800 26–42px, letter-spacing -.02em
- Radii: 6–9px chips/buttons, 10–12px cards, 16px panels, 999px pills. Max content width 1280px; side padding `clamp(16px,4vw,40px)`; section padding ~110px top.

## Assets
None besides Google Fonts. No images. Favicon: optionally add a 32×32 lime (`#c8f560`) rounded square with "GP" in `#0f1012`.

## Rebuilding the bundle after editing the source
Edit `design/portfolio.dc.html`, then run:
```bash
python -I scripts/build.py   # rewrites public/index.html (loader, React, fonts come from design/bundle-base.html + design/fonts.css)
```
Commit and push; Vercel redeploys `public/` automatically.
