# Bicknell & Brust (2020) — Duolingo's Birdbrain Algorithm

**Citation (APA):**
Bicknell, K., & Brust, C. (2020, October 7). *Learning how to help you learn: Introducing Birdbrain!* Duolingo Blog. https://blog.duolingo.com/learning-how-to-help-you-learn-introducing-birdbrain/

*Source type: First-party algorithmic disclosure (company research blog). Per `docs/research/CLAUDE.md` line 15, Duolingo Research materials are acceptable in this corpus; this file cites the company's own description of its supervisory algorithm for the HFACS Level 3 analysis.*

---

## Summary

- Duolingo's item-selection supervisor, **Birdbrain**, is described by its own authors as a model that "makes an educated guess about whether a learner will get a given exercise right" based on learner ability and item difficulty — a classic Item Response Theory / adaptive-testing formulation.
- The stated optimization target is **matching exercise difficulty to the learner** so that items are neither "too challenging" nor "too easy," with the Session Generator selecting items at the right difficulty level "for _this specific learner_."
- The post does **not** describe any assessment of, adaptation to, or feedback on spoken conversational performance. The supervisory loop is entirely specified over discrete exercise correctness — the same structural blind spot documented in Jiang et al. (2021).
- First-party confirmation that the algorithm's signal is **item-level correctness**, not conversational competence — directly supporting the HFACS Level 3 claim that the supervisor's *d'* for conversational transfer is zero by design.
- This is algorithmic disclosure by the company, not independent evaluation; it is strong evidence of *what the system optimizes for* and weaker evidence of *what the system accomplishes*. Pair with Jiang et al. (2021) for outcome evidence.

**Key Quote:**
> "Birdbrain... makes an educated guess about whether a learner will get a given exercise right."

---

**Rubric Phase:** Phase 1 — documents, in Duolingo's own words, that the supervisory algorithm optimizes for item-correctness matching rather than conversational competence; a first-party statement of the conversational-fluency limitation this project targets, and the direct companion to Jiang et al. (2021) on the outcome side. (The evidence also supplies the primary source for the HFACS Level 3 unsafe-supervision argument.)
