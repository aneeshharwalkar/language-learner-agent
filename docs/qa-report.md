# QA Report — Language Learner Agent
**Date:** 2026-04-14  
**Reviewer:** QA/Challenger Agent  
**Scope:** Research, HF Analysis, Backend, Frontend

---

## Summary

| Severity | Count |
|----------|-------|
| BLOCKER  | 2     |
| WARNING  | 7     |
| NOTE     | 5     |

BLOCKERs must be resolved before the April 24 demo.

---

## Section 1 — Research Agent (`docs/research/`)

### Credibility Assessment

All six sources are peer-reviewed:

| File | Venue | DOI/URL | Peer-Reviewed |
|------|-------|---------|---------------|
| essoe-2022.md | *npj Science of Learning* | ✓ DOI present | ✓ |
| godwin-jones-2018.md | *Language Learning & Technology* | ✗ No DOI | ✓ (LLT is peer-reviewed) |
| jiang-2021.md | *Foreign Language Annals* | ✓ DOI present | ✓ |
| kristensen-2024.md | *Computers & Education* | ✓ DOI present | ✓ |
| mayer-2021.md | *Cambridge Handbook of Multimedia Learning* (3rd ed.) | N/A (book chapter) | ✓ (edited scholarly volume) |
| mihaylova-2022.md | *Psychologica Belgica* | ✓ DOI present | ✓ |

---

> **WARNING — godwin-jones-2018.md, line 16–17:** The "Key Quote" (`Apps "teach vocabulary in isolated units rather than relevant contexts… these apps are behaviorist in nature."`) is formatted as a direct quotation but reads like a paraphrase or synthesis. No page number is provided, and the journal article has no DOI listed. It's not possible to verify verbatim accuracy. The quote is reused verbatim in `hfacs-analysis.md` at line 51. If this is a paraphrase, it must be rephrased or a page number/verified quote must be substituted before the demo.

> **WARNING — kristensen-2024.md:** The study population is **363 Norwegian second-graders** (children, L1 Norwegian). The project targets **adult Spanish learners**. The research file does not flag this generalizability gap. The HF analysis (lines 22–26, 64) uses this study as a direct mechanism explanation for adult transfer failure without qualification. At minimum, a caveat sentence should be added to the research file and the HF analysis.

> **NOTE — essoe-2022.md, line 17:** The Key Quote (`"Those who learned each language in its own unique context showed improved one-week retention (92%) compared to those learning in the same context (76%)."`) is written in a plain-prose, summary style atypical of academic journal text. This may be a paraphrase of the abstract rather than a verbatim quotation. Verify against the source before citing in a slide.

---

## Section 2 — HF Analysis Agent (`docs/hf-analysis/hfacs-analysis.md`)

### Citation Coverage Per Level

| HFACS Level | Citations Used | All in Research Files? |
|-------------|---------------|------------------------|
| L1 | Kristensen (2024), Jiang (2021) | ✓ |
| L2 | Godwin-Jones (2018), Essoe (2022), Mihaylova (2022) | ✓ |
| L3 | Jiang (2021), Godwin-Jones (2018), Kristensen (2024) | ✓ |
| L4 | Mayer (2021), Jiang (2021), Godwin-Jones (2018), **Loft et al. (2021)** | **✗ — see BLOCKER** |

### System-Blame Check

Each of the four levels includes an explicit "Why this is a system failure, not a user failure" paragraph. The analysis consistently locates the failure in design and incentive structures rather than learner behavior. This satisfies the course tenet requirement.

### Key Findings Slide Check

The three bullet points in "Key Findings" (lines 10–12) are accurate summaries of the body and are concise enough for a slide. Each maps cleanly to a HFACS level.

---

> **BLOCKER — hfacs-analysis.md, line 86:** `Loft et al. (2021)` is cited in-text ("transparency as a system variable (Loft et al., 2021)") but **no corresponding research file exists** in `docs/research/` and the source is **absent from the Sources table** (lines 99–106). This is an uncited claim supporting a key argument in Level 4. Either add a research file and sources table entry for Loft et al. (2021), or remove the citation and rephrase the argument around the existing sourced literature.

