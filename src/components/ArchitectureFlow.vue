<script setup>
const steps = [
  {
    n: '01',
    title: 'Mobile Evaluation Form',
    tool: 'Jotform (rebuilt)',
    desc: 'Per-equipment inspection loop rebuilt to mirror the scoring framework 1:1 — every yes/no, rubric and photo prompt feeds the engine. Works offline-friendly on a phone in 10–15 min.',
  },
  {
    n: '02',
    title: 'Submission Webhook',
    tool: 'Jotform → n8n',
    desc: 'Every completed evaluation fires instantly into an automation workflow. Photos and videos are captured, renamed and filed per property automatically.',
  },
  {
    n: '03',
    title: 'NFAC Scoring Engine',
    tool: 'Code node · versioned rules',
    desc: 'All 6 categories calculated exactly per your framework — severity deductions, 1–5 rubrics, weights, final ÷6. Deterministic: same inputs, same grade, any technician.',
  },
  {
    n: '04',
    title: 'Benchmark Database',
    tool: 'PostgreSQL database',
    desc: 'Every evaluation stored. Each new property is ranked against your full history — overall and per category, filtered by property type and market. Your data moat grows with every visit.',
  },
  {
    n: '05',
    title: 'Report Generation',
    tool: 'Vue template → web + PDF',
    desc: 'The dashboard you saw above, generated automatically: an interactive link to share up the chain, and a pixel-perfect PDF for email. Photos and evidence embedded.',
  },
  {
    n: '06',
    title: 'Delivery',
    tool: 'Email / CRM',
    desc: 'Report delivered to the prospect (and your sales pipeline) automatically, minutes after the technician taps submit in the parking lot.',
  },
]
</script>

<template>
  <section id="architecture" class="arch">
    <div class="wrap">
      <span class="kicker">Proposed Approach</span>
      <h2 class="section-title">The Automation Pipeline</h2>
      <p class="section-sub">
        Six stages, zero manual steps between the technician's phone and the customer's inbox.
        Built on proven, low-cost tools your team can see into and own — no black box.
      </p>

      <div class="flow">
        <div v-for="(s, i) in steps" :key="s.n" class="step-wrap">
          <div class="card step">
            <span class="num">{{ s.n }}</span>
            <h3>{{ s.title }}</h3>
            <span class="tool">{{ s.tool }}</span>
            <p>{{ s.desc }}</p>
          </div>
          <div v-if="i < steps.length - 1" class="connector" aria-hidden="true">▸</div>
        </div>
      </div>

      <div class="why card">
        <h4>Why this stack</h4>
        <div class="why-grid">
          <div><strong>Keeps Jotform</strong><span>Your team already drafted the form — we refine it, not replace your workflow.</span></div>
          <div><strong>n8n automation</strong><span>Visual workflows you can watch run; no per-task fees like Zapier at volume.</span></div>
          <div><strong>Versioned scoring</strong><span>Framework changes are code changes — auditable, testable, reversible.</span></div>
          <div><strong>Web + PDF output</strong><span>Interactive link impresses executives; PDF fits your current sales motion.</span></div>
        </div>
      </div>
    </div>
  </section>
</template>

<style scoped>
.arch { background: var(--bg); }
.flow {
  display: grid;
  grid-template-columns: repeat(3, 1fr);
  gap: 18px;
}
.step-wrap { position: relative; display: flex; }
.step { padding: 24px; flex: 1; display: flex; flex-direction: column; }
.num {
  font-family: var(--font-cond);
  font-weight: 800;
  font-size: 1rem;
  color: #fff;
  background: var(--red);
  border-radius: 6px;
  padding: 2px 10px;
  align-self: flex-start;
  margin-bottom: 12px;
}
.step h3 {
  font-family: var(--font-cond);
  text-transform: uppercase;
  letter-spacing: 0.04em;
  font-size: 1.2rem;
  color: var(--navy);
  line-height: 1.15;
}
.tool {
  font-size: 0.8rem;
  font-weight: 600;
  color: var(--blue);
  text-transform: uppercase;
  letter-spacing: 0.06em;
  margin: 6px 0 10px;
}
.step p { font-size: 0.9rem; color: var(--muted); }
.connector {
  position: absolute;
  right: -16px;
  top: 50%;
  transform: translateY(-50%);
  color: var(--red);
  font-size: 1.3rem;
  z-index: 1;
}
.step-wrap:nth-child(3n) .connector { display: none; }
.why { margin-top: 30px; padding: 26px 30px; }
.why h4 {
  font-family: var(--font-cond);
  text-transform: uppercase;
  letter-spacing: 0.08em;
  color: var(--navy);
  font-size: 1.1rem;
  margin-bottom: 16px;
}
.why-grid { display: grid; grid-template-columns: repeat(4, 1fr); gap: 20px; }
.why-grid div { display: flex; flex-direction: column; gap: 4px; }
.why-grid strong { color: var(--red); font-family: var(--font-cond); text-transform: uppercase; letter-spacing: 0.04em; }
.why-grid span { font-size: 0.87rem; color: var(--muted); }
@media (max-width: 960px) {
  .flow { grid-template-columns: 1fr; }
  .connector { display: none; }
  .why-grid { grid-template-columns: 1fr 1fr; }
}
@media (max-width: 560px) {
  .why-grid { grid-template-columns: 1fr; }
}
</style>
