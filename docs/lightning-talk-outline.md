# Lightning Talk Outline — Language Learner Agent
**Course:** Applied Human Factors, Spring 2026
**Team:** Preston Cusick + Aneesh Harwalkar
**Format:** 8-min Lightning Talk · 11 slides · due April 24, 2026
**Macro-arc:** **Evaluate → Analyze → Improve** (the course's own spine)

---

## Why this structure

The rubric rewards five things on the talk: **Rigor, Systems Thinking, Data Use, Design/Architectural Insight, Communication** — 4 pts each. Every slide below has to earn at least one. The structure is:

- **ACT I · Evaluate** (slides 1–3, ~2:15) — the system, its stressors, the measurable ceiling
- **ACT II · Analyze** (slides 4–7, ~3:00) — task/user demands, HFACS walk, name the enemy
- **ACT III · Improve** (slides 8–11, ~2:00) — redesign, system map, gap analysis, close

**Tentative speaker split** (adjust freely): P = Preston (hook, task-analysis handoff, redesign, close), A = Aneesh (ceiling data, HFACS, system map). Written to alternate in short blocks so each of you always has ~45 sec of breathing room.

---

# ACT I — EVALUATE

## Slide 1 — Title (P, 0:15)

**On screen**
- Title: **Deploying Conversational Agents to Bridge the Learning-Transfer Gap in Duolingo**
- Subtitle: Applied Human Factors · Spring 2026 · Cusick + Harwalkar
- Bottom accent line: *Evaluate → Analyze → Improve*

**Script**
> "Raise your hand if you've got a Duolingo streak going right now. *(beat)* Now keep it up if you can actually hold a five-minute conversation in the language you're learning. *(beat — very few hands)* That gap, right there, is our project."

**Rubric hit** — Communication (concrete, relatable hook)

---

## Slide 2 — The System & Its Stressors (P, 0:50)  *[Phase 1 · System & Context]*

**On screen**
- Headline: **500M+ users. One of the largest human-machine learning systems on Earth.**
- Three columns:
  - **Internal** — cognitive load · metacognitive illusion of fluency
  - **External** — streak pressure · XP · gamification
  - **Organizational** — DAU incentives · Innovator's Dilemma

**Script**
> "Duolingo is a human-machine system with over 500 million users. From the course we know every system sits under three kinds of stressors. Internal — cognitive load and the metacognitive illusion that seeing a word again means you know it. External — streaks, XP, crowns, the stuff the app makes you feel bad about when you miss a day. And organizational — Duolingo's business rewards daily active users, which locks them in an Innovator's Dilemma. They can't rebuild around real conversation without breaking the thing paying the bills."

**Rubric hit** — Systems Thinking, Rigor (course framework applied directly)

---

## Slide 3 — The Measurable Ceiling (A, 0:50)  *[Phase 1 continued]*

**On screen**
- BIG: **Intermediate Low** (reading) · **Novice High** (listening) · **Speaking: never assessed**
- Citation: Jiang, Rollinson, Plonsky et al. (2021), *Foreign Language Annals* · ACTFL scale
- Pull-quote from the paper: *"No other skills were assessed."*

**Script**
> "Here's what the measurement actually shows. Jiang, Rollinson, and Plonsky ran Duolingo learners through the ACTFL scale. Reading topped out at Intermediate Low. Listening at Novice High. And speaking — speaking was never tested. Duolingo's own outcome study literally says 'no other skills were assessed.' So the ceiling is real, it's measurable, and the productive skills — the ones that let you actually have a conversation — are invisible to the system that claims to be teaching you."

**Rubric hit** — Data Use (direct data-to-claim), Rigor

---

# ACT II — ANALYZE

## Slide 4 — Task & User Analysis (A, 0:45)  *[Phase 2]*

**On screen**
- Four quadrants, class demand lenses: **Attention · Memory · Workload · Cognition**
- One line under each:
  - Attention → fixates on XP/streaks (inattentional blindness)
  - Memory → Phonological Loop only · Episodic Buffer never engaged
  - Workload → over-loaded on gamification, under-loaded on production
  - Cognition → no pragmatic or sociolinguistic knowledge built

**Script**
> "We ran the four HF demand lenses from class. Attention — the learner's gaze and mental budget go to XP bars and streaks, not to linguistic content. Memory — Duolingo exercises the Phonological Loop but never the Episodic Buffer, the part of working memory that binds words to context. Workload — over-loaded on gamification, under-loaded on speech production. And Cognition — the pragmatic and sociolinguistic knowledge you need for real conversation is never built. The recognition task succeeds. The production task fails."

**Rubric hit** — Systems Thinking, Rigor (class vocab verbatim)

---

## Slide 5 — Data & Methodology (P, 0:40)  *[Phase 3]*

**On screen**
- Left: **14 peer-reviewed sources** (small stacked icons)
- Center: **Two meta-analyses carry the effect-size claims** — Bibauw d = 0.58 · Mayer d = 1.3
- Right: **Proposed future RCT** — simple 2×2: Agent Type (IV) × Speaking Performance (DV)
- Footer: *Acknowledged threat: no primary data in a 2-week window.*

**Script**
> "Two-week timeline, so we're upfront about the biggest threat to validity: no primary data of our own. Our approach is research-and-build — fourteen peer-reviewed sources, two meta-analyses carrying the effect-size claims, and a working proof-of-concept. For causal evidence we propose a future randomized controlled trial modeled on Wang's 2024 twelve-week design, where Agent Type is the manipulated variable — our IV — and speaking performance is the dependent measure."

**Rubric hit** — Rigor (methods + threats named), Data Use

---

## Slide 6 — HFACS · The Method (A, 0:35)  *[Phase 4 intro]*

**On screen**
- Reason's Swiss Cheese diagram — four stacked slices with holes
- Labels: **Unsafe Acts → Preconditions → Unsafe Supervision → Organizational Influences**
- Callout: *"Work backward through all four levels. Avoid blaming individuals."*

**Script**
> "For the Human Factors analysis itself we used HFACS — Reason's Swiss Cheese. Four levels: Unsafe Acts at the operator, Preconditions in the environment, Unsafe Supervision over the operator, and Organizational Influences at the top. And the course's core tenet: work backward through all four. Don't blame the person. Look for where the system failed."

**Rubric hit** — Rigor, Systems Thinking

---

## Slide 7 — The Swiss Cheese Lines Up (A, 1:10)  *[Phase 4 walk — star slide]*

**On screen** — a single vertical stack, top to bottom, each row with a hole aligned:
- **L4 · Organizational** — DAU KPIs exclude speaking
- **L3 · Unsafe Supervision** — Birdbrain optimizes item-correctness, not conversation
- **L2 · Preconditions** — Episodic Buffer foreclosed; no contextual encoding *(Essoe: 92% vs 76%)*
- **L1 · Unsafe Acts** — learner sees XP, gets no true signal *(SDT: every streak = a False Alarm)*
- Arrow down the middle with the caption: *the holes all line up*

**Script**
> "Walk it with me, top to bottom. Level 4 — organizational KPIs are daily active users, which explicitly exclude speaking as a measured outcome. That cascades to Level 3 — Birdbrain, Duolingo's own algorithm, optimizes item-correctness, not conversational performance. By TADMUS principles, the supervisor's d-prime on conversational failure is effectively zero. That forecloses Level 2 — without a supervisor asking for speech, the environment never engages the Episodic Buffer, and words never bind to context. Essoe showed this cleanly: distinct contexts produced 92% retention versus 76% in uniform contexts. Which leaves Level 1 — the learner acts on the only signal available, which is XP. In Signal Detection terms, every streak is a False Alarm on the signal that matters. The holes line up. This isn't a user mistake. The incident is structurally predicted."

**Rubric hit** — Systems Thinking (this is the slide that earns the 4 points), Rigor, Data Use

---

## Slide 8 — Name the Enemy (P, 0:40)  *[Phase 4 punchline]*

**On screen** — four numbered cards, bold, 2–4 words each:
- **01 The Decontextualized Drill**
- **02 The Wrong Signal**
- **03 The Receptive-Only Evidence Base**
- **04 The Aligned Holes**
- small attribution: *per Rosling · Tufte · Musk — name the enemy*

**Script**
> "The course says: name the enemy. Rosling, Tufte, Musk. So here they are, named. One — the Decontextualized Drill: vocabulary taught as isolated items, not embedded in social context. Two — the Wrong Signal: confident feedback about the wrong variable. Three — the Receptive-Only Evidence Base: Duolingo's own research measures reading and listening; speaking is unsupervised by design. And four — the Aligned Holes: fix any single layer in isolation and the cheese still lines up. Our redesign has to span levels."

**Rubric hit** — Communication (memorable framing), Systems Thinking

---

# ACT III — IMPROVE

## Slide 9 — The Redesign · Three Pillars (P, 1:10)  *[Phase 5 solution]*

**On screen**
- Center: phone/app screenshot of the prototype mid-conversation with Carlos
- Three pillars flanking:
  - **Dialogue works** — Bibauw et al. 2022 · d = 0.58
  - **Persona matters** — Mayer 2021 · d = 1.3, 10/10 experiments
  - **Dialect is the input** — Geeslin & Long 2014
- Footer caption: *Meet Carlos (Mexican Spanish) and Elena (Castilian Spanish).*

**Script**
> "Here's the proof-of-concept. A dialect-specific conversational agent — Carlos, Mexican Spanish, and Elena, Castilian — that scaffolds the interaction rather than just responding. It rests on three findings from the literature. One: Bibauw's 2022 meta-analysis across seventeen studies — dialogue-based CALL produces a medium effect, d equals point-five-eight, on second-language proficiency. Two: Mayer's Personalization Principle — d equals one-point-three across ten of ten experiments. Embodiment and conversational style aren't UX decoration; they're the mechanism. Three: Geeslin and Long — communicative competence requires acquiring sociolinguistic variation, which means the learner has to hear real dialect input. Classrooms don't provide that. Duolingo doesn't provide that. That's our wedge."

**Rubric hit** — Design/Architectural Insight (THE slide for this criterion), Data Use, Rigor

---

## Slide 10 — System Map + Gap Analysis (A, 0:55)  *[Phase 5 visual + honesty]*

**On screen — split top/bottom**

*Top — System map (before vs. after):*
- **Before:** Learner → Item → XP (loop closes on the wrong variable)
- **After:** Learner ↔ Dialect Agent ↔ Scaffolded Dialogue → bound context → feedback on production

*Bottom — Gap Analysis:*
- No primary data (two-week window)
- No A/B of dialect-specific vs. generic agent
- Wang 2024: chatbot moved affect, not performance, in 12 weeks
- **NEXT:** eye-tracking (IX Lab) to sharpen the L1 attention claim

**Script**
> "Here's the system map. Before, Duolingo's loop runs learner to item to XP, and the loop closes on the wrong variable. After, the agent sits in the middle, dialogue scaffolds context, and feedback is about production — not recognition. And we want to be honest about the gaps. No primary data. No A/B comparing dialect-specific to generic agents. And Wang 2024 — the closest adult-learner GenAI chatbot study — moved willingness to communicate and reduced speaking anxiety over twelve weeks, but it did not move measured speaking performance. A proof-of-concept is proof of plausibility, not proof of effect. Our next step is an eye-tracking study in the IX Lab to turn the Level 1 attention claim from conceptual to measurable."

**Rubric hit** — Design/Architectural Insight (system map as required visual), Rigor (honest limits), Communication

---

## Slide 11 — Close · The Tenet (P, 0:25)

**On screen**
- Dark slide, single line, large type: **"The system never changed — you did."**
- Small below: *System failure, not user failure.*
- Bottom: *Preston Cusick + Aneesh Harwalkar · Applied Human Factors · 2026*

**Script**
> "The course taught us one tenet above all: error is a system property, not a human shortcoming. Duolingo's learners aren't failing. The system is measuring the wrong thing, so it's teaching the wrong thing. We built a piece that measures what matters. Thank you."

**Rubric hit** — Communication (strong close), Systems Thinking (payoff)

---

# Rubric coverage check

| Criterion (4 pts each) | Slides that deliver it |
|---|---|
| **Rigor** | 2, 3, 5, 6, 7, 9, 10 |
| **Systems Thinking** | 2, 4, 6, 7, 8, 11 |
| **Data Use** | 3, 5, 7, 9 |
| **Design / Architectural Insight** | 9, 10 |
| **Communication** | 1, 8, 11 |

All five criteria hit by ≥3 slides. Target = **20/20**.

---

# Time budget

| Slide | Speaker | Sec | Running |
|---|---|---|---|
| 1 Title | P | 15 | 0:15 |
| 2 System | P | 50 | 1:05 |
| 3 Ceiling | A | 50 | 1:55 |
| 4 Task | A | 45 | 2:40 |
| 5 Methodology | P | 40 | 3:20 |
| 6 HFACS intro | A | 35 | 3:55 |
| 7 Swiss Cheese walk | A | 70 | 5:05 |
| 8 Name the Enemy | P | 40 | 5:45 |
| 9 Redesign | P | 70 | 6:55 |
| 10 Map + gaps | A | 55 | 7:50 |
| 11 Close | P | 25 | 8:15 |

**Total:** 8:15 — we'll trim ~15 sec in script rehearsal to land right at 8:00.

---

# Questions for Preston before we build the .pptx

1. **Speaker split** — P/A as marked above, or reshuffle? Particularly: do you want the close (slide 11), or does Aneesh want it?
2. **Opening hook** — the "raise your hand" gag. Keep, or swap for a personal Spanish-learning moment from you or Aneesh?
3. **Prototype screenshot (slide 9)** — can you grab a clean frame of the frontend mid-conversation with Carlos, or should I run the frontend and capture one? Also: background bubble color — keep the green ES treatment from your April 14 work, or scrub neutral for the deck?
4. **System-map visual (slide 10)** — want me to draw it in SVG when we build the deck, or do you/Aneesh want to sketch it first?
5. **Voice check** — re-read slide 7 and slide 9 scripts especially. Those are the densest. Mark anywhere it sounds too formal or not like you, and I'll rewrite.
6. **Does Aneesh need to sign off** on this outline before we build, or are you the final call?
7. **Design direction for the .pptx** — dark-theme to match your dashboard style (matches Airbnb deck approach), or the class's orange/black motif to mirror the professor's slides? I have a slight preference for dark-theme matching your brand, but this is your call.
