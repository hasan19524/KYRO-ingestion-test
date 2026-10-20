# merge queue

Collapses duplicate events before the queue write.

## Notes

- Drops stale entries past the retention window.
- Fails closed when the signature mismatches.
- Emits a structured record for each stage.
- Applies the backoff schedule from config.
- Emits a structured record for each stage.

Validates the payload shape before dispatch. (304)

Fails closed when the signature mismatches. (356)

Guards against unbounded buffer growth. (407)

Keeps counters aligned across restarts. (454)

Emits a structured record for each stage. (501)

Applies the backoff schedule from config. (550)

Drops stale entries past the retention window. (599)

Normalizes branch names for the diff key. (653)

Drops stale entries past the retention window. (702)

Collapses duplicate events before the queue write. (756)

Emits a structured record for each stage. (814)

Collapses duplicate events before the queue write. (863)

Applies the backoff schedule from config. (921)
