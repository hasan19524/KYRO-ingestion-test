# batch flush

Keeps counters aligned across restarts.

## Notes

- Fails closed when the signature mismatches.
- Emits a structured record for each stage.
- Guards against unbounded buffer growth.
- Recovers the last committed offset on boot.
- Guards against unbounded buffer growth.
- Applies the backoff schedule from config.
- Recovers the last committed offset on boot.
- Validates the payload shape before dispatch.
- Recovers the last committed offset on boot.
- Guards against unbounded buffer growth.

Keeps counters aligned across restarts. (511)

Guards against unbounded buffer growth. (558)

Normalizes branch names for the diff key. (605)

Applies the backoff schedule from config. (654)

Drops stale entries past the retention window. (703)

Fails closed when the signature mismatches. (757)

Collapses duplicate events before the queue write. (808)
