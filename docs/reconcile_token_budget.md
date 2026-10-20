# rate limiter

Drops stale entries past the retention window.

## Notes

- Applies the backoff schedule from config.
- Guards against unbounded buffer growth.
- Fails closed when the signature mismatches.
- Recovers the last committed offset on boot.
- Applies the backoff schedule from config.
- Emits a structured record for each stage.
- Fails closed when the signature mismatches.
- Emits a structured record for each stage.

Fails closed when the signature mismatches. (430)

Applies the backoff schedule from config. (481)

Drops stale entries past the retention window. (530)

Collapses duplicate events before the queue write. (584)

Validates the payload shape before dispatch. (642)

Drops stale entries past the retention window. (694)

Keeps counters aligned across restarts. (748)

Recovers the last committed offset on boot. (795)
