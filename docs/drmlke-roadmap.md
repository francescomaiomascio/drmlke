# drmlke Roadmap and Master Spine

This document is the canonical single source of truth for drmlke product shape,
system boundaries, delivery order, and future implementation waves.

This version records `P0.NAMING.1` naming normalization and the completed
Phase 0 product-core contracts through `P0.M - Paper Decision Record Boundary`,
historically aliased as `CORE.5`. It keeps canonical Phase 0 wave ids in front
of any Spark attachment, runtime deployment, trading feature, wallet feature,
exchange connection, mobile client scaffold, or AI model download.

## Naming Doctrine: Phase IDs, Legacy CORE Aliases, and Future Wave IDs

Phase ids are the canonical roadmap structure. `P0.*`, `P1.*`, `P2.*`, and
later phase ids are the canonical operational wave ids going forward.

`CORE.0` through `CORE.5` were temporary product-core labels introduced after
`DOCS.REVIEW.2`. They remain valid as historical aliases because they exist in
commit messages, previous prompts, and earlier docs. They are not the canonical
ids for new work after `P0.NAMING.1`.

Future implementation prompts must use canonical `P*.*` ids. A legacy alias may
appear in parentheses for traceability.

Example:

```text
P0.H - Identity, Capabilities, and Paper Treasury Boundary
(legacy alias: CORE.0)
```

Do not introduce new `CORE.*` names after this normalization unless the roadmap
explicitly creates a new major track. If a future prompt uses `CORE.*` alone as
the primary id, treat it as incomplete and correct the prompt before execution.

## 1. Current Project State

Current repository facts:

- Canonical Linux repo path: `/home/mothx/computer-science/projects/drmlke`.
- Current active workspace for this edit: `/home/mothx/computer-science/projects/drmlke`.
- MacBook repo path: `/Users/mothx/Developer/drmlke`.
- MacBook role: secondary active development node.
- Remote: `https://github.com/francescomaiomascio/drmlke.git`.
- Bootstrap commit: `e68a51b Bootstrap drmlke skeleton`.
- Master spine commit: `82f8fae DOCS.SPINE.3: complete master spine and correct next sequence`.
- `82f8fae` has been pushed to `origin/main`.
- Current canonical file: `docs/drmlke-roadmap.md`.
- Current completed wave: `P2.B - Tailscale Reachability`.
- Completed waves:
  - `P0.A - Repository Bootstrap` (legacy output: `BOOTSTRAP.0`).
  - `P0.B - Provider Stub`.
  - `P0.C - Environment Doctor`.
  - `P0.D - Safety Documentation`.
  - `P0.E - Treasury Model Correction` (legacy output: `DOCS.SPINE.2`).
  - `P0.F - Master Spine Completion` (legacy output: `DOCS.SPINE.3`).
  - `P0.G - Product Thesis, Decision Math, and MVP Gates`
    (legacy outputs: `DOCS.REVIEW.1`, `DOCS.REVIEW.2`).
  - `P0.H - Identity, Capabilities, and Paper Treasury Boundary`
    (legacy alias: `CORE.0`).
  - `P0.I - Append-Only Paper Treasury Ledger` (legacy alias: `CORE.1`).
  - `P0.J - Ledger Projection and Treasury Snapshot`
    (legacy alias: `CORE.2`).
  - `P0.K - Paper Position Boundary` (legacy alias: `CORE.3`).
  - `P0.L - Paper Portfolio Snapshot Boundary` (legacy alias: `CORE.4`).
  - `P0.M - Paper Decision Record Boundary` (legacy alias: `CORE.5`).
  - `P0.CLOSE - Phase 0 Product Core Closeout`.
  - `P2.A - Access Inventory`.
  - `P2.B - Tailscale Reachability`.
- Next recommended wave: `P2.C - SSH Verification`.

Current provider status:

- The provider stub works locally.
- Provider local health is expected to return ok.
- Provider local models are expected to return an empty list.
- The provider does not load a real AI model.
- The provider does not call an exchange.
- The provider does not execute orders.

Current environment status:

- Python is pinned to 3.12.
- Node is pinned to 24.
- Linux canonical repo path is
  `/home/mothx/computer-science/projects/drmlke`.
- Linux Node 24 is active as `v24.16.0`.
- Linux `make doctor`, `make check`, and local provider health/model checks
  pass.
- Linux provider stub is running through Docker Compose on port `8781`.
- MacBook Node 24 is active as `v24.16.0`.
- MacBook `uv` is active as `uv 0.11.17`.
- MacBook `pnpm` works through Corepack as `10.12.1`.
- MacBook Docker-compatible runtime is active through OrbStack on the
  `orbstack` Docker context.
- MacBook `make doctor`, `make check`, and local provider health/model checks
  pass.
- The MacBook system `python3` may be newer than 3.12; project validation uses
  the `uv` managed Python 3.12 environment.

Current Spark status:

- Spark is not attached yet for drmlke runtime work.
- Spark runtime deployment has not started.
- `/srv/drmlke` is not assumed to exist yet.
- The preferred future Spark access path is Tailscale or an explicit private SSH
  path, not a fragile local hostname dependency.
- Spark remains intentionally untouched by `MAC.SETUP.1-CLOSE`.
- Spark remains intentionally untouched by `LINUX.SETUP.1`.
- `DOCS.REVIEW.1` and `DOCS.REVIEW.2` keep Spark reserved until the product
  core is no longer blocked by identity, paper treasury, market data,
  benchmarks, and decision records.

What is implemented now:

- A Python monorepo workspace.
- `apps/api` FastAPI placeholder.
- `apps/provider` FastAPI provider stub.
- `apps/worker` worker heartbeat placeholder.
- `packages/core` shared settings and path helpers.
- `packages/core` typed identity, role, capability, global safety lock, and
  paper treasury boundary contracts.
- `packages/core` append-only paper ledger domain contracts for the single
  200 EUR paper treasury.
- `packages/core` paper treasury projection and snapshot contracts over the
  append-only ledger.
- `packages/core` paper position boundary contracts for initial BTC and ETH
  simulated long-only positions.
- `packages/core` paper portfolio snapshot contracts combining treasury cash
  snapshots and paper position books.
- `packages/core` paper decision record contracts for paper-only no-action,
  watch, action candidate, rejected, postponed, and risk-vetoed records.
- Placeholder packages for storage, wallet, agents, and risk.
- Dockerfiles for base, API, provider, and worker.
- Docker Compose profiles for local services.
- A Makefile with sync, lint, test, check, Docker, and doctor targets.
- Documentation for architecture, environment, deployment, and Spark planning.

What is not implemented now:

- No live trading.
- No exchange connection.
- No exchange API keys.
- No real wallet custody.
- No seed phrase generation.
- No private key storage.
- No withdrawal support.
- No market data collector.
- No persisted treasury ledger, database schema, or ledger API implementation.
- No persisted account, login, session, or device implementation.
- No API capability enforcement implementation.
- No paper orders or fills.
- No persisted paper positions, position transitions, paper orders, or fills.
- No market valuation.
- No realized or unrealized PnL calculation.
- No persisted portfolio snapshot.
- No mobile client scaffold.
- No web admin console.
- No strategy engine.
- No backtesting engine.
- No paper execution engine.
- No news or retrieval augmented generation system.
- No AI model download or inference.
- No Spark runtime deployment.

Sequencing correction:

1. `DOCS.SPINE.3` completes this master document.
2. `MAC.SETUP.1-CLOSE` records the MacBook as an active development node.
3. `LINUX.SETUP.1` records the canonical Linux development node and resolves
   stale Linux path references.
4. `DOCS.REVIEW.1` hardens product thesis, decision quality, math, strategy
   specification, backtest integrity, and MVP boundaries.
5. `DOCS.REVIEW.2` drafts MVP gates, promotion gates, and numeric risk policy.
6. `P0.H` implements identity, capabilities, and the paper treasury boundary
   (legacy alias: `CORE.0`).
7. `P0.I` implements the paper treasury ledger (legacy alias: `CORE.1`).
8. `P0.J` implements ledger projection and treasury snapshot contracts
   (legacy alias: `CORE.2`).
9. `P0.K` defines the paper position boundary (legacy alias: `CORE.3`).
10. `P0.L` defines a paper portfolio snapshot boundary
    (legacy alias: `CORE.4`).
11. `P0.M` defines the paper decision record boundary
    (legacy alias: `CORE.5`).
12. `P0.CLOSE` verifies Phase 0 product-core coherence before moving to
   infrastructure or persistence work.
13. `P2.A` inventories candidate Spark access paths without reachability
   testing, SSH login, Tailscale configuration, or deployment.
14. `P2.B` confirms Tailscale reachability without SSH login, remote mutation,
   Tailscale configuration, or deployment.
15. Tailscale and Spark remain infrastructure-only future work until they do
   not delay the decision core.

## 2. Product Definition

Product name: `drmlke`.

Meaning: `dreamlike`.

drmlke is a private and family-scoped, local-first crypto decision journal,
paper treasury, strategy research, benchmark, and auditability system. It is
designed to help Francesco observe markets, research conservative strategies,
simulate treasury behavior, preserve decision memory, and only much later
consider tightly gated manual real actions.

drmlke is not initially:

- a live trading bot
- a custodial wallet
- a public fund-management service
- an exchange
- a public financial advisory product
- a system that manages public user funds

drmlke is not an auto-trading product. Its first purpose is to help Francesco
make slower, better-tracked, less emotional decisions about a small private
crypto treasury. The system should make it easier to understand market context,
avoid damage, preserve capital, compare against simple alternatives, simulate
before acting, and review decisions after the outcome is known.

The long-term possibility of small manual real actions does not change the
early product thesis. Live action is a late extension only after paper evidence,
risk review, manual owner approval, and explicit gates. The core product is a
private decision and research system, not a machine that tries to trade by
itself.

The foundational product model is one treasury managed by Francesco. Francesco
is the owner and operator. Padre and Zio are initial observer users. They can
see permitted information, but they do not manage strategies, approve actions,
configure runtime behavior, or control funds.

The product has one application surface. It is not three different products and
not three independently traded portfolios. The same app serves all roles. The
difference between users is capability, not product identity.

If drmlke ever leaves private and family use, becomes public, provides public
financial service behavior, or manages money for people outside the private
family context, legal and regulatory review becomes mandatory before that
behavior is designed, shipped, marketed, or enabled.

### Target User and Target Outcome

Primary user:

- Francesco as owner, operator, and researcher.

Secondary users:

- Padre and Zio as trusted viewers.

Usage context:

- private
- local-first
- non-public
- one small owner-managed treasury
- conservative paper-first research

Initial capital assumption:

- small capital
- first real capital ceiling is 200 EUR
- first MVP paper treasury uses 200 EUR simulated capital

Target outcomes:

- learning
- discipline
- auditability
- capital preservation
- decision quality
- clear memory of why a decision was made
- clear comparison against doing nothing or simple accumulation

The desired user experience is not speed. It is friction in the right places:
better records, more explicit risk, clearer reasons not to act, and better
post-mortems.

### Expansion Discipline

drmlke has four expansion zones. Earlier zones must not be delayed by later
zones.

Core product:

- identity and capabilities
- paper treasury ledger
- market data
- deterministic feature engine
- benchmark engine
- backtest engine
- risk engine
- paper execution
- audit and reporting
- owner and viewer UI

Research extensions:

- classical ML
- compact time-series models
- LLM-assisted explanation
- embeddings
- sentiment
- retrieval augmented generation

Operator extensions:

- desktop console
- admin workflows
- reporting
- runtime observability
- backup and restore tools

Live extensions:

- shadow mode
- manual live action
- tightly gated auto-live candidate behavior

Live extensions are blocked until paper results prove value. Research
extensions are blocked until the core data, benchmark, backtest, and decision
records are reliable enough to evaluate them honestly.

### MVP Spine

MVP sequence:

1. `MVP.1 - Decision Journal and Paper Treasury`
2. `MVP.2 - Strategy Lab`
3. `MVP.3 - Risk and Paper Execution`

`MVP.1` is intentionally narrow:

- 200 EUR paper treasury
- BTC and ETH market data
- buy-and-hold benchmark
- scheduled accumulation benchmark
- paper ledger
- decision records
- risk veto records
- simple dashboard and reporting
- weekly report
- no ML
- no LLM
- no Spark dependency unless infrastructure-only and explicitly non-blocking

`MVP.2` adds strategy specification, deterministic features, benchmark
comparison, leakage-safe backtests, and regime-aware reports. It does not add
live trading.

`MVP.3` adds risk policy, risk veto enforcement, paper order simulation, fill
simulation, and promotion evidence. It does not add exchange execution.

If no strategy beats the relevant benchmark after realistic costs, the correct
product behavior is to preserve that negative result, keep the simple
benchmark visible, and avoid promoting the strategy.

## 2A. Decision Quality Spine

Decision quality is separate from economic outcome. A decision can be good and
lose money. A decision can be bad and make money. drmlke must preserve this
distinction as project doctrine.

Each decision is evaluated across four dimensions:

- process quality
- information quality
- risk compliance
- economic outcome

Process quality asks whether the owner followed the required thinking process.
Information quality asks whether the data and context were sufficient, fresh,
and correctly interpreted. Risk compliance asks whether the decision respected
policy, exposure, cost, and veto boundaries. Economic outcome asks what
happened financially after costs, but it must not rewrite the judgment of the
process by itself.

Required decision record fields:

- decision id
- timestamp
- actor
- treasury state
- asset
- timeframe
- market context
- regime
- data availability
- missing data
- stale data state
- hypothesis
- signal or observation
- expected risk
- estimated fee
- estimated spread
- estimated slippage
- break-even move required
- adverse scenario
- reasons not to act
- final decision
- risk decision
- execution mode
- later outcome
- post-mortem

Decision quality metrics:

- overtrading rate
- risk veto rate
- expected outcome vs realized outcome
- fee and slippage cost
- drawdown avoided
- stale-data decisions
- wrong-regime decisions
- decisions without a clear hypothesis
- decisions without a reason not to act
- post-mortem completion rate

The decision journal must record no-action decisions. For small capital, the
best action will often be no action.

## 2B. Mathematical Spine

Math is a product boundary, not a reporting decoration. With small capital,
fees, spread, slippage, minimum order size, and rounding can dominate the
result. Any strategy or decision that ignores these costs is not eligible for
promotion.

Core metrics:

- arithmetic returns
- log returns
- cumulative returns
- rolling returns
- realized volatility
- downside volatility
- max drawdown
- drawdown duration
- exposure
- turnover
- fee drag
- slippage drag
- expectancy
- win rate
- average win
- average loss
- profit factor
- payoff ratio
- Sharpe ratio with caution
- Sortino ratio with caution
- Calmar ratio
- benchmark-relative return
- risk-adjusted return after costs

Small-capital constraints:

- fee minimums
- spread
- slippage
- minimum order size
- position size rounding
- asset quantity precision
- quote currency precision
- break-even move required before a trade has any chance to matter
- cost as a percentage of position size
- turnover as a capital damage source

Every strategy report must show performance before costs and after costs. The
after-cost result is the promotion-relevant result.

`DOCS.REVIEW.2` records the initial numeric draft for simulated costs, maximum
weekly decision count, conservative strategy definition, and promotion
thresholds below.

## 2C. Strategy Specification and Backtest Integrity Spine

No strategy may be treated as real work until it has a written specification.

Strategy spec template:

- Strategy ID
- Hypothesis
- Market regime where it should work
- Market regime where it should not trade
- Asset universe
- Timeframe
- Inputs
- Signal formula
- Entry condition
- Exit condition
- Invalidation condition
- Position sizing
- Max holding period
- Fee and slippage assumptions
- Expected failure mode
- Benchmark
- Evaluation metrics
- Promotion criteria
- Deprecation criteria

Backtest integrity rules:

- no lookahead bias
- no survivorship bias
- no repainting indicators
- no same-candle entry when the signal uses the same close
- include costs and slippage
- explicitly handle missing data
- normalize timezone
- chronological train/test only
- no random split on time series
- separate hyperparameter tuning from final test
- mandatory benchmark
- results by regime, not only aggregate
- preserve negative results

Backtest output must include benchmark comparison, cost assumptions, drawdown,
drawdown duration, turnover, exposure, regime breakdown, and reasoned
promotion or rejection status.

Negative results are project assets. They prevent repeated mistakes and help
calibrate future decisions.

## 2D. DOCS.REVIEW.2 Numeric Draft Spine

This section is a conservative numeric draft for `MVP.1`, strategy promotion,
strategy rejection, and paper-mode risk policy. These numbers are placeholders
for local paper simulation. They are not exchange-specific truth, brokerage
configuration, live trading permission, or a promise that real orders will ever
be enabled.

### MVP.1 Exact Cut

`MVP.1 - Decision Journal and Paper Treasury` includes:

- 200 EUR paper treasury.
- BTC and ETH only.
- Paper-only ledger.
- Public/read-only market data ingestion boundary.
- Candle storage with source, timestamp, asset, timeframe, and feed health.
- Buy-and-hold benchmark.
- Scheduled accumulation benchmark.
- Decision records.
- No-action records.
- Risk veto records.
- Weekly report.
- Simple dashboard/reporting surface later.
- Owner and viewer capability boundaries later.

`MVP.1` excludes:

- ML.
- LLM.
- embeddings.
- RAG.
- Spark dependency.
- Tailscale dependency.
- live trading.
- exchange integration.
- real provider integration.
- wallet custody.
- credentials.
- model downloads.

Market data ingestion boundary:

- use public or local test data only
- no trading API keys
- no private exchange account access
- no account balance reads
- no order book dependency for MVP.1
- store enough source metadata to audit stale or missing data
- block decisions when data is stale beyond the draft freshness policy

Primary product outcome:

- improve decision quality and capital preservation before seeking returns
- keep benchmark comparison visible at all times
- preserve no-action decisions and negative results
- do not promote a strategy when a simple benchmark is better after costs

### Initial Decision Cadence

Default cadence:

- weekly owner review: 1 required review per week
- daily market check: optional, observation-only
- weekly report: 1 generated report per week

Decision limits:

- maximum decision records per week: 3
- maximum no-action records per week: unlimited
- maximum simulated trades per week: 2
- maximum simulated trades per asset per week: 1
- maximum same-day simulated trades: 1
- minimum cool-off after a veto or losing simulated trade: 24 hours

Forbidden cadence:

- no high-frequency behavior
- no scalping
- no reactionary same-day overtrading
- no strategy that requires continuous screen watching
- no repeated re-entry after a loss without a new decision record

