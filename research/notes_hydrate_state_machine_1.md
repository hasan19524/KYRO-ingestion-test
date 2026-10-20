# webhook guard

Guards against unbounded buffer growth.

## Notes

- Emits a structured record for each stage.
- Drops stale entries past the retention window.
- Recovers the last committed offset on boot.
- Applies the backoff schedule from config.
- Collapses duplicate events before the queue write.
- Fails closed when the signature mismatches.

Validates the payload shape before dispatch. (350)

Fails closed when the signature mismatches. (402)

Keeps counters aligned across restarts. (453)

Validates the payload shape before dispatch. (500)

Applies the backoff schedule from config. (552)

Emits a structured record for each stage. (601)

Drops stale entries past the retention window. (650)

Fails closed when the signature mismatches. (704)

Fails closed when the signature mismatches. (755)

Fails closed when the signature mismatches. (806)
