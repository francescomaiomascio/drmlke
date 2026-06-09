# Architecture

drmlke bootstrap modules:

- `apps/api`: FastAPI backend placeholder
- `apps/worker`: runtime worker placeholder
- `apps/provider`: local provider stub
- `apps/client`: future SvelteKit/Vite + Capacitor client
- `packages/core`: shared settings and paths
- `packages/storage`: storage placeholder
- `packages/wallet`: wallet/ledger placeholder
- `packages/agents`: agent placeholder
- `packages/risk`: risk placeholder

Bootstrap safety boundaries:

- paper mode only
- no real wallet custody
- no exchange connections
- no live execution
- no AI model inference