### Initial Timeframe Policy

Allowed initial timeframes:

- 1d candles as the primary decision timeframe
- 4h candles as context only
- 1w candles as regime context

Out of scope for MVP.1:

- sub-hour candles
- tick data
- order book microstructure
- intraday scalping signals
- same-candle execution when signal uses that candle close

Stale data policy:

- 1d data is stale if the latest expected daily candle is more than 36 hours
  old.
- 4h context is stale if the latest expected 4h candle is more than 8 hours
  old.
- Weekly context is stale if the latest expected weekly candle is more than 10
  days old.
- Any decision using stale required data must be marked stale or vetoed.
- A strategy cannot be promoted if its backtest ignores missing or stale data.

### Cost Model Assumptions

All values are conservative paper placeholders. They must be revisited before
any exchange-specific modeling.

Fee assumptions:

- simulated entry fee: 0.40% of notional
- simulated exit fee: 0.40% of notional
- simulated minimum fee: 0.10 EUR per side

Spread assumptions:

- BTC spread placeholder: 0.20%
- ETH spread placeholder: 0.30%
- severe-liquidity spread placeholder: 0.75%

Slippage assumptions:

- normal simulated slippage: 0.10% per side
- volatile simulated slippage: 0.25% per side
- severe-liquidity simulated slippage: 0.50% per side

Rounding and precision assumptions:

- EUR ledger precision: 0.01 EUR
- BTC precision: 0.00000001 BTC
- ETH precision: 0.00000001 ETH
- position value reports round to cents
- rounding loss must be included in after-cost results

Minimum trade size assumptions:

- minimum simulated trade size: 20 EUR notional
- preferred simulated trade size for strategy tests: at least 25 EUR notional
- no simulated trade below 10% of the 200 EUR paper treasury

Break-even move required:

```text
break_even_move_required =
  entry_fee
  + exit_fee
  + spread
  + entry_slippage
  + exit_slippage
  + rounding_buffer
```

Draft normal break-even placeholders:

- BTC normal round trip: at least 1.30%
- ETH normal round trip: at least 1.40%
- severe-liquidity round trip: at least 2.50%

Any strategy whose expected move is below the relevant break-even placeholder
is not eligible for paper execution.

### Conservative Strategy Numeric Definition

A conservative MVP.1/MVP.2 strategy must satisfy these draft limits:

- maximum total crypto exposure: 60% of paper treasury
- maximum single-asset exposure: 40% of paper treasury
- maximum strategy exposure: 25% of paper treasury
- maximum single simulated trade size: 25% of paper treasury
- maximum weekly turnover: 50% of paper treasury
- maximum simulated trades per week: 2
- maximum strategy drawdown warning: 3% of paper treasury
- maximum strategy drawdown lock: 5% of paper treasury
- maximum weekly realized loss lock: 2.5% of paper treasury
- maximum unresolved stale-data decisions: 0

With a 200 EUR paper treasury, these imply:

- maximum total crypto exposure: 120 EUR
- maximum single-asset exposure: 80 EUR
- maximum strategy exposure: 50 EUR
- maximum single simulated trade size: 50 EUR
- maximum weekly turnover: 100 EUR
- strategy drawdown warning: 6 EUR
- strategy drawdown lock: 10 EUR
- weekly realized loss lock: 5 EUR

Forbidden strategy behavior:

- martingale
- leverage
- futures
- margin
- grid trading
- averaging down unless explicitly specified, capped, and tested
- increasing size after a loss without a new owner-reviewed decision record
- trading during stale required data

### Promotion Gates

Promotion to `backtest_ready` requires:

- strategy spec complete
- hypothesis clear
- regime where it should work defined
- regime where it should not trade defined
- benchmark defined
- cost assumptions defined
- stale-data behavior defined
- invalidation condition defined

Promotion to `backtested` requires:

- benchmark comparison complete
- no lookahead bias
- no survivorship bias
- no repainting indicators
- no same-candle execution flaw
- chronological train/test split
- separate tuning and final test
- costs, spread, slippage, and rounding included
- missing and stale data handled explicitly
- negative results preserved

Promotion to `paper_enabled` requires:

- after-cost result is positive relative to the selected benchmark
- candidate active strategy beats benchmark by at least 2 percentage points
  after costs, or reduces max drawdown by at least 20% while trailing benchmark
  return by no more than 1 percentage point
- max drawdown does not exceed the strategy drawdown lock
- drawdown duration is acceptable and explained
- average weekly turnover is at or below 50% of paper treasury
- trade count stays within cadence limits
- behavior works across more than one regime or is explicitly regime-scoped
- risk policy does not veto the strategy in normal expected conditions
- owner review is recorded

Promotion to `future_live_candidate` is not part of MVP.1, MVP.2, or MVP.3.
It can only be considered by a later reviewed wave.

### Rejection and Deprecation Gates

Reject or deprecate a strategy when any of these are true:

- fails after costs
- fails to beat the selected benchmark after costs
- excessive turnover
- excessive drawdown
- drawdown duration is unexplained or unacceptable
- only works in a cherry-picked period
- only works before costs
- depends on stale data
- depends on missing data being silently ignored
- has unclear hypothesis
- lacks completed post-mortems
- creates decisions without reasons not to act
- encourages overtrading
- violates cadence limits
- violates exposure limits
- violates loss locks
- cannot be explained from stored source data

### Paper-Mode Risk Policy Draft

Risk policy is a hard boundary in paper mode. It does not become permission for
live mode.

Always veto:

- live trading request
- withdrawal request
- wallet custody request
- exchange credential request
- missing required benchmark
- missing required cost model
- missing strategy spec
- stale required data
- total exposure above 60%
- single-asset exposure above 40%
- strategy exposure above 25%
- weekly turnover above 50%
- weekly simulated trades above 2
- strategy drawdown at or above 5%
- weekly realized loss at or above 2.5%
- emergency stop active

Reduce or delay:

- volatile regime without explicit volatility handling
- 4h context stale but 1d decision data still fresh
- weekly report not yet reviewed
- recent veto within the last 24 hours
- severe news context without completed owner review

Record as risk event:

- every veto
- every reduction
- every delay
- every stale-data block
- every exposure block
- every cost-model block
- every emergency block

### Minimum Paper Duration Before Manual Live Consideration

Manual live remains locked. Passing paper gates does not automatically enable
live trading.

Minimum future review candidate:

- at least 90 calendar days of paper operation
- at least 12 completed weekly reports
- at least 30 decision or no-action records
- at least 1 full strategy post-mortem
- no unresolved data integrity issue
- no unresolved risk policy violation
- benchmark comparison complete after costs
- owner review complete
- new legal, safety, and operational review wave approved

Even if all evidence is positive, a later wave must still explicitly decide
whether manual live is worth considering. Auto-live remains out of scope.

## 3. Non-Negotiable Safety Boundary

drmlke must be built paper first. Paper first means simulated treasury state,
simulated orders, simulated fills, and reviewable research before any real money
path exists. The initial runtime must assume that live trading is disabled.

Hard rules:

- Paper trading comes before any live or shadow trading work.
- Live trading is disabled by default.
- No leverage.
- No futures.
- No margin.
- No withdrawals.
- No private keys in the repository.
- No seed phrases in the repository.
- No exchange API keys in the repository.
- No exchange API keys in the client.
- No AI model can execute orders.
- No AI model can override risk.
- Backend permissions are mandatory for every critical action.
- UI locks are helpful communication, not security.
- All future live actions require explicit gates.
- Family viewer accounts cannot trade.
- Family viewer accounts cannot configure strategies.
- Family viewer accounts cannot manage runtime state.
- Family viewer accounts cannot approve actions.
- Emergency stop must always be auditable.

The risk engine is a boundary, not a suggestion engine. A strategy, model, or
manual action can propose a candidate action, but the risk engine may reduce,
delay, or veto that action. Nothing below the risk layer may bypass it.

Every future operation that mutates treasury state, runtime state, user access,
strategy configuration, risk policy, or exchange connection state must be
enforced server-side. A modified client must never be enough to perform a
forbidden action.

The first real capital ceiling is 200 EUR. That ceiling is not permission to
trade aggressively. Small capital makes fees, spread, and overtrading more
dangerous. Capital preservation is more important than excitement.

## 4. Machine and Network Topology

drmlke has three planned machine roles.

### Linux Workstation

Role:

- primary development machine
- Codex work
- local provider and API tests
- Docker development tests
- repository authoring
- terminal and VS Code work

Known:

- Arch Linux target for initial local runtime.
- amd64 architecture.
- Studio workstation used for active development.
- This machine currently represents the primary repo authoring path.

The Linux workstation is allowed to run local development services and
validation. It is not the permanent runtime storage target.

### MacBook

Role:

- secondary active development machine
- home and evening work
- clone, pull, and push the GitHub repo
- VS Code editing
- future iOS packaging path
- Tailscale available for later private network verification
- setup completed before Spark runtime deployment

The MacBook is now a clean secondary development environment. The active repo is
`/Users/mothx/Developer/drmlke`, `origin/main` is synced, Node 24 is active,
`uv` and `pnpm` work, Docker is available through OrbStack, and the provider
stub validates locally. This closeout does not configure Spark and does not
deploy runtime services to Spark.

### Spark

Role:

- runtime, storage, and provider node
- Ubuntu 24.04 aarch64
- NVIDIA DGX Spark
- Ethernet 24H
- accessed later through Tailscale or an explicit SSH path
- not the primary development machine
- persistent root: `/srv/drmlke`

Important correction:

Spark access must not rely only on fragile LAN hostname resolution. The
preferred future path is Tailscale-based private access once the MacBook
workflow is prepared. Spark remains a private runtime node, not a public server.

## 5. Repository Spine

GitHub is the current source remote. The Linux workstation remains a primary
authoring path. The MacBook is also an active development node at
`/Users/mothx/Developer/drmlke`. Spark will later receive a deploy copy under
`/srv/drmlke/app`; Spark does not become the primary authoring repo.

Expected tree and responsibilities:

### `apps/api`

Purpose: backend API service for client, admin console, identity, runtime,
treasury, strategy, risk, reporting, and audit surfaces.

What belongs there:

- FastAPI app entrypoint.
- Route modules when backend API surfaces are implemented.
- Request and response schemas that are API specific.
- Server-side permission checks.
- Runtime-facing command endpoints.

What does not belong there yet:

- Exchange secrets.
- Trading execution logic.
- Wallet custody.
- Client UI code.
- Long-running worker jobs.

### `apps/worker`

Purpose: background runtime process for scheduled work, event processing,
market data collection, feature generation, strategy evaluation, paper
execution, reporting, and maintenance jobs.

What belongs there:

- Worker entrypoint.
- Job runners.
- Event consumers.
- Scheduled tasks.
- Runtime heartbeats.

What does not belong there yet:

- Direct UI code.
- Secrets committed to source.
- Live execution.
- Model downloads during bootstrap.

### `apps/provider`

Purpose: local provider service boundary. During bootstrap it is a stub. Later
it may expose local model, embedding, sentiment, or compute capabilities through
a narrow contract.

What belongs there:

- Provider health endpoint.
- Provider capability endpoint.
- Model registry reads after models are intentionally installed.
- Local inference boundary only after a later wave approves it.

What does not belong there yet:

- Real AI model downloads.
- Exchange connections.
- Order execution.
- Wallet custody.
- Business logic that belongs in API or worker.

### `apps/client`

Purpose: future shared product client for mobile packaging and possibly web
preview.

What belongs there later:

- Shared UI shell.
- Capability-aware screens.
- Client-side API calls.
- Mobile packaging integration after framework choice.

What does not belong there yet:

- A scaffold before the Node 24 and client framework decisions are ready.
- Exchange API keys.
- Wallet private keys.
- Permission enforcement that is treated as security.

### `packages/core`

Purpose: shared core settings, constants, path helpers, common types, and
cross-service contracts.

What belongs there:

- Pydantic settings.
- Shared enums.
- Capability names.
- Event names.
- Common schema primitives.
- Identity, capability, safety, paper treasury, append-only ledger, treasury
  projection, paper position, and paper portfolio snapshot contracts while they
  remain pure domain logic.

What does not belong there yet:

- Service-specific route implementations.
- Heavy runtime jobs.
- Persistence adapters.
- Paper execution.
- Position valuation.
- Portfolio valuation.
- Market data ingestion.
- Secrets.

### `packages/storage`

Purpose: storage access layer for SQLite operational state, DuckDB and Parquet
analytical data, backups, and future migrations.

What belongs there later:

- Database connection helpers.
- Migration helpers.
- Repository classes.
- Backup and restore primitives.

What does not belong there yet:

- Trading decisions.
- UI code.
- Secrets.

### `packages/wallet`

Purpose: paper treasury ledger and future read-only wallet or exchange account
tracking boundaries.

What belongs there:

- Paper treasury types.
- Ledger entry types.
- Position accounting.
- Read-only future tracking adapters after review.

What does not belong there:

- Seed phrase generation.
- Private key custody.
- On-chain signing.
- Withdrawal support.
- Exchange private key storage.

### `packages/agents`

Purpose: agent orchestration helpers for future research, reporting,
summarization, and controlled operator assistance.

What belongs there later:

- Agent task contracts.
- Report generation helpers.
- Retrieval and explanation workflows.
- Strictly non-executing advisory agents.

What does not belong there:

- Autonomous order execution.
- Risk override behavior.
- Secret management.

### `packages/risk`

Purpose: risk policy, veto logic, exposure checks, drawdown locks, stale data
checks, and emergency state rules.

What belongs there:

- Deterministic risk policy.
- Sizing constraints.
- Veto reasons.
- Drawdown and exposure checks.
- Audit-friendly risk decisions.

What does not belong there:

- UI rendering.
- Exchange adapters.
- Non-deterministic model behavior that can override policy.

### `infra/docker`

Purpose: Dockerfiles and container build assets.

What belongs there:

- Base image.
- Service Dockerfiles.
- Build-time dependency wiring.

What does not belong there:

- Runtime data.
- Secrets.
- Machine-specific environment files.

### `deploy/spark`

Purpose: Spark-specific deployment documentation and later deployment helpers.

What belongs there later:

- Spark preparation scripts after explicit wave approval.
- Systemd or Compose deployment notes.
- Storage layout docs.
- Operational checklists.

What does not belong there yet:

- A live deploy script that runs without review.
- Secrets.
- Private keys.

### `scripts`

Purpose: local developer and operator helper scripts.

What belongs there:

- Doctor checks.
- Validation helpers.
- Future backup and migration helpers.
- Future deployment preflight checks.

What does not belong there:

- Destructive maintenance commands without explicit safeguards.
- Secret material.

### `docs`

Purpose: canonical planning, architecture, environment, deployment, and review
records.

What belongs there:

- Master spine.
- Architecture notes.
- Environment setup.
- Deployment plans.
- Future runbooks.

What does not belong there:

- Credentials.
- Seed phrases.
- Private keys.
- Undecided details written as if they were final decisions.

## 6. Development Environment Spine

### Linux

The Linux workstation is the current primary development target.

Expected tools:

- Python 3.12.
- `uv`.
- Node 24.
- `corepack`.
- `pnpm`.
- Docker.
- Docker Compose v2.
- Docker buildx.
- Makefile.
- git.
- openssh.
- vim.
- curl.
- VS Code if desired.

Expected validation:

```sh
git status --short --branch
uv sync --dev
make doctor
make check
docker compose ps
docker compose --profile provider up -d provider
curl -sS http://127.0.0.1:8781/health
curl -sS http://127.0.0.1:8781/models
```

Current status:

- Python 3.12 is the pinned Python version.
- Node 24 alignment is resolved.
- Canonical repo path is `/home/mothx/computer-science/projects/drmlke`.
- The provider stub validates locally on port `8781`.
- Provider health returns `status=ok`, `provider=stub`, and
  `live_trading_enabled=false`.
- Provider models returns an empty list.
- The Linux workstation is the canonical authoring machine.
- MacBook remains a secondary active development node.
- Spark remains untouched.

### MacBook

`MAC.SETUP.1-CLOSE` has verified the MacBook as an active development node.

Verified state:

- Repo path: `/Users/mothx/Developer/drmlke`.
- Remote: `https://github.com/francescomaiomascio/drmlke`.
- Branch: `main`.
- GitHub sync: `82f8fae DOCS.SPINE.3` pushed to `origin/main`.
- Host: macOS arm64.
- Shell: `/bin/zsh`.
- Node: `v24.16.0`.
- Corepack: `0.35.0`.
- pnpm: `10.12.1`.
- uv: `0.11.17`.
- Project Python: Python 3.12 through `uv`.
- System `python3`: may be newer and is not the project interpreter.
- Docker runtime: OrbStack Docker context.
- VS Code CLI: available.
- `make doctor`: passes.
- `make check`: passes.
- Provider container: validates locally on port `8781`.
- Provider health: `status=ok`, `provider=stub`,
  `live_trading_enabled=false`.
- Provider models: empty list.
- Spark: intentionally untouched.

Useful MacBook commands:

```sh
cd /Users/mothx/Developer/drmlke
git status --short --branch
uv sync --dev
node -v
pnpm -v
make doctor
make check
make docker-base
docker compose --profile provider up -d provider
curl -sS http://127.0.0.1:8781/health
curl -sS http://127.0.0.1:8781/models
```

### Spark

This is plan only. Do not attach Spark or deploy runtime in `DOCS.SPINE.3`.

Future checks:

- Verify SSH over the selected private path.
- Verify Tailscale reachability.
- Verify Docker.
- Verify Docker Compose.
- Verify NVIDIA runtime visibility if model or GPU work is later approved.
- Prepare `/srv/drmlke`.
- Deploy the provider only after `TAILSCALE.SPARK.1`.

Spark must not receive secrets through the repository. Runtime data, env files,
models, logs, and backups live outside source control.

## 7. MacBook Setup Spine

### Purpose

The MacBook must become a clean alternate development machine so work can
continue from home without relying on the Linux workstation terminal.

### Target State

- Repository cloned.
- Current branch visible.
- GitHub remote working.
- Node 24 active.
- `uv` working.
- Python 3.12 working.
- `pnpm` working.
- `make doctor` passes or clearly documents missing Docker.
- `make check` passes.
- Provider can run locally if Docker is available.
- VS Code can open the repo.
- The roadmap can be edited from MacBook.

### Non-Goals

- No Spark deployment.
- No Tailscale production routing changes.
- No client implementation.
- No trading logic.
- No model downloads.
- No wallet custody.
- No exchange connections.

### Future Wave Name

