# HFACS Analysis: Duolingo's Learning Transfer Failure

**Project:** Language Learner Agent — Applied Human Factors, Spring 2026
**Phase:** 4 — Human Factors Analysis (20 pts)

---

## Key Findings

- **Systemic design gap, not user laziness.** Every level of the HFACS hierarchy — from the operator's inability to self-correct up through organizational KPIs — traces to design and incentive failures, not learner effort. This is the course's core tenet made concrete: *error is a system property, not a human shortcoming.*
- **Context is the missing ingredient.** Cognitive science (Essoe et al., 2022) shows that memory retrieval depends on episodic reinstatement — re-activating the encoding context. Duolingo's uniform gamified interface forecloses this mechanism entirely, blocking transfer at the neurological level.
- **The evidence base is deliberately narrow — a Swiss Cheese hole at the organizational layer.** Duolingo's published outcome research assesses only receptive skills and never speaking, masking the transfer gap from public view. All four HFACS holes line up: operator has no signal, environment provides no context, algorithm ignores error patterns, and the organization never measures what matters.

---

## Level 1 — Unsafe Acts (Learner / Operator)

### Failure: Skill-Based Error Repetition With No Signal Detection Opportunity

In HFACS terms, learners exhibit *skill-based errors* — practiced routines that produce consistent wrong outputs because the underlying mental model was never corrected. But the deeper human factors explanation comes from **Signal Detection Theory (SDT)**: a correct learning signal can only be detected if it is present in the display. Duolingo's feedback loop is engineered so that learners receive *hits* on memorization (correct XP, streak continuation) while systematically *missing* the real signal — the absence of conversational competence. The app has effectively set the learner's response criterion (β) to maximize engagement-positive outcomes, not proficiency outcomes.

