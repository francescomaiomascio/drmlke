# Architecture

The canonical project spine is [drmlke-roadmap.md](drmlke-roadmap.md).
Canonical operational wave ids are phase ids such as `P0.H`, `P1.A`, and
`P2.A`. Legacy `CORE.*` names remain only as aliases for commits and prior
documentation.

Current architecture priority:

- product core before Spark runtime
- identity and capabilities before mutating treasury state
- paper treasury ledger before paper execution
- treasury snapshot projection before UI, risk, reporting, or execution consumes
  ledger state
- paper position boundary before market data, valuation, orders, fills, or
  execution
- paper portfolio snapshot before client, risk, reporting, market valuation, or
  execution consumes combined cash and position state
- paper decision record boundary before market data, strategy engines, paper
  execution, reports, or model assistance consume decision memory
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
  ledger, treasury projection, paper position, paper portfolio snapshot, and
  paper decision record domain contracts
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
- `P0.H` contracts, historically `CORE.0`, are typed identity, safety, and
  treasury boundaries only; authentication, sessions, database storage, and API
  enforcement remain later work
- `P0.I` ledger contracts, historically `CORE.1`, are append-only domain logic
  only; persistence, database schema, API routes, paper orders, fills, market
  data, strategies, and execution remain later work
- `P0.J` treasury projection contracts, historically `CORE.2`, are pure
  in-memory read-side domain logic only; persistence, API enforcement, paper
  orders, fills, paper positions, market data, market valuation, strategies, and
  execution remain later work
- `P0.K` paper position contracts, historically `CORE.3`, are pure in-memory
  domain logic only; persistence, API enforcement, paper orders, fills, ledger
  mutation, market data, market valuation, realized or unrealized PnL,
  strategies, and execution remain later work
- `P0.L` paper portfolio snapshot contracts, historically `CORE.4`, are pure
  in-memory read-side domain logic only; they combine treasury cash snapshots
  and paper position books without persistence, API enforcement, UI, paper
  orders, fills, ledger mutation, market data, market valuation, realized or
  unrealized PnL, returns, strategies, or execution
- `P0.M` paper decision record contracts, historically `CORE.5`, are pure
  in-memory domain logic only; they record paper no-action, watch, action
  candidate, rejected, postponed, and risk-vetoed decisions without market data
  ingestion, strategy execution, orders, fills, persistence, API enforcement,
  UI, provider runtime, exchange integration, wallet custody, or live trading