`MAC.SETUP.1-CLOSE - finalize MacBook development node`

## 8. Tailscale and Spark Access Spine

### Purpose

Use Tailscale as the preferred private network path between MacBook,
workstation, and Spark, instead of relying only on fragile local hostname
resolution.

### Target Future Behavior

- MacBook can reach Spark through Tailscale.
- Linux workstation may also use Tailscale if configured later.
- Spark provider and API remain private.
- No public internet exposure.
- drmlke mobile and admin clients connect through LAN, VPN, or Tailscale later.
- Spark access uses an explicit, documented address or SSH alias.

### Non-Goals Now

- Do not configure Tailscale in this docs wave.
- Do not expose the provider publicly.
- Do not create Cloudflare tunnels.
- Do not open router ports.
- Do not deploy drmlke runtime.

### Future Wave Name

`TAILSCALE.SPARK.1 - verify Spark private network access path`

## 9. Spark Runtime and Storage Spine

Spark is a future runtime and storage target. It is not the current authoring
machine.

Target root:

```text
/srv/drmlke
```

Target tree:

```text
/srv/drmlke/env
/srv/drmlke/app
/srv/drmlke/state
/srv/drmlke/lake/parquet
/srv/drmlke/lake/duckdb
/srv/drmlke/vector/lancedb
/srv/drmlke/models/embeddings
/srv/drmlke/models/llm
/srv/drmlke/models/timeseries
/srv/drmlke/logs/api
/srv/drmlke/logs/worker
/srv/drmlke/logs/provider
/srv/drmlke/backups/daily
/srv/drmlke/backups/weekly
/srv/drmlke/runtime/sockets
/srv/drmlke/runtime/pids
```

Rules:

- Runtime data lives outside the repository.
- Environment files live outside the repository.
- Secrets are never committed.
- Environment files are backed up before overwrite.
- Source deploy copy goes to `/srv/drmlke/app`.
- Spark is a deploy target, not the authoring source.
- Provider and API must remain private to LAN, VPN, or Tailscale.
- Live trading remains disabled on Spark until a future live gate wave.
- Withdrawals remain disabled on Spark.

Future wave:

`SPARK.RUNTIME.1 - prepare Spark storage and deploy provider`

## 10. Container and Runtime Spine

Docker Compose is the initial orchestrator.

drmlke will not use these in the early runtime:

- Kubernetes.
- Docker Swarm.
- Cloud-managed orchestration.
- Public cloud dependency.

Current services:

- `provider`: FastAPI provider stub.
- `api`: FastAPI API placeholder.
- `worker`: background worker placeholder.

Future services:

- `client`: local preview or packaged web surface later.
- `db-tools`: migration, backup, restore, and analytical maintenance helpers.

Expected Compose profiles:

- `provider`: run the provider service only.
- `dev`: run API and worker for local development.
- `spark`: run the private Spark runtime profile later.
- `full`: run the full local stack when it exists.

Ports:

- `8780`: API.
- `8781`: provider.
- `8782`: client preview later.
- `8783`: worker metrics later.

Current runtime truth:

- The local provider is a stub.
- API and worker are placeholders.
- No market data flows.
- No execution flows.
- No models are loaded.

Future runtime direction:

- Define a provider contract.
- Add API runtime surfaces with server-side permission enforcement.
- Add a worker and event bus.
- Keep containers portable between LAN nodes by using environment variables and
  a configurable storage root.
- Bind ports cautiously on Spark so services remain private.

## 11. Account, Role, and Capability Spine

Correct account model:

- One treasury.
- One owner and operator.
- Padre and Zio are viewer family accounts.
- Same app for everyone.
- Capability-driven UI.
- Server-side enforcement.
- Disabled UI is not security.

### Roles

#### `owner_operator`

Primary user: Francesco.

Allowed actions:

- View all treasury, position, runtime, risk, audit, provider, and strategy
  data.
- Configure runtime behavior.
- Manage strategies.
- Manage risk policy.
- Pause runtime.
- Resume runtime when gates allow.
- Trigger emergency stop.
- Manage users.
- Manage devices.
- Manage exchange connections only in future reviewed waves.
- Approve future paper actions where approval is required.
- Approve future live actions only after live gates exist.

Forbidden actions:

- Bypass risk.
- Enable live trading before the live gate exists.
- Store secrets in the repository.
- Enable withdrawals during early development.

UI behavior:

- Owner sees all product sections.
- Mutating controls are enabled only when the backend capability and runtime
  gate allow them.
- Locked controls explain the lock reason.

API enforcement:

- Every owner action is checked server-side.
- Denied owner actions produce safe responses and audit records.

#### `viewer_family`

Initial users: Padre and Zio.

Allowed actions:

- View permitted treasury state.
- View positions.
- View PnL if allowed.
- View runtime status.
- View news.
- View alerts.
- View explanatory summaries.

Forbidden actions:

- Trade.
- Approve trades.
- Configure strategies.
- Change risk policy.
- Pause or resume runtime unless a future emergency permission explicitly grants
  a narrow action.
- Manage exchange connections.
- Add secrets.
- Manage users.
- Manage devices.
- View sensitive logs.

UI behavior:

- Viewer sees the same app and same general navigation.
- Mutating actions are hidden, disabled, or replaced with a clear lock reason.
- Viewer can understand status without seeing sensitive controls.

API enforcement:

- Viewer requests for forbidden actions are denied server-side.
- Permission denial may be audited.

#### `emergency_only`

Future optional role.

Allowed actions:

- View critical status.
- Trigger emergency stop if explicitly granted.

Forbidden actions:

- Resume runtime.
- Change configuration.
- Approve trades.
- Manage strategies.
- Manage risk.

UI behavior:

- This role sees a minimal emergency surface.
- The emergency action requires clear confirmation and produces an audit record.

API enforcement:

- Emergency action is checked by capability and runtime state.
- Resume remains owner-only.

#### `admin_technical`

Future optional role.

Allowed actions:

- Perform technical maintenance if explicitly granted.
- View system health if allowed.
- Assist with deployment and logs if allowed.

Forbidden actions:

- Trading authority by default.
- Strategy authority by default.
- Risk policy authority by default.
- Exchange connection authority by default.

UI behavior:

- Technical surfaces appear only if capability grants them.
- Trading and treasury controls remain locked unless separately granted.

API enforcement:

- Technical authority and trading authority are separate capabilities.

### Capabilities

Initial capability names:

- `view_treasury`
- `view_positions`
- `view_pnl`
- `view_runtime_status`
- `view_signals`
- `view_news`
- `view_alerts`
- `view_audit_summary`
- `manage_runtime`
- `pause_runtime`
- `resume_runtime`
- `emergency_stop`
- `manage_strategies`
- `manage_risk_policy`
- `approve_paper_action`
- `approve_future_live_action`
- `manage_devices`
- `manage_users`
- `manage_exchange_connections`
- `view_sensitive_logs`

Capability assignment:

- Francesco starts with owner and operator capabilities, while future live
  actions remain globally locked until live gates exist.
- Padre starts with family viewer capabilities.
- Zio starts with family viewer capabilities.
- Live trading capabilities are globally disabled.

`P0.H` implementation (legacy alias: `CORE.0`):

- `drmlke_core.identity.Role` defines the initial roles.
- `drmlke_core.identity.Capability` defines the initial capability names.
- `drmlke_core.identity.capabilities_for_role` applies deterministic role
  defaults.
- `approve_future_live_action` and `manage_exchange_connections` are globally
  locked.
- Initial profile contracts exist for Francesco, Padre, and Zio.
- This is a typed domain contract only, not authentication, login, session
  storage, or API enforcement.

## 12. Treasury and Capital Spine

Correct capital model:

- Future real capital ceiling: 200 EUR.
- Current live capital: 0 EUR.
- Current implementation: paper only.
- Paper treasury: one simulated 200 EUR treasury.
- No per-person budget split.

`P0.H` implementation (legacy alias: `CORE.0`):

- `drmlke_core.treasury.PaperTreasuryBoundary` defines the one-paper-treasury
  boundary.
- Initial paper capital is 200 EUR.
- Live capital is 0 EUR.
- Per-person portfolios are forbidden.
- Family viewer roles can view allowed treasury state but cannot manage it.
- Padre and Zio are viewers, not independent portfolio managers.

`P0.I` implementation (legacy alias: `CORE.1`):

- `drmlke_core.ledger.LedgerEntry` defines typed paper ledger entries.
- `drmlke_core.ledger.PaperLedger` defines an immutable in-memory ledger
  contract for the single paper treasury.
- `create_initial_paper_ledger` creates exactly one 200 EUR initial capital
  entry.
- `append_paper_ledger_entry` returns a new ledger object instead of mutating
  existing entries.
- `project_paper_cash_balance_eur` computes paper cash from ledger entries.
- Corrections are represented as new compensating entries, not edits.
- Persistence, database schema, API enforcement, paper orders, fills, positions,
  PnL accounting, market data, and trading logic remain later work.
- Padre and Zio remain viewers, not independent portfolio managers.

`P0.J` implementation (legacy alias: `CORE.2`):

- `drmlke_core.treasury_projection.PaperTreasurySnapshot` defines a frozen
  read-side view over the paper ledger.
- `project_paper_treasury_snapshot` derives available cash, reserved cash,
  total cash, fees, adjustments, corrections, entry count, and last sequence
  from append-only ledger entries.
- `validate_paper_treasury_snapshot` enforces paper mode, canonical treasury id,
  200 EUR initial capital, 0 EUR live capital, nonnegative cash, nonnegative
  reserved cash, nonnegative fees, and reconciliation.
- `is_paper_treasury_snapshot_reconciled` provides deterministic reconciliation
  for tests and future read surfaces.
- The snapshot is in-memory domain logic only and does not introduce storage,
  API routes, paper orders, fills, positions, market valuation, strategy logic,
  live trading, or provider/runtime changes.

`P0.K` implementation (legacy alias: `CORE.3`):

- `drmlke_core.position.PaperPosition` defines a frozen paper-only position
  contract.
- `drmlke_core.position.PaperPositionBook` groups paper positions for the
  canonical paper treasury without persistence or mutation.
- `AssetSymbol` and `normalize_asset_symbol` provide strict local symbol
  normalization.
- `INITIAL_PAPER_POSITION_ASSETS` limits the initial paper position boundary to
  BTC and ETH.
- `PaperPositionSide` is long-only. There is no shorting, margin, leverage, or
  live-backed state.
- `create_open_paper_position` constructs an open simulated position with cost
  basis equal to quantity times average entry price plus fees.
- `total_open_cost_basis_eur` and `total_position_fees_eur` provide pure
  position-book summaries only.
- The position boundary does not read market data, mark positions to market,
  calculate PnL, create orders, create fills, mutate the ledger, reserve cash,
  release cash, persist state, expose API routes, or change provider/runtime
  behavior.

`P0.L` implementation (legacy alias: `CORE.4`):

- `drmlke_core.portfolio.PaperPortfolioSnapshot` defines a frozen structural
  paper portfolio read model.
- `project_paper_portfolio_snapshot` combines a `P0.J` treasury cash snapshot
  with a `P0.K` paper position book.
- The snapshot reports available cash, reserved cash, total cash, open position
  count, closed position count, total position count, open cost basis, position
  fees, total structural exposure, and open cost basis ratio.
- Total structural exposure is cash plus open position cost basis. This is not
  market value.
- Open cost basis ratio is open cost basis divided by initial paper capital.
- `P0.L` does not subtract position cost from cash. Future paper execution must
  create ledger entries before treasury cash changes.
- The portfolio snapshot does not read prices, mark to market, calculate PnL,
  calculate returns, create orders, create fills, mutate the ledger, persist
  state, expose API routes, or change provider/runtime behavior.

`P0.M` implementation (legacy alias: `CORE.5`):

- `drmlke_core.decision.DecisionRecord` defines a frozen paper decision record
  contract for no-action, watch, action candidate, rejected, postponed, and
  risk-vetoed decisions.
- `DecisionContext` records the paper treasury id, optional paper portfolio
  snapshot, optional BTC/ETH asset, timeframe, data freshness, risk state, cost
  assumptions, and reference metadata.
- `DecisionCostAssumption` records estimated fees, spread, slippage, rounding
  buffer, and break-even move using `Decimal`.
- Decision creation remains owner/operator-only at the domain boundary.
- Reasons not to act are mandatory.
- Action candidates require fresh data, reasons to act, reasons not to act,
  paper-review risk allowance, and cost assumptions.
- Completed outcome states require a post-mortem, keeping decision process
  quality separate from economic result.
- The decision boundary does not ingest market data, compute strategy signals,
  create orders or fills, execute actions, persist state, expose API routes, or
  change provider/runtime behavior.

Contribution metadata may exist later, but it is accounting metadata. It is not
trading authority and does not create independent family portfolios.

Useful treasury splits:

- cash
- positions
- realized PnL
- unrealized PnL
- fees
- slippage
- strategy attribution
- risk exposure
- audit events

The 200 EUR ceiling is a constraint, not an invitation to trade aggressively.
Small capital makes fees, spread, and overtrading more dangerous. Any strategy
that depends on frequent trading must show realistic fee and spread assumptions
before it can even become paper-enabled.

The ledger should eventually answer:

- What cash does the paper treasury hold?
- Which positions are open?
- What is the realized result?
- What is the unrealized result?
- What fees and slippage were simulated?
- Which strategy caused each candidate action?
- Which risk decision allowed, reduced, delayed, or vetoed it?
- Which user or runtime job caused each mutation?
- What audit record proves the sequence?

## 13. Wallet Boundary Spine

drmlke is initially a ledger and paper treasury. It is not initially a
custodial wallet.

Hard wallet boundaries:

- No seed phrase generation.
- No private key custody.
- No withdrawals.
- No on-chain signing.
- No exchange private key in the client.
- No wallet seed in the client.
- No wallet secret in the repository.

Future possibilities, only after review:

- Read-only exchange adapter.
- Shadow exchange mode.
- Future trading adapter behind explicit gates.
- On-chain read-only tracking.
- WalletConnect or on-chain interaction as a future optional surface.

The wallet package may contain paper treasury and ledger code. It must not
contain custody behavior during early development.

## 14. Interface and Product Surface Spine

drmlke has one product interface with capability-aware behavior. The owner and
viewers use the same product. The backend decides what data and actions are
available.

### Mobile Client

Purpose:

- Daily monitoring.
- Viewer family access.
- Owner emergency control.
- Future owner approval flows.

Same app for all roles.

#### Login

- Purpose: authenticate the user and establish a session.
- Visible to owner: yes.
- Visible to viewer: yes.
- Owner actions: sign in, manage trusted device later.
- Viewer locked actions: device management unless granted.
- Key data shown: app name, connection target, session status, safe error
  messages.

#### Home

- Purpose: show the day status at a glance.
- Visible to owner: yes.
- Visible to viewer: yes.
- Owner actions: inspect runtime, pause if allowed, open emergency.
- Viewer locked actions: pause, resume, configure, approve.
- Key data shown: current mode, treasury value, today PnL, open positions, risk
  state, runtime state, latest important alert.

#### Treasury

- Purpose: show cash, positions, and ledger state for the one treasury.
- Visible to owner: yes.
- Visible to viewer: yes if `view_treasury` is granted.
- Owner actions: inspect ledger details and future approved manual paper
  actions.
- Viewer locked actions: mutate treasury, approve orders, change settings.
- Key data shown: paper balance, cash, positions, realized PnL, unrealized PnL,
  fees, slippage, strategy attribution, recent ledger entries.

#### Positions

- Purpose: show open and historical asset exposure.
- Visible to owner: yes.
- Visible to viewer: yes if `view_positions` is granted.
- Owner actions: inspect attribution and risk details.
- Viewer locked actions: close, rebalance, or modify exposure.
- Key data shown: asset, quantity, average simulated price, current mark, PnL,
  exposure share, source strategy.

#### PnL

- Purpose: explain performance without hiding fees and slippage.
- Visible to owner: yes.
- Visible to viewer: yes if `view_pnl` is granted.
- Owner actions: inspect periods, strategy attribution, and report details.
- Viewer locked actions: change evaluation settings.
- Key data shown: daily PnL, realized PnL, unrealized PnL, drawdown, fees,
  slippage, benchmark comparison.

#### Signals

- Purpose: show strategy candidate signals and their review status.
- Visible to owner: yes.
- Visible to viewer: yes if `view_signals` is granted.
- Owner actions: inspect signal details and future approve paper action if
  enabled.
- Viewer locked actions: approve, reject, tune, or create signals.
- Key data shown: asset, strategy, direction, confidence, model score, risk
  status, created time.

#### News

- Purpose: show market news relevant to treasury risk.
- Visible to owner: yes.
- Visible to viewer: yes if `view_news` is granted.
- Owner actions: inspect source, severity, related assets, and retrieval memory.
- Viewer locked actions: tune news model or source policy.
- Key data shown: headline, source, time, severity, affected assets, summary,
  risk relevance.

#### Runtime

- Purpose: show whether the system is running, paused, stopped, or locked.
- Visible to owner: yes.
- Visible to viewer: yes if `view_runtime_status` is granted.
- Owner actions: pause, resume, inspect jobs, inspect provider, future restart
  flows.
- Viewer locked actions: pause, resume, restart, configure.
- Key data shown: mode, runtime state, last heartbeat, jobs, service health,
  current locks.

#### Risk

- Purpose: show risk policy and current risk state.
- Visible to owner: yes.
- Visible to viewer: limited view if allowed.
- Owner actions: inspect policy and manage policy in future.
- Viewer locked actions: change limits, unlock drawdown, override veto.
- Key data shown: exposure, drawdown, vetoes, stale data state, liquidity state,
  news severity locks.

#### Alerts

- Purpose: show important system, market, risk, and permission events.
- Visible to owner: yes.
- Visible to viewer: yes if `view_alerts` is granted.
- Owner actions: acknowledge alerts, inspect audit details.
- Viewer locked actions: change alert rules.
- Key data shown: severity, time, source, affected entity, action required,
  acknowledgement state.

#### Settings

- Purpose: account, device, notification, and owner configuration.
- Visible to owner: yes.
- Visible to viewer: yes in limited form.
- Owner actions: manage users, devices, notifications, and future connections.
- Viewer locked actions: role changes, device trust changes beyond self, runtime
  configuration, exchange configuration.
- Key data shown: account, role, capabilities, device state, notification
  preferences.

#### Emergency

