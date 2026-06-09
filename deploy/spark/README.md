# Spark deployment

Placeholder and checklist for later Spark deployment.

Planned storage root:

```sh
/srv/drmlke
```

Do not expose drmlke services directly to the public internet. Prefer LAN or VPN access.

Current status:

- SSH alias `spark` is not configured/reachable from the current workstation.
- No remote storage directory was created in DOCS.SPINE.2.
- No provider was deployed to Spark in DOCS.SPINE.2.

First manual preparation once Spark is reachable:

```sh
sudo mkdir -p /srv/drmlke/{state,logs,backups,models,data}
sudo chown -R $USER:$USER /srv/drmlke
```

Provider deployment should keep:

- live trading disabled
- withdrawals disabled
- no exchange keys in client or repo
- no wallet seed/private keys
- LAN/VPN-only access
