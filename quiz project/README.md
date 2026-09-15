# CLI Quiz Engine

A command-line quiz game written in Python, with score tracking and a replay option.

## Features
- Loads questions from a JSON file
- Randomizes question order each round (without mutating the original data)
- Normalizes answers (case-insensitive, whitespace-trimmed) before checking correctness
- Tracks score and gives tiered feedback based on performance
- Lets the player choose to replay after each round

## How to Run
```bash
python quiz.py
```

## Requirements
- Python 3.8+
- No external libraries needed

## What I Learned
- Function scope and the call stack — how functions pause and resume when calling other functions
- Mutable vs. immutable data — copying a list before mutating it to protect the original from unintended changes
- Reading tracebacks and debugging indentation, syntax, and scope errors methodically
- Structuring a small program into single-responsibility functions instead of one long script