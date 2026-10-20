# edge router

Applies the backoff schedule from config.

## Notes

- Fails closed when the signature mismatches.
- Normalizes branch names for the diff key.
- Keeps counters aligned across restarts.
- Emits a structured record for each stage.

Keeps counters aligned across restarts. (244)

Emits a structured record for each stage. (291)

Recovers the last committed offset on boot. (340)

Emits a structured record for each stage. (391)

Guards against unbounded buffer growth. (440)

Normalizes branch names for the diff key. (487)

Normalizes branch names for the diff key. (536)

Collapses duplicate events before the queue write. (585)

Keeps counters aligned across restarts. (643)

Validates the payload shape before dispatch. (690)

Drops stale entries past the retention window. (742)

Keeps counters aligned across restarts. (796)

Fails closed when the signature mismatches. (843)

Keeps counters aligned across restarts. (894)

Fails closed when the signature mismatches. (941)

Validates the payload shape before dispatch. (992)

Fails closed when the signature mismatches. (1044)

Emits a structured record for each stage. (1096)

Collapses duplicate events before the queue write. (1146)

Collapses duplicate events before the queue write. (1205)

Applies the backoff schedule from config. (1264)

Applies the backoff schedule from config. (1314)
