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

SCENARIOS = {
    "restaurant": "at a restaurant — the learner is a customer ordering food, asking about dishes, and interacting with you as the server or host",
    "market": "at a local market — the learner is shopping, asking about produce, prices, and making small purchases from you as the vendor",
    "meeting-someone": "meeting someone new — a casual first introduction, small talk about where each of you is from, work, and interests",
    "directions": "getting directions — the learner is a visitor who needs help reaching a place, and you are a local giving directions",
}

_SYSTEM_TEMPLATE = """{persona}

{content_summary}{scenario_block}

The learner is practicing conversational Spanish. Respond ONLY with a JSON object — no extra text, no markdown:
{{
  "reply": "<your conversational response in Spanish; add a brief English gloss in parentheses where helpful>",
  "correction": <null, OR an object: {{"text": "[what was wrong] — [the grammar rule behind it].", "severity": "critical" | "polish"}}>,
  "vocab_tip": "<one dialect-specific word or phrase tip relevant to this exchange, or null>"
}}

Correction rules (IMPORTANT — follow strictly):
- Do NOT issue a correction when the learner's only error is a missing diacritic (e.g. tú/tu, sí/si, cómo/como, qué/que, está/esta, más/mas) or casing, and the intended meaning is unambiguous from context. This app is typed chat with no voice input — accents are inaudible, so we mirror the signal fidelity of real spoken conversation. Set correction to null in this case.
- Reserve corrections for: verb conjugation, gender/number agreement, wrong tense or mood, wrong pronoun, wrong vocabulary, wrong preposition, wrong auxiliary (ser vs. estar), or wrong word order.
- When you do correct, correction.text must follow the pattern "[what was wrong] — [the grammar rule behind it]." Explain the underlying rule so the learner understands WHY, not just WHAT.
- correction.severity = "critical" if the error changes meaning, breaks agreement, uses the wrong tense, or would confuse a native speaker (e.g. estoy vs. soy, wrong gender agreement, pensar en vs. pensar de).
- correction.severity = "polish" if the meaning is clear but phrasing is off, a more natural alternative exists, or there is a word-order preference.
- If there is no correctable error per the rules above, set correction to null.

Keep replies to 1–3 sentences. Be warm, natural, and encouraging.{opener_block}"""

_OPENER_BLOCK = (
    "\n\nTHIS IS THE OPENING TURN. The learner has not spoken yet — you speak first. "
    "Produce a short, warm, in-character opener that plants the scenario (you're the server, the vendor, "
    "a local, or a new acquaintance — whichever fits). Use your dialect's colloquialisms naturally. "
    "Set correction and vocab_tip to null, since the learner has not produced any language yet."
)

_OPENER_TRIGGER = "(Open the conversation now.)"


def _build_scenario_block(scenario: str | None) -> str:
    if not scenario:
        return ""
    description = SCENARIOS.get(scenario)
    if not description:
        return ""
    return (
        f"\n\nThis conversation is set in the following scenario: {description}. "
        "Stay grounded in this scenario for the whole conversation."
    )


def chat(
    dialect: str,
    message: str,
    scenario: str | None = None,
    history: list[dict] | None = None,
    turn: int = 0,
) -> dict:
    """Call the dialect agent and return a structured response dict.

    `history` is a list of prior turns ({"role": "user"|"assistant", "content": str})
    forwarded to Claude as the messages list so the agent has episodic context.

    When `turn == 0` and `scenario` is set and no history is present, the agent
    speaks first and produces an in-scenario opener (Essoe 2022 context
    reinstatement needs the environment to cue the scenario before the learner
    speaks).
    """
    if dialect not in AGENTS:
        raise ValueError(
            f"Unknown dialect '{dialect}'. Valid options: {list(AGENTS.keys())}"
        )
    if scenario is not None and scenario not in SCENARIOS:
        raise ValueError(
            f"Unknown scenario '{scenario}'. Valid options: {list(SCENARIOS.keys())}"
        )

    agent = AGENTS[dialect]
    client = anthropic.Anthropic()

    normalized_history: list[dict] = []
    for item in history or []:
        role = item.get("role")
        content = item.get("content")
        if role in ("user", "assistant") and isinstance(content, str) and content:
            normalized_history.append({"role": role, "content": content})

    is_opener = turn == 0 and bool(scenario) and not normalized_history and not message.strip()

    system = _SYSTEM_TEMPLATE.format(
        persona=agent["persona"],
        content_summary=get_content_summary(dialect),
        scenario_block=_build_scenario_block(scenario),
        opener_block=_OPENER_BLOCK if is_opener else "",
    )

    messages: list[dict] = list(normalized_history)
    messages.append(
        {
            "role": "user",
            "content": _OPENER_TRIGGER if is_opener else message,
        }
    )

    response = client.messages.create(
        model="claude-sonnet-4-6",
        max_tokens=512,
        system=system,
        messages=messages,
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
