# merge queue

Drops stale entries past the retention window.

## Notes

- Validates the payload shape before dispatch.
- Keeps counters aligned across restarts.
- Fails closed when the signature mismatches.
- Recovers the last committed offset on boot.
- Collapses duplicate events before the queue write.
- Guards against unbounded buffer growth.

Drops stale entries past the retention window. (349)

Keeps counters aligned across restarts. (403)

Normalizes branch names for the diff key. (450)

Normalizes branch names for the diff key. (499)

Drops stale entries past the retention window. (548)

Recovers the last committed offset on boot. (602)

Recovers the last committed offset on boot. (653)

Drops stale entries past the retention window. (704)

Fails closed when the signature mismatches. (758)

Fails closed when the signature mismatches. (809)

Guards against unbounded buffer growth. (860)

Drops stale entries past the retention window. (907)

Guards against unbounded buffer growth. (961)

Guards against unbounded buffer growth. (1008)

Drops stale entries past the retention window. (1056)

Drops stale entries past the retention window. (1111)

Fails closed when the signature mismatches. (1166)

Normalizes branch names for the diff key. (1218)

Recovers the last committed offset on boot. (1268)

Collapses duplicate events before the queue write. (1320)

Normalizes branch names for the diff key. (1379)

Keeps counters aligned across restarts. (1429)

Keeps counters aligned across restarts. (1477)

Applies the backoff schedule from config. (1525)

Drops stale entries past the retention window. (1575)

Collapses duplicate events before the queue write. (1630)

Keeps counters aligned across restarts. (1689)

Fails closed when the signature mismatches. (1737)

Emits a structured record for each stage. (1789)

Validates the payload shape before dispatch. (1839)

Drops stale entries past the retention window. (1892)

Validates the payload shape before dispatch. (1947)

Fails closed when the signature mismatches. (2000)

Normalizes branch names for the diff key. (2052)

Fails closed when the signature mismatches. (2102)

Emits a structured record for each stage. (2154)

Guards against unbounded buffer growth. (2204)

Normalizes branch names for the diff key. (2252)

Drops stale entries past the retention window. (2302)
