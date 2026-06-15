# DRMLKE Manual Command Runbook

## Purpose

This file collects manual commands for local validation, provider checks,
access verification, read-only Spark preflight, and future approved remote
operations.

It is for owner/operator convenience. It is not the canonical roadmap, not a
deployment approval, and not a place for secrets.

## Safety Rules

- Read each command before running it.
- Run commands from the expected machine and directory.
- Do not run remote mutation commands unless a future wave explicitly approves
  them.
- Do not paste secrets, IPs, usernames, private key paths, or environment file
  contents into docs.
- Do not use `sudo` unless a future manual task explicitly asks for it.
- Do not create `/srv/drmlke` until the approved storage-root wave.
- Do not deploy the provider to Spark until the approved runtime wave.

## Machine Contexts

- Local Linux workstation: primary development machine.
- MacBook: secondary development node.
- Spark: future runtime, storage, and provider node reached through `spark-vpn`.

## Execution Context Doctrine

Every manual command belongs to one execution context:

- `LOCAL / Exon`: run directly on the Linux workstation at
  `/home/mothx/computer-science/projects/drmlke`.
- `REMOTE / Spark one-shot`: typed on Exon, executed on Spark through
  `ssh spark-vpn '...'`.
- `REMOTE / Spark interactive`: typed inside an SSH session opened with
  `ssh -tt spark-vpn`.
- `REMOTE mutating`: any remote command that creates, edits, deletes, copies,
  starts, stops, changes ownership, changes permissions, or reconfigures Spark.
- `FORBIDDEN`: not approved for the current wave.

Do not run commands from the wrong machine. Code, tests, git, commits, and
pushes are local development work on Exon. Spark storage, runtime, and provider
operations happen only through the approved `spark-vpn` path.

For interactive Spark work, open a session and confirm context before running
approved commands:

```bash
ssh -tt spark-vpn
```

Inside Spark:

```bash
hostname
id
pwd
```

Exit the Spark session before returning to local git or validation work.

## LOCAL / Exon Repository Commands

Run on the local Linux workstation.

```bash
cd /home/mothx/computer-science/projects/drmlke
git status --short --branch
git log --oneline -8
git diff --check
```

## LOCAL / Exon Validation Commands

Run on the local Linux workstation.

```bash
cd /home/mothx/computer-science/projects/drmlke
make doctor
make check
```

Targeted core contract tests:

```bash
cd /home/mothx/computer-science/projects/drmlke
uv run pytest -q tests/test_core_contracts.py
```

## LOCAL / Exon Provider and Docker Commands

Run on the local Linux workstation. These commands inspect or start the local
provider only. They do not run on Spark.

```bash
cd /home/mothx/computer-science/projects/drmlke
docker context show
docker compose ps
docker compose --profile provider up -d provider
curl -sS http://127.0.0.1:8781/health
curl -sS http://127.0.0.1:8781/models
```

## LOCAL / Exon Tailscale Inventory Commands

Run locally. These commands inspect local Tailscale state only.

```bash
command -v tailscale || true
tailscale status 2>/dev/null || true
tailscale ip -4 2>/dev/null || true
```

Do not run `tailscale up`, `tailscale login`, or `tailscale set` unless a
future wave explicitly approves it.

## LOCAL / Exon Tailscale Reachability Commands

Run locally. These commands check reachability only. They do not prove SSH
login.

```bash
tailscale ping spark-7c3d 2>/dev/null || true
getent hosts spark-7c3d 2>/dev/null || true
```

## LOCAL / Exon SSH Config Inspection Commands

Run locally.

```bash
ssh -G spark-vpn 2>/dev/null | sed -n '1,160p' || true
ssh -G spark 2>/dev/null | sed -n '1,160p' || true
```

Do not paste full output into docs. Redact user, identity file, host, IP, and
private paths.

## REMOTE / Spark One-Shot SSH Verification Commands

Run from Exon. These commands execute on Spark through `spark-vpn` without
changing host key policy.

```bash
ssh -o BatchMode=yes -o ConnectTimeout=8 -o StrictHostKeyChecking=yes spark-vpn true
```

If the host key is already trusted and the previous command succeeds:

```bash
ssh -o BatchMode=yes -o ConnectTimeout=8 -o StrictHostKeyChecking=yes spark-vpn 'hostname; uname -a; id -un; pwd'
```

Do not use `StrictHostKeyChecking=no`. Do not auto-accept unknown host keys.
Do not run mutating remote commands.

## REMOTE / Spark One-Shot Read-Only Preflight Commands

Run from Exon through `spark-vpn`. These commands inspect Spark without
creating files, changing services, or deploying anything.

```bash
ssh -o BatchMode=yes -o ConnectTimeout=8 -o StrictHostKeyChecking=yes spark-vpn 'hostname; uname -a; cat /etc/os-release; id; pwd'
```

