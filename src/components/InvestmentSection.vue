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
          <div class="rate-num">$12–20<small>/hr</small></div>
          <div class="avail">
            <strong>Up to 40 hrs/week</strong>
            <span>maximum weekly workload</span>
          </div>
          <span class="rate-note">Weekly time reports · weekly review checkpoints</span>
        </div>
        <div class="card est">
          <h3>Build — Estimated Effort</h3>
          <div class="rows">
            <div><span>Phase 1 — Discovery &amp; form rebuild</span><strong>20–30 hrs</strong></div>
            <div><span>Phase 2 — Scoring engine</span><strong>20–30 hrs</strong></div>
            <div><span>Phase 3 — Automation &amp; reports</span><strong>25–35 hrs</strong></div>
            <div><span>Phase 4 — Benchmarking &amp; handoff</span><strong>15–25 hrs</strong></div>
            <div class="total"><span>Total build estimate</span><strong>80–120 hrs · $960–$2,400</strong></div>
          </div>
          <div class="review-note">
            <strong>Review &amp; adjust — built in.</strong>
            Every phase ends with your review, and hours/scope adjust from that feedback.
            Calendar weeks can shift because they depend on review cycles — but every phase
            kickoff commits to a <em>specific delivery timeline for its output</em>, so you
            always know exactly what lands and when. Work is billed up to a
            <em>maximum of 40 hrs/week</em>.
          </div>
        </div>
        <div class="card incl">
          <h3>Included in the Build</h3>
          <ul>
            <li>All development, testing &amp; deployment</li>
            <li>Documentation &amp; team training</li>
            <li>2 weeks post-launch support</li>
            <li>You own everything — accounts, code, data</li>
          </ul>
          <h3 class="ongoing">Ongoing Maintenance Fee</h3>
          <div class="maint">
            <div class="maint-row"><span>Monthly retainer (up to 10 hrs)</span><strong>$150–$200/mo</strong></div>
            <div class="maint-row"><span>Extra work beyond retainer</span><strong>$12–20/hr</strong></div>
            <div class="maint-row"><span>Runtime tooling (Jotform + VPS)</span><strong>~$10–50/mo</strong></div>
          </div>
          <p>
            Covers framework updates, report tweaks, monitoring and fixes — so the system
            keeps pace as your evaluation campaign scales.
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
.rate-num { font-family: var(--font-cond); font-weight: 800; font-size: 3.6rem; line-height: 1; margin: 10px 0; }
.rate-num small { font-size: 1.3rem; opacity: 0.75; font-weight: 600; }
.avail {
  background: rgba(255, 255, 255, 0.1);
  border: 1px solid rgba(255, 255, 255, 0.2);
  border-radius: 8px;
  padding: 8px 18px;
  margin: 6px 0 12px;
  display: flex;
  flex-direction: column;
}
.avail strong { font-family: var(--font-cond); font-weight: 800; font-size: 1.3rem; }
.avail span { font-size: 0.78rem; opacity: 0.75; }
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
.review-note {
  margin-top: 14px;
  font-size: 0.86rem;
  color: var(--muted);
  background: var(--bg);
  border-left: 4px solid var(--red);
  border-radius: 0 8px 8px 0;
  padding: 12px 16px;
}
.review-note strong { color: var(--navy); }
.review-note em { color: var(--red); font-style: normal; font-weight: 700; }
.incl ul { list-style: none; display: flex; flex-direction: column; gap: 8px; margin-bottom: 18px; }
.incl li { padding-left: 22px; position: relative; font-size: 0.92rem; color: var(--ink); }
.incl li::before { content: '✓'; position: absolute; left: 0; color: var(--green); font-weight: 800; }
.ongoing { margin-top: 4px; }
.maint { display: flex; flex-direction: column; margin-bottom: 10px; }
.maint-row {
  display: flex;
  justify-content: space-between;
  gap: 10px;
  padding: 7px 0;
  border-bottom: 1px solid var(--line);
  font-size: 0.88rem;
}
.maint-row span { color: var(--muted); }
.maint-row strong { color: var(--red); white-space: nowrap; }
.incl p { font-size: 0.85rem; color: var(--muted); }
@media (max-width: 960px) { .grid { grid-template-columns: 1fr; } }
</style>
