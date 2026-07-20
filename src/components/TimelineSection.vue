<script setup>
const phases = [
  {
    phase: 'Phase 1',
    weeks: 'Weeks 1–2',
    title: 'Discovery & Form Rebuild',
    hours: '~20–30 hrs',
    items: [
      'Kickoff call: lock scoring rules & edge cases',
      'Rebuild Jotform to mirror the framework 1:1',
      'Per-equipment loop, photo prompts, validation',
      'Field-test with your technicians',
    ],
  },
  {
    phase: 'Phase 2',
    weeks: 'Weeks 2–3',
    title: 'Scoring Engine',
    hours: '~20–30 hrs',
    items: [
      'Codify all 6 NFAC categories + severity tiers',
      'Validate against your existing sample grades',
      'Benchmark database schema & percentile logic',
      'Handle partial/edge submissions gracefully',
    ],
  },
  {
    phase: 'Phase 3',
    weeks: 'Weeks 3–5',
    title: 'Automation & Report Generation',
    hours: '~25–35 hrs',
    items: [
      'Jotform → n8n webhook pipeline, media handling',
      'Dashboard report template (web link + PDF)',
      'Automated delivery to prospect & your team',
      'End-to-end test: form submit → report in inbox',
    ],
  },
  {
    phase: 'Phase 4',
    weeks: 'Weeks 5–6',
    title: 'Benchmarking, Polish & Handoff',
    hours: '~15–25 hrs',
    items: [
      'Backfill past evaluations into benchmark DB',
      'Branding pass & report refinements from feedback',
      'Documentation + team training session',
      '2 weeks post-launch support included',
    ],
  },
]
</script>

<template>
  <section id="timeline" class="timeline">
    <div class="wrap">
      <span class="kicker">Timeline</span>
      <h2 class="section-title">4–6 Weeks to Fully Automated</h2>
      <p class="section-sub">
        Phased so you see working output early: the rebuilt form ships in week 2, the first
        auto-generated report by week 4. Each phase ends with something you can put in front of a prospect.
      </p>
      <p class="review-banner">
        <strong>Everything is reviewed &amp; adjusted.</strong> Week ranges are indicative — each phase
        closes with your review, and the plan adjusts from that feedback. What stays fixed: every phase
        kickoff commits to a specific delivery timeline for its output, at a minimum of 40 hrs/week of dedicated work.
      </p>

      <div class="phases">
        <div v-for="(p, i) in phases" :key="p.phase" class="card phase">
          <div class="ph-head">
            <span class="ph-tag">{{ p.phase }}</span>
            <span class="ph-weeks">{{ p.weeks }}</span>
          </div>
          <h3>{{ p.title }}</h3>
          <span class="ph-hours">{{ p.hours }}</span>
          <ul>
            <li v-for="item in p.items" :key="item">{{ item }}</li>
          </ul>
          <div class="ph-bar"><div :style="{ width: ((i + 1) / phases.length) * 100 + '%' }"></div></div>
        </div>
      </div>
    </div>
  </section>
</template>

<style scoped>
.timeline { background: #fff; }
.review-banner {
  background: var(--bg);
  border-left: 4px solid var(--red);
  border-radius: 0 8px 8px 0;
  padding: 14px 18px;
  font-size: 0.92rem;
  color: var(--muted);
  max-width: 860px;
  margin: -20px 0 34px;
}
.review-banner strong { color: var(--navy); }
.phases { display: grid; grid-template-columns: repeat(4, 1fr); gap: 18px; }
.phase { padding: 24px; display: flex; flex-direction: column; }
.ph-head { display: flex; justify-content: space-between; align-items: center; margin-bottom: 12px; }
.ph-tag {
  font-family: var(--font-cond);
  font-weight: 800;
  text-transform: uppercase;
  letter-spacing: 0.06em;
  color: #fff;
  background: var(--navy);
  border-radius: 6px;
  padding: 3px 12px;
  font-size: 0.85rem;
}
.ph-weeks { font-size: 0.8rem; color: var(--muted); font-weight: 600; }
.phase h3 {
  font-family: var(--font-cond);
  text-transform: uppercase;
  letter-spacing: 0.03em;
  font-size: 1.15rem;
  color: var(--navy);
  line-height: 1.2;
}
.ph-hours { font-size: 0.82rem; color: var(--red); font-weight: 700; margin: 4px 0 12px; }
.phase ul { list-style: none; display: flex; flex-direction: column; gap: 8px; flex: 1; }
.phase li { padding-left: 20px; position: relative; font-size: 0.88rem; color: var(--muted); }
.phase li::before { content: '›'; position: absolute; left: 4px; color: var(--red); font-weight: 800; }
.ph-bar { height: 6px; background: var(--line); border-radius: 999px; margin-top: 18px; overflow: hidden; }
.ph-bar div { height: 100%; background: var(--red); border-radius: 999px; }
@media (max-width: 1020px) { .phases { grid-template-columns: 1fr 1fr; } }
@media (max-width: 620px) { .phases { grid-template-columns: 1fr; } }
</style>
