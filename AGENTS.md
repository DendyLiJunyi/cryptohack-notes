# CryptoHack code repository instructions

## Purpose and scope

This is Junyi Li's personal repository for code written while learning cryptography through CryptoHack. Codex helps maintain the repository and supports learning through implementation.

The repository stores code and the minimum information required to run it. Mathematical notes, detailed write-ups, learning progress, and study plans belong on the owner's blog, 天涯不远: https://dendylijunyi.github.io/.

- Do not create learning journals, progress trackers, mathematical notes, or lengthy challenge explanations in this repository unless explicitly requested.
- Do not automatically edit or publish the blog.
- A short README, dependency files, concise code comments, and necessary execution instructions are appropriate.
- Treat the owner's current request as authoritative. These instructions supply defaults, not additional approval gates for ordinary local work.

## Communication

- Communicate with the owner in Chinese by default.
- Use clear English for identifiers, filenames, short code comments, and commit messages unless asked otherwise.
- Explain what changed, how to run it, and what was actually checked. Keep reports brief.
- If an important requirement is unclear, inspect the existing code first. Ask a focused question only when the uncertainty affects correctness or the owner's learning intent.

## Preserve the learning process

- Repository management does not authorize completing unsolved challenges. When asked to organize files, configure the environment, or maintain the repository, do only that work.
- When asked for help with a challenge, match the requested level of assistance. Give a hint when asked for a hint; provide a full implementation when explicitly asked for one.
- Do not search for complete solutions, fetch flags, or replace the owner's approach with a published solution unless requested.
- When debugging, preserve the owner's approach where practical and explain the relevant error. Do not silently turn a partial attempt into a complete solution.
- Keep meaningful existing attempts. Do not delete them or overwrite them with a new approach without a clear reason supported by the task.
- Do not describe AI-written or externally adapted code as the owner's independent work. Preserve relevant source attribution.

## Repository structure

Follow the existing structure if the repository already has one. For a new repository, use lowercase snake_case names and group challenges by topic.

Examples of paths:

- `general/<challenge_name>/solve.py`
- `mathematics/<challenge_name>/solve.py`
- `rsa/<challenge_name>/solve.py`
- `diffie_hellman/<challenge_name>/solve.py`
- `symmetric_ciphers/<challenge_name>/solve.py`
- `elliptic_curves/<challenge_name>/solve.sage`
- `hash_functions/<challenge_name>/solve.py`
- `lattices/<challenge_name>/solve.sage`
- `zero_knowledge/<challenge_name>/solve.py`
- `utils/` for genuinely shared code

Create categories only as needed. Do not generate empty category trees or placeholder challenge solutions. One self-contained script per challenge is the default; additional modules are justified only when they make the code easier to understand.

Keep required public challenge inputs beside the script, with descriptive filenames. Reference the original challenge URL. Do not copy entire challenge collections into the repository.

## Code conventions

- Prefer Python 3 for ordinary scripts and SageMath when its mathematical facilities are needed. Keep `.sage` scripts clearly distinguished from ordinary Python scripts.
- Use readable, direct code. Avoid introducing frameworks, plugin systems, or elaborate abstractions for short solutions.
- Use `main()` and an `if __name__ == "__main__":` guard for runnable Python scripts where practical.
- Use descriptive names and explicit conversions between integers, bytes, and strings. State byte order when relevant.
- Use exact integer or finite-field operations where the problem requires them; do not replace these with floating-point approximations.
- Add concise comments explaining non-obvious implementation choices or mathematical assumptions. Full derivations belong on the blog.
- Where useful, include a short module docstring with the challenge URL, an existing blog write-up URL, and the command to run the script. Never invent a blog URL.
- Make file paths relative to the script location when loading adjacent inputs so scripts do not depend on the caller's working directory.
- Keep network operations explicit, with sensible timeouts and bounded retries. Never run remote requests merely by importing a module.
- Do not hard-code a recovered flag as a substitute for implementing the solution. Avoid committing redundant output logs or flag-only files.

## Environment and dependencies

- Use a project-local Python virtual environment such as `.venv`. Do not alter the global Python installation.
- Follow an existing dependency-management convention. For a new small repository, `requirements.txt` is sufficient; add packages only when the code actually needs them.
- Do not add both a new package manager and a second dependency manifest without a concrete need.
- Document SageMath separately; do not assume installing a similarly named package through pip provides the SageMath runtime.
- Keep the root README short: repository purpose, environment setup, how to run Python/SageMath scripts, and a link to the blog.
- Record exact tested versions when relevant to reproducibility. Do not invent version pins or claim compatibility that was not checked.
- Ignore `.venv/`, `__pycache__/`, Python bytecode, `.env`, notebook checkpoints, OS metadata, and generated temporary outputs. Do not ignore public challenge inputs required to reproduce a solution.
- Never commit credentials, account cookies, private keys unrelated to a public challenge, or local environment secrets. Public challenge keys and sample data should be identified as such.

## Validation

- Validate the smallest relevant unit of work. For a short solution, running it on its supplied local input or checking a mathematical invariant is usually enough.
- Useful checks include verifying a modular inverse, checking that recovered plaintext re-encrypts correctly, or confirming that a recovered value satisfies the original equations.
- Distinguish syntax checks, local execution, and acceptance by CryptoHack. Do not claim that a challenge is solved or accepted without the corresponding evidence.
- If execution needs unavailable input, a dependency, or a remote service, say exactly what remains unchecked.
- Do not add a testing framework or CI pipeline by default. Add focused tests when reusable helpers or substantive changes justify them.
- Running a remote challenge solver is appropriate when the owner requests it or clearly includes it in the task. Ordinary file cleanup or refactoring should not contact challenge servers.
- Do not submit flags, log into accounts, or modify platform progress without an explicit request.

## Git workflow and change scope

- Inspect `git status` and relevant files before editing. Preserve unrelated local changes.
- Make focused changes that address the current task. Avoid repository-wide renaming or formatting unless requested.
- Do not create a commit merely because files changed. Commit when the owner requests it or has established a standing instruction to do so.
- When committing, stage only relevant files, review the staged diff, and use a short descriptive message such as `Add RSA challenge solver` or `Fix byte conversion in XOR solver`.
- Push when explicitly requested or covered by an established workflow. Never assume that a local edit also authorizes publishing it.
- Do not force-push, rewrite shared history, change repository visibility, delete remote branches, or publish releases without explicit authorization.
- Do not add dashboards, badges, generated statistics, GitHub Actions, Docker configuration, or automated blog integration unless requested or necessary for a concrete task.

## Completion report

After a task, briefly report:

1. The files changed and the purpose of the change.
2. The command needed to run the relevant script, if applicable.
3. What validation was performed and any remaining limitation.
4. Whether a commit or push occurred, if relevant.

Keep the repository useful as a collection of runnable cryptography code. Let the blog carry the explanations and learning narrative.
