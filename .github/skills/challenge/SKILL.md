---
name: challenge
description: "Test understanding of recently implemented code. Use when: challenge, quiz, test knowledge, do I understand, check understanding, comprehension check."
argument-hint: "Quiz me on code I just wrote"
---

# Challenge — Comprehension Check

## Purpose

After a user implements code with Copilot's help, this skill tests whether they genuinely understand what was written on their behalf.

## Procedure

### Step 1 — Identify the code to quiz on

Look at the user's current file or recent changes (use `git diff HEAD~1` if needed). Focus on the most substantive logic — not boilerplate.

### Step 2 — Ask 3–5 targeted questions

Use the ask-questions tool to present the questions one at a time or as a batch. Questions should fall into three categories:

1. **What does it do?** — Ask the user to explain a specific block, function, or expression in their own words. Pick something non-obvious.
2. **Why this approach?** — Ask why a particular decision was made (e.g. "Why does this use `replace` instead of `dropna`?" or "Why is the guard clause checking `<= 0` and not `< 0`?").
3. **What if?** — Ask what would happen if a key part changed (e.g. "What would happen if you removed line X?" or "What would this return if the input were empty?").

Guidelines for good questions:
- Target lines that Copilot likely generated, not lines the user clearly wrote themselves.
- Avoid trivia ("What does `import` do?"). Focus on domain logic, edge cases, and design trade-offs.
- Be specific — reference exact function names, variable names, or line numbers.
- At least one question should probe an edge case or failure mode.

### Step 3 — Evaluate the answers

After the user responds, give honest, supportive feedback:

- **Strong understanding** — The user can explain the logic, justify decisions, and predict behaviour under change. Acknowledge this clearly.
- **Partial understanding** — The user gets the gist but is vague on details or edge cases. Point out exactly which parts are fuzzy and explain them briefly.
- **Surface-level understanding** — The user cannot explain core logic or gives answers that repeat code without insight. Be direct but kind: explain what the code actually does, why, and encourage them to step through it.

End with a one-line verdict: "You understand this well", "You're most of the way there — review X", or "Worth spending a few minutes stepping through this before moving on."
