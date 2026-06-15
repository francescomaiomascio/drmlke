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

## Multi-Machine Execution Context Policy

DRMLKE now operates across distinct machine contexts:

- Linux / Exon: local development context for Codex, git, tests, commits, and
  pushes.
- Spark: remote runtime, storage, and provider context reached through
  `spark-vpn`.
- MacBook: secondary development context, not the primary runtime.

Future waves must label commands by execution context:

- `LOCAL / Exon`: entered and executed on the local Linux workstation.
- `REMOTE / Spark one-shot`: entered locally, executed remotely through
  `ssh spark-vpn '...'`.
- `REMOTE / Spark interactive`: entered after opening an interactive Spark
  shell, normally with `ssh -tt spark-vpn`.
- `REMOTE mutating`: remote command that creates, changes, deletes, starts,
  stops, copies, or reconfigures anything on Spark.
- `FORBIDDEN`: command pattern not approved for the current wave.

Long or interactive remote operations should prefer an explicit Spark session
with a context check before mutation. A Spark interactive session must confirm
host, user, and working directory before approved remote commands run.

The current verified Spark SSH candidate is the Tailscale SSH alias `spark-vpn`.
This verifies access only. It does not approve deployment.

Spark has been inspected through the verified SSH path. The storage root
`/srv/drmlke` now exists with dedicated `drmlke:drmlke` ownership and
conservative `0750` directory permissions. Docker inspection is not currently
available to the verified remote user without elevated permissions. Any Docker
permission change belongs to a later reviewed wave.

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

The runtime root is `/srv/drmlke`. Runtime data, environment files, logs,
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

## P2 Access Planning Closeout

P2 access planning is closed as a policy and access decision phase.

Locked P2 decisions and facts:

- Selected Spark operator path: `spark-vpn`.
- `spark-vpn` uses the Tailscale/private path.
- Spark reachability and SSH access through `spark-vpn` are verified.
- Spark services remain private by policy.
- No public tunnels, router port forwarding, or public exposure are approved.
- Spark Docker access policy is explicit owner-approved `sudo` in future
  approved waves.
- Docker group membership has not been granted.
- Docker socket permissions have not been changed.
- `/srv/drmlke` does not exist and was not created during P2.
- No Spark runtime deployment occurred during P2.

P3 prerequisites:

- An approved sudo-based Spark storage or runtime wave must define the exact
  commands before any privileged operation runs.
- The storage-root plan must be approved before `/srv/drmlke` is created.
- Runtime data, environment files, logs, models, and backups must stay outside
  source control.
- No secrets may be committed or copied through docs or chat.
- Spark services must remain private.
- Provider deployment to Spark must wait for an approved runtime wave.

The first eligible P3 step is a preflight/plan wave that writes the exact
sudo-based storage-root commands for review. It is not direct storage creation
and not provider deployment.

## Spark Storage Root Sudo Plan

Purpose:

- Create the future runtime root under `/srv/drmlke`.
- Keep runtime state outside git.
- Separate app source, environment files, state, analytical lake, vector data,
  model artifacts, logs, backups, runtime sockets, and runtime pids.

Target tree:

- `/srv/drmlke/env`
- `/srv/drmlke/app`
- `/srv/drmlke/state`
- `/srv/drmlke/lake/parquet`
- `/srv/drmlke/lake/duckdb`
- `/srv/drmlke/vector/lancedb`
- `/srv/drmlke/models/embeddings`
- `/srv/drmlke/models/llm`
- `/srv/drmlke/models/timeseries`
- `/srv/drmlke/logs/api`
- `/srv/drmlke/logs/worker`
- `/srv/drmlke/logs/provider`
- `/srv/drmlke/backups/daily`
- `/srv/drmlke/backups/weekly`
- `/srv/drmlke/runtime/sockets`
- `/srv/drmlke/runtime/pids`

Ownership policy:

