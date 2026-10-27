# AI Meeting Intelligence Assistant

A local transcript-processing demo that turns plain-text meeting notes into a short summary, candidate decisions, action items, and recurring terms.

## What works today
- Accepts a pasted transcript as plain text.
- Extracts action-like sentences with a named owner.
- Detects a few explicit decision phrases.
- Returns a bounded summary and frequent terms.
- Includes synthetic transcript data and unit tests.

## Run
Requires Python 3.10+ and no external services.

```bash
python - <<'PY'
import json
from app import analyze_transcript
sample = json.load(open("examples/meeting.json", encoding="utf-8"))
print(analyze_transcript(sample["transcript"]))
PY
```

## Tests
`python -m unittest discover -s tests -v`

## Limitations
This is a text heuristic, not speech recognition or an LLM summarizer. It will miss implied tasks, may misidentify names, and does not infer dates or speaker identity. Always check the output against the original meeting. A next step is adding a transcript-provider interface, calendar-aware due dates, and a review screen before exporting tasks to project-management tools.

## Explore more

- [AI Automated QA Test Generator](https://github.com/HardikPaghdar/ai-automated-qa-test-generator) — turns requirements into a test checklist.
- [Agentic Sales Outreach Copilot](https://github.com/HardikPaghdar/agentic-sales-outreach-copilot) — human-reviewed outreach drafts.
- [More projects on my portfolio](https://hardikpaghdar.netlify.app/).
