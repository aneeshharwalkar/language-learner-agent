---
title: "Language Learner Agent"
type: project
tags: [project, agentic-ai, language-learning, human-factors, anthropic, spring-2026, portfolio]
created: 2026-04-10
updated: 2026-04-12
sources: [human-factors-final-project-chat, hf-project-proposal, hf-final-project-rubric]
---

# Language Learner Agent

**Full title:** *Deploying Conversational Agents to Bridge the Learning Transfer Gap in Language Learning*

A proof-of-concept agentic AI system that addresses the conversational learning transfer gap in app-based language education. The identified human-machine system under analysis is Duolingo — it teaches vocabulary and grammar effectively but fails to produce real conversational fluency. The Language Learner Agent is the proposed solution: dialect-specific conversational AI agents that ingest authentic language content and teach users to speak naturally in context. Built as the Human Factors final project (Spring 2026, Dr. Neumann) by Aneesh Harwalkar and Preston Cusick. **Due: April 24, 2026.** Deliverable: 8-minute Lightning Talk with a working proof of concept, system diagrams, and preliminary evaluation data.

---

## Goal

Demonstrate that agentic AI can improve [[learning-transfer]] in language learning by:
1. Exposing users to authentic language content — not textbook sentences
2. Offering dialect choice — different agents represent different regional varieties
3. Grounding the interaction in learning transfer theory: the *relationship* between learner and teacher affects how well knowledge sticks

The dialect-as-teacher-type framing is the core human factors insight: just as some people learn better from a friend vs. a professor vs. a coach, learners may transfer more from a dialect/persona they identify with or find engaging.

---

## Two-Layer Architecture

### Layer 1 — Build Team (5 Claude Code agents, development only)

Five agents collaborate across a shared GitHub repo to produce both the report and the consumer-facing product. They do not run in production — they exist only to build the project. GitHub is the coordination layer between two machines.

```
Aneesh's machine                    Preston's machine
─────────────────                   ─────────────────
Claude Code (Research)              Claude Code (HF Analysis)
Claude Code (Backend)               Claude Code (Frontend)
                                    Claude Code (QA/Challenger)
        │                                   │
        └──── git push ──► GitHub ◄──── git pull ──┘
```

| Agent | Owner | Machine | Directory | Starts when |
|-------|-------|---------|-----------|-------------|
| **Research Agent** | Aneesh | Aneesh | `docs/research/` | Immediately |
| **Backend Agent** | Aneesh | Aneesh | `backend/` | Immediately |
| **HF Analysis Agent** | Preston | Preston | `docs/hf-analysis/` | After Research Agent commits |
| **Frontend Agent** | Preston | Preston | `frontend/` | After `docs/api-contract.md` exists |
| **QA/Challenger Agent** | Preston | Preston | repo root | Last — after all agents committed |

**Why one QA agent, not two:** The QA agent challenges everything — backend code, research claims, HF analysis, and frontend outputs. Splitting it across two machines creates two partial reviewers that each miss half the project. Preston owns it; it reads the full repo via git.

### Layer 2 — Consumer-Facing Product (what the build team produces)

A working language learning app. Internal architecture is determined by the Backend Agent — number of agents and routing logic is Aneesh's call. Preston sees one clean chat interface.

**Lightning Talk meta-narrative:** We used a Claude Code agent team to build an agent-based language learning product. The tools we used to build it mirror the architecture we're proposing as a fix for Duolingo. We dogfooded the concept.

---

## Rubric Map (100 pts total)

### Report / Slide Deck — 80 pts

| Phase | Points | Deliverable | Fed by |
|-------|--------|-------------|--------|
| 1 — System & Context | 20 | Duolingo as human-machine system; learning transfer failure historically framed; contrast app-based vs. immersive methods; why it matters at scale | Research Agent |
| 2 — Task & User Analysis | 10 | Recognition-based tasks Duolingo handles well vs. production-based tasks where transfer breaks down; cognitive + perceptual demand map | Research Agent + HF Analysis Agent |
| 3 — Data & Methodology | 10 | Existing literature on transfer failure; Claude Code POC as primary method; design decision documentation; weaknesses acknowledged; future controlled study proposed | QA Agent eval log |
| 4 — HF Analysis & Findings | 20 | HFACS applied to Duolingo across all 4 levels; performance breakdowns; why failures occur; HF concepts applied | HF Analysis Agent |
| 5 — Redesign & Recommendations | 20 | Working consumer-facing app; system architecture diagrams; UI screenshots; gap analysis; preliminary eval data | All agents |

### Lightning Talk — 20 pts (4 pts each)