- Purpose: provide a clear, auditable stop path.
- Visible to owner: yes.
- Visible to viewer: only if `emergency_stop` is granted.
- Owner actions: trigger emergency stop and inspect stop state.
- Viewer locked actions: resume, clear lock, change policy.
- Key data shown: current runtime state, last stop event, confirmation text,
  audit summary.

### Web Admin Console

Purpose:

- Richer owner browser console.
- LAN, VPN, or Tailscale only.
- Not public.
- Designed for repeated operational use, not marketing.

Sections:

- Dashboard.
- Runtime.
- Provider.
- Storage.
- Treasury.
- Strategies.
- Signals.
- Paper Trading.
- Risk.
- News and retrieval memory.
- Reports.
- Audit.
- Users and Devices.
- Settings.

Layout:

- Dark-first console.
- Dense information layout.
- Left rail for primary navigation.
- Top status bar for mode, runtime, provider health, risk state, and emergency
  status.
- Main workspace for the selected section.
- Right inspector for selected entity details.
- Event timeline or log strip for recent important events.

The web admin console is for owner operation and deeper inspection. It does not
replace backend enforcement.

### Terminal and Makefile

Purpose:

- Diagnostics.
- Deployment.
- Tests.
- Backup and restore later.
- Migrations later.
- Spark operations later.

Make targets should remain safe, explicit, and reviewable. Destructive or
stateful targets must explain what they affect and must not hide secret
movement.

### VS Code

Purpose:

- Code editing.
- Documentation editing.
- Roadmap editing.
- Tests.
- Codex review.
- Git workflow.

The roadmap is expected to be open during major implementation waves.

### Future Desktop Console

Purpose:

- Richer owner desktop app.
- Strategy lab.
- Backtest lab.
- Model registry.
- Audit timeline.
- Data lake browser.

Technology preference:

- Tauri and Rust shell.
- TypeScript UI.
- Talks to Spark API.
- No local secrets.
- No local exchange keys.
- No local wallet private keys.

Do not implement desktop now.

## 15. Trading Strategy Spine

All strategies start as research or paper-only behavior. A strategy creates a
candidate signal. It does not directly execute real orders.

Initial paper universe:

- BTC/EUR or BTC/USDT, pending exchange and data source decisions.
- ETH/EUR or ETH/USDT, pending exchange and data source decisions.
- Later high-liquidity large caps only after review.

### 1. Buy and Hold Benchmark

- Purpose: measure whether any active strategy is better than doing nothing.
- Inputs: start date, asset, initial simulated allocation, mark prices, fees if
  a simulated buy is modeled.
- Behavior: simulate buying once and holding through the evaluation period.
- Outputs: benchmark equity curve, PnL, drawdown, volatility, comparison
  metrics.
- Risk interaction: not a trading strategy; used to judge whether active logic
  earns its complexity.
- Non-goals: no timing, no prediction, no frequent trading.
- Acceptance before promotion: benchmark is reproducible, fee assumptions are
  explicit, and comparison reports can reference it.

### 2. Scheduled Accumulation Benchmark

- Purpose: compare complex timing against a simple periodic accumulation plan.
- Inputs: schedule, amount, asset, price history, fees, slippage assumption.
- Behavior: simulate recurring buys on a fixed schedule.
- Outputs: equity curve, average cost, PnL, drawdown, fee load.
- Risk interaction: risk engine may cap paper exposure and flag over-allocation.
- Non-goals: no prediction, no short-term timing, no leverage.
- Acceptance before promotion: schedule is deterministic, cost model is
  explicit, and benchmark is easy to reproduce.

### 3. Trend Following

- Purpose: participate only when trend and market conditions support long-only
  exposure.
- Inputs: moving average slope, multi-timeframe alignment, realized volatility,
  volume, liquidity, regime label, stale data state.
- Behavior: emit long-only candidate signals when trend is aligned and market
  state is acceptable.
- Outputs: candidate signal with direction, confidence, invalidation condition,
  expected holding window, and evidence.
- Risk interaction: risk can reduce size, delay entry, or veto for exposure,
  volatility shock, stale data, liquidity, or news severity.
- Non-goals: no shorting, no futures, no margin, no high-frequency entries.
- Acceptance before promotion: improves risk-adjusted paper performance after
  fees and slippage across multiple regimes and does not depend on overtrading.

### 4. Mean Reversion

- Purpose: test whether temporary dislocations can be paper-traded without
  fighting strong adverse regimes.
- Inputs: RSI, Bollinger distance, rolling z-score, volatility state, trend
  filter, liquidity, regime label.
- Behavior: emit long-only candidate signals when price appears stretched and
  the regime does not indicate panic or persistent breakdown.
- Outputs: candidate signal with entry reason, invalidation threshold, maximum
  holding window, and expected reversion zone.
- Risk interaction: risk vetoes stale data, panic regimes, poor liquidity,
  excessive exposure, or drawdown lock.
- Non-goals: no falling-knife averaging, no martingale, no leverage.
- Acceptance before promotion: drawdowns are controlled, invalidation is
  explicit, and paper results beat a simple benchmark after costs.

### 5. Volatility Breakout

- Purpose: test whether volatility compression followed by expansion can create
  controlled paper opportunities.
- Inputs: ATR, realized volatility, volatility compression, volume z-score,
  breakout level, liquidity, regime state.
- Behavior: emit candidate signals only after clear breakout confirmation and
  strict invalidation.
- Outputs: breakout signal, trigger level, invalidation level, expected holding
  horizon, evidence bundle.
- Risk interaction: risk limits size, blocks illiquid breakouts, blocks severe
  news, and blocks excessive volatility shocks.
- Non-goals: no chasing thin assets, no leverage, no scalping.
- Acceptance before promotion: false breakout cost is understood, slippage is
  modeled, and the strategy remains robust across volatility regimes.

### 6. News Risk Avoidance

- Purpose: block or reduce risk when severe news increases uncertainty.
- Inputs: news items, source credibility, sentiment, severity, affected assets,
  entity extraction, similar historical events from retrieval memory.
- Behavior: create risk context and possible veto conditions. News does not
  create buy orders by itself.
- Outputs: severity labels, affected assets, risk annotations, suggested lock or
  caution state.
- Risk interaction: risk uses news severity to veto, reduce, or delay candidate
  actions.
- Non-goals: no autonomous trading from headlines, no rumor chasing.
- Acceptance before promotion: false positives and false negatives are tracked,
  severe news handling is auditable, and news blocks more risky behavior than it
  creates.

### 7. Portfolio and Risk Rebalancing

- Purpose: future treasury-level exposure management after the ledger and paper
  engine are stable.
- Inputs: cash, positions, target exposure ranges, risk state, strategy
  attribution, fees, slippage, volatility.
- Behavior: recommend paper rebalancing only when exposure drift or risk policy
  requires it.
- Outputs: candidate rebalance actions, rationale, estimated cost, risk impact.
- Risk interaction: risk owns final approval and can veto rebalancing.
- Non-goals: no aggressive tactical churn, no per-family-member portfolio split.
- Acceptance before promotion: reduces risk or improves benchmark comparison
  after costs without creating overtrading.

### 8. Ensemble Decision Matrix

- Purpose: combine strategy signals, model scores, news context, and risk
  context into one candidate action.
- Inputs: strategy signals, feature state, regime state, news state, model
  scores, treasury state, existing exposure.
- Behavior: produce candidate action, hold decision, reduce decision, or no-op.
- Outputs: decision record with inputs, weights, reason codes, confidence, and
  audit references.
- Risk interaction: the matrix does not override risk. Risk makes the final
  allow, reduce, delay, or veto decision.
- Non-goals: no autonomous live trading, no hidden black-box authority.
- Acceptance before promotion: outputs are explainable, reproducible, and
  evaluated against benchmarks and risk outcomes.

### Forbidden Early Strategies

- reinforcement learning trading
- scalping
- HFT
- futures
- leverage
- grid
- martingale
- meme coin chasing
- autonomous LLM trading
- market making with 200 EUR

### Strategy Promotion Pipeline

Pipeline:

```text
idea -> specified -> backtest_ready -> backtested -> paper_enabled -> paper_observed -> blocked/deprecated/future_live_candidate
```

Promotion requires:

- Clear specification.
- Completed strategy spec template.
- Realistic fees.
- Realistic slippage.
- Explicit break-even move required.
- No lookahead.
- No same-candle execution when the signal uses the same close.
- Out-of-sample validation.
- Walk-forward validation.
- Acceptable drawdown.
- Drawdown duration review.
- Stable behavior across regimes.
- Benchmark comparison.
- After-cost benchmark-relative result.
- Turnover and exposure review.
- Risk review.
- Owner review.
- Auditability.
- Preserved negative results and rejection reasons.

Hard rule:

Accuracy is not enough. A strategy must improve risk-adjusted paper performance
after fees, slippage, spread, rounding, drawdown, and regime analysis.
Promotion is not allowed when the strategy only looks good before costs, only
works in one cherry-picked regime, or depends on overtrading a small treasury.

Deprecation criteria:

- fails to beat the selected benchmark after costs
- violates risk policy too often
- depends on stale or missing data
- degrades outside one narrow regime
- creates excessive fee or slippage drag
- encourages overtrading
- lacks completed post-mortems
- cannot be explained to the owner with source data

## 16. Algorithmic and Model Spine

Every model and algorithm is a candidate until evaluated. No model is chosen
permanently in this document.

### Layer 1. Deterministic Features

- Purpose: create transparent market and treasury features that can be audited.
- Inputs: candles, trades if available, spreads if available, volume, treasury
  state, position state.
- Outputs: feature rows with timestamp, asset, timeframe, and calculation
  metadata.
- Candidate algorithms: log returns, rolling returns, realized volatility, ATR,
  RSI, MACD, moving average slope, Bollinger distance, volume z-score,
  spread/liquidity estimates.
- First implementation: deterministic pandas or Polars style feature functions
  over stored candles.
- Future candidates: multi-timeframe feature stores, microstructure features,
  and richer liquidity metrics.
- Non-goals: no prediction, no order execution, no opaque model behavior.
- Evaluation: unit tests, known-value examples, no leakage, stable output schema.

### Layer 2. Statistical Baselines

- Purpose: provide simple baselines that every complex strategy must beat.
- Inputs: price history, fees, slippage assumptions, schedule configuration.
- Outputs: benchmark curves and metrics.
- Candidate algorithms: buy-and-hold, scheduled accumulation, simple momentum,
  mean reversion, moving average crossover, EWMA volatility, rolling z-score.
- First implementation: reproducible backtest baselines with fixed parameters.
- Future candidates: ARIMA, SARIMAX, and GARCH if useful.
- Non-goals: no black-box optimization, no live execution.
- Evaluation: reproducibility, benchmark report integration, cost realism.

### Layer 3. Classical ML

- Purpose: test whether tabular features improve signal quality.
- Inputs: deterministic features, labels created from future returns without
  leakage, regime labels, cost assumptions.
- Outputs: calibrated probabilities, feature importance, evaluation metrics.
- Candidate algorithms: logistic regression, random forest, ExtraTrees,
  LightGBM, XGBoost, CatBoost, probability calibration.
- First implementation: logistic regression or tree baseline only after feature
  storage and labels are reliable.
- Future candidates: calibrated gradient boosting and stacked simple models.
- Non-goals: no autonomous trading, no model that bypasses rule checks.
- Evaluation: chronological splits, calibration, precision and recall by regime,
  paper PnL after costs.

### Layer 4. Regime Detection

- Purpose: classify market state so strategies know when to stand down or
  reduce activity.
- Inputs: trend features, volatility features, liquidity features, drawdown
  features, volume features.
- Outputs: regime label, confidence, reason codes.
- Candidate algorithms: rule-based regime labels, HMM, GMM, KMeans, change point
  detection later.
- First implementation: rule-based labels such as calm trend, volatile trend,
  chop, panic, stale, and illiquid.
- Future candidates: Hidden Markov Models, Gaussian Mixture Models, clustering,
  and change point detection.
- Non-goals: no regime label can force execution.
- Evaluation: stability, interpretability, transition behavior, strategy
  performance by regime.

### Layer 5. Compact Time-Series Models

- Purpose: evaluate whether compact forecasting models add value over simple
  baselines.
- Inputs: normalized time-series windows, features, calendar context, regime
  labels.
- Outputs: forecasts, uncertainty estimates if available, evaluation records.
- Candidate algorithms: TinyTimeMixer or Granite TTM, TimesFM, PatchTST,
  N-BEATS, N-HiTS.
- First implementation: none until baselines, features, and evaluation are
  mature.
- Future candidates: small reference LSTM or GRU only as comparison, not as a
  main plan.
- Non-goals: no large model download during bootstrap, no live order path.
- Evaluation: walk-forward validation, cost-aware paper impact, robustness by
  regime.

### Layer 6. News and Sentiment

- Purpose: detect news that should reduce or block risk.
- Inputs: news items, source, timestamp, assets, entities, text, historical
  related items.
- Outputs: sentiment, severity, affected assets, summary, confidence, source
  credibility.
- Candidate algorithms: FinBERT-style sentiment, rule-based severity, entity
  extraction, deduplication, source credibility scoring.
- First implementation: deterministic source and severity rules before local
  model inference.
- Future candidates: financial sentiment models and richer event classifiers.
- Non-goals: no headline-driven buy orders, no public advice.
- Evaluation: human review of severe events, false positive tracking, veto
  usefulness.

### Layer 7. Retrieval and Embeddings

- Purpose: create memory for news, decisions, reports, and historical context.
- Inputs: news text, audit records, reports, strategy notes, model evaluation
  summaries.
- Outputs: vector records, retrieved context, citations or source references.
- Candidate algorithms: Qwen, BGE, and E5 style embedding candidates.
- First implementation: no embedding model until model download is approved.
- Future candidates: LanceDB, sqlite-vec, or another local vector store after
  evaluation.
- Non-goals: no secret indexing, no private key indexing, no order execution.
- Evaluation: retrieval relevance, latency, storage size, source traceability.

### Layer 8. Small LLM

- Purpose: summarize, explain, and help the owner inspect the system.
- Inputs: retrieved context, strategy reports, audit summaries, news summaries,
  runtime state.
- Outputs: explanations, summaries, report drafts, operator Q&A.
- Candidate algorithms: small 3B to 4B local LLM later if needed.
- First implementation: none during bootstrap.
- Future candidates: local instruction model selected after hardware, memory,
  and quality review.
- Non-goals: no order execution, no risk override, no secret handling.
- Evaluation: factuality, source grounding, refusal to exceed authority, latency.

### Layer 9. Decision Matrix

- Purpose: combine deterministic strategy evidence into one candidate decision.
- Inputs: strategy outputs, model scores, regime labels, news severity, treasury
  state, exposure, risk context.
- Outputs: candidate action, no-op decision, confidence, reason codes, audit
  references.
- Candidate algorithms: deterministic scoring, weighted rules, calibrated model
  blending later.
- First implementation: deterministic rules with transparent weights.
- Future candidates: learned ranking only after sufficient paper history.
- Non-goals: no direct execution, no hidden model authority.
- Evaluation: reproducibility, auditability, paper performance, veto frequency.

### Layer 10. Risk Model

- Purpose: protect the treasury from unacceptable exposure, stale data, and
  unsafe market conditions.
- Inputs: candidate action, treasury state, position state, market state, news
  state, runtime locks, user action context.
- Outputs: allow, reduce, delay, veto, reason codes, audit record.
- Candidate algorithms: fixed fractional sizing, max exposure, stale-data veto,
  spread/liquidity veto, news severity veto, volatility shock veto, drawdown
  lock, manual and emergency locks.
- First implementation: deterministic policy with explicit thresholds.
- Future candidates: adaptive thresholds only after review.
- Non-goals: no black-box risk override, no live trading enablement by default.
- Evaluation: scenario tests, veto tests, drawdown behavior, audit completeness.

### Layer 11. Evaluation and Governance

- Purpose: prove that strategy and model changes are real improvements.
- Inputs: backtest results, paper results, benchmark results, risk decisions,
  audit records.
- Outputs: promotion recommendations, rejection reasons, evaluation reports.
- Candidate algorithms: chronological splits, walk-forward, fee and slippage
  modeling, PnL, max drawdown, expectancy, profit factor, Sharpe and Sortino
  with caution, performance by regime.
- First implementation: deterministic evaluation reports after backtesting.
- Future candidates: richer experiment tracking and model comparison.
- Non-goals: no metric-only promotion without review.
- Evaluation: governance rules are followed and no leakage is present.

### Layer 12. Model Registry

- Purpose: track model candidates, artifacts, evaluations, and allowed runtime
  status.
- Inputs: artifact metadata, training or download source, checksums, evaluation
  results, hardware notes.
- Outputs: model registry entries, active or inactive status, approval record.
- Candidate algorithms: not applicable; this is governance and storage.
- First implementation: metadata-only registry before real models.
- Future candidates: artifact checksum verification and runtime compatibility
  checks.
- Non-goals: no automatic download, no unreviewed activation.
- Evaluation: every model has provenance, evaluation, and approval state.

## 17. Data, Storage, and Schema Spine

Primary stores:

- SQLite operational state: source for users, sessions, runtime state, current
  treasury state, and small transactional records.
- DuckDB and Parquet analytical lake: source for candles, features, reports,
  backtests, and larger analytical tables.
- LanceDB or vector store later: source for embeddings and retrieval memory
  after model download is approved.
- Model artifacts later: local files for evaluated models, outside the repo.
- Logs and audit: append-friendly records for service behavior and security
  review.
- Backups: daily and weekly copies of operational and analytical state.

Future categories:

- `users`: stores account identity, role, display name, and status.
- `devices`: stores trusted device records, labels, and trust state.
- `sessions`: stores active and historical login sessions.
- `treasury`: stores one treasury summary and current paper mode state.
- `ledger_entries`: stores immutable accounting entries for paper treasury
  changes.
- `positions`: stores open and closed asset exposure.
- `paper_orders`: stores simulated order intents.
- `paper_fills`: stores simulated fills with price, fee, and slippage.
- `market_feeds`: stores source configuration and feed health.
- `candles`: stores OHLCV market data by asset, source, and timeframe.
- `features`: stores deterministic features derived from market data.
- `news_items`: stores normalized news records and source metadata.
- `embeddings`: stores vector references for retrieval memory after approval.
- `decision_records`: stores owner decisions, no-action decisions, hypotheses,
  missing data, reasons not to act, risk context, later outcomes, and
  post-mortems.
- `strategy_specs`: stores written strategy specifications and promotion state.
- `strategy_signals`: stores candidate signals emitted by strategies.
- `backtest_runs`: stores leakage-safe backtest configuration, benchmark
  comparison, regime breakdown, and cost assumptions.
