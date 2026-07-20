<script setup>
import HeroSection from './components/HeroSection.vue'
import UnderstandingSection from './components/UnderstandingSection.vue'
import DashboardDemo from './components/DashboardDemo.vue'
import AnalyticsSection from './components/AnalyticsSection.vue'
import ScoringModel from './components/ScoringModel.vue'
import ArchitectureFlow from './components/ArchitectureFlow.vue'
import TimelineSection from './components/TimelineSection.vue'
import InvestmentSection from './components/InvestmentSection.vue'
import NextSteps from './components/NextSteps.vue'
</script>

<template>
  <HeroSection />
  <UnderstandingSection />
  <DashboardDemo />
  <AnalyticsSection />
  <ScoringModel />
  <ArchitectureFlow />
  <TimelineSection />
  <InvestmentSection />
  <NextSteps />
  <footer class="footer">
    <div class="wrap">
      <span>NFAC Report Automation — Project Proposal</span>
      <span>Prepared for Premier Fitness · {{ new Date().getFullYear() }}</span>
    </div>
  </footer>
</template>

<style scoped>
.footer {
  background: var(--navy-3);
  color: rgba(255, 255, 255, 0.65);
  padding: 26px 0;
  font-size: 0.9rem;
}
.footer .wrap {
  display: flex;
  justify-content: space-between;
  gap: 12px;
  flex-wrap: wrap;
}
</style>
