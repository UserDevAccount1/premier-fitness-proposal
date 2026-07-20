<template>
  <section id="next" class="next">
    <div class="wrap inner">
      <h2>Ready When You Are</h2>
      <p>
        You've seen the dashboard working with your real data and your real scoring model.
        Next step: a call to walk through this proposal, refine scope, and kick off Phase 1.
      </p>
      <div class="steps">
        <div><span>1</span>Schedule the call</div>
        <div><span>2</span>Lock scope &amp; kickoff</div>
        <div><span>3</span>Rebuilt form live in 2 weeks</div>
      </div>
      <a class="btn btn-red" href="mailto:gabrielalvin.jobs@gmail.com?subject=NFAC%20Automation%20Proposal%20—%20Let's%20Talk">Schedule the Call</a>
    </div>
  </section>
</template>

<style scoped>
.next {
  background:
    radial-gradient(900px 400px at 20% 120%, rgba(200, 16, 46, 0.3), transparent 60%),
    linear-gradient(200deg, var(--navy-2), var(--navy-3));
  color: #fff;
  text-align: center;
}
.inner { max-width: 760px; }
h2 {
  font-family: var(--font-cond);
  font-weight: 800;
  font-size: clamp(2.2rem, 4.5vw, 3.4rem);
  text-transform: uppercase;
  letter-spacing: 0.02em;
}
p { color: rgba(255, 255, 255, 0.82); font-size: 1.1rem; margin: 16px auto 34px; max-width: 600px; }
.steps {
  display: flex;
  justify-content: center;
  gap: 30px;
  margin-bottom: 38px;
  flex-wrap: wrap;
}
.steps div { display: flex; align-items: center; gap: 10px; font-family: var(--font-cond); font-weight: 600; letter-spacing: 0.05em; text-transform: uppercase; font-size: 0.95rem; }
.steps span {
  display: inline-flex;
  align-items: center;
  justify-content: center;
  width: 30px; height: 30px;
  border-radius: 50%;
  background: var(--red);
  font-weight: 800;
}
</style>
