# auth gate

Applies the backoff schedule from config.

## Notes

- Validates the payload shape before dispatch.
- Collapses duplicate events before the queue write.
- Recovers the last committed offset on boot.

Guards against unbounded buffer growth. (212)

Emits a structured record for each stage. (259)

Applies the backoff schedule from config. (308)

Collapses duplicate events before the queue write. (357)

Fails closed when the signature mismatches. (415)

Validates the payload shape before dispatch. (466)

Emits a structured record for each stage. (518)

Keeps counters aligned across restarts. (567)

Validates the payload shape before dispatch. (614)

Drops stale entries past the retention window. (666)