> **WARNING — hfacs-analysis.md, lines 46 and 63–64:** The **TADMUS** framework is invoked twice as a named authority ("From the TADMUS framework…", "TADMUS principles") but no specific TADMUS citation appears in the Sources table. TADMUS is treated as established background knowledge, which may be acceptable if the course has assigned it, but as written a reader cannot trace the claim to a source. Add a citation or attribute it explicitly to course materials.

---

## Section 3 — Backend Agent (`backend/`)

### API Contract Compliance

Contract source: `docs/api-contract.md`

**Request validation:**

| Contract Field | Required? | server.py behavior |
|---------------|-----------|-------------------|
| `dialect` | yes | validated, 400 if missing (line 28–29) ✓ |
| `message` | yes | validated, 400 if missing (line 30–31) ✓ |
| `turn` | yes (per contract) | accepted but silently ignored (comment line 25–26) ✓ |

**Response fields:**

| Contract Field | agent.py source | Present? |
|---------------|----------------|---------|
| `reply` | Claude JSON response | ✓ |
| `agent` | injected at agent.py line 69 | ✓ |
| `correction` | Claude JSON response (`null` allowed) | ✓ |
| `vocab_tip` | Claude JSON response (`null` allowed) | ✓ |

The server matches the API contract.

**Error handling:** `ValueError` → 400, `JSONDecodeError` → 502, generic `Exception` → 500. Adequate for a POC.

**Secrets:** `.env` is listed in `.gitignore` (root `.gitignore` lines 1–3). No API key is hardcoded in `server.py` or `agent.py`. `load_dotenv()` is called at `agent.py` line 13. No secrets issue.

---

### Live Conversation Testing

**Note:** The backend server was not running during this QA pass. The following is static analysis only. Live testing requires `python server.py` with a valid `ANTHROPIC_API_KEY` in `.env`.

**Mexican Spanish (static analysis):**
- Agent persona defined in `agent.py` lines 18–23.
- Agent name returned: `"Carlos (Mexican Spanish)"`.
- Dialect-specific expressions in prompt: `ahorita`, `órale`, `chido`, `cuate`, `¿Mande?`.

**Castilian Spanish (static analysis):**
- Agent persona defined in `agent.py` lines 24–31.
- Agent name returned: `"Elena (Castilian Spanish)"`.
- Dialect-specific expressions in prompt: `venga`, `tío/tía`, `guay`, `mola`.
- Prompt references `distinción` pronunciation — good for authenticity.

**What could fail at runtime:**
- Claude returns a response that fails JSON parsing → `JSONDecodeError` caught, 502 returned. The markdown-fence stripping at `agent.py` lines 65–67 mitigates the most common case.
- Claude omits a required field (`reply`) → `data` will be missing the key; the response is passed through without validation, so the frontend would receive an incomplete object.

> **WARNING — agent.py:** The `chat()` function does not validate that the Claude response dict contains the required `reply` field before returning it. If Claude produces valid JSON but omits `reply`, the frontend receives `{"agent": "Carlos...", "correction": null, "vocab_tip": null}` with no `reply` key, causing a silent blank message in the UI (no error surfaced to the user).

> **WARNING — agent.py, line 22:** The Mexican Spanish persona states `"You address learners as 'ustedes' in informal contexts"`. This is misleading: `ustedes` is plural. A single learner should be addressed as `tú`. The grammar note in `content.py` line 24 correctly states ustedes replaces vosotros for *plural* "you." This could cause the agent to produce unnatural Spanish.

> **WARNING — backend/content.py:** This module defines curated dialect-specific vocabulary and grammar notes with a `get_content_summary()` helper clearly designed for inclusion in the system prompt. However, **it is never imported by `agent.py` or `server.py`**. The agent relies entirely on Claude's parametric knowledge of dialects rather than the curated content. Either integrate `content.py` into the system prompt or remove it to avoid confusion.

