# HFACS Analysis: Duolingo's Learning Transfer Failure

**Project:** Language Learner Agent — Applied Human Factors, Spring 2026
**Phase:** 4 — Human Factors Analysis (20 pts)

---

## Key Findings

- **Systemic design gap, not user laziness.** Duolingo's architecture was built to maximize engagement metrics (streaks, DAU) rather than communicative transfer — every level of the HFACS hierarchy shows a failure originating in design and incentive, not learner effort.
- **Context is the missing ingredient.** Research across cognitive science, vocabulary pedagogy, and meta-analysis consistently shows that decontextualized drill cannot produce real-world conversational competence; Duolingo's core loop is decontextualized by design.
- **The evidence base is deliberately narrow.** Duolingo's own outcome research validates only receptive skills (reading, listening) and never assesses speaking — the exact domain where transfer is weakest — masking the failure from public view.

---

## Level 1 — Unsafe Acts (Learner / Operator)

### Failure: Error Repetition Without Self-Correction

Learners using Duolingo systematically repeat the same mistakes across sessions without the behavior diminishing over time. This is the HFACS category of *skill-based errors* — well-practiced routines that nonetheless produce consistent wrong outputs because the underlying mental model was never corrected.

Kristensen et al. (2024) tracked 363 second-graders over 8 weeks and found that error repetition rates remained **stable over time** — the app's continued exposure did not reduce the pattern. Students who repeated errors more showed significantly lower learning gains. The authors describe a "double threat": repeated exposure to wrong forms simultaneously reduces exposure to correct ones.

Additionally, Jiang et al. (2021) revealed that learners using Duolingo as their sole learning tool reach only **Intermediate Low in reading** and **Novice High in listening** — below the Intermediate Mid–High threshold where real conversational fluency begins. Critically, no speaking or writing was ever assessed. Learners receive no signal that their productive/conversational ability is failing; from within the app, they appear to be succeeding.

**Why this is a system failure, not a user failure.** The learner has no mechanism available to detect or correct these errors. The app neither flags repetitive errors nor delivers explanatory feedback. The learner is acting exactly as the system design elicits — completing exercises, earning points — and the system fails to surface the failure mode. A user who cannot observe their own error pattern cannot be blamed for not correcting it.

> *"The propensity to repeat mistakes remained stable over time."* — Kristensen et al. (2024)

---

## Level 2 — Preconditions for Unsafe Acts (Environment, Mental State, Context)

### Failure: Decontextualized Learning Environment Blocks Transfer

The preconditions that enable safe learning (accurate mental models, situational awareness, appropriate cognitive load distribution) are absent from Duolingo's design. Words and phrases are presented as isolated units stripped of social, relational, and situational context — the very context that makes transfer to real conversation possible.

Godwin-Jones (2018) documents this precisely: vocabulary apps including Duolingo "teach vocabulary in isolated units rather than relevant contexts... despite a pedagogical shift toward communicative approaches, these apps are behaviorist in nature." Spaced repetition systems produce strong memorization outcomes but do not build the *pragmatic knowledge* needed to deploy language in conversation — knowing a word is not the same as being able to use it.

Essoe et al. (2022) provides direct neural and behavioral evidence: learners who studied vocabulary in distinct, contextually rich environments retained **92%** at one-week follow-up versus **76%** in a same-context condition, and produced **38% fewer cross-language intrusions**. The benefit was mediated by *mental context reinstatement* — the ability to re-activate the encoding context during recall. Duolingo's uniform, gamified interface provides no context differentiation across sessions, precluding this mechanism entirely.

Mihaylova et al. (2022) synthesizes 23 studies and finds a moderate-to-strong immediate effect for mobile language apps (*g* = 0.88), but only 3 of 23 studies included delayed follow-up assessments — and those showed only small effects. The evidence base for long-term communicative transfer is rated "low" to "very low" quality by GRADE standards. The field's own data does not support the confident transfer claims app marketing implies.

**Why this is a system failure, not a user failure.** The decontextualized interface is an architectural decision, not a consequence of how learners choose to engage. Learners cannot inject social context, persona, or situational embedding into an app that offers none. The precondition gap is built into the product — no amount of user diligence can compensate for an environment that systematically withholds the cues memory retrieval requires.

> *"Apps 'teach vocabulary in isolated units rather than relevant contexts... these apps are behaviorist in nature.'"* — Godwin-Jones (2018)

---

## Level 3 — Unsafe Supervision (Algorithm Design, Metrics)

### Failure: Optimization Target Is Engagement, Not Communicative Competence

In HFACS, unsafe supervision refers to the oversight layer responsible for managing operator performance — in this domain, the algorithm that selects tasks, sequences content, delivers feedback, and signals progress. Duolingo's supervisory algorithm is designed around engagement proxies (streaks, XP, hearts, leaderboards) rather than language acquisition outcomes.

