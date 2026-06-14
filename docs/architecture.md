# Architecture

The canonical project spine is [drmlke-roadmap.md](drmlke-roadmap.md).

Current architecture priority:

- product core before Spark runtime
- identity and capabilities before mutating treasury state
- paper treasury ledger before paper execution
- treasury snapshot projection before UI, risk, reporting, or execution consumes
  ledger state
- paper position boundary before market data, valuation, orders, fills, or
  execution
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
  global safety locks, the one-paper-treasury boundary, and append-only paper
  ledger, treasury projection, and paper position domain contracts
- `packages/storage`: storage placeholder
- `packages/wallet`: future wallet, account-tracking, and execution-adjacent
  placeholder
- `packages/agents`: agent placeholder
- `packages/risk`: risk placeholder

Bootstrap safety boundaries:

- paper mode only
- no real wallet custody
- no exchange connections
- no live execution
- no AI model inference
- `CORE.0` contracts are typed identity, safety, and treasury boundaries only;
  authentication, sessions, database storage, and API enforcement remain later
  work
- `CORE.1` ledger contracts are append-only domain logic only; persistence,
  database schema, API routes, paper orders, fills, market data, strategies, and
  execution remain later work
- `CORE.2` treasury projection contracts are pure in-memory read-side domain
  logic only; persistence, API enforcement, paper orders, fills, paper
  positions, market data, market valuation, strategies, and execution remain
  later work
- `CORE.3` paper position contracts are pure in-memory domain logic only;
  persistence, API enforcement, paper orders, fills, ledger mutation, market
  data, market valuation, realized or unrealized PnL, strategies, and execution
  remain later work
