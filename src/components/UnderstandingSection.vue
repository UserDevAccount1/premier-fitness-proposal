<template>
  <section class="understanding">
    <div class="wrap">
      <span class="kicker">The Objective</span>
      <h2 class="section-title">What You're Building — As I Understand It</h2>
      <p class="section-sub">
        Premier Fitness is turning a door-to-door safety evaluation campaign into an
        education and data authority play: every property you visit gets a real grade,
        benchmarked against every other property you've evaluated.
      </p>

      <div class="grid">
        <div class="card col">
          <h3>Today</h3>
          <ul>
            <li>Technician evaluates on site, notes in a doc</li>
            <li>Findings rebuilt by hand in Canva — 15–20 min per location</li>
            <li>One-off safety report, no score, no comparison</li>
            <li>Grading lives in a spreadsheet, calculated manually</li>
          </ul>
        </div>
        <div class="arrow" aria-hidden="true">→</div>
        <div class="card col highlight">
          <h3>The Target State</h3>
          <ul>
            <li>Mobile form drives the entire on-site evaluation</li>
            <li>Submission triggers automated NFAC scoring — all 6 categories</li>
            <li>Property benchmarked against your full evaluation history</li>
            <li>Branded, presentation-quality report generated in minutes</li>
          </ul>
        </div>
      </div>

      <div class="materials card">
        <h4>Reviewed to prepare this proposal</h4>
        <div class="chips">
          <span>NFAC Scoring Framework v2 (both sheets, incl. sample grade)</span>
          <span>Broadstone Archive safety audit report (10 pages)</span>
          <span>Target dashboard design (5-page NFAC report)</span>
          <span>Sample Jotform (per-equipment inspection flow)</span>
          <span>Loom walkthrough (full video)</span>
        </div>
      </div>
    </div>
  </section>
</template>

<style scoped>
.grid {
  display: grid;
  grid-template-columns: 1fr auto 1fr;
  align-items: stretch;
  gap: 22px;
}
.col { padding: 28px; }
.col h3 {
  font-family: var(--font-cond);
  text-transform: uppercase;
  letter-spacing: 0.06em;
  color: var(--navy);
  font-size: 1.3rem;
  margin-bottom: 14px;
}
.col ul { list-style: none; display: flex; flex-direction: column; gap: 10px; }
.col li { padding-left: 24px; position: relative; color: var(--muted); }
.col li::before { content: '•'; position: absolute; left: 8px; color: var(--red); font-weight: 800; }
.highlight { border-top: 4px solid var(--red); }
.highlight li { color: var(--ink); }
.arrow {
  align-self: center;
  font-size: 2rem;
  color: var(--red);
  font-weight: 800;
}
.materials { margin-top: 26px; padding: 22px 26px; }
.materials h4 {
  font-family: var(--font-cond);
  text-transform: uppercase;
  letter-spacing: 0.09em;
  color: var(--muted);
  font-size: 0.95rem;
  margin-bottom: 12px;
}
.chips { display: flex; flex-wrap: wrap; gap: 10px; }
.chips span {
  background: var(--bg);
  border: 1px solid var(--line);
  border-radius: 999px;
  padding: 6px 14px;
  font-size: 0.86rem;
  color: var(--navy);
  font-weight: 500;
}
@media (max-width: 860px) {
  .grid { grid-template-columns: 1fr; }
  .arrow { transform: rotate(90deg); justify-self: center; }
}
</style>