- `performance_metrics`: stores returns, volatility, drawdown, expectancy,
  turnover, fee drag, slippage drag, and risk-adjusted after-cost results.
- `risk_decisions`: stores allow, reduce, delay, or veto outcomes.
- `audit_records`: stores security, permission, runtime, and treasury audit
  events.
- `runtime_jobs`: stores scheduled or running worker job state.
- `agent_events`: stores future agent task events, summaries, and decisions.

Storage rules:

- Operational mutations must be auditable.
- Analytical data should be append-friendly when possible.
- Runtime data must remain outside the repository.
- Backups must be restorable and documented.
- Sensitive data must not be written to logs unless explicitly reviewed and
  redacted.

## 18. Execution Flow Spine

Future full flow:

1. Market data arrives from an approved source.
2. Data is normalized into a consistent asset, timestamp, and candle schema.
3. Features are generated from normalized data.
4. Regime is identified from feature state.
5. Strategies generate candidate signals.
6. News and retrieval context is attached to the market and strategy context.
7. Models score the setup if evaluated models are approved for that role.
8. Decision matrix creates a candidate action or no-op decision.
9. Risk engine approves, reduces, delays, or vetoes the candidate action.
10. Paper execution simulates order creation and fill behavior.
11. Treasury ledger updates from the simulated fill.
12. Audit records all relevant inputs, outputs, decisions, and reason codes.
13. Client receives an update through API polling or future events.
14. Reports and evaluation records update.
15. Strategy promotion state changes only after review.

Current implementation flow:

- Provider stub starts.
- Provider health can be checked.
- Provider models endpoint returns an empty list.
- API placeholder can report health.
- Worker placeholder can emit a heartbeat.
- No market data arrives.
- No features are generated.
- No regime is identified.
- No strategy creates a signal.
- No decision matrix runs.
- No risk engine runs.
- No execution happens.

## 19. API and Event Spine

Do not implement new API surfaces in `DOCS.SPINE.3`. This section plans future
contracts.

Future API surfaces:

- Provider API: exposes provider health, capabilities, and future approved local
  compute operations.
- Runtime API: exposes runtime state, pause, resume, emergency stop, and job
  status.
- Treasury API: exposes treasury summary, positions, ledger, paper orders, and
  paper fills.
- Identity API: exposes login, sessions, users, devices, roles, and
  capabilities.
- Strategy API: exposes strategy definitions, signals, backtests, and promotion
  state.
- Risk API: exposes risk policy, risk state, veto reasons, and locked states.
- Report API: exposes daily, weekly, and strategy evaluation reports.
- Audit API: exposes filtered audit records according to capability.

Future events:

- `runtime.started`: records that the runtime started.
- `runtime.stopped`: records that the runtime stopped normally.
- `provider.healthy`: records that provider health is ok.
- `provider.unhealthy`: records that provider health failed.
- `treasury.updated`: records that treasury summary or ledger state changed.
- `signal.created`: records that a strategy emitted a candidate signal.
- `risk.vetoed`: records that risk blocked a candidate action.
- `paper.order_created`: records that a simulated paper order was created.
- `paper.fill_created`: records that a simulated paper fill was created.
- `news.severe`: records that severe news affected risk context.
- `model.evaluated`: records that a model candidate was evaluated.
- `emergency.stop`: records that emergency stop was triggered.
- `permission.denied`: records that a user attempted a forbidden action.
- `audit.recorded`: records that an audit entry was written.

Event rules:

- Events must be typed.
- Events must be timestamped.
- Events must reference actor or system source.
- Events that affect money, risk, runtime, or permissions must be auditable.

## 20. Delivery Spine Rules

Every future wave must have:

- wave id
- title
- purpose
- previous state
- target state
- scope
- non-goals
- target files
- target modules
- database changes
- API changes
- UI changes
- runtime changes
- security boundaries
- validation commands
- acceptance criteria
- expected completion report
- roadmap update requirement
- canonical phase id such as `P0.H`, `P1.A`, or `P2.A`

Every sub-wave must have:

- sub-wave id
- purpose
- tasks
- files
- output
- acceptance
- non-goals

Standard delivery box:

```text
Wave:
Title:
Purpose:
Previous state:
Target state:
Scope:
Non-goals:
Target files:
Target modules:
Database changes:
API changes:
UI changes:
Runtime changes:
Security boundaries:
Validation commands:
Acceptance criteria:
Expected completion report:
Roadmap update requirement:
```

Standard sub-wave box:

```text
Sub-wave:
Purpose:
Tasks:
Files:
Output:
Acceptance:
Non-goals:
```

Freeze rules:

- Future implementation prompts must use canonical `P*.*` ids.
- Legacy aliases may appear only in parentheses for traceability.
- If a prompt uses `CORE.*` alone after `P0.NAMING.1`, treat it as incomplete
  and correct the prompt before execution.
- Do not start Spark runtime work before `P0.G`, `P0.H`, `P0.I`, `P0.J`,
  `P0.K`, `P0.L`, and `P0.M` are complete, unless a later wave explicitly
  proves the Spark task is infrastructure-only and non-blocking.
- Do not treat Tailscale as trading, provider activation, model serving, or
  Spark runtime approval. Future Tailscale work is infrastructure access only.
- Do not scaffold the mobile client before the client framework decision is
  ready.
- Do not add exchange keys, wallet custody, live trading, withdrawals, or AI
  model downloads during bootstrap waves.
- Do not promote a strategy without evaluation and review.
- Do not promote a strategy that fails after costs, lacks benchmark comparison,
  or lacks backtest integrity checks.
- Do not treat UI locks as security.
- Do not convert open decisions into fake decisions.
- Do not implement public service behavior without legal and regulatory review.

## 21. Full Phase Roadmap

This phase map is designed so a future coding agent can copy a wave and execute
without reinventing architecture. Phase ids are canonical. Legacy aliases are
kept only for traceability to previous prompts and commit messages.

Current near-term Phase 0 product-core sequence:

1. `P0.H - Identity, Capabilities, and Paper Treasury Boundary`
   (legacy alias: `CORE.0`)
2. `P0.I - Append-Only Paper Treasury Ledger`
   (legacy alias: `CORE.1`)
3. `P0.J - Ledger Projection and Treasury Snapshot`
   (legacy alias: `CORE.2`)
4. `P0.K - Paper Position Boundary`
   (legacy alias: `CORE.3`)
5. `P0.L - Paper Portfolio Snapshot Boundary`
   (legacy alias: `CORE.4`)
6. `P0.M - Paper Decision Record Boundary`
   (legacy alias: `CORE.5`)

This product-core path remains inside Phase 0 because it is foundational. It
overrides the older Spark-first infrastructure sequence where they conflict.
Phase 1, Phase 2, and later phases remain future or reserved according to this
spine. Spark and Tailscale do not start until the Phase 0 product-core blockers
are complete or explicitly waived by a later documented wave.

`DOCS.REVIEW.2` establishes candidate paper-mode defaults for:

- first true MVP cut
- primary product outcome
- decision frequency
- initial timeframe
- primary benchmark
- simulated fee, spread, slippage, and rounding assumptions
- maximum decisions or trades per week
- conservative strategy numeric definition
- strategy promotion metric
- behavior when no strategy beats benchmark
- minimum paper duration before any manual live consideration
- trusted-enough data criteria

`P0.H` must establish identity, capabilities, and paper treasury boundaries
before any strategy or data pipeline can mutate treasury state.

`P0.I` must make the 200 EUR paper treasury ledger auditable before paper
execution exists.

`P0.J` must project the append-only paper ledger into a deterministic treasury
snapshot before UI, risk, paper execution, or reporting consumes treasury state.

`P0.K` must define paper position boundaries before any market data,
valuation, order, fill, strategy, or execution work.

`P0.L` must combine the treasury cash snapshot and paper position book into a
paper portfolio snapshot boundary without market prices, execution, or live
capital behavior.

`P0.M` must define paper decision records before market data, strategy
evaluation, paper execution, reporting, or model assistance.

### Phase 0. Bootstrap and Product Core Foundation

Outcome: drmlke has a safe repository skeleton, local provider stub, validated
development commands, complete master spine, and the first paper-only product
core boundaries. Phase 0 remains foundational. It does not include live trading,
market data ingestion, strategy execution, provider runtime expansion, Spark
deployment, wallet custody, or UI implementation.

- P0.A - Repository Bootstrap. Legacy output: `BOOTSTRAP.0`. Purpose: create
  the monorepo skeleton. Tasks: create app and package folders, workspace
  config, Makefile, Docker files. Status: completed.
- P0.B - Provider Stub. Legacy output: provider bootstrap. Purpose: create a
  safe local provider boundary with `/health` and `/models`, with no inference.
  Status: completed.
- P0.C - Environment Doctor. Purpose: create repeatable local checks through the
  doctor script and Make validation targets. Status: completed.
- P0.D - Safety Documentation. Purpose: document AGENTS, architecture,
  environment, deployment, and hard safety boundaries. Status: completed.
- P0.E - Treasury Model Correction. Legacy output: `DOCS.SPINE.2`. Purpose:
  correct the product model to one owner-managed treasury, Padre/Zio as viewers,
  and no per-family-member trading portfolios. Status: completed.
- P0.F - Master Spine Completion. Legacy output: `DOCS.SPINE.3`. Purpose: make
  the roadmap execution-grade, correct sequencing, and define delivery rules.
  Status: completed.
- P0.G - Product Thesis, Decision Math, and MVP Gates. Legacy outputs:
  `DOCS.REVIEW.1`, `DOCS.REVIEW.2`. Purpose: define product thesis, decision
  quality spine, mathematical spine, strategy specification template, backtest
  integrity, MVP exact cut, and numeric paper risk draft. Status: completed.
- P0.H - Identity, Capabilities, and Paper Treasury Boundary. Legacy alias:
  `CORE.0`. Purpose: define identity contracts, role/capability policy, safety
  locks, one paper treasury, 200 EUR paper capital, and 0 EUR live capital.
  Status: completed.
- P0.I - Append-Only Paper Treasury Ledger. Legacy alias: `CORE.1`. Purpose:
  define append-only ledger contracts, immutable ledger entries, and the initial
  200 EUR paper capital entry. Status: completed.
- P0.J - Ledger Projection and Treasury Snapshot. Legacy alias: `CORE.2`.
  Purpose: project the append-only ledger into a treasury cash snapshot with
  available cash, reserved cash, total cash, fees, adjustments, and corrections.
  Status: completed.
- P0.K - Paper Position Boundary. Legacy alias: `CORE.3`. Purpose: define
  paper-only BTC/ETH position contracts, long-only positions, non-live-backed
  state, position book, and no market valuation. Status: completed.
- P0.L - Paper Portfolio Snapshot Boundary. Legacy alias: `CORE.4`. Purpose:
  combine the treasury snapshot and paper position book into a structural
  portfolio snapshot with no market valuation, no PnL, and no execution. Status:
  completed.
- P0.M - Paper Decision Record Boundary. Legacy alias: `CORE.5`. Purpose:
  define paper decision records, action/no-action records, hypothesis, reasons
  not to act, risk context, stale data state, later outcome, and post-mortem
  fields. Status: completed.
- P0.CLOSE - Phase 0 Product Core Closeout. Purpose: verify that `P0.H`
  through `P0.M` remain coherent together before infrastructure, persistence,
  API, market data, strategy, execution, or UI work. Status: current closeout.

### Phase 1. MacBook development setup

Outcome: MacBook is a clean alternate development machine with the repo cloned
and local validation working.

- P1.A - Toolchain check. Purpose: learn current MacBook state. Tasks: check
  git, vim, Python, `uv`, Node, corepack, pnpm, Docker, VS Code, Tailscale.
  Output: setup report. Acceptance: missing tools are listed. Non-goals: Spark
  access.
- P1.B - Repository clone. Purpose: create a working checkout. Tasks: clone the
  GitHub remote, check branch, check remote, run git status. Output: local repo.
  Acceptance: repo matches remote. Non-goals: code changes.
- P1.C - Node 24 setup. Purpose: align frontend toolchain. Tasks: choose nvm,
  mise, fnm, or Homebrew node@24; activate Node 24; enable corepack; verify
  pnpm. Output: Node 24 ready. Acceptance: `node -v` returns v24.x. Non-goals:
  client scaffold.
- P1.D - Python and uv setup. Purpose: align backend toolchain. Tasks: verify
  Python 3.12, install or configure `uv`, run `uv sync --dev`. Output: Python
  workspace ready. Acceptance: dependencies install. Non-goals: new packages.
- P1.E - Docker runtime option check. Purpose: decide whether Docker Desktop,
  OrbStack, or another Docker-compatible runtime is needed now. Tasks: inspect
  Docker availability, document runtime status. Output: Docker status.
  Acceptance: doctor either passes or clearly documents missing Docker.
  Non-goals: production deployment.
- P1.F - Local validation and VS Code. Purpose: prove the MacBook can work.
  Tasks: run `make doctor`, run `make check`, optionally run provider, open VS
  Code. Output: validation report. Acceptance: checks pass or documented
  exceptions are understood. Non-goals: Spark deployment.

### Phase 2. Tailscale and Spark access planning

Status: active access-planning phase after `P0.CLOSE`.

Outcome: Spark private access path is inventoried, reachability is verified,
and SSH identity is confirmed before runtime deployment begins.

- P2.A - Access inventory. Purpose: identify available Spark access candidates.
  Tasks: inspect local Tailscale status, SSH config, known aliases, and missing
  access facts without logging in to Spark. Output: `docs/access-inventory.md`.
  Acceptance: candidate paths and unknowns are documented. Non-goals:
  reachability proof, SSH login, runtime deployment, or remote mutation.
- P2.B - Tailscale reachability. Purpose: confirm private network reachability.
  Tasks: ping Spark over Tailscale and record address. Output: reachability
  result. Acceptance: Tailscale path works or blocker is documented. Status:
  completed. Non-goals: SSH login, remote mutation, deployment, or public
  exposure.
- P2.C - SSH verification. Purpose: confirm an explicit SSH path. Tasks: use
  selected alias or address, verify host key, verify user. Output: SSH result.
  Acceptance: login succeeds or clear remediation exists. Non-goals: changing
  production routing.
- P2.D - Remote preflight. Purpose: inspect Spark without deploying. Tasks:
  check OS, architecture, disk, Docker, Compose, GPU visibility if appropriate.
  Output: preflight report. Acceptance: runtime blockers are known. Non-goals:
  creating `/srv/drmlke`.
- P2.E - Private service policy. Purpose: define how services stay private.
  Tasks: document bind addresses, firewall expectations, VPN route, and no
  public tunnels. Output: access policy. Acceptance: no public internet exposure
  is required. Non-goals: firewall changes unless explicitly approved.
- P2.F - Roadmap update. Purpose: lock the Spark access decision. Tasks: update
  docs with chosen path and next runtime wave. Output: roadmap delta.
  Acceptance: `SPARK.RUNTIME.1` can start with clear access. Non-goals:
  deployment.

### Phase 3. Reserved Later: Spark storage and provider runtime deployment

Status: reserved until the Product Core path no longer depends on identity,
paper treasury, market data, benchmarks, and decision records.

Outcome when unblocked: Spark has `/srv/drmlke`, a deploy copy, private
provider runtime, and repeatable validation.

- P3.A - Storage root preparation. Purpose: create persistent runtime layout.
  Tasks: create `/srv/drmlke` tree, set ownership, document permissions. Output:
  storage tree. Acceptance: directories exist with correct owner. Non-goals:
  secrets.
- P3.B - Environment file setup. Purpose: create runtime env outside repo.
  Tasks: create env file from example, force live trading and withdrawals off,
  back up before overwrite. Output: Spark env. Acceptance: env is outside git.
  Non-goals: exchange keys.
- P3.C - Deploy copy. Purpose: place source under `/srv/drmlke/app`. Tasks:
  clone or sync repo, verify commit, avoid authoring there. Output: deploy copy.
  Acceptance: source version is known. Non-goals: editing on Spark.
- P3.D - Compose profile. Purpose: run provider privately. Tasks: build or pull
  images, run provider profile, bind only to private path. Output: provider
  runtime. Acceptance: health ok from approved network. Non-goals: public port.
- P3.E - Logs and restart policy. Purpose: make runtime observable. Tasks:
  configure logs, inspect process, document restart. Output: operation notes.
  Acceptance: logs are in `/srv/drmlke/logs/provider`. Non-goals: full worker.
- P3.F - Spark report. Purpose: record deploy state. Tasks: run health, models,
  Docker status, git status, and update docs. Output: completion report.
  Acceptance: provider stub runs privately. Non-goals: live trading.

### Phase 4. Provider contract and backend adapter boundary

Outcome: provider and API have explicit contracts for health, capabilities, and
future compute without hidden execution authority.

- P4.A - Contract spec. Purpose: define provider requests and responses. Tasks:
  write schemas for health, capabilities, model list, and errors. Output:
  provider contract. Acceptance: schemas are documented. Non-goals: real models.
- P4.B - API adapter. Purpose: let API query provider safely. Tasks: add client
  wrapper, timeouts, and safe errors. Output: provider adapter. Acceptance:
  tests cover success and failure. Non-goals: model inference.
- P4.C - Capability endpoint. Purpose: expose what provider can do. Tasks:
  return stub capabilities and no active models. Output: capability response.
  Acceptance: live execution is absent. Non-goals: downloads.
- P4.D - Runtime config. Purpose: configure provider URL and timeouts. Tasks:
  add settings and env docs. Output: config entries. Acceptance: defaults are
  local and safe. Non-goals: secrets.
- P4.E - Error and audit hooks. Purpose: make failures inspectable. Tasks:
  define error shape and audit hook points. Output: typed failures. Acceptance:
  no raw stack leaks to clients. Non-goals: full audit store.
- P4.F - Validation. Purpose: prove boundary behavior. Tasks: run unit tests,
  API health, provider health. Output: validation report. Acceptance: contract
  stable. Non-goals: strategy logic.

### Phase 5. Identity, accounts, roles, capability model

Outcome: API can represent users, roles, sessions, devices, and capabilities
with server-side enforcement.

- P5.A - Capability definitions. Purpose: define all initial capabilities.
  Tasks: add enums and role defaults. Output: capability module. Acceptance:
  owner and viewer mappings match this spine. Non-goals: UI.
- P5.B - User schema. Purpose: store users and roles. Tasks: add storage schema
  and seed records for Francesco, Padre, and Zio. Output: user store.
  Acceptance: one owner and two viewers exist. Non-goals: public signup.
