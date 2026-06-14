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
