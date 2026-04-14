---
name: criticise
description: "Review the diff between the current branch and main. Use when: code review, criticise, critique, review changes, diff feedback, PR review."
argument-hint: "Review my changes against main"
---

# Criticise — Diff Review

## Procedure

### Step 1 — Get the diff

Run `git diff main...HEAD` in the terminal to obtain the changes between the current branch and `main`. If the command fails (e.g. `main` doesn't exist), try `git diff main..HEAD`, then fall back to `git diff HEAD~1`.

### Step 2 — Provide feedback

Review the diff and give constructive, specific feedback organised under these headings:

- **Code quality** — naming, structure, duplication, adherence to project conventions
- **Readability** — clarity of intent, unnecessary complexity, missing context
- **Potential bugs** — off-by-one errors, unhandled exceptions, race conditions, type mismatches
- **Missed edge cases** — boundary values, empty inputs, unusual but valid states

For each point raised, reference the exact file and line(s) involved.

### Step 3 — Suggest improvements

For every issue identified, propose a concrete fix or alternative. Show short code snippets where helpful. Prioritise suggestions from most to least impactful.

## Tone

Be supportive but honest. Acknowledge what the changes do well before pointing out problems. Avoid vague statements — every comment should be actionable.