> **NOTE — agent.py, line 58:** Model is `claude-sonnet-4-5`. The current latest is `claude-sonnet-4-6`. Not a breaking issue, but `4-6` has improved instruction-following which could reduce JSON-format violations at runtime.

> **NOTE — requirements.txt:** No version pins (e.g., `anthropic==0.x.x`). If Anthropic releases a breaking change before the demo, the install will silently upgrade. Pin versions before the demo to guarantee a reproducible environment.

> **NOTE — git status:** `backend/requirements.txt` and `backend/server.py` have uncommitted changes as of this report. These should be committed before the demo.

---

## Section 4 — Frontend Agent (`frontend/index.html`)

### Field Display

| Field | Element | How rendered | Correct? |
|-------|---------|-------------|---------|
| `agent` | `label.agent-label` (line 135) | `.textContent` | ✓ |
| `reply` | `div.agent-message` (line 140) | `.textContent` | ✓ |
| `correction` | callout div (line 143) | `escapeHtml()` → `.innerHTML` | ✓ (XSS-safe) |
| `vocab_tip` | callout div (line 144) | `escapeHtml()` → `.innerHTML` | ✓ (XSS-safe) |

Both `correction` and `vocab_tip` are null-checked before rendering (lines 143–144). If the backend omits them, nothing is rendered — correct behavior per contract.

### Dialect Selector

- Select element at line 17 uses the exact API contract values (`mexican-spanish`, `castilian-spanish`) as option values ✓
- `dialectEl.value` is read at submit time (line 169) and sent as the `dialect` field ✓
- Flag emoji updates on `change` event (lines 101–103) ✓
- Changing dialect mid-conversation is possible — the selector is live and not locked ✓

### Other Findings

> **WARNING — index.html, line 85:** When the backend returns an HTTP error (4xx/5xx), the frontend throws `Error("Server error: {status}")` and catches it to display a generic `"Could not reach the backend. Is the server running?"` message (line 181–182). The backend's JSON error body (e.g., `{"error": "Unknown dialect 'foo'"}`) is **never read or shown**. This means actionable error information from the server is silently discarded. At minimum, parse and display `res.json().error` on non-OK responses.

> **NOTE — index.html, line 46:** `API_URL = "http://localhost:8080/chat"` is hardcoded. Acceptable for the demo (which runs locally), but not deployable as-is.

> **NOTE — index.html:** No display of which dialect is currently active in the chat window itself. If a user changes the dialect mid-conversation, there is no visual indicator in the message history that the agent switched. A system message on dialect change would improve clarity.

---

## Required Actions Before Demo

### BLOCKERs (must fix)

1. **Add or remove Loft et al. (2021) citation** — `hfacs-analysis.md` line 86. Either create `docs/research/loft-2021.md` and add a Sources table entry, or remove the in-text citation and reframe the transparency argument using Jiang (2021) and Mayer (2021) which are already cited.

2. **Fix Mexican Spanish persona wording** — `agent.py` line 22. Change `"You address learners as 'ustedes' in informal contexts"` to `"You use 'ustedes' for informal plural address (no vosotros)"` to accurately reflect the grammar and avoid generating incorrect Spanish.

### WARNINGs (nice-to-fix)

3. Add Godwin-Jones (2018) page number or verify the Key Quote is verbatim.
4. Add a generalizability caveat for Kristensen (2024) in both the research file and HF analysis.
5. Add a TADMUS citation or attribute it to course materials.
6. Add `reply` field validation in `agent.py` `chat()` before returning.
7. Integrate or remove `content.py` — it is currently dead code.
8. Display backend error message body in the frontend instead of the generic fallback.

---

*QA pass complete. Live conversation tests against a running backend are pending and should be conducted by the backend agent or a team member before the April 24 demo.*
