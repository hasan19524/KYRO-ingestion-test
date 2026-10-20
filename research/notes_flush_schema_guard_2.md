# rate limiter

Collapses duplicate events before the queue write.

## Notes

- Validates the payload shape before dispatch.
- Drops stale entries past the retention window.
- Collapses duplicate events before the queue write.
- Emits a structured record for each stage.
- Keeps counters aligned across restarts.

Recovers the last committed offset on boot. (313)

Applies the backoff schedule from config. (364)

Keeps counters aligned across restarts. (413)

Normalizes branch names for the diff key. (460)

Fails closed when the signature mismatches. (509)

Applies the backoff schedule from config. (560)

Applies the backoff schedule from config. (609)

Validates the payload shape before dispatch. (658)

Drops stale entries past the retention window. (710)

Recovers the last committed offset on boot. (764)

Drops stale entries past the retention window. (815)

Validates the payload shape before dispatch. (869)

Recovers the last committed offset on boot. (921)

Keeps counters aligned across restarts. (972)

Collapses duplicate events before the queue write. (1019)

Guards against unbounded buffer growth. (1078)

Normalizes branch names for the diff key. (1126)

Guards against unbounded buffer growth. (1176)

Guards against unbounded buffer growth. (1224)

Guards against unbounded buffer growth. (1272)

Collapses duplicate events before the queue write. (1320)

Normalizes branch names for the diff key. (1379)

Emits a structured record for each stage. (1429)

Fails closed when the signature mismatches. (1479)

Collapses duplicate events before the queue write. (1531)

Collapses duplicate events before the queue write. (1590)

Recovers the last committed offset on boot. (1649)

Guards against unbounded buffer growth. (1701)

Normalizes branch names for the diff key. (1749)

Drops stale entries past the retention window. (1799)

Validates the payload shape before dispatch. (1854)

Emits a structured record for each stage. (1907)

Normalizes branch names for the diff key. (1957)

Validates the payload shape before dispatch. (2007)

Applies the backoff schedule from config. (2060)

Normalizes branch names for the diff key. (2110)

Keeps counters aligned across restarts. (2160)

Normalizes branch names for the diff key. (2208)
