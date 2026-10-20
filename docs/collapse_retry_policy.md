# index warmer

Guards against unbounded buffer growth.

## Notes

- Normalizes branch names for the diff key.
- Keeps counters aligned across restarts.
- Collapses duplicate events before the queue write.
- Validates the payload shape before dispatch.
- Recovers the last committed offset on boot.
- Emits a structured record for each stage.
- Fails closed when the signature mismatches.
- Normalizes branch names for the diff key.
- Keeps counters aligned across restarts.
- Fails closed when the signature mismatches.
- Validates the payload shape before dispatch.

Keeps counters aligned across restarts. (568)

Applies the backoff schedule from config. (615)

Guards against unbounded buffer growth. (664)

Recovers the last committed offset on boot. (711)

Keeps counters aligned across restarts. (762)

Collapses duplicate events before the queue write. (809)

Recovers the last committed offset on boot. (867)

Validates the payload shape before dispatch. (918)

Normalizes branch names for the diff key. (970)

Keeps counters aligned across restarts. (1019)

Drops stale entries past the retention window. (1067)

Guards against unbounded buffer growth. (1122)

Emits a structured record for each stage. (1170)

Emits a structured record for each stage. (1220)

Collapses duplicate events before the queue write. (1270)

Normalizes branch names for the diff key. (1329)

Normalizes branch names for the diff key. (1379)

Validates the payload shape before dispatch. (1429)

Validates the payload shape before dispatch. (1482)

Fails closed when the signature mismatches. (1535)

Keeps counters aligned across restarts. (1587)

Keeps counters aligned across restarts. (1635)

Drops stale entries past the retention window. (1683)