The selected ownership model is a dedicated runtime user and group:
`drmlke:drmlke`.

- The human SSH operator is not the runtime owner by default.
- Docker group membership is not granted by this ownership decision.
- Runtime data, environment files, logs, models, and backups remain outside
  source control.
- `P3.A.APPLY.INTERACTIVE` created the `drmlke` user/group and storage tree with
  explicit owner-approved sudo commands.

No deploy occurs in this storage-root wave. No source copy, environment file,
secret, model artifact, log payload, backup payload, Docker container, or
provider runtime is created by this storage-root wave.

Applied by `P3.A.APPLY.INTERACTIVE`.

Interactive TTY sudo was required. The owner entered the sudo password manually
on Spark. No password was stored, copied into chat, or written into docs.

`LOCAL / Exon` opens the Spark session:

```bash
ssh -tt spark-vpn
```

`REMOTE / Spark interactive` confirms context:

```bash
hostname
id
pwd
```

`REMOTE / Spark mutating` applied storage-root commands:

```bash
if ! getent group drmlke >/dev/null; then
  sudo groupadd --system drmlke
fi

if ! getent passwd drmlke >/dev/null; then
  sudo useradd --system --gid drmlke --home-dir /srv/drmlke --shell /usr/sbin/nologin drmlke
fi

sudo install -d -m 0750 -o drmlke -g drmlke /srv/drmlke

sudo install -d -m 0750 -o drmlke -g drmlke \
  /srv/drmlke/env \
  /srv/drmlke/app \
  /srv/drmlke/state \
  /srv/drmlke/lake \
  /srv/drmlke/lake/parquet \
  /srv/drmlke/lake/duckdb \
  /srv/drmlke/vector \
  /srv/drmlke/vector/lancedb \
  /srv/drmlke/models \
  /srv/drmlke/models/embeddings \
  /srv/drmlke/models/llm \
  /srv/drmlke/models/timeseries \
  /srv/drmlke/logs \
  /srv/drmlke/logs/api \
  /srv/drmlke/logs/worker \
  /srv/drmlke/logs/provider \
  /srv/drmlke/backups \
  /srv/drmlke/backups/daily \
  /srv/drmlke/backups/weekly \
  /srv/drmlke/runtime \
  /srv/drmlke/runtime/sockets \
  /srv/drmlke/runtime/pids

sudo chown -R drmlke:drmlke /srv/drmlke
sudo find /srv/drmlke -type d -exec chmod 0750 {} +
```

Storage-root result:

- `drmlke` group exists.
- `drmlke` user exists.
- `/srv/drmlke` exists.
- `/srv/drmlke` and expected child directories are owned by `drmlke:drmlke`.
- `/srv/drmlke` and expected child directories use mode `0750`.
- `P3.A.CLOSE` verified that the storage tree still contains no file payloads.
  File payload count is `0`.
- The verified human SSH user is separate from the runtime owner and cannot
  list child directories without sudo. This is expected from the `0750`
  permission model.
- Docker group membership remains ungranted.
- Docker socket permissions remain unchanged.
- Provider deployment remains future work.

`REMOTE / Spark interactive` read-only validation command:

```bash
getent group drmlke
getent passwd drmlke
sudo stat -c "%U:%G %a %n" /srv/drmlke
sudo find /srv/drmlke -maxdepth 3 -type d -exec stat -c "%U:%G %a %n" {} + | sort
sudo find /srv/drmlke -type f -print | wc -l
```

Forbidden storage-root behavior:

- No secrets in `/srv/drmlke/app`.
- No environment files in git.
- No model artifacts in git.
- No logs in git.
- No backups in git.
- No exchange keys.
- No wallet keys.
- No seed phrases.

Execution gate:

- `P3.A.APPLY.INTERACTIVE` created storage only.
- `P3.A.CLOSE` verified storage only.
- Provider deployment remains a later runtime wave.
- Any additional Spark mutation still requires an explicit approved wave.

