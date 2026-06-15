# DRMLKE Access Inventory

## Purpose

Read-only inventory for future Spark access planning.

This document records known local access facts, Tailscale reachability results,
and remaining unknowns for future Spark access planning.

## Scope

Technical access facts only.

This document records inventory, reachability, SSH verification, remote
preflight, and Docker access facts. It does not define current or next wave
status, does not approve deployment, does not configure Tailscale, does not edit
SSH configuration, and does not authorize runtime mutation.

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

## P2.D.REMEDIATION Docker Access Review

- Current Docker access state: Docker and Docker Compose are installed, but the
  verified remote user cannot inspect Docker without elevated permissions.
- Docker group state: a Docker group exists, but the verified remote user does
  not appear to be a member. User and group details are summarized only.
- Docker socket state: the Docker socket is owned by `root:docker` and is not
  world-accessible.
- No Docker permission change was made.
- No `sudo` command was run.
- No container was started or stopped.
- No Docker daemon configuration was changed.
- No `/srv/drmlke` directory was created.

Options reviewed:

1. Owner manually adds the verified runtime user to the Docker group.
   - Pros: Docker and Docker Compose become usable without `sudo` for later
     deploy and operations waves.
   - Cons: Docker group access is effectively root-equivalent and requires
     explicit trust.
   - Manual action pattern, if approved outside this wave:
     `sudo usermod -aG docker <verified-spark-user>`, followed by a fresh login
     session and a read-only Docker access check.
2. Use explicit `sudo` for Docker operations in later waves.
   - Pros: avoids Docker group membership.
   - Cons: every Docker-related wave requires controlled owner approval and is
     harder to automate safely.
3. Use a separate deployment/runtime user.
   - Pros: clearer operational boundary.
   - Cons: requires user, group, and policy setup before runtime work.
4. Keep Spark Docker work blocked.
   - Pros: safest until an owner policy decision exists.
   - Cons: blocks Spark runtime deployment.

Decision outcome:

- Docker access is privileged/root-equivalent.
- DRMLKE does not grant Docker group access in P2.
- Docker socket permissions remain unchanged.
- Future Spark Docker operations use explicit owner-approved `sudo` in future
  approved waves unless a later reviewed wave changes the policy.
- `P3` runtime deployment remains blocked until a future approved sudo-based
  storage or runtime wave defines the exact operation.

## P2 Closeout Facts

- Primary Spark operator path: `spark-vpn`.
- `spark-vpn` uses the Tailscale/private path.
- Tailscale reachability to Spark is verified.
- SSH through `spark-vpn` is verified.
- Remote preflight is complete through read-only inspection.
- Spark OS family, architecture, Docker, Compose, GPU visibility, disk summary,
  and `/srv/drmlke` absence are recorded above.
- Docker access blocker is identified: the verified remote user cannot inspect
  Docker without elevated permissions.
- Docker access policy is recorded as explicit owner-approved `sudo` for future
  approved Spark Docker waves.
- Docker group membership has not been granted.
- Docker socket permissions have not been changed.
- Storage-root creation commands are draft-only and have not been run.
- `/srv/drmlke` ownership policy is dedicated `drmlke:drmlke`.
- The `drmlke` user/group has not been created by this documentation wave.
- No Spark files, directories, services, containers, or runtime state were
  created or changed during P2.

## Unknowns

- Whether `spark` over LAN is reliable enough.
- Whether the Spark Tailscale node name `spark-7c3d` is stable.
- Whether the configured SSH username is the intended long-term runtime user.
- Whether host key fingerprint documentation belongs in private operator notes
  outside this repository.
- Whether Linux workstation should be the primary Spark access source.
- Whether MacBook remains the preferred private access path for remote work.
- Which future approved sudo-based wave should create the `drmlke` user/group
  and `/srv/drmlke` storage tree.
- Whether Spark should later bind services only to localhost, a Tailscale
  interface, or another private interface.
