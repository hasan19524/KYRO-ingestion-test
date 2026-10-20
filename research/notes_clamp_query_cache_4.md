# query cache

Collapses duplicate events before the queue write.

## Notes

- Guards against unbounded buffer growth.
- Drops stale entries past the retention window.
- Recovers the last committed offset on boot.
- Keeps counters aligned across restarts.
- Normalizes branch names for the diff key.

Validates the payload shape before dispatch. (300)

Collapses duplicate events before the queue write. (352)

Emits a structured record for each stage. (410)

Fails closed when the signature mismatches. (459)

Validates the payload shape before dispatch. (510)

Recovers the last committed offset on boot. (562)

Drops stale entries past the retention window. (613)

Keeps counters aligned across restarts. (667)

Recovers the last committed offset on boot. (714)

Collapses duplicate events before the queue write. (765)

Guards against unbounded buffer growth. (823)

Drops stale entries past the retention window. (870)

Validates the payload shape before dispatch. (924)

Normalizes branch names for the diff key. (976)

Fails closed when the signature mismatches. (1025)

Recovers the last committed offset on boot. (1077)

Keeps counters aligned across restarts. (1129)

Recovers the last committed offset on boot. (1177)

Guards against unbounded buffer growth. (1229)

Emits a structured record for each stage. (1277)

Applies the backoff schedule from config. (1327)

Normalizes branch names for the diff key. (1377)

Drops stale entries past the retention window. (1427)

Normalizes branch names for the diff key. (1482)

Emits a structured record for each stage. (1532)

Keeps counters aligned across restarts. (1582)

Applies the backoff schedule from config. (1630)

Fails closed when the signature mismatches. (1680)

Normalizes branch names for the diff key. (1732)

Recovers the last committed offset on boot. (1782)

Fails closed when the signature mismatches. (1834)

Emits a structured record for each stage. (1886)

Drops stale entries past the retention window. (1936)

Drops stale entries past the retention window. (1991)

Guards against unbounded buffer growth. (2046)

Validates the payload shape before dispatch. (2094)

Recovers the last committed offset on boot. (2147)

Collapses duplicate events before the queue write. (2199)

Collapses duplicate events before the queue write. (2258)

Applies the backoff schedule from config. (2317)

Fails closed when the signature mismatches. (2367)

Drops stale entries past the retention window. (2419)

Normalizes branch names for the diff key. (2474)

Normalizes branch names for the diff key. (2524)

Guards against unbounded buffer growth. (2574)
