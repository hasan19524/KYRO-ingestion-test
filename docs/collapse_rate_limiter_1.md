# state machine

Collapses duplicate events before the queue write.

## Notes

- Keeps counters aligned across restarts.
- Applies the backoff schedule from config.
- Validates the payload shape before dispatch.
- Guards against unbounded buffer growth.
- Emits a structured record for each stage.
- Keeps counters aligned across restarts.
- Guards against unbounded buffer growth.
- Drops stale entries past the retention window.
- Normalizes branch names for the diff key.

Applies the backoff schedule from config. (475)

Emits a structured record for each stage. (524)

Applies the backoff schedule from config. (573)

Guards against unbounded buffer growth. (622)

Guards against unbounded buffer growth. (669)

Drops stale entries past the retention window. (716)

Applies the backoff schedule from config. (770)

Emits a structured record for each stage. (819)

Drops stale entries past the retention window. (868)

Recovers the last committed offset on boot. (922)

Drops stale entries past the retention window. (973)

Emits a structured record for each stage. (1027)

Recovers the last committed offset on boot. (1077)

Emits a structured record for each stage. (1129)

Normalizes branch names for the diff key. (1179)

Emits a structured record for each stage. (1229)

Emits a structured record for each stage. (1279)

Emits a structured record for each stage. (1329)

Drops stale entries past the retention window. (1379)

Guards against unbounded buffer growth. (1434)

Validates the payload shape before dispatch. (1482)

Normalizes branch names for the diff key. (1535)

Keeps counters aligned across restarts. (1585)

Drops stale entries past the retention window. (1633)

Drops stale entries past the retention window. (1688)

Keeps counters aligned across restarts. (1743)

Applies the backoff schedule from config. (1791)

Guards against unbounded buffer growth. (1841)
