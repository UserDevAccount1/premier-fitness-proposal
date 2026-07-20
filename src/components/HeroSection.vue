<script setup>
import { inject } from 'vue'
const deck = inject('deck', null)
</script>

<template>
  <header class="hero">
    <div class="nav wrap">
      <div class="brand">
        <div class="shield">NFAC</div>
        <div class="brand-text">
          <strong>Report Automation</strong>
          <span>Powered by Premier Fitness</span>
        </div>
      </div>
    </div>

    <div class="hero-body wrap">
      <span class="tag">Project Proposal</span>
      <h1>From On-Site Evaluation to<br /><em>Customer-Ready Report</em> — Automatically</h1>
      <p>
        A complete automation pipeline that turns your NFAC field evaluations into graded,
        benchmarked, presentation-quality reports — in minutes, not hours of Canva work.
      </p>
      <div class="hero-cta">
        <button class="btn btn-red" @click="deck && deck.goToId('demo')">See the Live Dashboard</button>
        <button class="btn btn-ghost" @click="deck && deck.goToId('architecture')">How It Works</button>
      </div>
      <div class="hero-stats">
        <div><strong>15–20 min</strong><span>manual report today</span></div>
        <div><strong>&lt; 2 min</strong><span>automated tomorrow</span></div>
        <div><strong>6</strong><span>NFAC score categories</span></div>
        <div><strong>100%</strong><span>consistent grading</span></div>
      </div>
    </div>
  </header>
</template>

<style scoped>
.hero {
  background:
    radial-gradient(1200px 500px at 80% -10%, rgba(200, 16, 46, 0.28), transparent 60%),
    linear-gradient(160deg, var(--navy-2) 0%, var(--navy-3) 70%);
  color: #fff;
  padding-bottom: 90px;
}
.nav {
  display: flex;
  justify-content: space-between;
  align-items: center;
  padding-top: 22px;
  padding-bottom: 22px;
}
.brand { display: flex; align-items: center; gap: 12px; }
.shield {
  background: var(--red);
  font-family: var(--font-cond);
  font-weight: 800;
  letter-spacing: 0.06em;
  padding: 9px 12px;
  border-radius: 8px 8px 14px 14px;
  box-shadow: 0 4px 14px rgba(0, 0, 0, 0.35);
}
.brand-text { display: flex; flex-direction: column; line-height: 1.25; }
.brand-text strong { font-family: var(--font-cond); letter-spacing: 0.05em; text-transform: uppercase; }
.brand-text span { font-size: 0.72rem; opacity: 0.7; letter-spacing: 0.12em; text-transform: uppercase; }
.hero-body { padding-top: 54px; }
.tag {
  font-family: var(--font-cond);
  font-weight: 700;
  letter-spacing: 0.16em;
  text-transform: uppercase;
  font-size: 0.9rem;
  color: #ffb3bf;
  border: 1.5px solid rgba(255, 179, 191, 0.55);
  border-radius: 999px;
  padding: 5px 16px;
}
h1 {
  font-family: var(--font-cond);
  font-weight: 800;
  font-size: clamp(2.4rem, 5.5vw, 4.2rem);
  line-height: 1.05;
  text-transform: uppercase;
  letter-spacing: 0.015em;
  margin: 26px 0 18px;
}
h1 em { color: #ff9daa; font-style: normal; }
.hero-body p { max-width: 640px; font-size: 1.15rem; color: rgba(255, 255, 255, 0.85); }
.hero-cta { display: flex; gap: 16px; margin-top: 34px; flex-wrap: wrap; }
.hero-stats {
  display: grid;
  grid-template-columns: repeat(4, minmax(0, 1fr));
  gap: 18px;
  margin-top: 60px;
  max-width: 780px;
}
.hero-stats div {
  background: rgba(255, 255, 255, 0.07);
  border: 1px solid rgba(255, 255, 255, 0.14);
  border-radius: 10px;
  padding: 14px 16px;
  display: flex;
  flex-direction: column;
}
.hero-stats strong { font-family: var(--font-cond); font-size: 1.6rem; font-weight: 800; }
.hero-stats span { font-size: 0.8rem; opacity: 0.75; }
@media (max-width: 760px) {
  .hero-stats { grid-template-columns: repeat(2, 1fr); }
}
</style>
