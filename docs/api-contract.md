# API Contract — Language Learner Agent

**Locked. Do not modify without agreement from both Aneesh and Preston.**

---

## POST /chat

### Request

```json
{
  "dialect": "mexican-spanish" | "castilian-spanish",
  "message": "string",
  "turn": number
}
```

| Field | Type | Description |
|-------|------|-------------|
| `dialect` | string | Which dialect agent to route to |
| `message` | string | The learner's message |
| `turn` | number | Conversation turn index (for history tracking in UI) |

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