| Criterion | Target |
|-----------|--------|
| Rigor | Justify literature + POC build as right methodology for a 2-week sprint |
| Systems Thinking | HFACS across all 4 levels; Technical / System / Human / Environment dimensions |
| Data Use | Learning transfer research grounds claims; POC demo as live evidence |
| Design/Architectural Insight | Agent architecture diagram; user journey map; dialect-as-persona framing |
| Communication | Narrative arc: problem → evidence → insight → solution → future work; crisp 8-minute pacing |

---

## HFACS Applied to Duolingo (Phase 4)

Working backward from the observable failure: *users complete Duolingo but cannot hold real conversations in the target language.*

| HFACS Level | Application |
|-------------|-------------|
| **1 — Unsafe Acts** (operator level) | Learner relies on recognition (tapping the right bubble) rather than production (generating speech). Streak maintenance rewarded over actual fluency. User behavior is shaped by app incentives, not learning outcomes. |
| **2 — Preconditions** (environment, mental state) | No authentic conversational context. Tasks are decontextualized isolated vocabulary drills. No relational element — learner has no consistent teacher persona to build rapport with. |
| **3 — Unsafe Supervision** (system design) | Duolingo's adaptive algorithm tracks retention of isolated vocab, not conversational transfer. No mechanism detects that learners cannot apply what they've memorized. Progress metrics (streaks, XP) mask fluency gaps. |
| **4 — Organizational Influences** (culture, policy) | Gamification is core to Duolingo's business model (DAU, streak engagement). This structurally de-incentivizes investment in harder-to-measure outcomes like conversational transfer. The system optimizes for the measurable metric (retention), not the meaningful one (fluency). |

**Key rule:** blame is placed on the *system*, not the learner. Users engage faithfully — the interface is the failure.

---

## API Contract (locked — do not change without both agreeing)

```
POST /chat

Request:
{
  "dialect": "mexican-spanish" | "castilian-spanish",
  "message": string,
  "turn": number
}

Response:
{
  "reply": string,
  "agent": string,
  "correction": string | null,
  "vocab_tip": string | null
}
```

- `turn` — Preston needs this for conversation history tracking in the UI
- `agent` — Preston's UI displays which agent is responding (scores Design/Architectural Insight rubric criterion)
- `correction` + `vocab_tip` — genuinely useful UI elements that show the system is teaching, not just chatting

---

## Repo Structure

```
language-learner-agent/
├── CLAUDE.md                  ← shared top-level context, read by all agents
├── docs/
│   ├── api-contract.md        ← locked interface between frontend and backend
│   ├── research/
│   │   ├── CLAUDE.md          ← Research Agent instructions
│   │   └── <author-year>.md   ← one file per source
│   └── hf-analysis/
│       ├── CLAUDE.md          ← HF Analysis Agent instructions
│       └── hfacs-analysis.md  ← HFACS output → feeds Phase 4 slides
├── backend/
│   ├── CLAUDE.md              ← Backend Agent instructions
│   ├── agent.py               ← dialect agent core logic (Anthropic API)
│   ├── server.py              ← Flask server (/chat endpoint)
│   ├── content.py             ← content parser (real-world text fetcher)
│   └── requirements.txt
└── frontend/
    ├── CLAUDE.md              ← Frontend Agent instructions
    ├── index.html             ← dialect selector + chat interface
    └── style.css
```

---

## CLAUDE.md Files

### Root `CLAUDE.md` (shared by all agents)
```
Project: Language Learner Agent
Course: Applied Human Factors, Spring 2026
Team: Aneesh Harwalkar (backend) + Preston Cusick (frontend)
Due: April 24, 2026

Goal: Build a proof-of-concept language learning app that addresses
Duolingo's conversational transfer gap using dialect-specific AI agents.

Stack: Python + Flask + Anthropic API (backend), HTML/CSS/JS (frontend)
API contract: docs/api-contract.md — never modify without team agreement

Do not touch files outside your assigned directory.
Do not modify docs/api-contract.md.
Commit frequently with clear messages.
```

### `docs/research/CLAUDE.md`
```
You are the Research Agent for the Language Learner Agent HF project.
Scope: this directory only. Output one .md file per source.

Goal: find and summarize 5-7 sources on:
  (1) Duolingo's conversational fluency limitations
  (2) learning transfer failure in app-based language learning
  (3) how context, relationship, or persona affects knowledge retention

For each source write <author-year>.md with:
  - Citation (APA)
  - 3-5 bullet summary
  - Key quote if available
  - Which rubric phase this supports (Phase 1, 2, or 4)

Prioritize peer-reviewed sources. Duolingo Research blog is acceptable.
When done, commit all files with message: "research: agent complete"
```