Kristensen et al. (2024) tracked 363 second-graders over 8 weeks and found that error repetition rates remained **stable over time** — continued app exposure did not reduce the pattern. Students who repeated mistakes more frequently showed significantly lower learning gains. The authors describe a "double threat": error repetition simultaneously reduces exposure to correct forms and increases exposure to incorrect ones, compounding the signal-to-noise problem in exactly the way SDT predicts when a detection system has poor sensitivity (low *d'*).

Jiang et al. (2021) document the downstream consequence: learners using Duolingo as their sole tool reach only **Intermediate Low in reading** and **Novice High in listening** — below the Intermediate Mid–High threshold where real conversational fluency begins. Critically, no speaking or writing was ever assessed. From within the app, the learner's dashboard signals success — a *False Alarm* in SDT terms, a confident "present" response to a signal that was never there.

This is also an instance of **Inattentional Blindness**. The gamified interface pulls foveal attention toward XP counts, streak flames, and leaderboard ranks. The conversational competence signal — which would require a speaking assessment to surface — is never placed in the operator's attentional field. Learners cannot detect what the system never displays. This is not a failure of attention; it is a failure of interface design to place the critical signal where attention lands.

**Why this is a system failure, not a user failure.** The course tenet applies directly: *the burden should move upstream, not remain on the operator.* A learner operating faithfully within the system — completing exercises, earning points — has no mechanism to detect or correct skill-based errors. The SDT failure (bad β, absent signal) is designed in. Blaming the learner for not noticing a signal the system never generated is a textbook instance of the **Fundamental Attribution Error**.

> *"The propensity to repeat mistakes remained stable over time."* — Kristensen et al. (2024)

---

## Level 2 — Preconditions for Unsafe Acts (Environment, Mental State, Context)

### Failure: Decontextualized Interface Collapses Working Memory's Episodic Buffer

HFACS Level 2 examines the preconditions that enable safe performance: accurate mental models, appropriate cognitive load distribution, and sufficient situational awareness. In learning science, the equivalent construct is **Baddeley's Working Memory model**. Effective vocabulary acquisition requires not just the Phonological Loop (verbal repetition) but the **Episodic Buffer** — the system that integrates current experience with long-term memory through contextual, cross-modal encoding. Duolingo's architecture engages only the Phonological Loop.

Godwin-Jones (2018) documents this precisely: vocabulary apps including Duolingo "teach vocabulary in isolated units rather than relevant contexts... despite a pedagogical shift toward communicative approaches, these apps are behaviorist in nature." Spaced repetition systems (SRS) produce strong memorization outcomes but do not build the *pragmatic knowledge* needed to deploy language in conversation — because SRS optimizes for Phonological Loop rehearsal without engaging episodic context.

Essoe et al. (2022) provide direct neural and behavioral evidence for the episodic buffer mechanism. Learners who studied vocabulary in distinct, contextually rich environments retained **92%** at one-week follow-up versus **76%** in a same-context condition, and produced **38% fewer cross-language intrusions**. The benefit was mediated by *mental context reinstatement* — the Episodic Buffer re-activating encoding conditions at retrieval. Duolingo's uniform, gamified interface provides zero context differentiation across sessions, making this reinstatement impossible by design.

Mihaylova et al. (2022) synthesized 23 studies and found a moderate-to-strong immediate effect for mobile language apps (*g* = 0.88), but only 3 of 23 included delayed follow-up — and those showed only small effects. The GRADE evidence quality for long-term communicative transfer is rated "low to very low." This pattern is consistent with a system that engages working memory for short-term rehearsal but fails to consolidate into long-term memory through episodic encoding. The impressive immediate *g* is a working memory artifact, not a transfer outcome.

From the **TADMUS** framework: operators (learners) need timely, accurate feedback to update their mental model of the task environment. TADMUS research established that decision-making under stress degrades when environmental feedback does not match the operator's internal model. Duolingo provides feedback calibrated to item-memorization, not conversational performance — systematically miscalibrating the learner's mental model of their own ability.

**Why this is a system failure, not a user failure.** The decontextualized interface is an architectural decision. Learners cannot inject social context, persona, or situational embedding into an app that offers none. The Episodic Buffer requires distinct encoding environments to operate — that is basic Baddeley, not a user preference. No amount of learner diligence compensates for a system that architecturally forecloses the memory mechanisms learning requires.

> *"Apps 'teach vocabulary in isolated units rather than relevant contexts... these apps are behaviorist in nature.'"* — Godwin-Jones (2018)

---

## Level 3 — Unsafe Supervision (Algorithm Design, Metrics)

### Failure: The Algorithm's SDT Sensitivity Is Calibrated to the Wrong Signal

In HFACS, unsafe supervision refers to the oversight layer responsible for managing operator performance — in this domain, the algorithm that selects tasks, sequences content, delivers feedback, and signals progress. The supervisory algorithm is Duolingo's equivalent of an air traffic control system, and like any control system, its performance can be analyzed through SDT: what signal is it detecting, and how accurately?

The algorithm's *d'* for conversational-transfer failure is effectively zero. Jiang et al. (2021) establish that the supervisory loop — task selection, performance measurement, feedback, and progression — is built entirely around receptive skills. Speaking, the terminal goal, is *unsupervised by design*. A supervisor that never observes the critical performance domain cannot detect failure within it. The supervisory hole in the Swiss Cheese model is open.

Godwin-Jones (2018) explains the optimization mismatch: Duolingo's SRS scheduler is calibrated for item-memorization — surfacing flashcard items at intervals that minimize forgetting of isolated forms. This is the *wrong variable*. SRS produces excellent retention of decontextualized vocabulary but "does not build the pragmatic knowledge needed to deploy words appropriately in conversation." The supervisor is optimizing for a proxy metric, not the outcome it is responsible for.

Kristensen et al. (2024) reveal the deeper supervisory failure: the algorithm does not detect or respond to error repetition patterns. Learners who repeatedly make the same mistakes continue to receive the same exercise format; no corrective explanation, no adaptive path change, no escalation. The authors recommend automated detection of error patterns and explanatory corrective feedback — a proposal directly grounded in TADMUS principles, which established that effective supervisory systems must provide timely, accurate feedback that operators can act on. Duolingo's algorithm provides neither detection nor actionable feedback.

This is also an instance of **Plan Continuation Bias** at the algorithmic level. Like the Air India 812 crew that continued an instrument approach past obvious warning signals, Duolingo's algorithm continues advancing learners through gamified progression milestones despite accumulating signals that conversational transfer is not occurring. The algorithm has no mechanism to recognize "we are past the point where this plan is working."

**Why this is a system failure, not a user failure.** Learners cannot override the algorithm's task selection or feedback logic. If the supervisory algorithm optimizes for engagement rather than transfer, learners operating faithfully within it will achieve engagement and not transfer. The SDT failure — a supervisor with zero sensitivity to the critical signal — belongs to the system designer, not the operator being supervised.

> *"No other skills were assessed."* — Jiang et al. (2021), on Duolingo's own outcome research

---

## Level 4 — Organizational Influences (Business Model, Incentives)

### Failure: Innovator's Dilemma — DAU Optimization Systematically Selects Against Transfer Features

HFACS Level 4 identifies the organizational pressures and resource allocation decisions that create every hole downstream. For Duolingo, the relevant organizational facts are: it is a publicly traded company, its primary business metric is Daily Active Users (DAU), and its product decisions are driven by engagement proxies — exactly the pattern Christensen's **Innovator's Dilemma** predicts. Established companies optimize relentlessly for their existing profitable metrics (streak engagement, DAU) while the disruptive feature set that would actually serve users (dialect-specific AI conversation, adaptive speaking assessment) carries implementation cost and does not move the KPI.

Mayer (2021) establishes that the instructional features with the strongest effect on learning outcomes — personalized conversational delivery (Personalization Principle, *d* = 1.3 across 10/10 studies), native human voice (Voice Principle, *d* = 0.8), and embodied social cues (Embodiment Principle) — all require dialect expertise, conversational AI infrastructure, and scenario design. None of these drive a streak notification. The organizational incentive structure selects against them with perfect consistency.

Jiang et al. (2021) document the organizational decision about what to measure. Duolingo's own research program covers reading and listening — skills where receptive gains are measurable and favorable — and explicitly excludes speaking. This is not a methodology gap; it is a research strategy. Validating speaking outcomes would require expensive human raters or validated automated assessments, and the results, given what Level 1–3 analysis predicts, might be unflattering. Publishing only favorable metrics while leaving productive skills unstudied insulates the brand while the transfer gap persists.

Godwin-Jones (2018) names the commercial logic: isolated drill items are cheap to generate at scale, easy to gamify, and produce the short-term memorization gains that feel rewarding to users. Context-rich, socially embedded instruction costs more and converts less directly to DAU. The decontextualized architecture is not pedagogically naive — it is commercially efficient. The organization's cost-benefit calculus consistently favors the scalable, gamified approach.

From the perspective of **transparency as a system variable** (Bhaskara et al., 2021): when Duolingo surfaces confident progress indicators — skill levels, crowns, completion percentages — it is amplifying learner confidence in a representation of ability that does not include speaking. Transparency about the wrong signal is worse than no signal, because it suppresses the healthy skepticism that might lead a learner to seek supplementary practice. "The System never changed — You did."

The Swiss Cheese model maps the full failure chain: organizational KPIs exclude speaking (L4 hole) → algorithm never tasks or measures speaking (L3 hole) → environment provides no contextual encoding (L2 hole) → learner has no signal to act on (L1 hole). All holes are aligned. The incident — failure to transfer to real conversation — is structurally guaranteed.

**Why this is a system failure, not a user failure.** Individual learners do not set the company's KPIs, allocate the engineering budget, or decide which skills get assessed in outcome research. The FAE — attributing transfer failure to learner consistency ("keep your streak") rather than to system design — is embedded in how the product is marketed and how Duolingo's own research is scoped. The failure originates at the level of organizational design choices and accountability structures. The burden must move upstream.

> *"The personalization principle...was supported in 10 out of 10 experimental tests, yielding a median effect size of 1.3."* — Mayer (2021)
> *(A finding the organizational incentive structure systematically underweights.)*

---

## Sources

| Citation | Level Applied | Course Concept Bridge |
|---|---|---|
| Jiang et al. (2021). *Foreign Language Annals*, 54(4), 974–1002. | L1, L3, L4 | SDT False Alarm; Swiss Cheese; FAE |
| Kristensen et al. (2024). *Computers & Education*, 210, 104966. | L1, L3 | SDT d'; TADMUS feedback; Plan Continuation Bias |
| Godwin-Jones (2018). *Language Learning & Technology*, 22(3), 1–19. | L2, L3, L4 | Phonological Loop vs. Episodic Buffer; Innovator's Dilemma |
| Essoe et al. (2022). *npj Science of Learning*, 7, 31. | L2 | Baddeley Episodic Buffer; context reinstatement |
| Mihaylova et al. (2022). *Psychologica Belgica*, 62(1), 252–271. | L2 | Working memory artifact vs. LTM transfer |
| Mayer (2021). In *Cambridge Handbook of Multimedia Learning* (3rd ed.). | L4 | Social Agency Theory; Personalization Principle; Transparency |
| Bhaskara, A., Duong, L., Brooks, J., Li, R., McInerney, R., Skinner, M., Pongracic, H., & Loft, S. (2021). Effect of automation transparency in the management of multiple unmanned vehicles. *Applied Ergonomics*, *90*, 103243. https://doi.org/10.1016/j.apergo.2020.103243 | L4 | Transparency as system variable; reasoning transparency vs. outcome visualization; automation reliance |