- P5.C - Session skeleton. Purpose: represent authenticated sessions. Tasks:
  define session model and simple dev auth path. Output: session state.
  Acceptance: tests verify role resolution. Non-goals: final auth.
- P5.D - Permission guard. Purpose: enforce capabilities server-side. Tasks:
  add reusable guard and denial response. Output: permission boundary.
  Acceptance: forbidden viewer action is denied. Non-goals: relying on UI lock.
- P5.E - Audit permission denials. Purpose: record security-relevant denials.
  Tasks: write audit records for denied actions. Output: denial audit.
  Acceptance: denial is inspectable. Non-goals: full audit UI.
- P5.F - Validation. Purpose: prove corrected account model. Tasks: unit tests
  for owner, viewer, emergency, technical roles. Output: test report.
  Acceptance: no per-person trading portfolio exists. Non-goals: ledger.

### Phase 6. Treasury and paper ledger

Outcome: one simulated 200 EUR treasury, ledger entries, positions, and PnL are
represented safely.

- P6.A - Treasury schema. Purpose: define one paper treasury. Tasks: create
  treasury table or model with mode and currency. Output: treasury record.
  Acceptance: exactly one active treasury. Non-goals: real funds.
- P6.B - Ledger entries. Purpose: record immutable accounting events. Tasks:
  define entry types, amounts, asset, source, and audit reference. Output:
  ledger model. Acceptance: entries are append-only. Non-goals: withdrawals.
- P6.C - Position accounting. Purpose: derive holdings from ledger and fills.
  Tasks: implement position summaries. Output: positions view. Acceptance:
  known examples reconcile. Non-goals: exchange balances.
- P6.D - PnL accounting. Purpose: show realized and unrealized results. Tasks:
  calculate PnL with fees and slippage. Output: PnL summary. Acceptance:
  tests cover fee effects. Non-goals: tax reporting.
- P6.E - Treasury API. Purpose: expose read-only treasury state. Tasks: add
  endpoints guarded by capabilities. Output: treasury read API. Acceptance:
  viewer can read permitted data. Non-goals: mutating UI.
- P6.F - Validation. Purpose: prove paper ledger safety. Tasks: run unit tests
  and API tests. Output: validation report. Acceptance: live capital remains 0
  EUR. Non-goals: exchange integration.

### Phase 7. Mobile public client shell with permission-locked UI

Outcome: shared client shell exists with login, navigation, role-aware state,
and locked controls, without trading implementation.

- P7.A - Framework decision. Purpose: choose SvelteKit or React. Tasks: compare
  fit for mobile packaging and shared UI. Output: decision record. Acceptance:
  choice is documented. Non-goals: scaffold before decision.
- P7.B - Client scaffold. Purpose: create app shell. Tasks: initialize project,
  wire lint and build. Output: client app. Acceptance: build passes. Non-goals:
  trading logic.
- P7.C - Auth shell. Purpose: represent session and role. Tasks: add login view
  and mock or API-backed session. Output: login flow. Acceptance: owner and
  viewer states render. Non-goals: final auth.
- P7.D - Navigation and screens. Purpose: create listed mobile screens. Tasks:
  add Home, Treasury, Positions, PnL, Signals, News, Runtime, Risk, Alerts,
  Settings, Emergency. Output: navigable shell. Acceptance: screens fit mobile.
  Non-goals: real data.
- P7.E - Capability locks. Purpose: communicate permissions. Tasks: render
  disabled or hidden actions from API capability state. Output: locked UI.
  Acceptance: viewer cannot trigger mutating actions. Non-goals: treating UI as
  security.
- P7.F - Validation. Purpose: verify shell quality. Tasks: run client tests,
  responsive checks, and API permission checks. Output: validation report.
  Acceptance: one shared app for roles. Non-goals: packaging release.

### Phase 8. Web admin console shell

Outcome: private owner console shell exists for dense runtime inspection.

- P8.A - Admin route plan. Purpose: define sections and layout. Tasks: map left
  rail, top status bar, workspace, inspector, event strip. Output: UI plan.
  Acceptance: all required sections covered. Non-goals: public landing page.
- P8.B - Shell implementation. Purpose: create admin console frame. Tasks: add
  layout and routing. Output: admin shell. Acceptance: owner navigation works.
  Non-goals: full data.
- P8.C - Status bar. Purpose: show runtime essentials. Tasks: display mode,
  runtime, provider, risk, emergency state. Output: status bar. Acceptance:
  stale and loading states exist. Non-goals: live controls.
- P8.D - Inspector pattern. Purpose: support detailed entity review. Tasks:
  create right inspector for selected rows or cards. Output: inspector
  component. Acceptance: works with placeholder entities. Non-goals: nested
  card clutter.
- P8.E - Permission handling. Purpose: enforce owner-only surfaces. Tasks:
  guard admin routes and show safe denial. Output: admin guard. Acceptance:
  viewer cannot access admin actions. Non-goals: client-only security.
- P8.F - Validation. Purpose: test console shell. Tasks: run frontend and API
  checks. Output: validation report. Acceptance: console remains private.
  Non-goals: public deployment.

### Phase 9. Runtime control and event bus

Outcome: runtime state, commands, jobs, and events have a safe operational
foundation.

- P9.A - Runtime state model. Purpose: represent stopped, running, paused, and
  emergency states. Tasks: add state schema and transitions. Output: runtime
  model. Acceptance: invalid transitions are rejected. Non-goals: trading.
- P9.B - Command API. Purpose: expose pause, resume, and emergency stop. Tasks:
  add guarded endpoints. Output: runtime API. Acceptance: viewer denied,
  owner audited. Non-goals: live execution.
- P9.C - Event table. Purpose: store runtime events. Tasks: define event schema
  and writer. Output: event store. Acceptance: events are typed. Non-goals:
  distributed streaming.
- P9.D - Worker job model. Purpose: represent scheduled jobs. Tasks: define job
  states and heartbeat. Output: job records. Acceptance: worker heartbeat is
  visible. Non-goals: market collection.
- P9.E - Client updates. Purpose: show runtime state in UI. Tasks: wire API
  reads to mobile and admin shells. Output: runtime views. Acceptance: pause
  state is visible. Non-goals: real-time sockets unless needed.
- P9.F - Validation. Purpose: prove command safety. Tasks: tests for state
  transitions, permissions, audit. Output: validation report. Acceptance:
  emergency stop is auditable. Non-goals: resume after live lock.

### Phase 10. Market data collector

Outcome: approved public market data can be collected, normalized, stored, and
monitored without exchange trading keys.

- P10.A - Source decision. Purpose: choose first public data source. Tasks:
  evaluate source reliability, symbols, rate limits, and terms. Output:
  decision record. Acceptance: source is approved. Non-goals: private exchange
  keys.
- P10.B - Symbol model. Purpose: normalize asset notation. Tasks: define BTC/EUR
  or BTC/USDT notation and mapping. Output: symbol schema. Acceptance: notation
  is consistent. Non-goals: all assets.
- P10.C - Collector job. Purpose: fetch market data. Tasks: implement scheduled
  public data collection. Output: collector. Acceptance: stores candles.
  Non-goals: trading.
- P10.D - Normalization. Purpose: produce stable candle schema. Tasks: validate
  timestamps, price fields, volume, source metadata. Output: normalized candles.
  Acceptance: malformed data is rejected. Non-goals: predictions.
- P10.E - Feed health. Purpose: detect stale data. Tasks: add feed status and
  stale thresholds. Output: feed health records. Acceptance: stale source is
  visible. Non-goals: risk engine integration yet.
- P10.F - Validation. Purpose: prove data collection. Tasks: unit tests, sample
  fetch, storage checks. Output: validation report. Acceptance: no exchange keys
  required. Non-goals: live order book trading.

### Phase 11. Feature and regime engine

Outcome: deterministic features and rule-based regimes are generated from stored
market data.

- P11.A - Feature schema. Purpose: define feature rows and metadata. Tasks: add
  feature table or parquet schema. Output: schema. Acceptance: asset/timeframe
  keys are stable. Non-goals: ML model.
- P11.B - Feature functions. Purpose: calculate transparent indicators. Tasks:
  implement returns, volatility, ATR, RSI, MACD, moving average slope,
  Bollinger distance, volume z-score. Output: feature library. Acceptance:
  known-value tests pass. Non-goals: prediction.
- P11.C - Feature job. Purpose: generate features on schedule. Tasks: add worker
  job from candles to features. Output: feature pipeline. Acceptance: idempotent
  reruns. Non-goals: trading.
- P11.D - Regime rules. Purpose: classify market state. Tasks: implement calm,
  trend, chop, volatile, panic, stale, illiquid labels. Output: regime labels.
  Acceptance: reason codes are present. Non-goals: HMM first.
- P11.E - API and views. Purpose: expose feature and regime summaries. Tasks:
  add read endpoints and UI summaries. Output: inspectable state. Acceptance:
  owner can inspect calculations. Non-goals: strategy approval.
- P11.F - Validation. Purpose: prevent leakage and instability. Tasks: tests for
  windows, timestamps, missing data. Output: validation report. Acceptance: no
  future data is used. Non-goals: backtest engine.

### Phase 12. Strategy lab and backtesting

Outcome: strategies can be specified, backtested, compared to benchmarks, and
kept out of execution until promoted.

- P12.A - Strategy spec model. Purpose: define strategy metadata and parameters.
  Tasks: add strategy definitions and states. Output: strategy registry.
  Acceptance: promotion pipeline states exist. Non-goals: live trading.
- P12.B - Benchmark backtests. Purpose: implement buy-and-hold and scheduled
  accumulation. Tasks: run deterministic simulations. Output: benchmark
  results. Acceptance: reproducible reports. Non-goals: complex ML.
- P12.C - Strategy backtest engine. Purpose: test candidate signals over
  history. Tasks: implement chronological runner with fees and slippage. Output:
  backtest engine. Acceptance: no lookahead. Non-goals: real orders.
- P12.D - Strategy families. Purpose: specify trend, mean reversion, breakout,
  and news avoidance. Tasks: implement paper signal logic or specs. Output:
  strategy candidates. Acceptance: outputs include reason codes. Non-goals:
  promotion without review.
- P12.E - Reports. Purpose: compare strategy to benchmarks. Tasks: produce PnL,
  drawdown, expectancy, profit factor, and regime breakdown. Output: report.
  Acceptance: costs included. Non-goals: public claims.
- P12.F - Validation. Purpose: prove backtest integrity. Tasks: tests for
  splits, costs, signal timing, and metrics. Output: validation report.
  Acceptance: strategy remains paper-only. Non-goals: exchange adapter.

### Phase 13. Paper trading engine

Outcome: candidate actions can become simulated paper orders and fills that
update the single treasury ledger.

- P13.A - Paper order model. Purpose: represent simulated order intent. Tasks:
  add order fields, source signal, status, and audit link. Output: paper order
  schema. Acceptance: no real venue fields imply execution. Non-goals: exchange
  order.
- P13.B - Fill simulator. Purpose: simulate fills realistically. Tasks: model
  mark price, slippage, fee, partial fill policy if needed. Output: simulated
  fills. Acceptance: fill math is tested. Non-goals: live order book.
- P13.C - Ledger integration. Purpose: update treasury from fills. Tasks: write
  ledger entries and positions. Output: paper accounting. Acceptance: cash and
  position reconcile. Non-goals: withdrawal.
- P13.D - Order lifecycle. Purpose: model created, filled, cancelled, rejected.
  Tasks: implement state transitions and audit. Output: lifecycle logic.
  Acceptance: invalid transitions fail. Non-goals: broker integration.
- P13.E - UI inspection. Purpose: show orders and fills. Tasks: add mobile and
  admin read views. Output: paper trading views. Acceptance: viewer read rules
  apply. Non-goals: viewer actions.
- P13.F - Validation. Purpose: prove paper safety. Tasks: run unit, integration,
  and permission tests. Output: validation report. Acceptance: no live path.
  Non-goals: shadow exchange.

### Phase 14. News, retrieval, and sentiment engine

Outcome: news can be collected, normalized, scored, stored, and used for risk
context without creating autonomous trades.

- P14.A - News source decision. Purpose: choose initial source. Tasks: evaluate
  RSS, APIs, rate limits, and terms. Output: source decision. Acceptance:
  source is approved. Non-goals: paid integrations unless decided.
- P14.B - News ingestion. Purpose: collect and normalize news. Tasks: fetch,
  deduplicate, store source and timestamp. Output: news items. Acceptance:
  duplicates collapse. Non-goals: trading.
- P14.C - Severity rules. Purpose: classify risk severity. Tasks: implement
  deterministic rules and affected asset extraction. Output: severity labels.
  Acceptance: severe items are visible. Non-goals: LLM first.
- P14.D - Sentiment candidate. Purpose: evaluate financial sentiment. Tasks:
  define model candidate and offline evaluation plan. Output: candidate record.
  Acceptance: no download without approval. Non-goals: model runtime now.
- P14.E - Retrieval memory. Purpose: plan or implement embedding storage after
  approval. Tasks: store source text and retrieval metadata. Output: retrieval
  ready data. Acceptance: source traceability. Non-goals: secret indexing.
- P14.F - Validation. Purpose: prove news blocks risk safely. Tasks: test
  severity, dedupe, and risk context handoff. Output: validation report.
  Acceptance: news creates veto context, not buy orders. Non-goals: autonomous
  LLM.

### Phase 15. Baseline and time-series model lab

Outcome: model candidates can be evaluated offline against baselines without
runtime authority.

- P15.A - Model registry metadata. Purpose: track candidates before artifacts.
  Tasks: define registry schema and statuses. Output: registry. Acceptance:
  inactive by default. Non-goals: downloads.
- P15.B - Evaluation dataset. Purpose: create leakage-safe windows. Tasks:
  build chronological splits and labels. Output: dataset builder. Acceptance:
  tests prevent future leakage. Non-goals: production inference.
- P15.C - Classical baseline. Purpose: test simple models first. Tasks: train or
  evaluate logistic regression or tree baselines. Output: baseline metrics.
  Acceptance: cost-aware comparison. Non-goals: live decisions.
- P15.D - Time-series candidates. Purpose: evaluate TTM, TimesFM, PatchTST, or
  N-BEATS later. Tasks: document requirements and run only approved candidates.
  Output: candidate evaluation. Acceptance: no unapproved downloads. Non-goals:
  permanent model choice.
- P15.E - Provider integration plan. Purpose: define how evaluated models become
  provider capabilities. Tasks: map registry status to provider response.
  Output: integration plan. Acceptance: inactive models cannot run. Non-goals:
  execution.
- P15.F - Validation. Purpose: prove governance. Tasks: verify registry,
  metrics, and approval state. Output: validation report. Acceptance: no model
  can trade. Non-goals: risk override.

### Phase 16. Decision matrix and risk integration

Outcome: signals, models, news, treasury state, and risk policy combine into
auditable candidate decisions and final paper-only risk outcomes.

- P16.A - Decision schema. Purpose: define candidate action record. Tasks: add
  fields for signal, score, reason codes, confidence, and audit refs. Output:
  decision model. Acceptance: explainable record. Non-goals: order execution.
- P16.B - Matrix rules. Purpose: combine evidence. Tasks: implement
  deterministic weights or rules. Output: matrix function. Acceptance:
  reproducible output. Non-goals: black box.
- P16.C - Risk policy. Purpose: enforce hard safety. Tasks: implement exposure,
  stale data, liquidity, news, volatility, drawdown, and emergency checks.
  Output: risk engine. Acceptance: veto tests pass. Non-goals: live enable.
- P16.D - Paper handoff. Purpose: allow approved paper decisions to create
  paper orders. Tasks: connect decision to paper engine. Output: paper handoff.
  Acceptance: risk decision is required. Non-goals: exchange handoff.
- P16.E - UI and audit. Purpose: show decision and risk reasons. Tasks: add
  detail views and audit records. Output: inspectable decisions. Acceptance:
  owner can see why. Non-goals: hidden scoring.
- P16.F - Validation. Purpose: prove risk cannot be bypassed. Tasks: permission,
  scenario, and integration tests. Output: validation report. Acceptance: all
  candidate actions pass through risk. Non-goals: live gate.

### Phase 17. Reporting, audit, and evaluation

Outcome: owner can review performance, risk, events, permission denials, and
strategy promotion evidence.

- P17.A - Audit schema. Purpose: define immutable audit records. Tasks: include
  actor, action, target, result, reason, and timestamp. Output: audit store.
  Acceptance: critical actions audited. Non-goals: editable audit.
- P17.B - Report jobs. Purpose: generate daily and weekly summaries. Tasks:
  compute treasury, PnL, risk, signals, news, and runtime summaries. Output:
  reports. Acceptance: report job is repeatable. Non-goals: public advice.
- P17.C - Evaluation reports. Purpose: compare strategy and model performance.
  Tasks: produce benchmark and regime-aware reports. Output: evaluation view.
  Acceptance: costs included. Non-goals: metric-only promotion.
- P17.D - Audit API. Purpose: expose records by capability. Tasks: add filters
  and pagination. Output: audit endpoint. Acceptance: viewer sees only allowed
  summary. Non-goals: sensitive logs to viewers.
- P17.E - UI surfaces. Purpose: show reports and audit. Tasks: add mobile
  summary and admin detail views. Output: report UI. Acceptance: owner can
  inspect evidence. Non-goals: public dashboard.
- P17.F - Validation. Purpose: prove audit and report integrity. Tasks: tests
  for critical events, filters, and report math. Output: validation report.
  Acceptance: emergency and permission denials are auditable. Non-goals:
  compliance claims.

### Phase 18. Viewer experience hardening

Outcome: Padre and Zio have a calm, clear observer experience without access to
controls that mutate state.

- P18.A - Viewer journey review. Purpose: map daily viewer use. Tasks: inspect
  Home, Treasury, PnL, News, Alerts, and Runtime. Output: journey checklist.
  Acceptance: viewers can understand status. Non-goals: owner controls.
- P18.B - Lock copy. Purpose: make locked actions understandable. Tasks: write
  clear reasons such as viewer account, live disabled, risk locked. Output:
  copy system. Acceptance: no confusing dead buttons. Non-goals: security by
  copy.
- P18.C - Sensitive data filter. Purpose: prevent accidental exposure. Tasks:
  audit API responses and UI fields. Output: viewer-safe data map. Acceptance:
  sensitive logs hidden. Non-goals: hiding permitted data.
