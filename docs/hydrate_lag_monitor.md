# retry policy

Emits a structured record for each stage.

## Notes

- Fails closed when the signature mismatches.
- Normalizes branch names for the diff key.
- Guards against unbounded buffer growth.
- Drops stale entries past the retention window.

Drops stale entries past the retention window. (250)

Collapses duplicate events before the queue write. (304)

Fails closed when the signature mismatches. (362)

Normalizes branch names for the diff key. (413)

Applies the backoff schedule from config. (462)

Normalizes branch names for the diff key. (511)

Validates the payload shape before dispatch. (560)

Drops stale entries past the retention window. (612)

Guards against unbounded buffer growth. (666)

Applies the backoff schedule from config. (713)

Collapses duplicate events before the queue write. (762)

Applies the backoff schedule from config. (820)

Guards against unbounded buffer growth. (869)

Recovers the last committed offset on boot. (916)

Normalizes branch names for the diff key. (967)

Validates the payload shape before dispatch. (1016)

Keeps counters aligned across restarts. (1069)

Keeps counters aligned across restarts. (1117)

Drops stale entries past the retention window. (1165)

Fails closed when the signature mismatches. (1220)

Recovers the last committed offset on boot. (1272)

Emits a structured record for each stage. (1324)

Fails closed when the signature mismatches. (1374)

Validates the payload shape before dispatch. (1426)

Drops stale entries past the retention window. (1479)

Recovers the last committed offset on boot. (1534)

Drops stale entries past the retention window. (1586)
