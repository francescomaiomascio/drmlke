# drmlke Roadmap and Master Spine

This document is the canonical project spine for drmlke after DOCS.SPINE.2.

## Current Bootstrap Status

- Local repo path: `/home/mothx/code/drmlke`
- Remote: `https://github.com/francescomaiomascio/drmlke.git`
- Bootstrap commit: `e68a51b Bootstrap drmlke skeleton`
- Provider local health: ok
- Provider local models: ok, empty list
- `uv sync --dev`: ok
- `make check`: ok
- Docker base: ok with `--network=host`
- Compose provider build/up: ok
- Provider still active on `localhost:8781`
- Environment issue from bootstrap: `.node-version` required Node 24 while shell used Node 20.19.6 from nvm.
- Current correction: Node 24 alignment is handled in ENV.NODE.SPARK.2; acceptance is `node -v` returning v24.x.
- Spark status: SSH alias `spark` is not currently configured/reachable from this workstation.

## Product Spine

drmlke is a private/family, local-first crypto intelligence, paper-trading, wallet-ledger, and agentic runtime project.

drmlke is not initially:

- a public financial service
- a custodial wallet
- a public fund-management platform
- an exchange
- a live trading bot
- a system that manages public user funds

If drmlke ever becomes a public app/service or manages money for others beyond the private family context, legal and regulatory review becomes mandatory. No legal claim beyond this private/family boundary is assumed.

## Foundational Correction

drmlke is not "three people, three portfolios".

Correct model:

- one managed treasury / account / portfolio
- Francesco is the owner and operator
- Francesco manages runtime, strategy configuration, trading decisions, gates, and risk controls
- Padre and Zio initially have observer accounts
- Padre and Zio can see permitted portfolio/account/runtime state during the day
- Padre and Zio do not trade manually
- Padre and Zio do not manage strategies
- Padre and Zio do not control exchange keys, wallet settings, runtime, risk policy, or live gates

The client is the same product for all users. Different users receive different permissions and capability locks.

## Account and Permission Spine

drmlke uses one shared product interface with capability-based access.

### Roles

1. `owner_operator`

Francesco.

Can:

- configure runtime
- manage strategies
- view all data
- approve future gated actions
- pause and resume runtime
- use emergency controls
- configure accounts, devices, and permissions
- view audit and logs

2. `viewer_family`

Padre and Zio initially.

Can:

- see portfolio state
- see PnL and daily status if allowed
- see current paper/live mode
- see relevant alerts

Cannot:

- change strategies
- approve trades
- change risk limits
- add exchange keys
- access secrets
- start live trading
- modify wallet or treasury settings

3. `emergency_only`, future optional

Can:

- see critical status
- trigger emergency stop if explicitly allowed

Cannot:

- resume trading
- change configuration

4. `admin_technical`, future optional

For technical maintenance if needed. This role does not imply trading authority unless explicitly granted.

### Permission Rules

- UI permissions are capability-driven.
- The API returns both data and allowed actions.
- The UI renders the same screens for all users but disables, locks, or hides actions based on capability.
- Critical actions must be blocked server-side even if a client is modified.
- Disabled UI buttons are not security.
- Every denied action should produce a safe response and may be audited.
- Role changes are owner-only.
- Device trust and session validity are separate from trading permission.

### Capability Model

Initial capabilities:

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

Initial assignment:

- Francesco: all owner/operator capabilities, except future live actions remain locked until live gates exist.
- Padre: `view_treasury`, `view_positions`, `view_pnl`, `view_runtime_status`, `view_news`, `view_alerts`.
- Zio: same as Padre.
- Live trading capabilities: disabled globally.

## Treasury and Capital Spine

Correct capital model:

- Future real capital ceiling: 200 EUR
- Current live capital: 0 EUR
- Current implementation: paper only
- Paper treasury: one simulated 200 EUR treasury
- No per-person trading allocation initially

Rejected obsolete split:

- Francesco 100 EUR
- Padre 50 EUR
- Zio 50 EUR

