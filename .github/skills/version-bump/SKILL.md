---
name: version-bump
description: "Bump the Python package version in pyproject.toml following Semantic Versioning. Use when: version bump, release, update version number, semver."
argument-hint: "Bump the package version"
---

# Version Bump

## Procedure

### Step 1 — Explain Semantic Versioning

Briefly explain Semantic Versioning (semVer) to the user:

> A version number has three parts: **MAJOR.MINOR.PATCH** (e.g. `1.4.2`).
>
> | Part      | When to increment             | Example                                   |
> |-----------|-------------------------------|--------------------------------------------|
> | **MAJOR** | Breaking change — existing users must update their code | `1.4.2` → `2.0.0` (removed a function)    |
> | **MINOR** | New feature — everything old still works               | `1.4.2` → `1.5.0` (added a new function)  |
> | **PATCH** | Bug fix or small tweak — no new features               | `1.4.2` → `1.4.3` (fixed a calculation)   |
>
> When you bump a higher part, the lower parts reset to zero.

### Step 2 — Ask the user what changed

Use the ask-questions tool to ask the user what kind of change they made. Provide these options:

- **Breaking change** — removed, renamed, or changed how something works (bumps MAJOR)
- **New feature** — added something new, nothing existing changed (bumps MINOR)
- **Bug fix / small tweak** — fixed a problem or made a minor improvement (bumps PATCH)

### Step 3 — Read the current version

Read `pyproject.toml` at the workspace root and locate the `version` field under `[project]`.

### Step 4 — Compute the new version

Parse the current version as `MAJOR.MINOR.PATCH` (integers). Based on the user's answer:

- **Breaking change** → increment MAJOR, reset MINOR and PATCH to 0
- **New feature** → increment MINOR, reset PATCH to 0
- **Bug fix / small tweak** → increment PATCH

### Step 5 — Update pyproject.toml

Replace the old `version = "..."` line in `pyproject.toml` with the new version. Report the change to the user (e.g. `0.1.0` → `0.2.0`).
