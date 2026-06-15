# DRMLKE Manual Command Runbook

## Purpose

This file collects manual commands for local validation, provider checks,
access verification, and read-only Spark preflight.

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

## Local Repository Commands

Run on the local Linux workstation.

```bash
cd /home/mothx/computer-science/projects/drmlke
git status --short --branch
git log --oneline -8
git diff --check
```

## Local Validation Commands

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

## Local Provider and Docker Commands

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

## Local Tailscale Inventory Commands

Run locally. These commands inspect local Tailscale state only.

```bash
command -v tailscale || true
tailscale status 2>/dev/null || true
tailscale ip -4 2>/dev/null || true
```

Do not run `tailscale up`, `tailscale login`, or `tailscale set` unless a
future wave explicitly approves it.

## Tailscale Reachability Commands

Run locally. These commands check reachability only. They do not prove SSH
login.

```bash
tailscale ping spark-7c3d 2>/dev/null || true
getent hosts spark-7c3d 2>/dev/null || true
```

## SSH Config Inspection Commands

Run locally.

```bash
ssh -G spark-vpn 2>/dev/null | sed -n '1,160p' || true
ssh -G spark 2>/dev/null | sed -n '1,160p' || true
```

Do not paste full output into docs. Redact user, identity file, host, IP, and
private paths.

## SSH Verification Commands

Run locally. These commands verify the already configured SSH path without
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

## Remote Spark Read-Only Preflight Commands

Run locally through `spark-vpn`. These commands inspect Spark without creating
files, changing services, or deploying anything.

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

## Spark Docker Access Review Commands

Run locally through `spark-vpn`. This reviews Docker access state only.

```bash
ssh -o BatchMode=yes -o ConnectTimeout=8 -o StrictHostKeyChecking=yes spark-vpn 'id; groups; getent group docker || true; ls -l /var/run/docker.sock 2>/dev/null || true; command -v docker || true; docker --version 2>/dev/null || true; docker compose version 2>/dev/null || true'
```

Do not modify group membership, Docker socket permissions, Docker daemon
configuration, or service state from this runbook.

## Forbidden Commands Until Explicit Future Approval

These are examples of currently forbidden operations unless a future wave
explicitly approves them.

```bash
ssh spark-vpn 'sudo usermod -aG docker ...'
ssh spark-vpn 'sudo mkdir -p /srv/drmlke'
ssh spark-vpn 'sudo chown ... /srv/drmlke'
ssh spark-vpn 'docker compose up -d'
scp ...
rsync ...
tailscale up
tailscale login
tailscale set ...
```

## Manual Decision Placeholders

- Spark Docker access policy decision pending.
- `/srv/drmlke` creation pending.
- Spark private service bind policy pending.
- Provider deployment to Spark pending.

