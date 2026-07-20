# NFAC Report Automation — Project Proposal

Static Vue 3 proposal/presentation for Premier Fitness: automating NFAC fitness-amenity
assessment reports (Jotform evaluation → automated scoring → benchmarked dashboard report).

**Live:** https://userdevaccount1.github.io/premier-fitness-proposal/

## Stack

- Vue 3 + Vite, no UI framework — custom SVG gauges/donuts
- Sample data in `src/data/*.json` (Broadstone from the NFAC scoring spreadsheet, Westin from the target design)
- Deployed to GitHub Pages via Actions on push to `main`

## Develop

```bash
npm install
npm run dev
npm run build   # production build to dist/
```
