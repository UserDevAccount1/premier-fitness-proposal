<script setup>
import { ref, computed } from 'vue'
import ScoreDial from './ScoreDial.vue'
import CategoryDonut from './CategoryDonut.vue'
import broadstone from '../data/broadstone.json'
import westin from '../data/westin.json'

const properties = { broadstone, westin }
const activeId = ref('broadstone')
const p = computed(() => properties[activeId.value])

const donutData = computed(() => p.value.assetAnalysis.lifecycle)

// conic-gradient string for lifecycle donut
const lifecycleGradient = computed(() => {
  let acc = 0
  const stops = donutData.value.map((s) => {
    const from = acc
    acc += s.pct
    return `${s.color} ${from}% ${acc}%`
  })
  return `conic-gradient(${stops.join(', ')})`
})

const riskColor = computed(() => {
  const r = p.value.riskRating
  if (r === 'LOW') return 'var(--green)'
  if (r === 'MODERATE') return 'var(--amber)'
  return 'var(--red)'
})

const severityColor = (s) => (s === 'CRITICAL' || s === 'URGENT' ? 'var(--red)' : 'var(--amber)')

const ordinal = (n) => {
  const rem10 = n % 10
  const rem100 = n % 100
  if (rem10 === 1 && rem100 !== 11) return `${n}st`
  if (rem10 === 2 && rem100 !== 12) return `${n}nd`
  if (rem10 === 3 && rem100 !== 13) return `${n}rd`
  return `${n}th`
}
</script>

