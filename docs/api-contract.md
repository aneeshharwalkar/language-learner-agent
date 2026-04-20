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
| `message` | string | The learner's message |
| `turn` | number | Conversation turn index (for history tracking in UI) |
| `scenario` | string or null | Optional. Conversation context (e.g., `"restaurant"`). Agent uses it to scaffold the opening and stay on-topic. `null` or omitted = freeform. |
| `history` | array | Optional. Prior turns in the same conversation, oldest first. Each item has `role` (`"user"` or `"assistant"`) and `content`. Empty or omitted on turn 0. Backend forwards this to Claude as the `messages` list. |

### Response

```json
{
  "reply": "string",
  "agent": "string",
  "correction": "string | null",
  "vocab_tip": "string | null"
}
```

| Field | Type | Description |
|-------|------|-------------|
| `reply` | string | The agent's conversational response |
| `agent` | string | Which agent responded (displayed in UI) |
| `correction` | string or null | Grammar/usage correction if applicable |
| `vocab_tip` | string or null | Vocabulary note if applicable |