- P18.D - Alert tuning. Purpose: show useful alerts without noise. Tasks:
  categorize alerts for viewer relevance. Output: alert policy. Acceptance:
  severe states visible. Non-goals: notification spam.
- P18.E - Device and session UX. Purpose: make access reliable. Tasks: review
  login, trusted device, session expiry. Output: UX fixes. Acceptance: viewer
  access is predictable. Non-goals: public signup.
- P18.F - Validation. Purpose: prove viewer cannot mutate. Tasks: permission
  tests and UI tests. Output: validation report. Acceptance: every mutating API
  denies viewer. Non-goals: new roles.

### Phase 19. Shadow exchange mode

Outcome: drmlke can read or mirror exchange-like market/account context without
placing real orders.

- P19.A - Exchange decision. Purpose: choose first exchange or data venue.
  Tasks: review public data, account read needs, pairs, and fees. Output:
  decision record. Acceptance: no secret committed. Non-goals: live trading.
- P19.B - Read-only adapter. Purpose: connect safely if approved. Tasks:
  implement public or read-only calls with env-only secrets if needed. Output:
  adapter. Acceptance: no withdrawal scope. Non-goals: order placement.
- P19.C - Shadow mapping. Purpose: map paper orders to hypothetical venue
  behavior. Tasks: compare fills to venue prices and fees. Output: shadow
  records. Acceptance: no real orders sent. Non-goals: trading.
- P19.D - Secret handling. Purpose: protect credentials if read-only keys are
  used. Tasks: env outside repo, redaction, no client exposure. Output: secret
  policy. Acceptance: scans find no keys. Non-goals: custody.
- P19.E - Risk comparison. Purpose: compare paper assumptions to venue reality.
  Tasks: analyze spread, slippage, availability. Output: comparison report.
  Acceptance: differences are visible. Non-goals: promotion to live.
- P19.F - Validation. Purpose: prove shadow cannot trade. Tasks: tests and
  adapter scope checks. Output: validation report. Acceptance: no order endpoint
  exists. Non-goals: live gate.

### Phase 20. Manual micro-live gate, future only

Outcome: a future reviewed path may allow manual, tiny, explicitly approved
live actions after legal, risk, and safety review.

- P20.A - Legal and scope review. Purpose: confirm private family boundary.
  Tasks: review intended behavior and regulatory implications. Output: review
  record. Acceptance: approval exists before work. Non-goals: public service.
- P20.B - Gate design. Purpose: define live enable conditions. Tasks: specify
  global locks, owner confirmations, capital ceiling, and rollback. Output:
  gate spec. Acceptance: disabled by default. Non-goals: automation.
- P20.C - Adapter design. Purpose: design minimal order adapter. Tasks: define
  order types, venue, limits, and error handling. Output: adapter spec.
  Acceptance: no withdrawals. Non-goals: margin.
- P20.D - Manual approval UI. Purpose: owner-only approval. Tasks: design
  confirmation, risk summary, and audit. Output: approval flow. Acceptance:
  viewer denied. Non-goals: autonomous approval.
- P20.E - Dry-run and kill switch. Purpose: prove safety before real use.
  Tasks: simulate live path, emergency stop, disable controls. Output: dry-run
  report. Acceptance: kill switch works. Non-goals: repeated live trading.
- P20.F - Validation. Purpose: prove gate discipline. Tasks: tests, secrets
  scan, audit review, owner signoff. Output: validation report. Acceptance:
  capital ceiling enforced. Non-goals: auto-live.

### Phase 21. Desktop console / Tauri Studio, future

Outcome: a richer desktop owner console may exist after core runtime and web
surfaces are mature.

- P21.A - Timing review. Purpose: decide whether desktop is worth building.
  Tasks: review web console gaps and operator needs. Output: decision record.
  Acceptance: clear reason to proceed. Non-goals: premature app.
- P21.B - Tauri scaffold. Purpose: create lightweight desktop shell. Tasks:
  initialize Tauri and TypeScript UI. Output: desktop app. Acceptance: opens and
  talks to API. Non-goals: local secrets.
- P21.C - Strategy lab UI. Purpose: improve research workflow. Tasks: build
  richer charts, tables, and inspectors. Output: lab surface. Acceptance:
  owner can inspect backtests. Non-goals: trading.
- P21.D - Data lake browser. Purpose: inspect stored data. Tasks: add safe
  browser for candles, features, reports. Output: browser. Acceptance:
  read-only by default. Non-goals: direct DB mutation.
- P21.E - Packaging. Purpose: package for local machine. Tasks: sign or package
  as appropriate. Output: desktop build. Acceptance: no secrets included.
  Non-goals: public app store.
- P21.F - Validation. Purpose: verify desktop safety. Tasks: API permission
  tests and packaged build checks. Output: validation report. Acceptance:
  desktop cannot bypass API. Non-goals: mobile replacement.

### Phase 22. Limited auto-live, future only

Outcome: only after extensive evidence and review, a limited automated live path
could be considered. This is intentionally far away.

- P22.A - Evidence review. Purpose: decide whether auto-live is even justified.
  Tasks: review paper history, shadow history, drawdown, risk, and legal scope.
  Output: go or no-go record. Acceptance: explicit approval required.
  Non-goals: assuming this will happen.
- P22.B - Live policy. Purpose: define strict automatic limits. Tasks: set
  capital ceiling, asset universe, frequency, max loss, and kill switch. Output:
  policy. Acceptance: safer than manual path. Non-goals: leverage.
- P22.C - Adapter hardening. Purpose: make execution robust. Tasks: handle
  idempotency, retries, exchange errors, reconciliation. Output: hardened
  adapter. Acceptance: failures are safe. Non-goals: withdrawals.
- P22.D - Monitoring. Purpose: watch live behavior constantly. Tasks: add
  alerts, logs, metrics, and emergency paths. Output: monitoring. Acceptance:
  severe issues stop runtime. Non-goals: silent automation.
- P22.E - Phased rollout. Purpose: start with tiny limits if approved. Tasks:
  run controlled sessions and review after each. Output: rollout records.
  Acceptance: owner review after every session. Non-goals: unattended growth.
- P22.F - Validation. Purpose: prove strict controls. Tasks: scenario tests,
  failure injection, audit review, secret scan. Output: validation report.
  Acceptance: auto-live can be disabled instantly. Non-goals: public fund
  management.

## 22. DOCS.SPINE.3 Wave Detail

Previous spine wave:

`DOCS.SPINE.3 - complete master spine before new implementation`

Purpose:

- Review current roadmap.
- Expand missing sections.
- Correct sequencing.
- Stop inventing new scope before the document is complete.
- Make future waves executable.

Allowed:

- `docs/drmlke-roadmap.md`.
- README link or status if needed.
- AGENTS guidance if needed.
- `docs/environment.md` if needed.
- `docs/deployment.md` if needed.

Forbidden:

- Code implementation.
- Spark deploy.
- Mac setup execution.
- Model downloads.
- Client scaffold.
- Trading logic.
- Wallet custody.
- Exchange keys.

Acceptance:

- Roadmap is self-contained.
- Historical next sequence at the time of this wave was docs, then MacBook,
  then Tailscale, then Spark. `DOCS.REVIEW.1` supersedes that active sequence
  with Product Core before Spark.
- Treasury model is correct.
- Account and capability model is correct.
- Interface surfaces are clear.
- Strategy and algorithm sections are detailed.
- Every phase has sub-waves.
- Delivery rules are explicit.
- Open decisions are captured.
- Commit is created.

Validation for this wave:

```sh
git status --short
git diff --check
make doctor
make check
```

Spark checks are not required in this wave.

Commit message:

`DOCS.SPINE.3: complete master spine and correct next sequence`

Expected final report:

- files changed
- validation results
- commit hash
- whether `docs/drmlke-roadmap.md` was fully expanded
- historical next wave at the time of `DOCS.SPINE.3`: `MAC.SETUP.1`

## 23. Historical Closeout and Review Records

Historical closeout:

`MAC.SETUP.1-CLOSE - finalize MacBook development node`

Purpose:

- Record the MacBook as a secondary active development node.
- Push `82f8fae DOCS.SPINE.3` to GitHub.
- Verify Node 24, `uv`, `pnpm`, git, vim, VS Code, and Docker-compatible
  runtime access.
- Run `make doctor`.
- Run `make check`.
- Run the provider locally through Docker Compose.
- Do not deploy Spark yet.

Completed checks:

- M1.A toolchain check. Purpose: check installed tools. Tasks: inspect git,
  vim, Python, `uv`, Node, corepack, pnpm, Docker, VS Code, and Tailscale.
  Output: tool status. Acceptance: missing tools listed. Non-goals: Spark.
- M1.B repo clone. Purpose: create local checkout. Tasks: clone remote, inspect
  branch, inspect remote. Output: MacBook repo. Acceptance: git status clean.
  Non-goals: edits.
- M1.C Node 24, corepack, and pnpm. Purpose: align JavaScript toolchain. Tasks:
  choose version manager, activate Node 24, enable corepack, verify pnpm.
  Output: JS tools ready. Acceptance: Node returns v24.x. Non-goals: client
  scaffold.
- M1.D uv and Python setup. Purpose: align Python toolchain. Tasks: verify
  Python 3.12, install or configure `uv`, run sync. Output: Python workspace.
  Acceptance: `uv sync --dev` succeeds. Non-goals: dependency changes.
- M1.E Docker runtime optional check. Purpose: decide if Docker is required now.
  Tasks: inspect Docker and Compose availability. Output: Docker status.
  Acceptance: doctor passes or records missing Docker. Non-goals: Spark
  containers.
- M1.F make doctor and make check. Purpose: validate repo. Tasks: run required
  Make targets. Output: check report. Acceptance: checks pass or blockers are
  documented. Non-goals: feature implementation.
- M1.G VS Code open and roadmap review. Purpose: confirm practical editing.
  Tasks: open repo in VS Code, inspect roadmap, confirm workflow. Output:
  editor-ready state. Acceptance: roadmap can be edited on MacBook. Non-goals:
  client implementation.

Closeout acceptance:

- `origin/main` includes `82f8fae DOCS.SPINE.3`.
- `main` is synced with `origin/main` after the closeout commit is pushed.
- MacBook Node is `v24.16.0`.
- MacBook pnpm is `10.12.1`.
- MacBook uv is `0.11.17`.
- Docker-compatible runtime is available through OrbStack.
- Local provider health returns ok with live trading disabled.
- Local provider models returns an empty list.
- Spark remains intentionally untouched.

Historical Linux closeout:

`LINUX.SETUP.1 - Canonical Linux Development Node`

Purpose:

- Establish `/home/mothx/computer-science/projects/drmlke` as the canonical
  Linux workspace.
- Replace stale legacy Linux workspace references.
- Record Linux provider stub status without changing provider behavior.
- Keep MacBook documented as secondary.
- Keep Spark untouched.

Completed checks:

- L1.A documentation audit. Purpose: find stale Linux workspace path
  references. Tasks: inspect README and `docs/`. Output: stale path list.
  Acceptance: the legacy Linux workspace path is no longer used as canonical
  path.
  Non-goals: code changes.
- L1.B environment status. Purpose: record the Linux node as the canonical
  development node. Tasks: document repo path, provider status, port, and local
  verification commands. Output: Linux status section. Acceptance: commands are
  explicit and reproducible. Non-goals: Docker behavior changes.
- L1.C provider verification. Purpose: confirm current local provider state.
  Tasks: inspect Compose status and call health/model endpoints. Output:
  provider status. Acceptance: provider remains stub-only, live trading is
  false, and models are empty. Non-goals: real provider, model downloads,
  trading, credentials, or Spark deployment.

Closeout acceptance:

- Canonical Linux path is `/home/mothx/computer-science/projects/drmlke`.
- `main` is aligned with `origin/main` before this documentation edit.
- `make doctor` passes on Linux.
- `make check` passes on Linux.
- Docker Compose provider is running on port `8781`.
- Local provider health returns ok with live trading disabled.
- Local provider models returns an empty list.
- Spark remains intentionally untouched.

Completed review wave:

`DOCS.REVIEW.1 - Product, Decision, Math, and Strategy Hardening`

Purpose:

- Refocus the roadmap away from infrastructure-first execution.
- Establish product thesis and target outcome.
- Define decision quality doctrine.
- Define mathematical minimums for small-capital strategy evaluation.
- Define strategy specification and backtest integrity requirements.
- Define MVP sequence.
- Move Tailscale and Spark behind the product core path.

Completed tasks:

- D1.A product thesis. Purpose: clarify that drmlke is not an auto-trading
  product. Tasks: define decision-journal and paper-treasury product thesis.
  Output: product thesis and target outcome. Acceptance: small private treasury
  learning, discipline, auditability, and capital preservation are explicit.
  Non-goals: trading implementation.
- D1.B expansion discipline. Purpose: separate core product, research,
  operator, and live extension zones. Tasks: define which zones may follow
  which prerequisites. Output: expansion discipline. Acceptance: research and
  live work cannot outrun core data, benchmarks, risk, and paper evidence.
  Non-goals: model downloads.
- D1.C decision quality spine. Purpose: separate process quality, information
  quality, risk compliance, and economic outcome. Tasks: define decision record
  fields and metrics. Output: decision doctrine. Acceptance: good losing
  decisions and bad winning decisions can be distinguished. Non-goals: journal
  implementation.
- D1.D mathematical spine. Purpose: make costs and small-capital math primary.
  Tasks: define returns, volatility, drawdown, expectancy, benchmarks, fee
  drag, slippage drag, and break-even constraints. Output: math minimums.
  Acceptance: after-cost results govern promotion. Non-goals: metric code.
- D1.E strategy and backtest integrity. Purpose: standardize strategy specs and
  reject biased backtests. Tasks: define strategy template, promotion criteria,
  deprecation criteria, and integrity rules. Output: strategy hardening.
  Acceptance: no strategy can be promoted without benchmark, cost, regime, and
  leakage checks. Non-goals: strategy implementation.
- D1.F MVP sequence. Purpose: define narrow MVPs before runtime infrastructure.
  Tasks: define MVP 1, MVP 2, MVP 3 and the product core path. Output: sequence
  update. Acceptance: `P0.G`, `P0.H`, `P0.I`, `P0.J`, `P0.K`, `P0.L`, and
  `P0.M` precede Spark runtime work. Non-goals: Spark activation.

Closeout acceptance:

- Product thesis is explicit.
- Target users and target outcomes are explicit.
- Expansion discipline is explicit.
- Decision quality record fields and metrics are explicit.
- Mathematical spine covers returns, volatility, drawdown, costs, expectancy,
  benchmark-relative results, and small-capital constraints.
- Strategy spec template is explicit.
- Backtest integrity rules are explicit.
- MVP sequence is explicit.
- Spark remains untouched.
- No application code changes are required.

Completed review wave:

`DOCS.REVIEW.2 - MVP, Promotion Gates, and Risk Policy Numeric Draft`

Purpose:

- Convert `DOCS.REVIEW.1` doctrine into candidate paper-mode numbers.
- Define the exact `MVP.1` cut.
- Draft initial decision cadence and timeframe rules.
- Draft conservative fee, spread, slippage, rounding, and break-even
  assumptions.
- Draft conservative strategy limits.
- Draft promotion and rejection gates.
- Draft paper-mode risk policy.
- Keep manual live locked.
- Keep Spark and Tailscale reserved for later infrastructure work.

Completed tasks:

- D2.A MVP cut. Purpose: make `MVP.1` implementable. Tasks: define 200 EUR
  paper treasury, BTC/ETH only, paper ledger, market data boundary, benchmarks,
  decision records, veto records, and weekly report. Output: exact MVP cut.
  Acceptance: no ML, LLM, Spark dependency, live trading, exchange integration,
  or credentials are included. Non-goals: implementation.
- D2.B outcome and cadence. Purpose: make decision behavior conservative.
  Tasks: define primary outcome, weekly review, maximum decisions, maximum
  simulated trades, and cool-off rules. Output: cadence draft. Acceptance:
  high-frequency, scalping, and same-day overtrading are out of scope.
  Non-goals: scheduler code.
- D2.C timeframe and stale data. Purpose: define initial timeframes and data
  freshness rules. Tasks: define 1d primary, 4h context, 1w regime context, and
  stale thresholds. Output: timeframe policy. Acceptance: stale data decisions
  are marked or vetoed. Non-goals: data collector code.
- D2.D cost model. Purpose: force conservative after-cost evaluation. Tasks:
  draft fee, spread, slippage, rounding, minimum size, and break-even
  assumptions. Output: cost model draft. Acceptance: all values are
  placeholders and not exchange-specific truth. Non-goals: real provider.
- D2.E conservative strategy and risk policy. Purpose: bound paper behavior.
  Tasks: define exposure, turnover, drawdown, trade count, loss locks, veto
  rules, and delay rules. Output: paper-mode risk draft. Acceptance: risk
  policy remains a boundary and does not enable live mode. Non-goals: risk
  engine code.
- D2.F promotion and rejection gates. Purpose: define what evidence is required
  before strategy advancement. Tasks: define gates for `backtest_ready`,
  `backtested`, `paper_enabled`, rejection, deprecation, and future manual-live
  review evidence. Output: promotion gate draft. Acceptance: passing paper
  gates does not automatically enable live trading. Non-goals: live gate.

Closeout acceptance:

- `MVP.1` exact cut is explicit.
- Primary product outcome is explicit.
- Initial decision cadence is explicit.
- Initial timeframe policy is explicit.
- Cost model assumptions are explicit and conservative.
- Conservative strategy numeric definition is explicit.
- Promotion gates are explicit.
- Rejection and deprecation gates are explicit.
- Paper-mode risk policy draft is explicit.
- Minimum paper duration before manual live consideration is explicit.
- Spark remains untouched.
- No application code changes are required.

Completed Phase 0 wave:

`P0.H - Identity, Capabilities, and Paper Treasury Boundary`
(legacy alias: `CORE.0`)

Purpose:

- Implement identity, account roles, capabilities, and the one-paper-treasury
  boundary required before ledger or decision records mutate state.
- Keep the implementation narrow and paper-only.
- Preserve server-side permission enforcement as the real security boundary.
- Keep Spark reserved until the Product Core path no longer depends on local
  identity, treasury, benchmark, and decision objects.

Completed tasks:

- C0.A identity contracts. Purpose: define user and actor identity primitives.
  Tasks: add `UserId`, `UserProfile`, and actor metadata contracts. Output:
  typed core identity contracts. Acceptance: no authentication or session
  storage is introduced. Non-goals: login implementation.
