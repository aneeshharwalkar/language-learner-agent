# API Contract — Language Learner Agent

**Locked. Do not modify without agreement from both Aneesh and Preston.**

---

## POST /chat

### Request

```json
{
  "dialect": "mexican-spanish" | "castilian-spanish",
  "message": "string",
  "turn": number,
  "scenario": "restaurant" | "market" | "meeting-someone" | "directions" | null,
  "history": [
    { "role": "user" | "assistant", "content": "string" }
  ]
}
```

| Field | Type | Description |
|-------|------|-------------|
| `dialect` | string | Which dialect agent to route to |
| `message` | string | The learner's message. May be an empty string **only** on the turn-0 opener request (see below); otherwise required. |
| `turn` | number | Conversation turn index (for history tracking in UI). `0` on the very first request of a session. |
| `scenario` | string or null | Optional. Conversation context (e.g., `"restaurant"`). Agent uses it to scaffold the opening and stay on-topic. `null` or omitted = freeform. |
| `history` | array | Optional. Prior turns in the same conversation, oldest first. Each item has `role` (`"user"` or `"assistant"`) and `content`. Empty or omitted on turn 0. Backend forwards this to Claude as the `messages` list. |

**Turn-0 scenario opener.** When `turn == 0`, `scenario` is set, `history` is empty, and `message` is an empty string, the backend treats the request as an opener request: the agent speaks first with an in-scenario, in-dialect greeting. The response is a normal `reply` with `correction` and `vocab_tip` both `null` — the frontend renders it as the first agent bubble. Research basis: Essoe et al. 2022 (context reinstatement requires the environment to cue the scenario before the learner speaks).

### Response

```json
{
  "reply": "string",
  "agent": "string",
  "correction": null | {
    "text": "string",
    "severity": "critical" | "polish"
  },
  "vocab_tip": "string | null"
}
```

| Field | Type | Description |
|-------|------|-------------|
| `reply` | string | The agent's conversational response |
| `agent` | string | Which agent responded (displayed in UI) |
| `correction` | object or null | Grammar/usage correction if applicable. When non-null, contains `text` (formatted as "[what was wrong] — [the grammar rule behind it]") and `severity` (`"critical"` = meaning/agreement/tense errors; `"polish"` = natural-phrasing suggestions). Null when no correction is warranted. Diacritic-only and casing-only errors never produce a correction (typed chat mirrors the signal fidelity of spoken conversation). |
| `vocab_tip` | string or null | Vocabulary note if applicable |