```bash
ssh -o BatchMode=yes -o ConnectTimeout=8 -o StrictHostKeyChecking=yes spark-vpn 'df -h; lsblk; mount | sed -n "1,120p"; test -e /srv/drmlke && stat /srv/drmlke || true'
```

```bash
ssh -o BatchMode=yes -o ConnectTimeout=8 -o StrictHostKeyChecking=yes spark-vpn 'command -v docker || true; docker --version 2>/dev/null || true; docker compose version 2>/dev/null || true; docker ps 2>/dev/null || true'
```

```bash
ssh -o BatchMode=yes -o ConnectTimeout=8 -o StrictHostKeyChecking=yes spark-vpn 'command -v nvidia-smi || true; nvidia-smi 2>/dev/null || true'
```

If Docker inspection fails due to permissions, record the blocker. Do not fix
it from this runbook.

## REMOTE / Spark One-Shot Docker Access Review Commands

Run from Exon through `spark-vpn`. This reviews Docker access state only.

```bash
ssh -o BatchMode=yes -o ConnectTimeout=8 -o StrictHostKeyChecking=yes spark-vpn 'id; groups; getent group docker || true; ls -l /var/run/docker.sock 2>/dev/null || true; command -v docker || true; docker --version 2>/dev/null || true; docker compose version 2>/dev/null || true'
```

Do not modify group membership, Docker socket permissions, Docker daemon
configuration, or service state from this runbook.

## REMOTE / Spark Mutating Docker Sudo Policy

Spark Docker operations use explicit owner-approved `sudo` in future approved
waves. Sudo Docker commands are not generally reusable yet.

Do not add destructive or mutating sudo commands here unless a future wave
explicitly approves the operation and records the exact command. Future sudo
commands must be copied from the approved wave.

## REMOTE / Spark Mutating Future P3 Command Discipline

No `sudo` commands are reusable until a future approved wave records the exact
command, purpose, expected effect, and rollback or verification step.

Do not create `/srv/drmlke` manually before approval. Do not copy files to
Spark, run Compose on Spark, or start provider services from this runbook until
a future P3 wave explicitly approves the operation.

Future sudo commands must be copied exactly from the approved wave. Do not
improvise path ownership, Docker, service, firewall, Tailscale, or deployment
commands.

## REMOTE / Spark Storage Root Plan

Read-only storage-root checks may be reused:

```bash
ssh -o BatchMode=yes -o ConnectTimeout=8 -o StrictHostKeyChecking=yes spark-vpn 'test -e /srv/drmlke && stat /srv/drmlke || true; df -h /srv / 2>/dev/null || df -h; id; groups'
```

DRAFT - forbidden until `P3.A.APPLY.INTERACTIVE` or an equivalent apply wave
approves it.

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

`REMOTE / Spark mutating` draft storage-root commands:

```bash
set -eu

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

Do not create `/srv/drmlke` manually before an approved apply wave. Storage
ownership is dedicated `drmlke:drmlke`, but no user, group, directory, `chown`,
or permission command is approved until a future apply wave records the exact
commands.

## REMOTE / Spark Storage Ownership Decision

Storage ownership policy is dedicated `drmlke:drmlke`.

- The human SSH operator remains separate from the runtime owner.
- Docker group membership is not granted by this decision.
- Do not run user or group creation manually yet.
- A future apply wave will provide exact `sudo` commands for user/group
  creation, directory creation, ownership, and validation.
- Keep draft storage-root commands labelled as forbidden until the approved
  apply wave.

## LOCAL / Exon Private Service Policy Checks

Run on the local Linux workstation. These commands inspect local planning
references only.

```bash
cd /home/mothx/computer-science/projects/drmlke
grep -R "8780\\|8781\\|8782\\|8783" -n compose.yaml apps docs 2>/dev/null || true
docker compose ps
```

These commands do not inspect Spark and do not change service exposure.

## FORBIDDEN Commands Until Explicit Future Approval

These command patterns remain forbidden unless a future wave explicitly approves
them. Values in angle brackets are placeholders, not real values. The Spark SSH
username is written explicitly because this is a private repository. Do not run
these by filling placeholders during an access-planning wave.

```bash
ssh spark-vpn 'sudo usermod -aG docker dgmothx'
ssh spark-vpn 'sudo mkdir -p /srv/drmlke'
ssh spark-vpn 'sudo chown -R drmlke:drmlke /srv/drmlke'
ssh spark-vpn 'cd /srv/drmlke/app && docker compose --profile provider up -d provider'
scp -r /home/mothx/computer-science/projects/drmlke spark-vpn:/srv/drmlke/app
rsync -av /home/mothx/computer-science/projects/drmlke/ spark-vpn:/srv/drmlke/app/
tailscale up
tailscale login
tailscale set --accept-routes=true
```

## Manual Decision Notes

- Spark Docker access policy recorded: explicit owner-approved `sudo` in future
  approved Spark Docker waves.
- `/srv/drmlke` creation pending.
- Exact Spark private service bind implementation pending.
- Provider deployment to Spark pending.
