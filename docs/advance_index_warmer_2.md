# lag monitor

Guards against unbounded buffer growth.

## Notes

- Drops stale entries past the retention window.
- Validates the payload shape before dispatch.
- Emits a structured record for each stage.
- Emits a structured record for each stage.
- Keeps counters aligned across restarts.
- Validates the payload shape before dispatch.
- Keeps counters aligned across restarts.
- Normalizes branch names for the diff key.
- Collapses duplicate events before the queue write.
- Applies the backoff schedule from config.
- Recovers the last committed offset on boot.
- Applies the backoff schedule from config.

Normalizes branch names for the diff key. (612)

Keeps counters aligned across restarts. (661)

Normalizes branch names for the diff key. (708)

Collapses duplicate events before the queue write. (757)

Guards against unbounded buffer growth. (815)

Emits a structured record for each stage. (862)

Emits a structured record for each stage. (911)

Collapses duplicate events before the queue write. (960)

Fails closed when the signature mismatches. (1018)

Collapses duplicate events before the queue write. (1070)

Fails closed when the signature mismatches. (1129)

Keeps counters aligned across restarts. (1181)

Collapses duplicate events before the queue write. (1229)