### `docs/hf-analysis/CLAUDE.md`
```
You are the HF Analysis Agent for the Language Learner Agent project.
Scope: this directory only.

First: read all .md files in docs/research/.
Goal: produce hfacs-analysis.md — HFACS analysis of Duolingo's
learning transfer failure across all 4 levels:
  Level 1 — Unsafe Acts (operator/learner)
  Level 2 — Preconditions (environment, mental state, context)
  Level 3 — Unsafe Supervision (algorithm design, metrics)
  Level 4 — Organizational Influences (business model, incentives)

For each level: state the failure, cite a research source, explain
why this is a system failure not a user failure.
Also write a 3-bullet "Key Findings" summary for the slide header.
This feeds Phase 4 of the slide deck (20 pts).
When done, commit with message: "hf-analysis: agent complete"
```

### `backend/CLAUDE.md`
```
You are the Backend Agent for the Language Learner Agent.
Scope: backend/ directory only.
Stack: Python, Anthropic API (claude-sonnet-4-5), Flask.
API contract is in docs/api-contract.md — build exactly to that spec.

Build order:
  1. agent.py — CLI that accepts dialect + message, returns a response
  2. server.py — Flask wrapper exposing POST /chat per the API contract
  3. content.py — simple content fetcher (curated static text is fine for POC)

Never commit .env or API keys.
Add .env to .gitignore immediately.
When server.py is running locally, commit with: "backend: server running"
```

### `frontend/CLAUDE.md`
```
You are the Frontend Agent for the Language Learner Agent.
Scope: frontend/ directory only.
Stack: plain HTML + CSS + vanilla JS. No frameworks needed for a POC.
Backend runs at http://localhost:5000.
API contract: docs/api-contract.md — build fetch calls to that spec.

Build:
  - Dialect selector at the top (mexican-spanish / castilian-spanish)
  - Chat window below showing the conversation
  - Display which agent responded (from response.agent field)
  - Show correction and vocab_tip inline if not null
  - Clean language-learning aesthetic

You can mock /chat with a static JSON response during development.
When UI is functional against mock, commit: "frontend: UI complete"
```

### QA/Challenger Agent (run from repo root on Preston's machine)
```
You are the QA/Challenger Agent for the Language Learner Agent project.
You have access to the entire repo.

Your job is to challenge every output produced by the other agents.
Be specific and cite line numbers or file names.

Check the following:
  Research Agent (docs/research/):
    - Are sources credible and peer-reviewed?
    - Do the summaries accurately represent the source?
    - Is there sufficient evidence to support each HFACS level claim?

  HF Analysis Agent (docs/hf-analysis/):
    - Is each HFACS level claim backed by a research citation?
    - Does the analysis blame the system, not the user?
    - Is the Key Findings summary slide-ready and accurate?

  Backend Agent (backend/):
    - Does server.py match the API contract in docs/api-contract.md exactly?
    - Are there any hardcoded secrets or missing error handling?
    - Run 3 test conversations: one Mexican Spanish, one Castilian Spanish.
      Document what works and what fails.

  Frontend Agent (frontend/):
    - Does the UI correctly display agent, correction, and vocab_tip fields?
    - Does the dialect selector actually change the request?

Output your findings to docs/qa-report.md.
Flag each issue as BLOCKER, WARNING, or NOTE.
BLOCKERs must be fixed before the demo. WARNINGs are nice-to-fix.
When done, commit: "qa: report complete"
```

---

## Tmux Setup

Running agents in tmux lets you watch all of them in split panes simultaneously — you can see when one goes idle (signal to start the next dependent agent).

### Aneesh's machine — 2 panes

```bash
tmux new -s lla-backend

# Pane 1 (Research Agent)
cd docs/research && claude

# Ctrl+b " to split → Pane 2 (Backend Agent)
cd backend && claude
```

### Preston's machine — 3 panes

```bash
tmux new -s lla-frontend

# Pane 1 (HF Analysis Agent)
cd docs/hf-analysis && claude

# Ctrl+b " → Pane 2 (Frontend Agent)
cd frontend && claude

# Ctrl+b " → Pane 3 (QA/Challenger — run last)
claude
```

**Key bindings:** `Ctrl+b "` horizontal split · `Ctrl+b %` vertical split · `Ctrl+b ↑↓←→` move between panes

---

## Getting Started — First Prompt

Drop the final plan file into the repo root. Then your first prompt to Claude Code should be:

> *"Read the final plan file and scaffold the repo structure, then write all the CLAUDE.md files from the plan into their correct directories."*

After that, Claude Code is fully oriented and can start the Research Agent and Backend Agent independently. Preston does the same after cloning.

---

## Sprint — Dependency Order

```
[Research Agent] ──────────────────────────────────────────────┐
      │                                                         │
      ▼ (needs research files)                                  │
[HF Analysis Agent]        [Backend Agent] ◄── start now       │
      │                           │                             │
      ▼                           ▼                             │
[Phase 4 slides drafted]   [server.py running]                  │
                                  │                             │
                    [Frontend Agent] ◄── needs api-contract.md  │
                                  │                             │
                          [QA/Challenger Agent] ◄───────────────┘
                                  │
                          [Slide deck assembly]
                                  │
                          [Lightning Talk rehearsal]
                                  │
                          [Submit — April 24]
```

### Phase checklist

**Phase A — start immediately, both machines**
- [ ] Aneesh: Research Agent running in `docs/research/`
- [ ] Aneesh: Backend Agent: `agent.py` CLI working
- [ ] Aneesh: `docs/api-contract.md` written and pushed
- [ ] Preston: dialect selector wireframes + slide deck template

**Phase B — unblocked once Phase A commits exist**
- [ ] Preston: `git pull` Aneesh's research commits → start HF Analysis Agent
- [ ] Aneesh: `server.py` Flask wrapper running locally
- [ ] Preston: Frontend Agent building `index.html` (needs api-contract.md)

**Phase C — report work, unblocked once Phase B analysis exists**
- [ ] Pull `hfacs-analysis.md` into Phase 3 + 4 slides
- [ ] Phase 1 + 2 slides drafted (system description, task analysis)
- [ ] System architecture diagram + user journey map

**Phase D — integration and QA**
- [ ] Preston: `git pull` all of Aneesh's backend commits
- [ ] Preston: QA/Challenger Agent runs → `docs/qa-report.md` produced
- [ ] Fix all BLOCKERs from QA report
- [ ] All 5 phases assembled in slide deck; screenshots embedded

**Phase E — presentation**
- [ ] Full 8-minute rehearsal; time each section
- [ ] Final polish and submit — **April 24, 2026**

---

## Lightning Talk Script Structure (8 minutes)

| Section | Time | Content |
|---------|------|---------|
| Hook | 0:00–0:30 | "You can finish Duolingo and still not be able to order coffee." |
| Phase 1 — System | 0:30–2:00 | Duolingo as human-machine system; why the transfer gap exists |
| Phase 2 — Task Analysis | 2:00–3:00 | Recognition vs. production; where cognitive demand breaks down |
| Phase 3 — Methodology | 3:00–3:30 | Research + build approach; honest about limitations |
| Phase 4 — HFACS | 3:30–5:00 | All 4 levels; system blame not user blame |
| Phase 5 — Live Demo | 5:00–7:00 | Show the working dialect agent; architecture diagram |
| Close | 7:00–8:00 | Future study design; what a controlled trial would measure |

---

## Team Roles

| Person | Owns | Agents |
|--------|------|--------|
| **Aneesh Harwalkar** | `backend/`, `docs/research/`, `docs/api-contract.md` | Research Agent, Backend Agent |
| **Preston Cusick** | `frontend/`, `docs/hf-analysis/` | HF Analysis Agent, Frontend Agent, QA/Challenger Agent |

---

## Open Questions

- [ ] Which 5–7 learning transfer studies anchor Phase 4? (Research Agent surfaces these)
- [ ] Mexican Spanish + Castilian Spanish as demo dialect pair — confirm with Preston
- [ ] Content source for `content.py` — static curated text vs. live RSS feed (static safer for POC)
- [ ] Pre/post fluency test within the sprint — feasible, or propose as future work?

---

## Connections

- [[learning-transfer]] — the core theory this project is built to address
- [[hf-project-proposal]] — the submitted proposal document this page is built from
- [[hf-final-project-rubric]] — the official grading rubric; drives the phase checklist and point allocation above
- [[human-factors-final-project-chat]] — the planning conversation that produced this project direction
- [[claude-agent-teams]] — reference for agent architecture thinking; GitHub coordinates across machines
- [[claude-code-skills]] — CLAUDE.md files serve the same context-loading purpose as skills
- [[job-agent]] — same Anthropic API + Python agentic architecture
- [[applied-machine-learning]] — multi-step agentic reasoning extends ML concepts from I 320D
- [[aneesh-harwalkar]] — Spring 2026 Human Factors capstone; partner: Preston Cusick
