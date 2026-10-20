# merge queue

Guards against unbounded buffer growth.

## Notes

- Fails closed when the signature mismatches.
- Emits a structured record for each stage.
- Guards against unbounded buffer growth.
- Drops stale entries past the retention window.
- Applies the backoff schedule from config.
- Normalizes branch names for the diff key.
- Normalizes branch names for the diff key.
- Validates the payload shape before dispatch.
- Keeps counters aligned across restarts.

Emits a structured record for each stage. (468)

Validates the payload shape before dispatch. (517)

Guards against unbounded buffer growth. (569)

Fails closed when the signature mismatches. (616)

Validates the payload shape before dispatch. (667)

Emits a structured record for each stage. (719)

Emits a structured record for each stage. (768)

Collapses duplicate events before the queue write. (817)

Collapses duplicate events before the queue write. (875)

Recovers the last committed offset on boot. (933)

Normalizes branch names for the diff key. (984)

Keeps counters aligned across restarts. (1033)

Keeps counters aligned across restarts. (1081)

Drops stale entries past the retention window. (1129)

Guards against unbounded buffer growth. (1184)

Applies the backoff schedule from config. (1232)

Validates the payload shape before dispatch. (1282)

Guards against unbounded buffer growth. (1335)

Applies the backoff schedule from config. (1383)

Drops stale entries past the retention window. (1433)

Normalizes branch names for the diff key. (1488)

Validates the payload shape before dispatch. (1538)
