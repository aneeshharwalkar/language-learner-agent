"""
Language learner agent CLI.
Usage: python agent.py <dialect> <message>
Dialects: mexican-spanish, castilian-spanish
"""

import json
import sys

import anthropic
from dotenv import load_dotenv

from content import get_content_summary

load_dotenv()

AGENTS = {
    "mexican-spanish": {
        "name": "Carlos (Mexican Spanish)",
        "persona": (
            "You are Carlos, a warm and patient Mexican Spanish tutor from Mexico City. "
            "You naturally use Mexican expressions: 'ahorita', 'órale', 'chido', 'cuate', '¿Mande?'. "
            "You use 'ustedes' for informal plural address (no vosotros). Address a single learner as 'tú'."
        ),
    },
    "castilian-spanish": {
        "name": "Elena (Castilian Spanish)",
        "persona": (
            "You are Elena, an enthusiastic Castilian Spanish tutor from Madrid. "
            "You naturally use Castilian expressions: 'venga', 'tío/tía', 'guay', 'mola'. "
            "You use 'vosotros' naturally and apply the Castilian distinción (c/z pronounced like 'th')."
        ),
    },
}

_SYSTEM_TEMPLATE = """{persona}

{content_summary}

The learner is practicing conversational Spanish. Respond ONLY with a JSON object — no extra text, no markdown:
{{
  "reply": "<your conversational response in Spanish; add a brief English gloss in parentheses where helpful>",
  "correction": "<a gentle grammar or usage correction if the learner made a mistake, or null>",
  "vocab_tip": "<one dialect-specific word or phrase tip relevant to this exchange, or null>"
}}

Keep replies to 1–3 sentences. Be warm, natural, and encouraging."""


def chat(dialect: str, message: str) -> dict:
    """Call the dialect agent and return a structured response dict."""
    if dialect not in AGENTS:
        raise ValueError(
            f"Unknown dialect '{dialect}'. Valid options: {list(AGENTS.keys())}"
        )

    agent = AGENTS[dialect]
    client = anthropic.Anthropic()

    system = _SYSTEM_TEMPLATE.format(
        persona=agent["persona"],
        content_summary=get_content_summary(dialect),
    )

    response = client.messages.create(
        model="claude-sonnet-4-6",
        max_tokens=512,
        system=system,
        messages=[{"role": "user", "content": message}],
    )

    text = next(b.text for b in response.content if b.type == "text")
    # Claude sometimes wraps JSON in markdown fences — strip them
    text = text.strip()
    if text.startswith("```"):
        text = text.split("\n", 1)[1].rsplit("```", 1)[0].strip()
    data = json.loads(text)

    if "reply" not in data:
        raise ValueError("Agent response missing required 'reply' field")

    data["agent"] = agent["name"]
    return data


if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python agent.py <dialect> <message>")
        print("Dialects: mexican-spanish, castilian-spanish")
        sys.exit(1)

    try:
        result = chat(sys.argv[1], sys.argv[2])
        print(json.dumps(result, ensure_ascii=False, indent=2))
    except (ValueError, json.JSONDecodeError) as e:
        print(f"Error: {e}", file=sys.stderr)
        sys.exit(1)
