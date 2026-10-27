"""Transcript-to-notes helper with conservative, rule-based extraction."""
import re
from collections import Counter

ACTION = re.compile(r"\b(?P<owner>[A-Z][\w.-]{1,24})\s+(?:will|to)\s+(?P<task>[^.!?]+)", re.I)
DECISION = re.compile(r"\b(?:we decided|decision:|agreed that)\s+([^.!?]+)", re.I)

def analyze_transcript(transcript: str) -> dict:
    if not transcript or not transcript.strip():
        raise ValueError("transcript must not be empty")
    lines = [line.strip(" -\t") for line in transcript.splitlines() if line.strip()]
    actions = []
    decisions = []
    for line in lines:
        for match in ACTION.finditer(line):
            actions.append({"owner": match.group("owner"), "task": match.group("task").strip()})
        for match in DECISION.finditer(line):
            decisions.append(match.group(1).strip())
    words = re.findall(r"[A-Za-z][A-Za-z'-]{3,}", transcript.lower())
    stop = {"about","after","again","also","been","could","from","have","into","just","more","need","that","their","there","this","will","with","would","your","they","then","them","were"}
    themes = [{"term": word, "count": count} for word, count in Counter(w for w in words if w not in stop).most_common(8)]
    return {"summary": " ".join(lines[:3])[:600], "decisions": decisions, "action_items": actions,
            "themes": themes, "source_lines": len(lines),
            "note": "Extraction is heuristic; review names, ownership, and decisions against the recording."}
