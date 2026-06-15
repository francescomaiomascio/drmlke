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
| Tailscale SSH alias | known locally | SSH config contains alias `spark-vpn`; host details are redacted from repository docs. |
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
- No SSH login was attempted in this wave.
- Host key verification state remains unverified by this wave.

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

## Unknowns

- Exact Spark SSH path to prefer for future work.
- Whether `spark` over LAN is reliable enough.
- Whether `spark-vpn` over Tailscale should become the primary SSH path after
  host identity verification.
- Whether the Spark Tailscale node name `spark-7c3d` is stable.
- Whether the configured SSH username is the intended long-term runtime user.
- Whether host key verification is already trusted and current.
- Whether Linux workstation should be the primary Spark access source.
- Whether MacBook remains the preferred private access path for remote work.
- Whether Spark should later bind services only to localhost, a Tailscale
  interface, or another private interface.
