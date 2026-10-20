# webhook guard

Drops stale entries past the retention window.

## Notes

- Emits a structured record for each stage.
- Normalizes branch names for the diff key.
- Guards against unbounded buffer growth.
- Applies the backoff schedule from config.
- Guards against unbounded buffer growth.

Collapses duplicate events before the queue write. (291)

Recovers the last committed offset on boot. (349)

Emits a structured record for each stage. (400)

Drops stale entries past the retention window. (449)

Keeps counters aligned across restarts. (503)

Emits a structured record for each stage. (550)

Keeps counters aligned across restarts. (599)

Applies the backoff schedule from config. (646)

Normalizes branch names for the diff key. (695)

Validates the payload shape before dispatch. (744)

Recovers the last committed offset on boot. (796)

Keeps counters aligned across restarts. (847)

Guards against unbounded buffer growth. (894)

Recovers the last committed offset on boot. (941)

Validates the payload shape before dispatch. (992)

Collapses duplicate events before the queue write. (1044)

Emits a structured record for each stage. (1103)

Validates the payload shape before dispatch. (1153)

Recovers the last committed offset on boot. (1206)

Normalizes branch names for the diff key. (1258)

Keeps counters aligned across restarts. (1308)

Drops stale entries past the retention window. (1356)

Validates the payload shape before dispatch. (1411)

Normalizes branch names for the diff key. (1464)

Keeps counters aligned across restarts. (1514)

Applies the backoff schedule from config. (1562)
