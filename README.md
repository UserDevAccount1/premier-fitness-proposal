# NFAC Report Automation — Proposal & Dashboard

Interactive slide-deck proposal + working analytics dashboard for **Premier Fitness**'s
NFAC (National Fitness Amenity Council™) initiative.

**Live:** https://userdevaccount1.github.io/premier-fitness-proposal/
**Calculation knowledge base:** [docs/NFAC-Scoring-Calculation-Insight.pdf](docs/NFAC-Scoring-Calculation-Insight.pdf)

---

## The Goal

Premier Fitness — a fitness equipment service company (maintenance, repair, diagnostics for
apartment communities and hotels) — is turning its free on-site safety evaluation campaign into
an **education and data authority play**: become the recognized authority on fitness amenity
condition, safety, and education for its clientele base, and reach the decision-makers
*above* the property manager.

## The Vision

Every property visited gets:

1. A real **NFAC Score™** (0–100, graded A–F) calculated from a codified 6-category framework
2. A **benchmark ranking** against every other property evaluated — by property type and market
3. A **customer-ready report** — interactive dashboard link + print-ready PDF — generated
   automatically minutes after the technician submits the on-site evaluation form

No more 15–20 minutes of manual Canva work per location. Every evaluation grows a benchmark
dataset nobody else in the space has.

## How Scoring Works (summary)

Six categories, each /100, averaged:

| Category | Raw scale | Weight | Source inputs |
|---|---|---|---|
| Safety & Risk | severity tier (100/94/84/69/49/25) | direct | equipment inspection findings |
| Asset Condition | 5 metrics × 1–5 = /25 | × 4 | readiness, cosmetics, lifecycle, maintenance, stewardship |
| User Experience | 4 metrics × 1–5 = /20 | × 5 | cleanliness, comfort, layout, aesthetics |
| Utilization | 4 metrics × 1–5 = /20 | × 5 | wear patterns, selection, space, throughput |
| Exercise Coverage | 10 modalities × 0/1 | × 10 | movement category presence |
| Sanitation Readiness | 1 rubric × 1–5 | × 20 | sanitizer/wipes availability |

**FINAL = sum ÷ 6.** Validated against the framework's sample grade:
(49 + 68 + 90 + 95 + 100 + 100) ÷ 6 = **83.67 → B-** (Broadstone Archive).

Full formulas, deduction tiers, rubrics, the worked example, and the calculation-integrity
checklist are in the **[Calculation Insight PDF](docs/NFAC-Scoring-Calculation-Insight.pdf)**
(regenerate with `python docs/generate_insight_pdf.py`).

## What Needs to Be Done (project roadmap)

- [x] **Proposal + working dashboard demo** (this repo) — live on GitHub Pages
- [x] **Scoring model decoded** from NFAC Scoring Framework v2 spreadsheet
- [x] **Calculation knowledge base** documented (insight PDF)
- [ ] **Phase 1 (wk 1–2):** Rebuild Jotform to mirror the framework 1:1 — per-equipment
      inspection loop, photo prompts, validation; field-test with technicians
- [ ] **Phase 2 (wk 2–3):** Codify the scoring engine (all 6 categories + severity tiers);
      Supabase benchmark database schema + percentile logic
- [ ] **Phase 3 (wk 3–5):** Jotform → n8n webhook automation, media handling; report
      generation (web + PDF); automated delivery
- [ ] **Phase 4 (wk 5–6):** Backfill past evaluations into the benchmark DB; branding pass;
      documentation + training; handoff

## Tech Stack

Jotform (field capture) · n8n self-hosted (automation) · **Supabase** (benchmark database) ·
Hostinger VPS (hosting) · Vue 3 + Vite (dashboard/report rendering) · Docker (deployment) ·
Claude Code (AI-assisted development) · GitHub (versioning + Pages hosting)

## This Repo

- Vue 3 + Vite slide-deck presentation (arrow keys / swipe / tab navigation)
- Live NFAC dashboard demo with two sample properties (Broadstone 83.67 from the framework
  spreadsheet, Westin 67.5 from the target design) — property switcher demonstrates benchmarking
- Sample data in `src/data/*.json` — demonstrates the "form data in → report out" model
- `docs/` — calculation insight PDF + generator script

## Develop

```bash
npm install
npm run dev
npm run build   # production build to dist/ (GitHub Pages subpath base)
```

## Docker

Container serves the site at root via nginx (built with `BASE_PATH=/`):

```bash
docker compose up -d --build   # http://localhost:8088
```

## Deploy

> **Note:** The Actions workflow (`.github/workflows/deploy.yml`) is disabled because the
> GitHub account is currently billing-locked, which blocks all Actions runners. Once billing
> is resolved at github.com/settings/billing, re-enable it (`gh workflow enable "Deploy to
> GitHub Pages"`) and switch Pages back to the workflow build. Until then, redeploy manually:
>
> ```bash
> npm run build
> cd dist && git init -b gh-pages && git add -A && git commit -m "deploy" \
>   && git push -f https://github.com/UserDevAccount1/premier-fitness-proposal.git gh-pages
> cd .. && rm -rf dist/.git
> ```
