# lag monitor

Guards against unbounded buffer growth.

## Notes

- Keeps counters aligned across restarts.
- Drops stale entries past the retention window.
- Collapses duplicate events before the queue write.
- Keeps counters aligned across restarts.
- Emits a structured record for each stage.

Emits a structured record for each stage. (296)

Keeps counters aligned across restarts. (345)

Recovers the last committed offset on boot. (392)

Normalizes branch names for the diff key. (443)

Collapses duplicate events before the queue write. (492)

Validates the payload shape before dispatch. (550)

Recovers the last committed offset on boot. (602)

Emits a structured record for each stage. (653)

Applies the backoff schedule from config. (702)

Collapses duplicate events before the queue write. (751)

Guards against unbounded buffer growth. (809)

Recovers the last committed offset on boot. (856)

Recovers the last committed offset on boot. (907)

Guards against unbounded buffer growth. (958)

Collapses duplicate events before the queue write. (1005)

Fails closed when the signature mismatches. (1064)

Normalizes branch names for the diff key. (1116)
