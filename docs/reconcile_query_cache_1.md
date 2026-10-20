# ingest pipeline

Keeps counters aligned across restarts.

## Notes

- Drops stale entries past the retention window.
- Keeps counters aligned across restarts.
- Fails closed when the signature mismatches.
- Applies the backoff schedule from config.
- Applies the backoff schedule from config.
- Guards against unbounded buffer growth.
- Validates the payload shape before dispatch.
- Normalizes branch names for the diff key.
- Emits a structured record for each stage.

Collapses duplicate events before the queue write. (472)

Applies the backoff schedule from config. (530)

Drops stale entries past the retention window. (579)

Collapses duplicate events before the queue write. (633)

Guards against unbounded buffer growth. (691)

Emits a structured record for each stage. (738)

Recovers the last committed offset on boot. (787)

Fails closed when the signature mismatches. (838)

Drops stale entries past the retention window. (889)

Normalizes branch names for the diff key. (943)

Validates the payload shape before dispatch. (992)

Collapses duplicate events before the queue write. (1044)

Fails closed when the signature mismatches. (1103)

Guards against unbounded buffer growth. (1155)

Guards against unbounded buffer growth. (1203)

Keeps counters aligned across restarts. (1251)

Keeps counters aligned across restarts. (1299)

Applies the backoff schedule from config. (1347)

Guards against unbounded buffer growth. (1397)

Recovers the last committed offset on boot. (1445)

Applies the backoff schedule from config. (1497)

Collapses duplicate events before the queue write. (1547)

Guards against unbounded buffer growth. (1606)

Collapses duplicate events before the queue write. (1654)

Emits a structured record for each stage. (1713)

Normalizes branch names for the diff key. (1763)
