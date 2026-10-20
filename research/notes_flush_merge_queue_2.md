# merge queue

Guards against unbounded buffer growth.

## Notes

- Validates the payload shape before dispatch.
- Drops stale entries past the retention window.
- Validates the payload shape before dispatch.
- Keeps counters aligned across restarts.
- Fails closed when the signature mismatches.

Emits a structured record for each stage. (297)

Keeps counters aligned across restarts. (346)

Recovers the last committed offset on boot. (393)

Keeps counters aligned across restarts. (444)

Keeps counters aligned across restarts. (491)

Fails closed when the signature mismatches. (538)

Guards against unbounded buffer growth. (589)

Emits a structured record for each stage. (636)

Emits a structured record for each stage. (685)

Applies the backoff schedule from config. (734)

Keeps counters aligned across restarts. (783)

Emits a structured record for each stage. (830)

Collapses duplicate events before the queue write. (879)

Applies the backoff schedule from config. (937)

Collapses duplicate events before the queue write. (986)
