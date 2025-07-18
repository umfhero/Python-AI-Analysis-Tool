import json

from paat.ast_linter.rules.base import Finding


def format_json(findings):
    """
    Format findings as a JSON array.
    """
    data = [f.to_dict() for f in findings]
    return json.dumps(data, indent=2)


def format_text(findings):
    """
    Format findings as plain text.
    """
    lines = []
    for f in findings:
        lines.append(f"{f.filename}:{f.lineno} [{f.type}] {f.message}")
    return "\n".join(lines)