The spaced repetition scheduler optimizes for *item memorization* — surfacing flashcard-style items at intervals calibrated to prevent forgetting. Godwin-Jones (2018) explains that while SRS produces excellent memorization outcomes, it "does not build the pragmatic knowledge needed to deploy words appropriately in conversation." The algorithm is optimized for the wrong variable: retention of isolated forms, not production in context.

Kristensen et al. (2024) further demonstrate that the supervisory algorithm does not detect or respond to error repetition patterns. Learners who repeatedly make the same mistakes continue to receive the same exercise format; the app provides no corrective explanation, no escalation, no adaptive path change. The authors recommend automated detection of error patterns and explanatory feedback — neither of which Duolingo's algorithm currently provides.

Jiang et al. (2021) expose the deepest supervisory failure: the algorithm tracks and reports progress on reading and listening, but never tasks learners with speaking or writing. The entire supervisory loop — task selection, performance measurement, feedback, progression — is built around skills that are not the point of language for most learners. Speaking, the terminal goal, is unsupervised by design.

**Why this is a system failure, not a user failure.** Learners cannot override the algorithm's task selection or feedback logic. They practice what the system assigns, receive the feedback the system generates, and progress according to the system's metrics. If the supervisory algorithm is optimizing for engagement rather than transfer, learners operating faithfully within it will achieve engagement and not transfer. The failure is in the design of the supervisor, not in the behavior of those supervised.

> *"No other skills were assessed."* — Jiang et al. (2021), on Duolingo's own outcome research

---

## Level 4 — Organizational Influences (Business Model, Incentives)

### Failure: Profit Metrics Misaligned with Language Learning Outcomes

HFACS Level 4 identifies the organizational pressures and resource allocation decisions that shape everything downstream. For Duolingo, the relevant organizational facts are: it is a publicly traded company, its primary business metric is Daily Active Users (DAU), and its product decisions are driven by what sustains engagement, not what produces communicative competence.

The streak mechanic — Duolingo's most prominent retention feature — is engineered to create habit loops and re-engagement anxiety. It measures daily platform presence, not language progress. Mayer (2021) documents that the instructional characteristics that most improve learning outcomes — personalized conversational delivery, relational persona, social cues, dialect-specific voice — carry an implementation cost and do not directly contribute to DAU. A feature that makes the app feel like a conversation with a real person from the target culture is harder to build and does not drive a streak notification. The organizational incentive structure selects against the features that would actually help.

Jiang et al. (2021) documents that Duolingo's own published research program covers reading and listening — and explicitly notes speaking was not assessed. This is not an oversight; it is a research strategy. Validating speaking outcomes would require expensive human raters or validated automated speaking assessments, and the results might be unflattering. Publishing only the favorable metrics (strong receptive skill gains) while leaving productive skill outcomes unstudied insulates the brand while the transfer gap persists. This is an organizational decision about what to measure and what to disclose.

Godwin-Jones (2018) observes that the behaviorist, decontextualized architecture of vocabulary apps is not pedagogically naive — it is commercially efficient. Isolated drill items are cheap to generate at scale, easy to gamify, and produce the short-term memorization gains that feel rewarding. Context-rich, socially embedded instruction would require dialect expertise, scenario design, and conversational AI infrastructure. The organizational cost-benefit calculus consistently favors the scalable, gamified approach.

**Why this is a system failure, not a user failure.** Individual learners do not set the company's KPIs, allocate the engineering budget, or decide which skills get assessed in outcome research. The misalignment between profit incentives and learning outcomes is an organizational architecture problem. Learners who trust a product marketed with outcome claims are not responsible for the fact that those claims rest on a selectively narrow evidence base. The failure originates at the level of the organization's design choices and accountability structures.

> *"The personalization principle...was supported in 10 out of 10 experimental tests, yielding a median effect size of 1.3."* — Mayer (2021)
> *(A finding the organizational incentive structure systematically underweights.)*

---

## Sources

| Citation | Level Applied |
|---|---|
| Jiang et al. (2021). *Foreign Language Annals*, 54(4), 974–1002. | L1, L3 |
| Kristensen et al. (2024). *Computers & Education*, 210, 104966. | L1, L3 |
| Godwin-Jones (2018). *Language Learning & Technology*, 22(3), 1–19. | L2, L3, L4 |
| Essoe et al. (2022). *npj Science of Learning*, 7, 31. | L2 |
| Mihaylova et al. (2022). *Psychologica Belgica*, 62(1), 252–271. | L2 |
| Mayer (2021). In *Cambridge Handbook of Multimedia Learning* (3rd ed.). | L4 |
