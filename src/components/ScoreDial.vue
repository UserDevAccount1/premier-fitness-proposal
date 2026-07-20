<script setup>
import { computed } from 'vue'

const props = defineProps({
  score: { type: Number, required: true },
  size: { type: Number, default: 190 },
})

const R = 80
const CIRC = 2 * Math.PI * R
const ARC_FRACTION = 0.75

const dashArray = computed(() => `${CIRC * ARC_FRACTION} ${CIRC}`)
const progress = computed(() => CIRC * ARC_FRACTION * (1 - Math.min(props.score, 100) / 100))
const color = computed(() => {
  if (props.score >= 85) return 'var(--green)'
  if (props.score >= 70) return 'var(--blue)'
  if (props.score >= 55) return 'var(--amber)'
  return 'var(--red)'
})
</script>

<template>
  <div class="dial" :style="{ width: size + 'px', height: size + 'px' }">
    <svg viewBox="0 0 200 200">
      <circle
        cx="100" cy="100" :r="R"
        fill="none" stroke="var(--line)" stroke-width="16"
        stroke-linecap="round"
        :stroke-dasharray="dashArray"
        transform="rotate(135 100 100)"
      />
      <circle
        cx="100" cy="100" :r="R"
        fill="none" :stroke="color" stroke-width="16"
        stroke-linecap="round"
        :stroke-dasharray="dashArray"
        :stroke-dashoffset="progress"
        transform="rotate(135 100 100)"
        class="progress"
      />
    </svg>
    <div class="dial-label">
      <strong>{{ Math.round(score * 100) / 100 }}</strong>
      <span>/100</span>
    </div>
  </div>
</template>

<style scoped>
.dial { position: relative; }
svg { width: 100%; height: 100%; }
.progress { transition: stroke-dashoffset 0.9s cubic-bezier(0.22, 1, 0.36, 1), stroke 0.5s; }
.dial-label {
  position: absolute;
  inset: 0;
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
}
.dial-label strong {
  font-family: var(--font-cond);
  font-weight: 800;
  font-size: 2.9rem;
  line-height: 1;
  color: var(--navy);
}
.dial-label span { color: var(--muted); font-size: 0.95rem; }
</style>
