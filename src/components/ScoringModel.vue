<script setup>
const categories = [
  {
    name: 'Safety & Risk',
    weight: '/100',
    method: 'Starts at 100; severity-tiered deductions (100 / 94 / 84 / 69 / 49 / 25) driven by equipment inspection findings.',
    detail: 'Treadmill belt test (5-tier), cable condition (4-tier), e-stop, structure, power — every yes/no in the field checklist maps to a severity tier.',
    color: 'var(--red)',
  },
  {
    name: 'Asset Condition',
    weight: '× 4',
    method: '5 metrics scored 1–5, summed, ×4 → /100.',
    detail: 'Operational readiness, cosmetic condition, equipment lifecycle, preventative maintenance indicators, asset stewardship.',
    color: 'var(--blue)',
  },
  {
    name: 'User Experience',
    weight: '× 5',
    method: '4 metrics scored 1–5, summed, ×5 → /100.',
    detail: 'Cleanliness & care, comfort & environment, layout & accessibility, aesthetic appeal.',
    color: 'var(--blue)',
  },
  {
    name: 'Utilization',
    weight: '× 5',
    method: '4 metrics scored 1–5, summed, ×5 → /100.',
    detail: 'Wear pattern analysis, equipment selection effectiveness, space utilization, throughput capacity vs. property size.',
    color: 'var(--blue)',
  },
  {
    name: 'Exercise Coverage',
    weight: '× 10',
    method: '10 core modalities, present = 1, ×10 → /100.',
    detail: 'Treadmill, elliptical, bike, stepmill, rower, free weights, press, leg curl/ext, pulldown, leg press (functional trainer counts).',
    color: 'var(--green)',
  },
  {
    name: 'Sanitation Readiness',
    weight: '× 20',
    method: 'Single 1–5 rubric, ×20 → /100.',
    detail: 'Hand sanitizer + wipe availability, stock level, and placement throughout the amenity.',
    color: 'var(--green)',
  },
]
</script>

<template>
  <section id="scoring" class="scoring">
    <div class="wrap">
      <span class="kicker">Your Framework, Codified</span>
      <h2 class="section-title">The NFAC Scoring Engine</h2>
      <p class="section-sub">
        Your <strong>NFAC Scoring Framework v2</strong> spreadsheet becomes a versioned scoring
        engine: every rubric, severity tier and weight below was extracted directly from it.
        Change the framework, and every future report follows — no formula left in a spreadsheet.
      </p>

      <div class="formula card">
        <span v-for="(c, i) in categories" :key="c.name" class="f-item">
          <span class="f-cat" :style="{ borderColor: c.color }">{{ c.name }}</span>
          <span v-if="i < categories.length - 1" class="f-op">+</span>
        </span>
        <span class="f-op">÷ 6 =</span>
        <span class="f-result">NFAC Score™</span>
      </div>

      <div class="cat-grid">
        <div v-for="c in categories" :key="c.name" class="card cat-card" :style="{ borderTopColor: c.color }">
          <div class="cat-top">
            <h3>{{ c.name }}</h3>
            <span class="weight">{{ c.weight }}</span>
          </div>
          <p class="method">{{ c.method }}</p>
          <p class="detail">{{ c.detail }}</p>
        </div>
      </div>

      <div class="proof card">
        <div>
          <h4>Validated against your sample grade</h4>
          <p>
            The engine reproduces your Broadstone Archive worksheet exactly:
            (49 + 68 + 90 + 95 + 100 + 100) ÷ 6 = <strong>83.67 → B-</strong>.
            Same inputs, same grade — every time, for every technician.
          </p>
        </div>
        <div class="proof-score">83.67</div>
      </div>
    </div>
  </section>
</template>

<style scoped>
.scoring { background: #fff; }
.formula {
  display: flex;
  flex-wrap: wrap;
  align-items: center;
  gap: 10px;
  padding: 20px 24px;
  margin-bottom: 30px;
  background: var(--navy-3);
  border: none;
}
.f-item { display: inline-flex; align-items: center; gap: 10px; }
.f-cat {
  font-family: var(--font-cond);
  font-weight: 700;
  font-size: 0.88rem;
  letter-spacing: 0.05em;
  text-transform: uppercase;
  color: #fff;
  border: 1.5px solid;
  border-radius: 6px;
  padding: 5px 12px;
}
.f-op { color: rgba(255,255,255,0.6); font-weight: 800; font-size: 1.1rem; }
.f-result {
  font-family: var(--font-cond);
  font-weight: 800;
  font-size: 1.15rem;
  letter-spacing: 0.05em;
  text-transform: uppercase;
  color: #fff;
  background: var(--red);
  border-radius: 6px;
  padding: 6px 16px;
}
.cat-grid { display: grid; grid-template-columns: repeat(3, 1fr); gap: 18px; }
.cat-card { padding: 22px 24px; border-top: 4px solid; }
.cat-top { display: flex; justify-content: space-between; align-items: baseline; margin-bottom: 10px; }
.cat-top h3 {
  font-family: var(--font-cond);
  text-transform: uppercase;
  letter-spacing: 0.05em;
  font-size: 1.15rem;
  color: var(--navy);
}
.weight { font-family: var(--font-cond); font-weight: 800; color: var(--muted); }
.method { font-size: 0.92rem; color: var(--ink); margin-bottom: 8px; }
.detail { font-size: 0.85rem; color: var(--muted); }
.proof {
  margin-top: 28px;
  padding: 26px 30px;
  display: flex;
  justify-content: space-between;
  align-items: center;
  gap: 24px;
  border-left: 5px solid var(--green);
}
.proof h4 {
  font-family: var(--font-cond);
  text-transform: uppercase;
  letter-spacing: 0.07em;
  color: var(--green);
  margin-bottom: 6px;
}
.proof p { color: var(--muted); max-width: 640px; }
.proof strong { color: var(--navy); }
.proof-score {
  font-family: var(--font-cond);
  font-weight: 800;
  font-size: 3.2rem;
  color: var(--navy);
  flex-shrink: 0;
}
@media (max-width: 900px) {
  .cat-grid { grid-template-columns: 1fr; }
  .proof { flex-direction: column; align-items: flex-start; }
}
</style>