Replacement model:

- Treasury paper balance: 200 EUR
- Owner/operator: Francesco
- Viewers: Padre, Zio
- Member-specific allocation: not part of initial model
- Contribution accounting: future optional
- Per-strategy ledger: useful
- Per-member trading portfolio: not initial

The system may later record contribution/source metadata, but that is accounting metadata, not independent trading authority.

Capital ownership/accounting model:

- one treasury
- one owner/operator
- multiple viewer accounts
- optional future contribution records
- optional future internal reporting per contributor
- trading strategy decisions apply to the treasury, not to individual family-member strategy accounts

The most useful internal split is not by family member at first. The useful split is by:

- treasury cash
- asset positions
- strategy attribution
- paper/live mode
- realized/unrealized PnL
- fees/slippage
- risk exposure
- audit events

The ledger can still record ownership, source, and contribution metadata later. Trading control remains owner/operator-controlled.

## Public Client / Private Capability Model

The drmlke client may be public/installable, but the runtime data and actions are private.

Client model:

- one app name: drmlke
- one UI codebase
- same screens for all roles
- iPhone and Android packaging later
- account permissions determine available actions
- the client never contains exchange keys
- the client never contains wallet seed/private keys
- the client talks to the Spark/API backend
- the backend enforces all permissions
- Spark/backend remains private and LAN/VPN-controlled unless explicitly changed in the future

Locked actions show clear explanations, for example:

- "Viewer account: action locked"
- "Live trading globally disabled"
- "Owner approval required"
- "Risk engine locked this action"
- "Shadow mode only"

Owner view:

- same app
- all sections visible
- action buttons enabled only when gates allow
- can pause/resume runtime
- can emergency stop
- can inspect strategies
- can inspect risk
- can approve future manual micro-live only after that gate exists

Viewer view:

- same app
- portfolio and status visible
- buttons that mutate state are locked or absent
- can read explanations
- can receive alerts
- cannot approve, trade, configure, or unlock

The UI must not fork into "owner app" and "viewer app". It is one client with role/capability gating.

## Interface Final Shape

### 1. Mobile Client

Purpose:

- daily monitoring
- father/uncle observer access
- owner emergency control
- owner quick approval in future gates

Users:

- Francesco
- Padre
- Zio

Screens:

- Login
- Home
- Treasury
- Positions
- PnL
- Signals
- News
- Runtime
- Risk
- Alerts
- Settings
- Emergency

Home screen should show:

- current mode: paper / shadow / live locked
- treasury value
- today PnL
- open positions
- risk state
- runtime state
- latest important alert
- emergency stop access for permitted users

Treasury screen should show:

- total paper treasury
- cash
- positions
- realized PnL
- unrealized PnL
- fees/slippage
- strategy attribution
- recent ledger entries

Viewer mode:

- same screens
- no mutating actions
- locked controls explain missing permission

### 2. Web Admin Console

Purpose:

- owner control from browser
- LAN/VPN access
- richer than mobile
- not exposed publicly

Sections:

- dashboard
- runtime
- provider
- storage
- strategies
- paper trading
- treasury
- signals
- risk
- news/RAG
- reports
- audit
- users/devices
- settings

### 3. Terminal/Makefile

Purpose:

- development
- deployment
- doctor
- validation
- Spark operations
- migrations and backups later

### 4. VS Code

Purpose:

- source editing
- roadmap editing
- tests
- Codex work
- docs review

### 5. Future Desktop Console

Purpose:

- richer owner dashboard
- strategy lab
- backtest lab
- model registry
- audit timeline
- data lake browser

Technology preference:

- Tauri/Rust shell for lightweight desktop
- TypeScript UI
- talks to Spark API
- no local exchange secrets
- no private keys

Do not implement desktop now. This is a documented direction only.

## Trading Strategy Spine

Capital premise:

- 200 EUR future live ceiling
- paper first
- small capital means fees and spread matter
- overtrading is dangerous
- preservation comes before excitement
- no leverage
- no futures
- no margin
- no low-liquidity assets
- no martingale
- no autonomous LLM trading

Initial paper universe:

- BTC/EUR or BTC/USDT depending exchange/data availability
- ETH/EUR or ETH/USDT depending exchange/data availability
- later high-liquidity large caps only after review

### Strategy Families

1. Buy and hold benchmark

Purpose:

- baseline
- compare every active strategy against doing nothing

2. Scheduled accumulation benchmark

Purpose:

- simple periodic buy simulation
- compare complex timing against a low-complexity family-friendly baseline

3. Trend following

Inputs:

- moving average slope
- multi-timeframe alignment
- volatility
- volume
- liquidity
- regime

Behavior:

- long-only
- spot only
- no shorting
- no leverage
- trade only in paper

4. Mean reversion

Inputs:

- RSI
- Bollinger distance
- rolling z-score
- volatility state
- trend filter

Rules:

- no panic regime
- no stale data
- no illiquid market

5. Volatility breakout

Inputs:

- volatility compression
- ATR expansion
- volume z-score
- breakout level

Rules:

- strict invalidation
- paper-only until enough samples

6. News risk avoidance

Purpose:

- news blocks trades before it creates trades

Inputs:

- sentiment
- severity
- affected assets
- source credibility
- similar events from RAG

7. Portfolio/risk rebalancing

Future only:

- treasury allocation management
- avoid overtrading
- include fees

8. Ensemble decision matrix

Purpose:

- combine strategy scores
- create candidate signal only
- risk engine decides

### Forbidden Early Strategies

- reinforcement learning trading
- scalping
- HFT
- futures
- leverage
- grid/martingale
- meme coin chasing
- autonomous LLM trading
- market making with 200 EUR

### Strategy Promotion Pipeline

Pipeline:

`idea -> specified -> backtest_ready -> backtested -> paper_enabled -> paper_observed -> blocked/deprecated/future_live_candidate`

Promotion requires:

- out-of-sample validation
- walk-forward validation
- realistic fees/slippage
- acceptable drawdown
- stable performance across regimes
- benchmark comparison
- owner review
- risk review
- auditability

## Algorithmic Spine

The following algorithmic layers will be evaluated over time. They are not implemented in the bootstrap.

### Layer 1: Deterministic Features

- log returns
- rolling returns
- realized volatility
- ATR
- RSI
- MACD
- moving average slopes
- Bollinger distance
- volume z-score
- spread/liquidity estimate
- multi-timeframe alignment
- drawdown from local high

### Layer 2: Statistical Baselines

- buy-and-hold
- scheduled accumulation
- simple momentum
- simple mean reversion
- moving average crossover
- EWMA volatility
- rolling z-score
- ARIMA/SARIMAX optional later
- GARCH optional later

### Layer 3: Classical ML

- logistic regression
- random forest
- ExtraTrees
- LightGBM
- XGBoost
- CatBoost
- probability calibration

### Layer 4: Regime Detection

- rule-based regime labels first
- Hidden Markov Models later
- Gaussian Mixture Models
- KMeans on trend/volatility/liquidity
- change point detection later

### Layer 5: Compact Time-Series Models

- TinyTimeMixer / Granite TTM candidate
- TimesFM candidate
- PatchTST candidate
- N-BEATS / N-HiTS candidate
- LSTM/GRU only as simple reference, not main plan

### Layer 6: News/Sentiment

- FinBERT or similar financial sentiment baseline
- entity/asset extraction
- severity classifier
- source credibility
- deduplication

### Layer 7: RAG/Embeddings

- Qwen/BGE/E5 style embeddings to evaluate
- LanceDB initially
- sqlite-vec possible later
- used for news memory, decision memory, backtest memory

### Layer 8: Small LLM

- 3B-4B class local model later if needed
- summarization
- explanations
- RAG Q&A
- report generation
- never order execution

### Layer 9: Risk Model