<template>
  <section id="demo" class="demo">
    <div class="wrap">
      <span class="kicker">Live Demo</span>
      <h2 class="section-title">This Is the Automated Output</h2>
      <p class="section-sub">
        A working dashboard built from your actual data — the Broadstone Archive grade from your
        NFAC scoring spreadsheet, and the Westin sample from your target design. Switch properties
        to see benchmarking in action. In production, this renders automatically from every form
        submission — as an interactive link <em>and</em> a print-ready PDF.
      </p>

      <div class="switcher" role="tablist" aria-label="Property selector">
        <button
          v-for="(prop, id) in properties"
          :key="id"
          :class="{ active: activeId === id }"
          role="tab"
          :aria-selected="activeId === id"
          @click="activeId = id"
        >
          {{ prop.name }}
        </button>
      </div>

      <!-- Report header -->
      <div class="report card">
        <div class="report-head">
          <div class="rh-brand">
            <span class="rh-shield">NFAC</span>
            <span class="rh-title">National Fitness Amenity Council™</span>
          </div>
          <span class="rh-powered">Powered by <strong>Premier Fitness</strong></span>
        </div>

        <div class="report-meta">
          <div>
            <h3>{{ p.name }}</h3>
            <span>{{ p.propertyType }} · {{ p.location }}</span>
          </div>
          <div class="meta-right">
            <span>Assessment {{ p.assessmentId }}</span>
            <span>{{ p.assessmentDate }}</span>
          </div>
        </div>

        <!-- Executive dashboard row -->
        <div class="exec-grid">
          <div class="panel score-panel">
            <span class="panel-label">NFAC Score™</span>
            <ScoreDial :score="p.nfacScore" />
            <div class="tier">{{ p.tier }}</div>
            <span class="tier-note">{{ p.riskNote }}</span>
          </div>

          <div class="panel">
            <span class="panel-label">Risk Rating</span>
            <div class="risk" :style="{ color: riskColor }">{{ p.riskRating }}</div>
            <div class="bench">
              <span class="panel-label">Benchmark Percentile</span>
              <div class="bench-bar">
                <div class="bench-fill" :style="{ width: p.benchmarkPercentile + '%' }"></div>
                <div class="bench-marker" :style="{ left: p.benchmarkPercentile + '%' }"></div>
              </div>
              <div class="bench-scale"><span>0</span><span>25</span><span>50</span><span>75</span><span>100</span></div>
              <p class="bench-note">
                <strong>{{ ordinal(p.benchmarkPercentile) }} percentile</strong> vs. comparable properties
                in the {{ p.benchmarkMarket }}
              </p>
            </div>
          </div>

          <div class="panel">
            <span class="panel-label">Ownership Impact Rating</span>
            <div class="impact">{{ p.ownershipImpact }}<small>/10</small></div>
            <div class="stars" aria-hidden="true">
              <span
                v-for="i in 5" :key="i"
                class="star"
                :class="{ on: i <= Math.round(p.ownershipImpact / 2) }"
              >★</span>
            </div>
            <span class="panel-label" style="margin-top: 18px">Overall Grade</span>
            <div class="grade">{{ p.grade }}</div>
          </div>
        </div>

        <!-- Category scores -->
        <div class="cat-block">
          <span class="panel-label">Category Scores</span>
          <div class="cat-row">
            <CategoryDonut
              v-for="c in p.categories"
              :key="c.key"
              :score="c.score"
              :label="c.label"
            />
          </div>
        </div>

        <!-- Priorities & strengths -->
        <div class="two-col">
          <div class="mini card-flat">
            <h4 class="red-h">Top Priorities</h4>
            <ol>
              <li v-for="(item, i) in p.priorities" :key="i">{{ item }}</li>
            </ol>
          </div>
          <div class="mini card-flat">
            <h4 class="green-h">Key Strengths</h4>
            <ul>
              <li v-for="(item, i) in p.strengths" :key="i">{{ item }}</li>
            </ul>
          </div>
        </div>

        <!-- Ownership impact summary -->
        <div class="asset-head">Ownership Impact Summary</div>
        <div class="own-tiles">
          <div v-for="t in p.ownership.tiles" :key="t.key" class="own-tile" :class="'tone-' + t.tone">
            <span class="own-label">{{ t.label }}</span>
            <strong class="own-value">{{ t.value }}</strong>
            <p>{{ t.note }}</p>
          </div>
        </div>
        <div class="exec-summary">
          <span>Executive Summary</span>
          <p>{{ p.ownership.summary }}</p>
        </div>
        <div class="meanings">
          <div v-for="m in p.ownership.meanings" :key="m">✓ {{ m }}</div>
        </div>

        <!-- Score composition analytics -->
        <div class="asset-head">Score Composition — How the Grade Was Built</div>
        <div class="comp-grid">
          <div v-for="mb in p.metricBreakdown" :key="mb.category" class="mini card-flat">
            <div class="comp-head">
              <h4>{{ mb.category }}</h4>
              <span class="comp-total">{{ mb.total }}/{{ mb.max }} → <strong>{{ mb.weighted }}/100</strong></span>
            </div>
            <div class="m-bars">
              <div v-for="m in mb.metrics" :key="m.label" class="m-row">
                <span class="m-label">{{ m.label }}</span>
                <div class="m-track">
                  <div
                    class="m-fill"
                    :style="{
                      width: (m.score / 5) * 100 + '%',
                      background: m.score >= 5 ? 'var(--green)' : m.score >= 4 ? 'var(--blue)' : m.score >= 3 ? 'var(--amber)' : 'var(--red)',
                    }"
                  ></div>
                </div>
                <span class="m-val">{{ m.score }}/5</span>
              </div>
            </div>
          </div>
          <div class="mini card-flat matrix">
            <div class="comp-head">
              <h4>NFAC Safety Matrix</h4>
              <span class="comp-total">Critical hazards: <strong style="color: var(--red)">{{ p.safetyMatrix.criticalHazards }}</strong></span>
            </div>
            <table class="mx-table">
              <tbody>
                <tr v-for="r in p.safetyMatrix.rows" :key="r.hazard">
                  <td>{{ r.hazard }}</td>
                  <td>
                    <span class="mx-status" :class="'mx-' + r.status.toLowerCase()">{{ r.status }}</span>
                  </td>
                </tr>
              </tbody>
            </table>
            <p class="mx-note">Safety Status: <strong>{{ p.safetyMatrix.status }}</strong> · Safety Score {{ p.safetyMatrix.score }}/100</p>
          </div>
        </div>

        <!-- Asset condition analysis -->
        <div class="asset-head">Asset Condition Analysis</div>
        <div class="asset-grid">
          <div class="mini card-flat lifecycle">
            <h4>Asset Lifecycle Position</h4>
            <div class="lc-flex">
              <div class="lc-donut" :style="{ background: lifecycleGradient }">
                <div class="lc-hole">
                  <strong>{{ p.assetAnalysis.averageAssetAge }}</strong>
                  <span>avg yrs</span>
                </div>
              </div>
              <ul class="lc-legend">
                <li v-for="s in donutData" :key="s.label">
                  <i :style="{ background: s.color }"></i>{{ s.label }} — <strong>{{ s.pct }}%</strong>
                </li>
              </ul>
            </div>
          </div>

          <div class="mini card-flat">
            <h4>Operational Readiness</h4>
            <div class="readiness">
              <strong>{{ p.assetAnalysis.readinessScore }}</strong><span>/100 · {{ p.assetAnalysis.readinessLabel }}</span>
            </div>
            <div class="r-bar">
              <div class="r-fill" :style="{ width: p.assetAnalysis.readinessScore + '%' }"></div>
            </div>
            <h4 style="margin-top: 22px">Deferred Capital Exposure</h4>
            <div class="capital">{{ p.assetAnalysis.deferredCapital }}</div>
            <span class="cap-note">Estimated investment needed over the next 12–24 months</span>
          </div>

          <div class="mini card-flat">
            <h4>Condition by Equipment Category</h4>
            <div class="bars">
              <div v-for="b in p.assetAnalysis.conditionByCategory" :key="b.label" class="bar-row">
                <span class="bar-label">{{ b.label }}</span>
                <div class="bar-track">
                  <div
                    class="bar-fill"
                    :style="{
                      width: b.score + '%',
                      background: b.score >= 80 ? 'var(--green)' : b.score >= 65 ? 'var(--blue)' : b.score >= 55 ? 'var(--amber)' : 'var(--red)',
                    }"
                  ></div>
                </div>
                <span class="bar-val">{{ b.score }}/100</span>
              </div>
            </div>
          </div>
        </div>

        <!-- Safety findings -->
        <div class="asset-head red-head">Safety &amp; Liability Findings</div>
        <div class="findings">
          <table>
            <thead>
              <tr><th>Finding</th><th>Severity</th><th>Risk</th><th>Time to Resolve</th></tr>
            </thead>
            <tbody>
              <tr v-for="f in p.safetyFindings" :key="f.finding">
                <td>
                  <strong>{{ f.finding }}</strong>
                  <p>{{ f.detail }}</p>
                </td>
                <td><span class="sev" :style="{ background: severityColor(f.severity) }">{{ f.severity }}</span></td>
                <td>{{ f.risk }}</td>
                <td class="resolve">{{ f.resolve }}</td>
              </tr>
            </tbody>
          </table>
        </div>
      </div>
    </div>
  </section>
