
# AI Project OS v2 - Automation Spec

## Core Mechanism
1. Every conversation = event stream
2. Events are classified into:
   - project_progress
   - decision
   - artifact
   - question

## Pipeline
Chat → Parse → Extract → Append → Index Update

## Output
- /projects/*/logs/daily.md
- /events/event_log.jsonl
- /index.json (auto-updated)