## Spark Environment File Policy

Environment files are a Spark-only operator-managed configuration and secret
boundary.

Rules:

- Environment files live only on Spark under `/srv/drmlke/env`.
- Environment files are never committed to the repository.
- Environment file contents are never pasted into docs, chat, roadmap, commit
  messages, issues, or run reports.
- Environment file contents are never copied into the master roadmap.
- Future environment files may contain secrets only after an explicit approved
  wave.
- No exchange, broker, wallet, withdrawal, custody, or live-trading secrets are
  allowed now.
- Provider, API, and worker environment files are future runtime configuration.
  They are not permission to deploy services.
- Provider deployment remains future work.

Target future environment files:

- `/srv/drmlke/env/drmlke.shared.env`
- `/srv/drmlke/env/drmlke.provider.env`
- `/srv/drmlke/env/drmlke.api.env`
- `/srv/drmlke/env/drmlke.worker.env`

Intended split:

- `drmlke.shared.env`: common storage root, environment mode, safety flags,
  live trading disabled flag, and shared path configuration.
- `drmlke.provider.env`: provider bind and port, provider mode, future
  model-runtime disabled/enabled flags, and no model download secrets.
- `drmlke.api.env`: API bind and port, private service mode, future auth or
  session settings, and no public exposure by default.
- `drmlke.worker.env`: worker mode, future job scheduling flags, storage/log
  roots, and no trading or execution enablement.

Target ownership and mode policy:

- `/srv/drmlke/env`: `root:drmlke 0750`.
- Environment files: `root:drmlke 0640`.

This is an intentional exception to the broader `/srv/drmlke` runtime tree
ownership. The runtime group can read future environment files, while the
runtime user cannot casually rewrite its own configuration. The human operator
uses approved sudo in a future apply wave for changes.

`P3.B.PREFLIGHT` defines this policy only. It does not change
`/srv/drmlke/env`, create environment files, write secrets, deploy the provider,
run Docker, or copy application code to Spark.

Future apply policy:

- The environment baseline apply wave is
  `P3.B.APPLY.INTERACTIVE - Spark Environment File Baseline With TTY Sudo`.
- It must run through an interactive Spark session.
- The owner types the sudo password manually in the terminal if prompted.
- LAN or private-network proximity does not make it acceptable to paste sudo
  passwords into chat, docs, command history, runbooks, or scripts.
- Do not use `sudo -S`.
- Do not store the sudo password.
- Do not change sudoers.
- Do not grant `NOPASSWD`.

Applied baseline:

- `P3.B.APPLY.INTERACTIVE` applied the environment-file baseline through an
  interactive Spark session with owner-entered sudo.
- `/srv/drmlke/env` is `root:drmlke 0750`.
- Baseline environment files are `root:drmlke 0640`:
  - `/srv/drmlke/env/drmlke.shared.env`
  - `/srv/drmlke/env/drmlke.provider.env`
  - `/srv/drmlke/env/drmlke.api.env`
  - `/srv/drmlke/env/drmlke.worker.env`
- Baseline environment files contain safe non-secret paths and disabled flags
  only.
- Validation found no secret-like key names matching `PASSWORD`, `TOKEN`,
  `SECRET`, `PRIVATE_KEY`, `SEED`, or `API_KEY`.
- Live trading remains disabled.
- Withdrawals remain disabled.
- Exchange connections remain disabled.
- Broker connections remain disabled.
- Wallet custody remains disabled.
- Provider inference remains disabled.
- Provider model runtime remains disabled.
- Provider model downloads remain disabled.
- API public exposure remains disabled.
- API live actions remain disabled.
- Market data remains disabled.
- Paper execution remains disabled.
- Live execution remains disabled.
- Provider deployment has not started.
- Docker was not used.
- No source copy, exchange credential, broker credential, wallet key, seed
  phrase, private key, API credential, model artifact, or runtime service was
  added.