</template>

<style scoped>
.demo { background: linear-gradient(180deg, var(--bg) 0%, #e9edf6 100%); }

.switcher { display: flex; gap: 10px; margin-bottom: 26px; flex-wrap: wrap; }
.switcher button {
  font-family: var(--font-cond);
  font-weight: 700;
  font-size: 1rem;
  letter-spacing: 0.05em;
  text-transform: uppercase;
  padding: 11px 22px;
  border-radius: 8px;
  border: 1.5px solid var(--line);
  background: #fff;
  color: var(--muted);
  cursor: pointer;
  transition: all 0.18s;
}
.switcher button.active { background: var(--navy); border-color: var(--navy); color: #fff; box-shadow: var(--shadow); }

.report { overflow: hidden; }
.report-head {
  background: var(--navy);
  color: #fff;
  display: flex;
  justify-content: space-between;
  align-items: center;
  padding: 14px 26px;
  flex-wrap: wrap;
  gap: 8px;
}
.rh-brand { display: flex; align-items: center; gap: 12px; }
.rh-shield {
  background: var(--red);
  font-family: var(--font-cond);
  font-weight: 800;
  font-size: 0.85rem;
  padding: 5px 9px;
  border-radius: 5px 5px 9px 9px;
}
.rh-title { font-family: var(--font-cond); font-weight: 700; letter-spacing: 0.1em; text-transform: uppercase; font-size: 0.95rem; }
.rh-powered { font-size: 0.8rem; opacity: 0.85; }

.report-meta {
  display: flex;
  justify-content: space-between;
  align-items: flex-end;
  padding: 24px 26px 6px;
  flex-wrap: wrap;
  gap: 10px;
}
.report-meta h3 { font-family: var(--font-cond); font-size: 1.7rem; text-transform: uppercase; color: var(--navy); line-height: 1.1; }
.report-meta > div > span { color: var(--muted); font-size: 0.92rem; }
.meta-right { display: flex; flex-direction: column; align-items: flex-end; font-size: 0.85rem; color: var(--muted); }

.exec-grid {
  display: grid;
  grid-template-columns: 1fr 1.3fr 1fr;
  gap: 18px;
  padding: 20px 26px;
}
.panel {
  border: 1px solid var(--line);
  border-radius: 10px;
  padding: 18px 20px;
  display: flex;
  flex-direction: column;
  align-items: center;
  text-align: center;
}
.panel-label {
  font-family: var(--font-cond);
  font-weight: 700;
  font-size: 0.8rem;
  letter-spacing: 0.11em;
  text-transform: uppercase;
  color: var(--muted);
  display: block;
  margin-bottom: 8px;
}
.score-panel { background: linear-gradient(180deg, #fff, #f5f7fc); }
.tier {
  font-family: var(--font-cond);
  font-weight: 800;
  letter-spacing: 0.08em;
  background: var(--navy);
  color: #fff;
  border-radius: 6px;
  padding: 4px 16px;
  margin-top: 4px;
}
.tier-note { font-size: 0.8rem; color: var(--muted); margin-top: 6px; }
.risk { font-family: var(--font-cond); font-weight: 800; font-size: 2rem; letter-spacing: 0.04em; }
.bench { width: 100%; margin-top: 18px; }
.bench-bar { position: relative; height: 12px; border-radius: 999px; background: linear-gradient(90deg, var(--red) 0%, var(--amber) 45%, var(--green) 100%); opacity: 0.95; }
.bench-fill { display: none; }
.bench-marker {
  position: absolute;
  top: -5px;
  width: 5px;
  height: 22px;
  background: var(--navy);
  border-radius: 3px;
  transform: translateX(-50%);
  box-shadow: 0 0 0 2px #fff;
  transition: left 0.8s cubic-bezier(0.22, 1, 0.36, 1);
}
.bench-scale { display: flex; justify-content: space-between; font-size: 0.7rem; color: var(--muted); margin-top: 6px; }
.bench-note { font-size: 0.85rem; color: var(--muted); margin-top: 10px; }
.bench-note strong { color: var(--navy); }
.impact { font-family: var(--font-cond); font-weight: 800; font-size: 2.7rem; color: var(--navy); line-height: 1; }
.impact small { font-size: 1.1rem; color: var(--muted); }
.stars { margin-top: 4px; font-size: 1.25rem; letter-spacing: 3px; }
.star { color: var(--line); }
.star.on { color: var(--amber); }
.grade { font-family: var(--font-cond); font-weight: 800; font-size: 2.2rem; color: var(--red); line-height: 1; }

.cat-block { padding: 8px 26px 20px; }
.cat-row {
  display: grid;
  grid-template-columns: repeat(6, 1fr);
  gap: 12px;
  margin-top: 10px;
}

.two-col { display: grid; grid-template-columns: 1fr 1fr; gap: 18px; padding: 0 26px 22px; }
.mini { border: 1px solid var(--line); border-radius: 10px; padding: 20px 22px; background: #fff; }
.mini h4 {
  font-family: var(--font-cond);
  text-transform: uppercase;
  letter-spacing: 0.08em;
  font-size: 0.95rem;
  color: var(--navy);
  margin-bottom: 12px;
}
.red-h { color: var(--red); }
.green-h { color: var(--green); }
.mini ol, .mini ul { padding-left: 20px; display: flex; flex-direction: column; gap: 7px; color: var(--ink); font-size: 0.94rem; }
.mini ul { list-style: none; padding-left: 4px; }
.mini ul li { padding-left: 22px; position: relative; }
.mini ul li::before { content: '✓'; position: absolute; left: 0; color: var(--green); font-weight: 800; }

.asset-head {
  font-family: var(--font-cond);
  font-weight: 800;
  letter-spacing: 0.06em;
  text-transform: uppercase;
  font-size: 1.15rem;
  color: #fff;
  background: var(--navy);
  padding: 10px 26px;
}
.red-head { background: var(--red); }
.asset-grid { display: grid; grid-template-columns: 1.2fr 1fr 1.1fr; gap: 18px; padding: 22px 26px; }

.lc-flex { display: flex; align-items: center; gap: 18px; flex-wrap: wrap; }
.lc-donut {
  width: 120px; height: 120px; border-radius: 50%;
  display: flex; align-items: center; justify-content: center;
  flex-shrink: 0;
}
.lc-hole {
  width: 72px; height: 72px; border-radius: 50%; background: #fff;
  display: flex; flex-direction: column; align-items: center; justify-content: center;
}
.lc-hole strong { font-family: var(--font-cond); font-weight: 800; font-size: 1.5rem; color: var(--navy); line-height: 1; }
.lc-hole span { font-size: 0.65rem; color: var(--muted); }
.lc-legend { list-style: none; display: flex; flex-direction: column; gap: 6px; font-size: 0.83rem; color: var(--muted); }
.lc-legend i { display: inline-block; width: 10px; height: 10px; border-radius: 3px; margin-right: 8px; }
.lc-legend strong { color: var(--navy); }

.readiness strong { font-family: var(--font-cond); font-weight: 800; font-size: 2.4rem; color: var(--navy); }
.readiness span { color: var(--muted); font-size: 0.9rem; margin-left: 6px; }
.r-bar { height: 10px; border-radius: 999px; background: var(--line); margin-top: 8px; overflow: hidden; }
.r-fill { height: 100%; border-radius: 999px; background: var(--amber); transition: width 0.8s cubic-bezier(0.22, 1, 0.36, 1); }
.capital { font-family: var(--font-cond); font-weight: 800; font-size: 1.7rem; color: var(--red); }
.cap-note { font-size: 0.8rem; color: var(--muted); }

.bars { display: flex; flex-direction: column; gap: 11px; }
.bar-row { display: grid; grid-template-columns: 96px 1fr 52px; align-items: center; gap: 10px; }
.bar-label { font-size: 0.84rem; color: var(--muted); }
.bar-track { height: 10px; background: var(--line); border-radius: 999px; overflow: hidden; }
.bar-fill { height: 100%; border-radius: 999px; transition: width 0.8s cubic-bezier(0.22, 1, 0.36, 1); }
.bar-val { font-size: 0.8rem; color: var(--navy); font-weight: 600; text-align: right; }

.own-tiles {
  display: grid;
  grid-template-columns: repeat(5, 1fr);
  gap: 14px;
  padding: 22px 26px 0;
}
.own-tile {
  border: 1px solid var(--line);
  border-radius: 10px;
  overflow: hidden;
  display: flex;
  flex-direction: column;
  text-align: center;
  padding-bottom: 14px;
}
.own-label {
  font-family: var(--font-cond);
  font-weight: 700;
  font-size: 0.78rem;
  letter-spacing: 0.09em;
  text-transform: uppercase;
  color: #fff;
  padding: 9px 6px;
  margin-bottom: 12px;
}
.tone-red .own-label { background: var(--red); }
.tone-blue .own-label { background: var(--blue); }
.tone-green .own-label { background: var(--green); }
.tone-gray .own-label { background: var(--muted); }
.own-value { font-family: var(--font-cond); font-weight: 800; font-size: 1.05rem; color: var(--navy); padding: 0 8px; }
.tone-red .own-value { color: var(--red); }
.tone-green .own-value { color: var(--green); }
.own-tile p { font-size: 0.74rem; color: var(--muted); padding: 6px 12px 0; }
.exec-summary {
  margin: 18px 26px 0;
  background: var(--navy-3);
  border-radius: 10px;
  color: #fff;
  padding: 18px 22px;
}
.exec-summary span {
  font-family: var(--font-cond);
  font-weight: 700;
  letter-spacing: 0.1em;
  text-transform: uppercase;
  font-size: 0.82rem;
  opacity: 0.75;
}
.exec-summary p { font-size: 0.92rem; margin-top: 6px; color: rgba(255,255,255,0.9); }
.meanings {
  display: grid;
  grid-template-columns: repeat(4, 1fr);
  gap: 12px;
  padding: 16px 26px 24px;
}
.meanings div {
  font-size: 0.84rem;
  color: var(--navy);
  font-weight: 600;
  background: var(--bg);
  border: 1px solid var(--line);
  border-radius: 8px;
  padding: 10px 14px;
  text-align: center;
}

.comp-grid {
  display: grid;
  grid-template-columns: repeat(2, 1fr);
  gap: 18px;
  padding: 22px 26px;
}
.comp-head { display: flex; justify-content: space-between; align-items: baseline; gap: 8px; margin-bottom: 12px; flex-wrap: wrap; }
.comp-total { font-size: 0.82rem; color: var(--muted); }
.comp-total strong { color: var(--navy); }
.m-bars { display: flex; flex-direction: column; gap: 10px; }
.m-row { display: grid; grid-template-columns: 170px 1fr 40px; align-items: center; gap: 10px; }
.m-label { font-size: 0.82rem; color: var(--muted); }
.m-track { height: 9px; background: var(--line); border-radius: 999px; overflow: hidden; }
.m-fill { height: 100%; border-radius: 999px; transition: width 0.8s cubic-bezier(0.22, 1, 0.36, 1); }
.m-val { font-size: 0.78rem; color: var(--navy); font-weight: 600; text-align: right; }
.mx-table { width: 100%; border-collapse: collapse; }
.mx-table td { padding: 7px 4px; border-bottom: 1px solid var(--line); font-size: 0.86rem; color: var(--ink); }
.mx-status {
  display: inline-block;
  font-family: var(--font-cond);
  font-weight: 700;
  font-size: 0.72rem;
  letter-spacing: 0.07em;
  text-transform: uppercase;
  padding: 3px 10px;
  border-radius: 5px;
  color: #fff;
}
.mx-pass { background: var(--green); }
.mx-major { background: var(--amber); }
.mx-critical { background: var(--red); }
.mx-note { font-size: 0.82rem; color: var(--muted); margin-top: 10px; }
.mx-note strong { color: var(--red); }

.findings { padding: 22px 26px 28px; overflow-x: auto; }
table { width: 100%; border-collapse: collapse; min-width: 640px; }
th {
  font-family: var(--font-cond);
  text-transform: uppercase;
  letter-spacing: 0.08em;
  font-size: 0.8rem;
  color: var(--muted);
  text-align: left;
  padding: 8px 12px;
  border-bottom: 2px solid var(--line);
}
td { padding: 14px 12px; border-bottom: 1px solid var(--line); vertical-align: top; font-size: 0.92rem; }
td strong { color: var(--navy); }
td p { color: var(--muted); font-size: 0.85rem; margin-top: 3px; }
.sev {
  display: inline-block;
  color: #fff;
  font-family: var(--font-cond);
  font-weight: 700;
  font-size: 0.75rem;
  letter-spacing: 0.08em;
  padding: 4px 10px;
  border-radius: 5px;
}
.resolve { white-space: nowrap; color: var(--navy); font-weight: 600; }

@media (max-width: 960px) {
  .exec-grid, .asset-grid { grid-template-columns: 1fr; }
  .own-tiles { grid-template-columns: repeat(2, 1fr); }
  .meanings { grid-template-columns: repeat(2, 1fr); }
  .comp-grid { grid-template-columns: 1fr; }
  .m-row { grid-template-columns: 130px 1fr 40px; }
  .cat-row { grid-template-columns: repeat(3, 1fr); row-gap: 20px; }
  .two-col { grid-template-columns: 1fr; }
}
@media (max-width: 520px) {
  .cat-row { grid-template-columns: repeat(2, 1fr); }
}
</style>
