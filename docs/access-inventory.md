# DRMLKE Access Inventory

## Purpose

Read-only inventory for future Spark access planning.

This document records known local access facts, Tailscale reachability results,
and remaining unknowns for future Spark access planning.

## Scope

Inventory only.

This wave does not prove reachability, does not log in to Spark, does not
configure Tailscale, does not edit SSH configuration, and does not deploy or
mutate runtime state.

## Local Development Node

- Canonical repo path: `/home/mothx/computer-science/projects/drmlke`.
- Local host role: primary Linux development workstation.
- Local hostname: `Exon`.
- Local OS family: Linux x86_64.
- Repository branch: `main`.
- Repository sync state at inventory time: aligned with `origin/main`.
- SSH client: installed locally.
- Tailscale client: installed locally.
- Tailscale local node state: local node appears logged in and has a Tailscale
  IPv4 address. The address is not recorded here.

## Known Future Spark Role

- Spark is the future runtime, storage, and provider node.
- Spark is not the authoring source.
- Spark remains private.
- Target runtime root remains `/srv/drmlke`.
- No Spark runtime deployment exists yet.
- No `/srv/drmlke` creation is part of this wave.

## Candidate Access Methods

| Method | Current inventory state | Notes |
| --- | --- | --- |
| LAN SSH alias | known locally | SSH config contains alias `spark`; host details are redacted from repository docs. |
| Tailscale SSH alias | verified locally | SSH config contains alias `spark-vpn`; host details are redacted from repository docs. |
| Tailscale node name | known locally | Tailscale status shows candidate node `spark-7c3d`. |
| Tailscale IP | known locally | Redacted from repository docs. |
| Direct private IP | known locally through SSH config | Redacted from repository docs. |
| MacBook path | known as future/secondary path | MacBook is a secondary development node; private access path still needs confirmation. |
| Linux workstation path | current inventory source | Linux workstation can see local SSH aliases and Tailscale state. |

## Local SSH Inventory

- `~/.ssh/config` exists locally.
- Relevant Spark-like aliases found:
  - `spark`
  - `spark-vpn`
- Both aliases include an SSH user, host target, identity file, and port in
  local SSH configuration.
- The SSH username, host targets, and private key path are intentionally not
  copied into this repository document.
- No SSH login was attempted during `P2.A` or `P2.B`.
- SSH verification results are recorded below.

## Local Tailscale Inventory

- `tailscale` command exists locally.
- Local Tailscale state appears authenticated.
- Local node appears in Tailscale status as `exon`.
- Candidate Spark-like Tailscale node appears as `spark-7c3d`.
- Other unrelated Tailscale nodes were excluded from this document.
- No Tailscale configuration command was run.
- No reachability test was run in this wave.

## P2.B Reachability Result

- Candidate node `spark-7c3d` appears in local Tailscale status.
- Tailscale reachability to `spark-7c3d` succeeds.
- Local name resolution for `spark-7c3d` appears usable through the tailnet
  name. The resolved address is intentionally not recorded here.
- `spark-vpn` does not appear as a normal system DNS name. It remains a local
  SSH config alias that appears intended for the Tailscale path.
- Reachability was tested without SSH.
- No remote command was run.
- No remote state was changed.
- No Tailscale configuration was changed.
- Tailscale addresses, private addresses, SSH username, and private key path
  were redacted from repository documentation.
- SSH identity and host-key verification remain separate future work.

## P2.C SSH Verification Result

- `spark-vpn` is recognized by local SSH configuration.
- `spark-vpn` appears to target the Tailscale/private path.
- `spark-vpn` has a configured SSH user, identity file, and port. The values are
  redacted from repository documentation.
- Host key verification with strict checking succeeds, so the host key is
  already trusted locally.
- SSH login through `spark-vpn` succeeds in non-interactive batch mode.
- Only read-only remote commands were run: connection test, remote hostname,
  kernel/architecture information, remote username, and remote working
  directory.
- Remote username, home directory, Tailscale address, private address, and key
  path are redacted from repository documentation.
- Remote facts confirmed: Spark-like hostname, Linux OS, NVIDIA kernel family,
  aarch64 architecture, remote username availability, and remote working
  directory availability.
- `spark` LAN alias was not tested; `spark-vpn` succeeded and remains the
  verified Tailscale SSH path.
- No files were copied.
- No directories were created.
- No remote files were changed.
- No `sudo`, Docker, service, package, runtime, or deployment commands were run
  on Spark.

## P2.D Remote Preflight Result

- SSH path used: `spark-vpn`.
- Remote preflight was read-only.
- Remote OS distribution: Ubuntu 24.04 LTS family.
- Remote architecture: `aarch64`.
- Remote kernel family: NVIDIA-related Linux kernel.
- Docker installed: yes.
- Docker Compose available: yes.
- Docker inspection without sudo: no. `docker ps` is not usable by the current
  remote user without elevated permissions.
- NVIDIA/GPU tooling visible: yes.
- GPU summary: NVIDIA GB10 is visible through NVIDIA tooling. Serial numbers,
  bus identifiers, process details, and unrelated display-process details are
  not recorded here.
- Disk summary: Spark exposes a large NVMe-backed root filesystem with ample
  free space and standard EFI/tmpfs/system mounts. Detailed mount output is not
  copied into this repository document.
- `/srv/drmlke` exists: no.
- `/srv/drmlke` was not created.
- No files were copied.
- No directories were created.
- No remote files were changed.
- No `sudo`, package installation, Docker container, service, runtime, or
  deployment command was run.
- Redacted values: SSH username, remote home directory, Tailscale/private
  addresses, private key path, detailed mount output, GPU bus/process details,
  and unrelated local runtime details.

## Unknowns

- Whether `spark-vpn` should be the long-term preferred SSH path for all Spark
  operations.
- Whether `spark` over LAN is reliable enough.
- Whether the Spark Tailscale node name `spark-7c3d` is stable.
- Whether the configured SSH username is the intended long-term runtime user.
- Whether host key fingerprint documentation belongs in private operator notes
  outside this repository.
- Whether Linux workstation should be the primary Spark access source.
- Whether MacBook remains the preferred private access path for remote work.
- Whether the remote user should be allowed to inspect Docker without sudo, or
  whether future runtime operations should use a different operator pattern.
- Which wave should create `/srv/drmlke` and with what ownership model.
- Whether Spark should later bind services only to localhost, a Tailscale
  interface, or another private interface.
