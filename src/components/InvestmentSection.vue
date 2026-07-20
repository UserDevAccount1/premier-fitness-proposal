<template>
  <section id="investment" class="invest">
    <div class="wrap">
      <span class="kicker">Investment</span>
      <h2 class="section-title">Simple Hourly Engagement</h2>
      <p class="section-sub">
        Transparent hourly billing with weekly hour reports — you only pay for work delivered,
        and scope can flex as the project reveals what matters most.
      </p>

      <div class="grid">
        <div class="card rate">
          <span class="rate-label">Rate</span>
          <div class="rate-num">$15<small>/hr</small></div>
          <span class="rate-note">Weekly time reports · no minimums · stop anytime</span>
        </div>
        <div class="card est">
          <h3>Estimated Effort</h3>
          <div class="rows">
            <div><span>Phase 1 — Discovery &amp; form rebuild</span><strong>20–30 hrs</strong></div>
            <div><span>Phase 2 — Scoring engine</span><strong>20–30 hrs</strong></div>
            <div><span>Phase 3 — Automation &amp; reports</span><strong>25–35 hrs</strong></div>
            <div><span>Phase 4 — Benchmarking &amp; handoff</span><strong>15–25 hrs</strong></div>
            <div class="total"><span>Total project estimate</span><strong>80–120 hrs · $1,200–$1,800</strong></div>
          </div>
        </div>
        <div class="card incl">
          <h3>Included</h3>
          <ul>
            <li>All development, testing &amp; deployment</li>
            <li>Documentation &amp; team training</li>
            <li>2 weeks post-launch support</li>
            <li>You own everything — accounts, code, data</li>
          </ul>
          <h3 class="ongoing">Ongoing (optional)</h3>
          <p>
            Maintenance, framework updates and new report types billed at the same rate,
            only when you need them. Runtime tooling costs ≈ $20–40/mo (Jotform + hosting).
          </p>
        </div>
      </div>
    </div>
  </section>
</template>

<style scoped>
.invest { background: var(--bg); }
.grid { display: grid; grid-template-columns: 0.8fr 1.2fr 1fr; gap: 18px; }
.card { padding: 28px; }
.rate {
  background: var(--navy-3);
  border: none;
  color: #fff;
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: center;
  text-align: center;
}
.rate-label {
  font-family: var(--font-cond);
  text-transform: uppercase;
  letter-spacing: 0.14em;
  font-size: 0.9rem;
  opacity: 0.7;
}
.rate-num { font-family: var(--font-cond); font-weight: 800; font-size: 4.2rem; line-height: 1; margin: 10px 0; }
.rate-num small { font-size: 1.4rem; opacity: 0.75; font-weight: 600; }
.rate-note { font-size: 0.85rem; opacity: 0.75; max-width: 220px; }
.est h3, .incl h3 {
  font-family: var(--font-cond);
  text-transform: uppercase;
  letter-spacing: 0.07em;
  color: var(--navy);
  font-size: 1.1rem;
  margin-bottom: 16px;
}
.rows { display: flex; flex-direction: column; }
.rows > div {
  display: flex;
  justify-content: space-between;
  gap: 12px;
  padding: 10px 0;
  border-bottom: 1px solid var(--line);
  font-size: 0.94rem;
}
.rows span { color: var(--muted); }
.rows strong { color: var(--navy); white-space: nowrap; }
.rows .total { border-bottom: none; padding-top: 14px; }
.rows .total span { color: var(--navy); font-weight: 700; }
.rows .total strong { color: var(--red); }
.incl ul { list-style: none; display: flex; flex-direction: column; gap: 8px; margin-bottom: 18px; }
.incl li { padding-left: 22px; position: relative; font-size: 0.92rem; color: var(--ink); }
.incl li::before { content: '✓'; position: absolute; left: 0; color: var(--green); font-weight: 800; }
.ongoing { margin-top: 4px; }
.incl p { font-size: 0.88rem; color: var(--muted); }
@media (max-width: 960px) { .grid { grid-template-columns: 1fr; } }
</style>
