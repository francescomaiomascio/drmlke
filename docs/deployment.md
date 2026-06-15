# Deployment

Initial deployment target is local Linux.

Current sequencing: Product Core comes before Spark runtime. Identity,
capabilities, paper treasury ledger, market data, benchmarks, and the decision
journal must not be delayed by deployment work.

Future Spark deployment should use:

- local storage under `/srv/drmlke`
- LAN/VPN access
- live trading disabled by default
- withdrawals disabled
- no secrets in the client

The Spark/backend remains private and LAN/VPN-controlled unless explicitly changed in a future reviewed wave.

Future Tailscale work is infrastructure access only. It is not provider
activation, model serving, trading enablement, or approval to deploy runtime
services.

Spark access facts are recorded in
[access-inventory.md](access-inventory.md). The roadmap remains the canonical
source for current and next wave status.

Reusable copy-paste commands for local validation, access checks, SSH
verification, and read-only Spark preflight live in
[manual-runbook.md](manual-runbook.md). Keep command blocks there instead of in
the roadmap.

The current verified Spark SSH candidate is the Tailscale SSH alias `spark-vpn`.
This verifies access only. It does not create `/srv/drmlke`, prove runtime
readiness, or approve deployment.

Spark has been inspected read-only through the verified SSH path. The host is
not deployment-ready yet: `/srv/drmlke` has not been created, and Docker
inspection is not currently available to the verified remote user without
elevated permissions. Storage-root preparation and any Docker permission change
belong to later reviewed waves.

## Spark Docker Access Policy

Docker access on Spark requires an explicit owner-approved policy before runtime
deployment.

Docker group membership is effectively root-equivalent. Do not add users to the
Docker group, change Docker socket permissions, or use `sudo` for Docker
operations without a reviewed owner decision.

No Docker permission change has been made. No runtime deployment can begin until
the project decides one of these paths:

- owner-approved Docker group membership for the verified runtime user
- explicit owner-approved `sudo` use in later Docker waves
- a separate deployment/runtime user with a documented policy
- keeping Spark Docker work blocked
