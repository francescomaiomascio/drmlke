# Architecture

The canonical project spine is [drmlke-roadmap.md](drmlke-roadmap.md).

Current architecture priority:

- product core before Spark runtime
- identity and capabilities before mutating treasury state
- paper treasury ledger before paper execution
- market data and benchmarks before strategy claims
- decision journal before advanced models or live extensions
- Spark remains reserved infrastructure until it does not delay the decision core

Architecture must follow the corrected account model:

- one owner-managed treasury
- Francesco as owner/operator
- Padre and Zio as initial viewer accounts
- one shared client with capability-based locks
- server-side permission enforcement for every critical action
- no per-family-member trading portfolios in the initial model

drmlke bootstrap modules:

- `apps/api`: FastAPI backend placeholder
- `apps/worker`: runtime worker placeholder
- `apps/provider`: local provider stub
- `apps/client`: future SvelteKit/Vite + Capacitor client
- `packages/core`: shared settings, paths, identity and capability contracts,
  global safety locks, and the one-paper-treasury boundary
- `packages/storage`: storage placeholder
- `packages/wallet`: treasury/ledger placeholder
- `packages/agents`: agent placeholder
- `packages/risk`: risk placeholder

Bootstrap safety boundaries:

- paper mode only
- no real wallet custody
- no exchange connections
- no live execution
- no AI model inference
- `CORE.0` contracts are typed domain boundaries only; authentication, sessions,
  database storage, API enforcement, ledger entries, market data, strategies,
  and execution remain later work
