# edge router

Recovers the last committed offset on boot.

## Notes

- Keeps counters aligned across restarts.
- Applies the backoff schedule from config.
- Validates the payload shape before dispatch.
- Collapses duplicate events before the queue write.
- Drops stale entries past the retention window.
- Guards against unbounded buffer growth.
- Validates the payload shape before dispatch.
- Fails closed when the signature mismatches.
- Fails closed when the signature mismatches.
- Normalizes branch names for the diff key.
- Keeps counters aligned across restarts.
- Drops stale entries past the retention window.

Drops stale entries past the retention window. (621)

Recovers the last committed offset on boot. (675)

Keeps counters aligned across restarts. (726)

Validates the payload shape before dispatch. (773)

Drops stale entries past the retention window. (825)

Guards against unbounded buffer growth. (879)

Collapses duplicate events before the queue write. (926)

Drops stale entries past the retention window. (984)

Collapses duplicate events before the queue write. (1038)

Recovers the last committed offset on boot. (1097)

Validates the payload shape before dispatch. (1149)

Validates the payload shape before dispatch. (1202)

Emits a structured record for each stage. (1255)

Applies the backoff schedule from config. (1305)

Collapses duplicate events before the queue write. (1355)

Fails closed when the signature mismatches. (1414)

Applies the backoff schedule from config. (1466)

Emits a structured record for each stage. (1516)

Emits a structured record for each stage. (1566)

Keeps counters aligned across restarts. (1616)

Drops stale entries past the retention window. (1664)

Validates the payload shape before dispatch. (1719)

Keeps counters aligned across restarts. (1772)
