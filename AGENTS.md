# AGENTS.md

drmlke is a private/family local-first crypto intelligence and paper-trading platform.

Canonical spine: `docs/drmlke-roadmap.md`.

Wave naming rules:

- use canonical roadmap wave IDs from `docs/drmlke-roadmap.md`
- do not create new naming tracks without updating the master spine
- legacy aliases are allowed only for traceability
- keep reusable command blocks, run reports, validation logs, and commit
  instructions out of the master spine; manual commands belong in
  `docs/manual-runbook.md`
- every wave that uses manual commands must state execution context explicitly:
  `LOCAL / Exon`, `REMOTE / Spark one-shot`, `REMOTE / Spark interactive`,
  `REMOTE mutating`, or `FORBIDDEN`
- do not run commands from the wrong machine; code, git, tests, commits, and
  pushes are local development work on Exon, while Spark operations happen only
  through the approved `spark-vpn` SSH path

Foundational model:

- one treasury / portfolio managed by Francesco
- Francesco is the owner/operator
- Padre and Zio are initial viewer accounts
- not three independently traded family portfolios
- one client UI, different capabilities
- API permissions are the real security boundary

Hard boundaries for early development:

- no live trading implementation
- no real wallet custody
- no seed phrase generation or storage
- no private key storage
- no withdrawal support
- no exchange API keys in client or repository
- no real AI model downloads during bootstrap

Machine roles:

- Linux / Exon: primary development machine for Codex, git, tests, commits, and
  pushes.
- Spark: future runtime, storage, and provider machine reached through
  `spark-vpn`.
- MacBook: secondary development machine, not the primary runtime.
