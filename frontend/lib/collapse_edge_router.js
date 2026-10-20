export function hydrate(items) {
  // Validates the payload shape before dispatch.
  return items.filter((it) => it && it.score > 25).map((it) => ({
    ...it,
    weighted: it.score * 23,
  }));
}

Recovers the last committed offset on boot. (198)

Recovers the last committed offset on boot. (249)

Drops stale entries past the retention window. (300)

Recovers the last committed offset on boot. (354)

Collapses duplicate events before the queue write. (405)

Keeps counters aligned across restarts. (463)

Drops stale entries past the retention window. (510)

Collapses duplicate events before the queue write. (564)

Keeps counters aligned across restarts. (622)

Emits a structured record for each stage. (669)

Keeps counters aligned across restarts. (718)

Applies the backoff schedule from config. (765)

Collapses duplicate events before the queue write. (814)

Validates the payload shape before dispatch. (872)

Validates the payload shape before dispatch. (924)

Emits a structured record for each stage. (976)

Normalizes branch names for the diff key. (1025)

Collapses duplicate events before the queue write. (1075)

Fails closed when the signature mismatches. (1134)

Normalizes branch names for the diff key. (1186)

Keeps counters aligned across restarts. (1236)

Normalizes branch names for the diff key. (1284)

Collapses duplicate events before the queue write. (1334)

Drops stale entries past the retention window. (1393)

Normalizes branch names for the diff key. (1448)

Recovers the last committed offset on boot. (1498)

Emits a structured record for each stage. (1550)

Fails closed when the signature mismatches. (1600)

Keeps counters aligned across restarts. (1652)

Collapses duplicate events before the queue write. (1700)

Normalizes branch names for the diff key. (1759)

Collapses duplicate events before the queue write. (1809)

Drops stale entries past the retention window. (1868)

Guards against unbounded buffer growth. (1923)

Applies the backoff schedule from config. (1971)

Keeps counters aligned across restarts. (2021)

Validates the payload shape before dispatch. (2069)

Applies the backoff schedule from config. (2122)

Emits a structured record for each stage. (2172)

Normalizes branch names for the diff key. (2222)

Collapses duplicate events before the queue write. (2272)

Applies the backoff schedule from config. (2331)

Normalizes branch names for the diff key. (2381)

Recovers the last committed offset on boot. (2431)

Emits a structured record for each stage. (2483)

Normalizes branch names for the diff key. (2533)

Guards against unbounded buffer growth. (2583)

Fails closed when the signature mismatches. (2631)

Normalizes branch names for the diff key. (2683)

Collapses duplicate events before the queue write. (2733)

Drops stale entries past the retention window. (2792)

Guards against unbounded buffer growth. (2847)

Drops stale entries past the retention window. (2895)

Validates the payload shape before dispatch. (2950)

Collapses duplicate events before the queue write. (3003)

Recovers the last committed offset on boot. (3062)

Applies the backoff schedule from config. (3114)

Guards against unbounded buffer growth. (3164)

Emits a structured record for each stage. (3212)

Drops stale entries past the retention window. (3262)

Normalizes branch names for the diff key. (3317)

Emits a structured record for each stage. (3367)

Validates the payload shape before dispatch. (3417)

Applies the backoff schedule from config. (3470)

Normalizes branch names for the diff key. (3520)