- fixed fractional sizing
- max exposure
- stale-data veto
- spread/liquidity veto
- news severity veto
- volatility shock veto
- drawdown lock
- manual/emergency lock

### Layer 10: Evaluation/Governance

- chronological splits
- walk-forward
- no leakage
- no lookahead
- fee/slippage
- PnL
- max drawdown
- expectancy
- profit factor
- Sharpe/Sortino with caution
- performance by regime
- model registry

Hard rule: accuracy is not enough. A strategy or model must improve risk-adjusted paper performance after fees, slippage, drawdown, and regime analysis.

## Expanded Delivery Spine

Each wave must be verbose enough to execute without guessing.

Each wave must include:

- wave id
- title
- purpose
- previous state
- target state
- allowed changes
- forbidden changes
- target files
- database changes
- API changes
- UI changes
- runtime changes
- security boundary
- validation commands
- acceptance criteria
- expected completion report
- roadmap update requirement

Each sub-wave must include:

- sub-wave id
- purpose
- tasks
- files
- output
- acceptance
- non-goals

Do not use vague sub-waves. Make every delivery executable.

## Environment Issue: Node Version Alignment

Problem from bootstrap:

- `.node-version` says 24.
- The terminal used Node 20.19.6 via nvm.
- pnpm/corepack environment should be aligned before client work.

Resolution options:

- use nvm to install/use Node 24
- or use mise/fnm later if preferred
- do not install random global npm packages
- do not scaffold client until Node 24 is active

Acceptance:

- `node -v` returns v24.x
- `corepack enable` works
- `pnpm -v` works
- no global npm pollution

Current resolution:

- Node v24.16.0 installed through nvm.
- nvm default alias points to Node 24.
- zsh login environment loads nvm default for terminal commands.
- Corepack and pnpm are available without installing random global npm packages.

## Phase Map

- Phase 0 - Repo, environment, provider skeleton, master spine
- Phase 1 - Spark attachment and provider deployment
- Phase 2 - Node/toolchain alignment and dev ergonomics
- Phase 3 - Identity, accounts, roles, capability model
- Phase 4 - Treasury and paper ledger
- Phase 5 - Mobile/public client shell and permission-locked UI
- Phase 6 - Web admin console shell
- Phase 7 - Runtime control and event bus
- Phase 8 - Market data collector
- Phase 9 - Feature and regime engine
- Phase 10 - Strategy lab and backtesting
- Phase 11 - Paper trading engine
- Phase 12 - News/RAG and sentiment engine
- Phase 13 - Baseline and time-series model lab
- Phase 14 - Decision matrix and risk integration
- Phase 15 - Reporting, audit, and evaluation
- Phase 16 - Family viewer experience hardening
- Phase 17 - Shadow exchange mode
- Phase 18 - Manual micro-live gate, future only
- Phase 19 - Desktop console / Tauri Studio, future
- Phase 20 - Limited auto-live, future only

## Next Wave

### ENV.NODE.SPARK.2 - Node 24 alignment, Spark storage, provider deployment, and master spine correction

Purpose:

- fix Node version mismatch
- prepare Spark storage
- deploy provider stub to Spark if reachable
- rewrite master spine with corrected treasury/account/client model
- keep live trading disabled
- keep wallet custody absent
- keep AI models absent

Allowed:

- docs
- README
- AGENTS
- Makefile
- doctor script
- env examples
- Spark deployment helpers
- Node version setup notes

Forbidden:

- trading logic
- exchange keys
- real wallet
- model downloads
- client scaffold beyond docs unless explicitly requested
- live trading

Validation:

- `node -v` shows v24.x or issue clearly documented
- `make doctor`
- `make check`
- local provider health
- local provider models
- Spark check if reachable
- Spark deploy if reachable
- roadmap updated
- commit created

Commit message:

`DOCS.SPINE.2: correct treasury model and expand master spine`

Final report must include:

- files changed
- validation results
- Node version result
- Spark status
- provider status
- commit hash
- next recommended wave
