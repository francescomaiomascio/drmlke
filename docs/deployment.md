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

## Spark Private Service Policy

Spark-hosted drmlke services must remain private by default. There must be no
public internet exposure, router port forwarding, public tunnel, public
marketing endpoint, or public product endpoint unless a future reviewed wave
explicitly changes that boundary.

Default future service exposure:

- Provider: bind only to loopback or a private interface. It must not be
  exposed publicly.
- API: bind only to a private interface, preferably the Tailscale/private
  network when remote clients are needed.
- Worker: no public bind. Metrics and logs remain private.
- Client preview: private only. It is not a public web deployment.

Access path policy:

- Primary admin/operator path: SSH through `spark-vpn`.
- Service access path: Tailscale/private network only unless a future wave
  selects another private route.
- LAN access may remain a secondary fallback, but it is not the primary path
  unless explicitly selected later.

Future internal planning ports:

- API: `8780`.
- Provider: `8781`.
- Client preview: `8782`.
- Worker metrics: `8783`.

These ports are planning values only. They are not active Spark exposure and do
not authorize any deployment.

The future runtime root is `/srv/drmlke`. It must not be created before an
approved storage-root preparation wave. Runtime data, environment files, logs,
models, and backups must stay outside source control.

Secrets policy:

- No secrets in the repository.
- Environment files live outside the repository.
- No exchange keys.
- No wallet custody keys.
- No seed phrase or private key handling.
- No secrets copied through chat or docs.

This policy wave defines exposure rules only. It does not deploy services,
create directories, change firewall or router rules, change Tailscale
configuration, or modify Spark runtime state.

## Spark Docker Access Policy

Docker access on Spark uses explicit owner-approved `sudo` for future Spark
Docker operations unless a later reviewed wave changes the policy.

Docker group membership is effectively root-equivalent. DRMLKE does not grant
Docker group membership in this policy decision. Docker socket permissions
remain unchanged.

Future `sudo` use for Spark Docker operations must appear in an approved wave
and in the manual runbook. Sudo-based Docker commands are not generally reusable
until that wave provides the exact command and context.

No Docker permission change has been made. No runtime deployment can begin until
the first approved sudo-based storage or runtime wave defines the exact
operation.
