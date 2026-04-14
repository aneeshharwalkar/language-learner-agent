"""
Content fetcher for dialect-specific learning material.
Curated static text — suitable for POC.

Usage:
    from content import get_vocab, get_grammar_notes, get_content_summary
"""

_CONTENT: dict[str, dict] = {
    "mexican-spanish": {
        "vocab": [
            {"word": "ahorita", "meaning": "right now / in a bit (context-dependent)"},
            {"word": "órale", "meaning": "okay / let's go / wow (multipurpose affirmation)"},
            {"word": "chido/a", "meaning": "cool, great"},
            {"word": "güey / wey", "meaning": "dude, man (casual, between friends)"},
            {"word": "cuate", "meaning": "close friend, buddy"},
            {"word": "¿Mande?", "meaning": "Pardon? / Come again? (polite)"},
            {"word": "chambear", "meaning": "to work"},
            {"word": "chamba", "meaning": "job, work"},
            {"word": "padrísimo/a", "meaning": "awesome, very cool"},
            {"word": "neta", "meaning": "truth, for real ('en neta' = seriously)"},
        ],
        "grammar_notes": [
            "Mexicans use 'ustedes' for both formal and informal plural 'you' (no vosotros).",
            "'ahorita' can mean immediately, soon, or a while ago — context is everything.",
            "Diminutives (-ito/-ita) are very common: 'momentito', 'cafecito', 'ahorita'.",
            "The usted form is used more often than in Spain, even with friends and family.",
        ],
    },
    "castilian-spanish": {
        "vocab": [
            {"word": "venga", "meaning": "okay / come on / let's go (multipurpose)"},
            {"word": "tío/tía", "meaning": "dude / mate (casual address)"},
            {"word": "guay", "meaning": "cool, great"},
            {"word": "mola", "meaning": "it's cool / I like it"},
            {"word": "chorrada", "meaning": "nonsense, rubbish"},
            {"word": "chaval/chavala", "meaning": "kid, young person"},
            {"word": "currar", "meaning": "to work"},
            {"word": "curro", "meaning": "job, work"},
            {"word": "mazo", "meaning": "a lot ('me mola mazo' = I really like it)"},
            {"word": "flipar", "meaning": "to be amazed, to freak out (positive)"},
        ],
        "grammar_notes": [
            "Castilian uses 'vosotros/vosotras' for informal plural 'you'.",
            "The 'distinción': 'c' (before e/i) and 'z' are pronounced like English 'th' in 'think'.",
            "'Tuteo' (tú) is used even in semi-formal contexts in Spain.",
            "Leísmo: using 'le' instead of 'lo' for a direct object person is common and accepted.",
        ],
    },
}


def get_vocab(dialect: str) -> list[dict]:
    """Return the curated vocabulary list for the given dialect."""
    return _CONTENT.get(dialect, {}).get("vocab", [])


def get_grammar_notes(dialect: str) -> list[str]:
    """Return grammar notes for the given dialect."""
    return _CONTENT.get(dialect, {}).get("grammar_notes", [])


def get_content_summary(dialect: str, vocab_limit: int = 5) -> str:
    """
    Return a formatted content summary suitable for inclusion in an agent prompt.
    Caps vocabulary to `vocab_limit` items to keep prompts concise.
    """
    vocab = get_vocab(dialect)
    notes = get_grammar_notes(dialect)
    if not vocab and not notes:
        return ""

    lines = [f"Key {dialect} vocabulary:"]
    for item in vocab[:vocab_limit]:
        lines.append(f"  - {item['word']}: {item['meaning']}")

    if notes:
        lines.append("\nGrammar notes:")
        for note in notes:
            lines.append(f"  - {note}")

    return "\n".join(lines)
