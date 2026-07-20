<script setup>
import { computed } from 'vue'
import broadstone from '../data/broadstone.json'
import westin from '../data/westin.json'

const props = [broadstone, westin]

const avg = (arr) => arr.reduce((a, b) => a + b, 0) / arr.length

const portfolioAvg = computed(() =>
  Math.round((avg(props.map((p) => p.nfacScore)) + Number.EPSILON) * 10) / 10
)

const categoryRows = computed(() =>
  broadstone.categories.map((c, i) => ({
    label: c.label,
    series: [
      { name: 'Broadstone', score: broadstone.categories[i].score, color: 'var(--navy)' },
      { name: 'Westin', score: westin.categories[i].score, color: 'var(--red)' },
      { name: 'Portfolio Avg', score: Math.round(avg([broadstone.categories[i].score, westin.categories[i].score])), color: '#9aa6be' },
    ],
  }))
)

const kpis = computed(() => [
  { label: 'Properties Evaluated', value: props.length, note: 'grows with every visit' },
  { label: 'Portfolio Avg NFAC Score', value: portfolioAvg.value, note: 'across all evaluations' },
  { label: 'Critical Hazards Found', value: props.reduce((a, p) => a + p.safetyMatrix.criticalHazards, 0), note: 'requiring 0–30 day action' },
  { label: 'Deferred Capital Identified', value: '$18k – $27k', note: 'combined 12–24 month exposure' },
])
</script>

<template>
  <section id="analytics" class="analytics">
    <div class="wrap">
      <span class="kicker">Portfolio Analytics</span>
      <h2 class="section-title">The Benchmark Grows With Every Evaluation</h2>
      <p class="section-sub">
        Every submitted evaluation lands in the benchmark database. This is what your portfolio
        view looks like with the two sample properties — same data, aggregated. At 50 evaluations,
        this becomes a market intelligence asset nobody else in your space has.
      </p>

      <div class="kpi-row">
        <div v-for="k in kpis" :key="k.label" class="card kpi">
          <strong>{{ k.value }}</strong>
          <span class="kpi-label">{{ k.label }}</span>
          <span class="kpi-note">{{ k.note }}</span>
        </div>
      </div>

      <div class="card compare">
        <div class="compare-head">
          <h3>Category Scores — Property vs. Portfolio</h3>
          <div class="legend">
            <span><i style="background: var(--navy)"></i>Broadstone Archive</span>
            <span><i style="background: var(--red)"></i>The Westin</span>
            <span><i style="background: #9aa6be"></i>Portfolio Avg</span>
          </div>
        </div>
        <div class="cmp-rows">
          <div v-for="row in categoryRows" :key="row.label" class="cmp-row">
            <span class="cmp-label">{{ row.label }}</span>
            <div class="cmp-bars">
              <div v-for="s in row.series" :key="s.name" class="cmp-bar">
                <div class="cmp-track">
                  <div class="cmp-fill" :style="{ width: s.score + '%', background: s.color }"></div>
                </div>
                <span class="cmp-val">{{ s.score }}</span>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>
  </section>
</template>

<style scoped>
.analytics { background: #fff; }
.kpi-row { display: grid; grid-template-columns: repeat(4, 1fr); gap: 18px; margin-bottom: 22px; }
.kpi { padding: 22px 24px; display: flex; flex-direction: column; }
.kpi strong { font-family: var(--font-cond); font-weight: 800; font-size: 2.3rem; color: var(--navy); line-height: 1.1; }
.kpi-label {
  font-family: var(--font-cond);
  font-weight: 700;
  font-size: 0.84rem;
  letter-spacing: 0.08em;
  text-transform: uppercase;
  color: var(--red);
  margin-top: 4px;
}
.kpi-note { font-size: 0.8rem; color: var(--muted); }
.compare { padding: 26px 30px; }
.compare-head { display: flex; justify-content: space-between; align-items: center; flex-wrap: wrap; gap: 12px; margin-bottom: 22px; }
.compare-head h3 {
  font-family: var(--font-cond);
  text-transform: uppercase;
  letter-spacing: 0.06em;
  color: var(--navy);
  font-size: 1.2rem;
}
.legend { display: flex; gap: 18px; flex-wrap: wrap; }
.legend span { display: flex; align-items: center; gap: 7px; font-size: 0.82rem; color: var(--muted); }
.legend i { width: 12px; height: 12px; border-radius: 3px; display: inline-block; }
.cmp-rows { display: flex; flex-direction: column; gap: 20px; }
.cmp-row { display: grid; grid-template-columns: 190px 1fr; gap: 16px; align-items: center; }
.cmp-label {
  font-family: var(--font-cond);
  font-weight: 700;
  font-size: 0.9rem;
  letter-spacing: 0.05em;
  text-transform: uppercase;
  color: var(--navy);
}
.cmp-bars { display: flex; flex-direction: column; gap: 5px; }
.cmp-bar { display: grid; grid-template-columns: 1fr 36px; align-items: center; gap: 10px; }
.cmp-track { height: 12px; background: var(--bg); border: 1px solid var(--line); border-radius: 999px; overflow: hidden; }
.cmp-fill { height: 100%; border-radius: 999px; transition: width 0.8s cubic-bezier(0.22, 1, 0.36, 1); }
.cmp-val { font-size: 0.8rem; font-weight: 700; color: var(--navy); }
@media (max-width: 960px) {
  .kpi-row { grid-template-columns: repeat(2, 1fr); }
  .cmp-row { grid-template-columns: 1fr; gap: 8px; }
}
@media (max-width: 560px) {
  .kpi-row { grid-template-columns: 1fr; }
}
</style>
