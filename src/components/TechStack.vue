<template>
  <section id="stack" class="stack">
    <div class="wrap">
      <span class="kicker">Tech Stack</span>
      <h2 class="section-title">Tools &amp; Infrastructure</h2>
      <p class="section-sub">
        Proven, low-cost tools — nothing exotic, nothing locked in. Everything runs on
        infrastructure you own, with total runtime cost around $10–50/month.
      </p>

      <div class="grid">
        <div v-for="t in tools" :key="t.name" class="card tool">
          <div class="tool-head">
            <span class="tool-icon" :style="{ background: t.color }">{{ t.icon }}</span>
            <div>
              <h3>{{ t.name }}</h3>
              <span class="tool-role">{{ t.role }}</span>
            </div>
          </div>
          <p>{{ t.desc }}</p>
          <span class="tool-cost">{{ t.cost }}</span>
        </div>
      </div>
    </div>
  </section>
</template>

<script setup>
const tools = [
  {
    name: 'Jotform',
    icon: 'J',
    color: '#ff6100',
    role: 'Field data capture',
    desc: 'Your existing mobile evaluation form, rebuilt to mirror the scoring framework 1:1 with per-equipment loops and photo prompts.',
    cost: 'Free tier – $39/mo',
  },
  {
    name: 'n8n (self-hosted)',
    icon: 'n8n',
    color: '#ea4b71',
    role: 'Automation engine',
    desc: 'Receives every submission via webhook, runs the scoring engine, files media, and triggers report generation. Visual workflows you can inspect.',
    cost: '$0 license — self-hosted',
  },
  {
    name: 'Hostinger VPS',
    icon: 'H',
    color: '#673de6',
    role: 'Hosting',
    desc: 'One low-cost VPS runs n8n, the PostgreSQL benchmark database, and the report service — all containerized with Docker.',
    cost: '~$5–10/mo',
  },
  {
    name: 'Supabase',
    icon: 'SB',
    color: '#3ecf8e',
    role: 'Benchmark database',
    desc: 'Managed Postgres storing every evaluation — percentile rankings by property type and market, instant APIs, auth-ready if a client portal comes later.',
    cost: 'Free tier – $25/mo',
  },
  {
    name: 'Vue 3 + Vite',
    icon: 'V',
    color: '#42b883',
    role: 'Report rendering',
    desc: 'The dashboard you are looking at right now — generated per property as an interactive web link and a print-ready PDF.',
    cost: 'Open source',
  },
  {
    name: 'Docker',
    icon: '🐳',
    color: '#1d63ed',
    role: 'Deployment',
    desc: 'Every service ships as a container — reproducible deploys, easy rollback, portable to any host if you ever migrate.',
    cost: 'Open source',
  },
  {
    name: 'Claude Code (AI)',
    icon: 'AI',
    color: '#c8722c',
    role: 'Development accelerator',
    desc: 'AI-assisted development for faster builds, plus optional AI-drafted narrative summaries in reports (executive summary text per property).',
    cost: 'Dev tooling',
  },
  {
    name: 'GitHub',
    icon: 'GH',
    color: '#24292f',
    role: 'Code & versioning',
    desc: 'All code version-controlled and owned by you. Scoring framework changes are tracked, auditable, reversible.',
    cost: 'Free',
  },
]
</script>

<style scoped>
.stack { background: var(--bg); }
.grid { display: grid; grid-template-columns: repeat(4, 1fr); gap: 16px; }
.tool { padding: 20px; display: flex; flex-direction: column; }
.tool-head { display: flex; align-items: center; gap: 12px; margin-bottom: 10px; }
.tool-icon {
  width: 42px; height: 42px;
  border-radius: 10px;
  color: #fff;
  display: flex; align-items: center; justify-content: center;
  font-family: var(--font-cond);
  font-weight: 800;
  font-size: 0.95rem;
  flex-shrink: 0;
}
.tool h3 { font-family: var(--font-cond); text-transform: uppercase; letter-spacing: 0.04em; font-size: 1.05rem; color: var(--navy); line-height: 1.1; }
.tool-role { font-size: 0.74rem; color: var(--red); font-weight: 700; text-transform: uppercase; letter-spacing: 0.06em; }
.tool p { font-size: 0.85rem; color: var(--muted); flex: 1; }
.tool-cost {
  margin-top: 12px;
  font-size: 0.8rem;
  font-weight: 700;
  color: var(--navy);
  background: var(--bg);
  border: 1px solid var(--line);
  border-radius: 999px;
  padding: 4px 12px;
  align-self: flex-start;
}
@media (max-width: 1020px) { .grid { grid-template-columns: repeat(2, 1fr); } }
@media (max-width: 560px) { .grid { grid-template-columns: 1fr; } }
</style>
