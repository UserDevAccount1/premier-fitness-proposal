<script setup>
import { computed } from 'vue'

const props = defineProps({
  score: { type: Number, required: true },
  label: { type: String, required: true },
})

const R = 42
const CIRC = 2 * Math.PI * R
const offset = computed(() => CIRC * (1 - Math.min(props.score, 100) / 100))
const color = computed(() => {
  if (props.score >= 85) return 'var(--green)'
  if (props.score >= 70) return 'var(--blue)'
  if (props.score >= 55) return 'var(--amber)'
  return 'var(--red)'
})
</script>

<template>
  <div class="donut-wrap">
    <div class="donut">
      <svg viewBox="0 0 100 100">
        <circle cx="50" cy="50" :r="R" fill="none" stroke="var(--line)" stroke-width="9" />
        <circle
          cx="50" cy="50" :r="R"
          fill="none" :stroke="color" stroke-width="9" stroke-linecap="round"
          :stroke-dasharray="CIRC"
          :stroke-dashoffset="offset"
          transform="rotate(-90 50 50)"
          class="ring"
        />
      </svg>
      <div class="value">{{ score }}<small>/100</small></div>
    </div>
    <span class="label">{{ label }}</span>
  </div>
</template>

<style scoped>
.donut-wrap { display: flex; flex-direction: column; align-items: center; gap: 8px; }
.donut { position: relative; width: 96px; height: 96px; }
svg { width: 100%; height: 100%; }
.ring { transition: stroke-dashoffset 0.9s cubic-bezier(0.22, 1, 0.36, 1), stroke 0.5s; }
.value {
  position: absolute; inset: 0;
  display: flex; align-items: center; justify-content: center;
  font-family: var(--font-cond); font-weight: 800; font-size: 1.5rem; color: var(--navy);
}
.value small { font-size: 0.62rem; color: var(--muted); font-weight: 600; margin-top: 8px; }
.label {
  font-family: var(--font-cond);
  font-weight: 700;
  font-size: 0.8rem;
  letter-spacing: 0.07em;
  text-transform: uppercase;
  color: var(--muted);
  text-align: center;
  max-width: 110px;
  line-height: 1.25;
}
</style>
