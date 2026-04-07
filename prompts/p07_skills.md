# Prompts — 07 Skills

1. <details>
     <summary><code>/version-bump</code></summary>
     <blockquote> Create a skill that adds a <code>/version-bump</code> slash command. The skill is for contributors to a Python package who may not know what Semantic Versioning (semVer) is. When invoked, the skill should: (a) briefly explain semVer — what major, minor, and patch mean with simple examples, (b) ask the user what kind of change they made (breaking, new feature, or fix), (c) read the current version from pyproject.toml, (d) bump the appropriate part of the version number, and (e) update pyproject.toml with the new version.</blockquote>
    </details>
    <br>

2. <details>
     <summary><code>/criticise</code></summary>
     <blockquote>
     Create a skill that adds a <code>/criticise</code> slash command. When invoked, the skill should: (a) identify the diff between the current branch and main, (b) provide constructive, specific feedback on the changes — covering code quality, readability, potential bugs, and missed edge cases, and (c) suggest concrete improvements where appropriate. The tone should be supportive but honest.
     </blockquote>
    </details>
    <br>

3. <details>
     <summary><code>/challenge</code></summary>
     <blockquote>
     Create a skill that adds a <code>/challenge</code> slash command. The purpose is to test my cognitive understanding of code I have just implemented with Copilot's help. When invoked, the skill should: (a) look at recent changes or the current file, (b) ask me 3–5 targeted questions about what the code does, why certain decisions were made, and what would happen if key parts changed, and (c) after I answer, give me honest feedback on whether I truly understand the implementation or just accepted suggestions.
     </blockquote>
    </details>