- C0.B role and capability policy. Purpose: define initial authority. Tasks:
  add roles, capability names, deterministic role defaults, and global locks.
  Output: role/capability policy. Acceptance: viewers cannot mutate treasury,
  runtime, risk, strategy, user, device, or exchange state. Non-goals: API
  routes.
- C0.C safety locks. Purpose: preserve bootstrap safety. Tasks: add global
  safety lock contract for live trading, withdrawals, wallet custody, exchange
  credentials, model override, UI lock doctrine, and server-side enforcement.
  Output: safety lock contract. Acceptance: unsafe lock combinations fail fast.
  Non-goals: runtime state store.
- C0.D paper treasury boundary. Purpose: enforce the single treasury model.
  Tasks: add one-paper-treasury boundary with 200 EUR paper capital and 0 EUR
  live capital. Output: treasury boundary contract. Acceptance: multiple
  treasuries and per-person portfolios are rejected. Non-goals: ledger entries.
- C0.E tests. Purpose: prove the authority and treasury boundary. Tasks: add
  tests for owner, viewer, admin, live locks, safety locks, and treasury
  policy. Output: core contract tests. Acceptance: tests pass without Docker,
  Spark, providers, credentials, ledger, market data, strategies, or UI.

Closeout acceptance:

- Role and capability contracts exist.
- Owner/operator has owner/operator paper capabilities.
- Viewer family accounts remain view-only.
- Emergency-only role remains narrow.
- Technical admin role has no trading authority by default.
- Future live and exchange capabilities remain globally locked.
- Global safety locks disable live trading, withdrawals, wallet custody,
  exchange credentials, and model risk override.
- Exactly one 200 EUR paper treasury boundary exists.
- Live capital remains 0 EUR.
- No per-person portfolio split exists.
- No application runtime, Docker, Spark, Tailscale, provider, persisted ledger,
  market data, strategy, backtest, paper execution, UI, or auth/session storage
  is introduced.

Completed Phase 0 wave:

`P0.I - Append-Only Paper Treasury Ledger`
(legacy alias: `CORE.1`)

Purpose:

- Implement the append-only paper ledger on top of the `P0.H` identity,
  capability, safety, and paper treasury boundary.
- Preserve exactly one paper treasury.
- Keep live capital at 0 EUR.
- Keep all future real-money behavior locked.

Allowed changes:

- Add typed paper ledger domain contracts under `packages/core`.
- Export safe ledger contracts from `drmlke_core`.
- Add tests for append-only behavior, owner authority, viewer/admin denial,
  treasury id checks, sequence checks, duplicate initial-capital rejection, zero
  amount rejection, and correction-by-compensating-entry behavior.
- Update roadmap and architecture documentation.

Forbidden changes:

- No persistence.
- No database schema.
- No API enforcement.
- No paper orders or fills.
- No market data.
- No trading logic.
- No strategy engine.
- No Spark or Tailscale work.
- No exchange, broker, wallet custody, withdrawal, credential, or model runtime
  work.

Implementation contracts:

- `LedgerEntryId` and `LedgerSequence` type aliases.
- `LedgerEntryType` paper-only entry categories.
- `LedgerEntry` frozen domain contract.
- `PaperLedger` frozen in-memory ledger contract.
- `create_initial_paper_ledger`.
- `append_paper_ledger_entry`.
- `project_paper_cash_balance_eur`.
- `validate_paper_ledger`.

Acceptance criteria:

- Initial paper ledger contains exactly one 200 EUR initial capital entry.
- Ledger uses the canonical paper treasury id.
- Ledger mode remains paper.
- Live capital remains 0 EUR through the treasury boundary.
- Only owner/operator authority can append ledger-changing entries.
- Viewer family and admin technical roles cannot append entries.
- Appends require the next sequence and return a new ledger object.
- Duplicate initial capital entries are rejected.
- Zero amount entries are rejected.
- Corrections change projected balance through a new entry, not mutation.
- Existing `P0.H` capability, safety, and treasury tests still pass.

Completed Phase 0 wave:

`P0.J - Ledger Projection and Treasury Snapshot`
(legacy alias: `CORE.2`)

Purpose:

- Add a deterministic read-side projection over the append-only paper ledger.
- Produce a paper treasury snapshot for future UI, risk, reporting, and paper
  execution work.
- Keep projection pure, in-memory, and separate from storage, API routes,
  positions, market data, strategy logic, and execution.

Previous state:

- `P0.H` defined identity, safety, and the one-paper-treasury boundary.
- `P0.I` defined append-only paper ledger entries and owner-only append
  authority.
- Ledger cash projection existed only as a simple summed cash helper.

Target state:

- The system can answer current paper available cash.
- The system can answer reserved cash.
- The system can answer total cash.
- The system can answer total recorded fees.
- The system can answer net adjustments and net corrections.
- The system can answer ledger entry count and last sequence.
- The system can prove the snapshot reconciles.

Allowed changes:

- Add `packages/core/src/drmlke_core/treasury_projection.py`.
- Export stable snapshot/projection contracts from `drmlke_core`.
- Extend core tests for projection behavior and invariants.
- Update roadmap and architecture documentation.

Forbidden changes:

- No persistence.
- No database schema.
- No API routes.
- No paper orders or fills.
- No paper positions.
- No market data.
- No market valuation.
- No trading logic.
- No strategy decisions.
- No provider, Docker, Spark, or Tailscale changes.
- No exchange, broker, wallet custody, withdrawal, credential, or model runtime
  work.

Implementation contracts:

- `PaperTreasurySnapshot`.
- `project_paper_treasury_snapshot`.
- `validate_paper_treasury_snapshot`.
- `is_paper_treasury_snapshot_reconciled`.

Validation requirements:

- Snapshot projection validates the ledger first.
- Projection rejects negative available cash.
- Projection rejects negative reserved cash.
- Projection rejects unreconciled total cash.
- Projection rejects release entries that exceed reserved cash.
- Projection preserves fee cost as a positive absolute cost.
- Projection keeps live capital locked at 0 EUR.
- Projection remains paper-only.

Acceptance criteria:

- Initial snapshot shows 200 EUR available cash, 0 EUR reserved cash, and
  200 EUR total cash.
- Fee entries reduce available cash and increase positive total fees.
- Reserve entries move available cash to reserved cash without changing total
  cash.
- Release entries move reserved cash back to available cash without changing
  total cash.
- Adjustments and corrections affect available cash through ledger entries.
- Snapshot reports ledger entry count and last sequence.
- Snapshot is immutable.
- Snapshot exposes no positions or market valuation fields.
- Existing `P0.H` and `P0.I` tests still pass.

Completed Phase 0 wave:

`P0.K - Paper Position Boundary`
(legacy alias: `CORE.3`)

Purpose:

- Define paper position domain contracts before market data, valuation, order,
  fill, strategy, or execution work.
- Represent simulated BTC/ETH long-only exposure without implying custody,
  exchange execution, live backing, or real asset ownership.
- Keep position contracts pure, in-memory, and separate from ledger mutation,
  treasury cash projection, storage, API routes, and runtime services.

Previous state:

- `P0.H` defined identity, safety, and the one-paper-treasury boundary.
- `P0.I` defined append-only paper ledger entries.
- `P0.J` projected ledger entries into a treasury cash snapshot.
- No paper position contract existed.

Target state:

- A paper position has a canonical treasury id.
- A paper position has an initial BTC/ETH asset boundary.
- A paper position is paper-only and not live-backed.
- A paper position is long-only.
- A paper position has positive quantity, positive average entry price,
  positive cost basis, and nonnegative fees.
- Cost basis is quantity times average entry price plus fees.
- A paper position book can group positions and summarize open cost basis and
  total fees without valuation or PnL.

Allowed changes:

- Add `packages/core/src/drmlke_core/position.py`.
- Export stable paper position contracts from `drmlke_core`.
- Extend core tests for position validation, asset boundary, position book, and
  non-goals.
- Update roadmap and architecture documentation.

Forbidden changes:

- No persistence.
- No database schema.
- No API routes.
- No paper orders or fills.
- No ledger mutation.
- No treasury cash mutation.
- No market data.
- No market valuation.
- No realized or unrealized PnL.
- No trading logic.
- No strategy decisions.
- No provider, Docker, Spark, or Tailscale changes.
- No exchange, broker, wallet custody, withdrawal, credential, or model runtime
  work.

Implementation contracts:

- `AssetSymbol`.
- `PaperPositionId`.
- `PaperPositionSide`.
- `PaperPositionStatus`.
- `PaperPosition`.
- `PaperPositionBook`.
- `INITIAL_PAPER_POSITION_ASSETS`.
- `normalize_asset_symbol`.
- `is_initial_paper_position_asset`.
- `validate_initial_paper_position_asset`.
- `validate_paper_position`.
- `validate_paper_position_book`.
- `create_open_paper_position`.
- `open_paper_positions`.
- `closed_paper_positions`.
- `total_open_cost_basis_eur`.
- `total_position_fees_eur`.

Validation commands:

- `git diff --check`.
- `uv run pytest -q tests/test_core_contracts.py`.
- `make doctor`.
- `make check`.
- `docker compose ps`.
- `curl -sS http://127.0.0.1:8781/health`.
- `curl -sS http://127.0.0.1:8781/models`.

Acceptance criteria:

- Asset symbols normalize deterministically.
- Empty or malformed symbols are rejected.
- Initial paper position assets are BTC and ETH only.
- Unsupported assets such as DOGE or AAPL are rejected.
- Valid open paper positions use the canonical treasury id.
- Positions are paper-only and not live-backed.
- Positions are long-only.
- Quantity, average entry price, and cost basis must be positive.
- Fees must be nonnegative.
- Position contracts are frozen.
- Position books reject duplicate position ids and mixed treasury ids.
- Open cost basis totals only open positions.
- Position contracts expose no market valuation or PnL fields.
- Existing `P0.H`, `P0.I`, and `P0.J` tests still pass.

Completed Phase 0 wave:

`P0.L - Paper Portfolio Snapshot Boundary`
(legacy alias: `CORE.4`)

Purpose:

- Combine the `P0.J` treasury cash snapshot and the `P0.K` paper position
  book into one structural paper portfolio snapshot.
- Keep the snapshot pure, in-memory, paper-only, and free of market prices,
  PnL, orders, fills, execution, storage, API routes, UI, and runtime services.
- Make future client/risk/reporting work consume a single structural read model
  without inventing cash movement or market valuation.

Previous state:

- `P0.J` could describe paper cash state.
- `P0.K` could describe paper positions.
- No combined portfolio read model existed.

Target state:

- A paper portfolio snapshot has the canonical treasury id.
- A paper portfolio snapshot exposes available cash, reserved cash, and total
  cash from the treasury snapshot.
- A paper portfolio snapshot exposes open and closed position counts.
- A paper portfolio snapshot exposes open cost basis and total position fees.
- A paper portfolio snapshot exposes structural exposure and open cost basis
  ratio.
- A paper portfolio snapshot remains paper-only and live-capital locked.
- A paper portfolio snapshot proves deterministic reconciliation.

Allowed changes:

- Add `packages/core/src/drmlke_core/portfolio.py`.
- Export stable portfolio snapshot contracts from `drmlke_core`.
- Extend core tests for portfolio projection, ratio, reconciliation, and
  non-goals.
- Update roadmap and architecture documentation.

Forbidden changes:

- No persistence.
- No database schema.
- No API routes.
- No UI/client.
- No paper orders or fills.
- No ledger mutation.
- No treasury cash mutation.
- No market data.
- No market valuation.
- No realized or unrealized PnL.
- No returns or performance metrics.
- No trading logic.
- No strategy decisions.
- No provider, Docker, Spark, or Tailscale changes.
- No exchange, broker, wallet custody, withdrawal, credential, or model runtime
  work.

Implementation contracts:

- `PaperPortfolioSnapshot`.
- `project_paper_portfolio_snapshot`.
- `validate_paper_portfolio_snapshot`.
- `is_paper_portfolio_snapshot_reconciled`.
- `calculate_open_cost_basis_ratio`.

Validation commands:

- `git diff --check`.
- `uv run pytest -q tests/test_core_contracts.py`.
- `make doctor`.
- `make check`.
- `docker compose ps`.
- `curl -sS http://127.0.0.1:8781/health`.
- `curl -sS http://127.0.0.1:8781/models`.

Acceptance criteria:

- Empty portfolio snapshot shows 200 EUR cash, no positions, zero open cost
  basis, zero position fees, zero open cost basis ratio, and reconciled true.
- One open BTC position contributes open cost basis and open cost basis ratio.
- Closed positions count as closed and contribute to total position fees, but
  not open cost basis.
- Treasury id mismatches are rejected.
- Live-backed positions are rejected.
- Non-reconciled treasury snapshots are rejected.
- Portfolio snapshots are frozen.
- Portfolio snapshots expose no market value, PnL, return, or strategy
  attribution fields.
- Existing `P0.H`, `P0.I`, `P0.J`, and `P0.K` tests still pass.

Completed closeout wave:

`P0.CLOSE - Phase 0 Product Core Closeout`

Purpose:

- Verify that `P0.H` through `P0.M` are coherent as one Phase 0 product-core
  foundation.
- Confirm that identity, safety, treasury, ledger, treasury projection, paper
  position, paper portfolio, and paper decision record boundaries remain
  separated.
- Confirm that no market data, persistence, API, strategy, execution, Spark,
  Tailscale, exchange, wallet custody, or model runtime behavior has leaked
  into the product core.

Previous state:

- `P0.M` completed the first paper decision record boundary.
- Phase 0 product-core domain contracts now cover authority, treasury state,
  paper accounting primitives, paper exposure, structural portfolio snapshots,
  and decision memory.

Target state:

- Phase 0 product-core foundation is declared coherent or any remaining
  inconsistency is explicitly listed.
- Roadmap and architecture docs reflect that `P0.M` is completed.
- The next canonical wave is chosen from the roadmap instead of invented.

Allowed changes:

- Documentation updates to this roadmap and architecture.
- No feature implementation.

Forbidden changes:

- No market data ingestion.
- No strategy engine.
- No paper execution.
- No orders or fills.
- No API routes.
- No database schema or persistence.
- No client/UI.
- No provider, Spark, Tailscale, exchange, broker, wallet custody, withdrawal,
  credential, or model runtime work.

Acceptance criteria:

- `P0.H` through `P0.M` are present in `packages/core`.
- Tests still pass.
- The product core remains pure in-memory domain logic.
- No forbidden runtime, trading, storage, API, or UI behavior is introduced.
- The next recommended canonical wave is documented as roadmap-derived.

## 24. Open Decisions

Current open decisions:

- Whether `DOCS.REVIEW.2` candidate thresholds need revision after the first
  paper reports.
- Whether the primary benchmark should remain buy-and-hold plus scheduled
  accumulation after first data-source selection.
- Whether BTC/ETH should use EUR pairs directly or normalized quote conversion
  if the first data source is stronger in USDT.
- Whether stale-data thresholds need adjustment after real feed behavior is
  observed.
- Whether the minimum 90-day paper observation candidate is too short, too long,
  or sufficient before any later manual-live review.
- Whether the MacBook Docker runtime remains OrbStack long-term or later moves
  to Docker Desktop.
- Tailscale hostname or address for Spark.
- Final Spark access route.
- Final provider backend.
- Final embedding model.
- Final sentiment model.
- First exchange or public source for market data.
- First trading pair notation: EUR or USDT.
- Client framework: SvelteKit or React.
- Web admin and mobile shared UI strategy.
- Tauri desktop timing.
- Auth method: passkey, PIN, password fallback, or a staged combination.
- Notification strategy.
- Backup cadence.
- Paper treasury initial strategy order.
- Whether the Linux workstation also needs Tailscale as a first-class path.
- Whether Spark provider ports bind to localhost behind a private proxy or bind
  directly to a Tailscale interface.
- Whether analytical feature storage starts in SQLite, DuckDB, Parquet, or a
  staged combination.

Open decision rule:

If a detail is not decided, keep it here. Do not write it elsewhere as a final
decision until the relevant wave makes and records the decision.

## 25. Change Log

- `BOOTSTRAP.0`: repo skeleton and provider stub.
- `DOCS.SPINE.2`: treasury model correction and initial expanded spine.
- `DOCS.SPINE.3`: full master spine completion before further implementation,
  with next sequence corrected to docs, MacBook, Tailscale, and Spark runtime.
- `MAC.SETUP.1-CLOSE`: MacBook recorded as a secondary active development node,
  `DOCS.SPINE.3` pushed to GitHub, local toolchain validated, and provider
  stub verified locally without touching Spark.
- `LINUX.SETUP.1`: Linux workstation recorded as the canonical development
  node, legacy path references removed, provider stub status documented, and
  Spark left untouched.
- `DOCS.REVIEW.1`: roadmap refocused on product thesis, decision quality,
  small-capital math, strategy specification, backtest integrity, MVP sequence,
  and Product Core before Spark.
- `DOCS.REVIEW.2`: `MVP.1` exact cut, candidate paper-mode cost assumptions,
  conservative strategy limits, promotion gates, rejection gates, risk policy
  draft, and minimum paper duration before any manual-live review.
- `CORE.0`: typed identity, role, capability, global safety lock, and
  one-paper-treasury boundary contracts, with tests and no runtime expansion.
- `CORE.1`: append-only paper ledger domain contracts for the single 200 EUR
  paper treasury, with no persistence, API route, paper execution, exchange, or
  wallet custody behavior.
- `CORE.2`: ledger projection and paper treasury snapshot contracts, with
  available cash, reserved cash, fee, correction, sequence, and reconciliation
  read models and no persistence, positions, market data, execution, provider,
  exchange, or wallet custody behavior.
- `CORE.3`: paper position boundary contracts for initial BTC/ETH long-only
  simulated positions, with no persistence, ledger mutation, orders, fills,
  market data, valuation, PnL, execution, provider, exchange, or wallet custody
  behavior.
- `CORE.4`: paper portfolio snapshot boundary contracts combining treasury cash
  snapshots and paper position books, with no persistence, market value, PnL,
  returns, strategy attribution, orders, fills, execution, provider, exchange,
  or wallet custody behavior.
- `P0.M` (legacy alias: `CORE.5`): paper decision record boundary contracts
  for owner-reviewed no-action, watch, action candidate, rejected, postponed,
  and risk-vetoed records, with no execution, strategy engine, market data,
  API, persistence, provider, exchange, or wallet custody behavior.
- `P0.CLOSE`: Phase 0 product-core closeout confirming coherence of `P0.H`
  through `P0.M` before moving toward infrastructure, persistence, API, market
  data, strategy, execution, or UI work.
