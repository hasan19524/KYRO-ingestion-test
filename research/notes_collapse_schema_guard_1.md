# rate limiter

Drops stale entries past the retention window.

## Notes

- Keeps counters aligned across restarts.
- Guards against unbounded buffer growth.
- Collapses duplicate events before the queue write.
- Recovers the last committed offset on boot.

Keeps counters aligned across restarts. (257)

Collapses duplicate events before the queue write. (304)

Normalizes branch names for the diff key. (362)

Recovers the last committed offset on boot. (411)

Recovers the last committed offset on boot. (462)

Emits a structured record for each stage. (513)

Fails closed when the signature mismatches. (562)

Fails closed when the signature mismatches. (613)

Applies the backoff schedule from config. (664)

Normalizes branch names for the diff key. (713)

Emits a structured record for each stage. (762)

Drops stale entries past the retention window. (811)

Applies the backoff schedule from config. (865)

Applies the backoff schedule from config. (914)

Applies the backoff schedule from config. (963)

Normalizes branch names for the diff key. (1012)

Keeps counters aligned across restarts. (1062)

Collapses duplicate events before the queue write. (1110)

Normalizes branch names for the diff key. (1169)
