# NFAC Report Automation — Project Proposal

Static Vue 3 proposal/presentation for Premier Fitness: automating NFAC fitness-amenity
assessment reports (Jotform evaluation → automated scoring → benchmarked dashboard report).

**Live:** https://userdevaccount1.github.io/premier-fitness-proposal/

## Stack

- Vue 3 + Vite, no UI framework — custom SVG gauges/donuts
- Sample data in `src/data/*.json` (Broadstone from the NFAC scoring spreadsheet, Westin from the target design)
- Deployed to GitHub Pages from the `gh-pages` branch (branch/legacy build)

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
# or
docker build -t premier-fitness-proposal .
docker run -d -p 8088:80 premier-fitness-proposal
```
