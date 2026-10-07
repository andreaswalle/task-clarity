# task-clarity

Analyzes task descriptions for evaluability.

Given a task, `task-clarity` identifies structural problems that make it
unsolvable or unmeasurable — missing constraints, ambiguous success criteria,
hidden assumptions.

## Usage

```bash
python main.py "Write a function that sorts a list."
```

Output:

```
SOLVABLE: unclear

PROBLEMS:
- No specification of sorting algorithm required
- No definition of list contents (integers, strings, objects?)
- No sort order specified (ascending, descending, custom?)
- No specification of in-place vs. new list requirement
- No programming language specified

MISSING FOR EVALUABILITY:
- Programming language
- Data type of list elements
- Sort order
- Edge case handling requirements
```

## Why

Most LLM evaluation fails before it starts — at the task level.
A task that cannot be clearly solved cannot be clearly evaluated.
This tool surfaces those problems before any model sees the task.

## Setup

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
cp .env.example .env
# add your Anthropic API key to .env
python main.py "your task here"
```

## Requirements

- Python 3.9+
- Anthropic API key