<script setup>
import { ref, computed, provide, onMounted, onBeforeUnmount } from 'vue'
import HeroSection from './components/HeroSection.vue'
import UnderstandingSection from './components/UnderstandingSection.vue'
import DashboardDemo from './components/DashboardDemo.vue'
import AnalyticsSection from './components/AnalyticsSection.vue'
import ScoringModel from './components/ScoringModel.vue'
import TechStack from './components/TechStack.vue'
import ArchitectureFlow from './components/ArchitectureFlow.vue'
import TimelineSection from './components/TimelineSection.vue'
import InvestmentSection from './components/InvestmentSection.vue'
import NextSteps from './components/NextSteps.vue'

const slides = [
  { id: 'hero', title: 'Intro', comp: HeroSection },
  { id: 'understanding', title: 'Objective', comp: UnderstandingSection },
  { id: 'demo', title: 'Live Demo', comp: DashboardDemo },
  { id: 'analytics', title: 'Analytics', comp: AnalyticsSection },
  { id: 'scoring', title: 'Scoring', comp: ScoringModel },
  { id: 'stack', title: 'Tech Stack', comp: TechStack },
  { id: 'architecture', title: 'Pipeline', comp: ArchitectureFlow },
  { id: 'timeline', title: 'Timeline', comp: TimelineSection },
  { id: 'investment', title: 'Investment', comp: InvestmentSection },
  { id: 'next', title: 'Next Steps', comp: NextSteps },
]

const active = ref(0)
const direction = ref('next')
const viewport = ref(null)

const goTo = (i) => {
  const target = Math.max(0, Math.min(slides.length - 1, i))
  if (target === active.value) return
  direction.value = target > active.value ? 'next' : 'prev'
  active.value = target
  if (viewport.value) viewport.value.scrollTop = 0
}
const next = () => goTo(active.value + 1)
const prev = () => goTo(active.value - 1)
const goToId = (id) => goTo(slides.findIndex((s) => s.id === id))

provide('deck', { goToId, next, prev })

const transitionName = computed(() => (direction.value === 'next' ? 'slide-next' : 'slide-prev'))

const onKey = (e) => {
  if (e.key === 'ArrowRight' || e.key === 'PageDown') next()
  if (e.key === 'ArrowLeft' || e.key === 'PageUp') prev()
  if (e.key === 'Home') goTo(0)
  if (e.key === 'End') goTo(slides.length - 1)
}

let touchX = null
const onTouchStart = (e) => { touchX = e.changedTouches[0].clientX }
const onTouchEnd = (e) => {
  if (touchX === null) return
  const dx = e.changedTouches[0].clientX - touchX
  if (Math.abs(dx) > 80) (dx < 0 ? next() : prev())
  touchX = null
}

onMounted(() => window.addEventListener('keydown', onKey))
onBeforeUnmount(() => window.removeEventListener('keydown', onKey))
</script>

<template>
  <div class="deck" @touchstart.passive="onTouchStart" @touchend.passive="onTouchEnd">
    <header class="deck-bar">
      <div class="db-brand">
        <span class="db-shield">NFAC</span>
        <span class="db-title">Report Automation — Proposal</span>
      </div>
      <nav class="db-tabs">
        <button
          v-for="(s, i) in slides"
          :key="s.id"
          :class="{ on: i === active }"
          @click="goTo(i)"
        >
          {{ s.title }}
        </button>
      </nav>
    </header>

    <div ref="viewport" class="deck-viewport">
      <Transition :name="transitionName" mode="out-in" :duration="{ enter: 300, leave: 200 }">
        <div class="slide" :key="active">
          <component :is="slides[active].comp" />
        </div>
      </Transition>
    </div>

    <button class="nav-arrow left" :disabled="active === 0" aria-label="Previous slide" @click="prev">‹</button>
    <button class="nav-arrow right" :disabled="active === slides.length - 1" aria-label="Next slide" @click="next">›</button>

    <footer class="deck-foot">
      <span class="df-note">Prepared for Premier Fitness</span>
      <div class="dots">
        <button
          v-for="(s, i) in slides"
          :key="s.id"
          :class="{ on: i === active }"
          :aria-label="'Go to ' + s.title"
          @click="goTo(i)"
        ></button>
      </div>
      <span class="df-count">{{ active + 1 }} / {{ slides.length }}</span>
    </footer>
  </div>
</template>

