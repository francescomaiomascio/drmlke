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

Initial runtime target is Linux/Arch locally, with later Spark deployment.