<style scoped>
.deck {
  height: 100vh;
  height: 100dvh;
  display: flex;
  flex-direction: column;
  overflow: hidden;
  background: var(--bg);
}

.deck-bar {
  background: var(--navy-3);
  color: #fff;
  display: flex;
  align-items: center;
  justify-content: space-between;
  gap: 16px;
  padding: 10px 18px;
  flex-shrink: 0;
  z-index: 5;
}
.db-brand { display: flex; align-items: center; gap: 10px; white-space: nowrap; }
.db-shield {
  background: var(--red);
  font-family: var(--font-cond);
  font-weight: 800;
  font-size: 0.82rem;
  letter-spacing: 0.06em;
  padding: 5px 9px;
  border-radius: 6px 6px 10px 10px;
}
.db-title {
  font-family: var(--font-cond);
  font-weight: 700;
  letter-spacing: 0.08em;
  text-transform: uppercase;
  font-size: 0.88rem;
  opacity: 0.9;
}
.db-tabs { display: flex; gap: 2px; overflow-x: auto; scrollbar-width: none; }
.db-tabs::-webkit-scrollbar { display: none; }
.db-tabs button {
  background: transparent;
  border: none;
  color: rgba(255, 255, 255, 0.62);
  font-family: var(--font-cond);
  font-weight: 600;
  font-size: 0.82rem;
  letter-spacing: 0.07em;
  text-transform: uppercase;
  padding: 7px 11px;
  border-radius: 6px;
  cursor: pointer;
  white-space: nowrap;
  transition: all 0.15s;
}
.db-tabs button:hover { color: #fff; }
.db-tabs button.on { background: var(--red); color: #fff; }

.deck-viewport {
  flex: 1;
  overflow-y: auto;
  overflow-x: hidden;
  position: relative;
}
.slide { min-height: 100%; display: flex; flex-direction: column; }
.slide > :deep(section), .slide > :deep(header) { flex: 1; }

.nav-arrow {
  position: fixed;
  top: 50%;
  transform: translateY(-50%);
  width: 46px;
  height: 46px;
  border-radius: 50%;
  border: none;
  background: var(--navy);
  color: #fff;
  font-size: 1.7rem;
  line-height: 1;
  cursor: pointer;
  z-index: 10;
  box-shadow: var(--shadow-lg);
  display: flex;
  align-items: center;
  justify-content: center;
  padding-bottom: 4px;
  transition: background 0.15s, opacity 0.15s;
}
.nav-arrow:hover:not(:disabled) { background: var(--red); }
.nav-arrow:disabled { opacity: 0.25; cursor: default; }
.nav-arrow.left { left: 14px; }
.nav-arrow.right { right: 14px; }

.deck-foot {
  background: var(--navy-3);
  color: rgba(255, 255, 255, 0.7);
  display: flex;
  align-items: center;
  justify-content: space-between;
  gap: 12px;
  padding: 9px 18px;
  flex-shrink: 0;
  font-size: 0.8rem;
  z-index: 5;
}
.df-note { font-family: var(--font-cond); letter-spacing: 0.08em; text-transform: uppercase; font-size: 0.75rem; }
.dots { display: flex; gap: 7px; }
.dots button {
  width: 9px;
  height: 9px;
  border-radius: 50%;
  border: none;
  background: rgba(255, 255, 255, 0.28);
  cursor: pointer;
  padding: 0;
  transition: all 0.2s;
}
.dots button.on { background: var(--red); transform: scale(1.35); }
.df-count { font-family: var(--font-cond); font-weight: 700; letter-spacing: 0.1em; }

/* slide transitions */
.slide-next-enter-active, .slide-prev-enter-active { transition: opacity 0.28s ease, transform 0.28s ease; }
.slide-next-leave-active, .slide-prev-leave-active { transition: opacity 0.18s ease, transform 0.18s ease; }
.slide-next-enter-from { opacity: 0; transform: translateX(60px); }
.slide-next-leave-to { opacity: 0; transform: translateX(-40px); }
.slide-prev-enter-from { opacity: 0; transform: translateX(-60px); }
.slide-prev-leave-to { opacity: 0; transform: translateX(40px); }

@media (max-width: 860px) {
  .db-title { display: none; }
  .nav-arrow { width: 40px; height: 40px; }
  .nav-arrow.left { left: 8px; }
  .nav-arrow.right { right: 8px; }
  .df-note { display: none; }
}
</style>
