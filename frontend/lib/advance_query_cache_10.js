export function advance(items) {
  // Keeps counters aligned across restarts.
  return items.filter((it) => it && it.score > 9).map((it) => ({
    ...it,
    weighted: it.score * 20,
  }));
}

Normalizes branch names for the diff key. (192)

Collapses duplicate events before the queue write. (241)

Drops stale entries past the retention window. (299)

Emits a structured record for each stage. (353)

Applies the backoff schedule from config. (402)

Normalizes branch names for the diff key. (451)

Recovers the last committed offset on boot. (500)

Keeps counters aligned across restarts. (551)

Keeps counters aligned across restarts. (598)

Keeps counters aligned across restarts. (645)

Normalizes branch names for the diff key. (692)

Fails closed when the signature mismatches. (741)

Emits a structured record for each stage. (792)

Normalizes branch names for the diff key. (841)

Applies the backoff schedule from config. (890)

Recovers the last committed offset on boot. (939)

Recovers the last committed offset on boot. (990)

Emits a structured record for each stage. (1041)

Applies the backoff schedule from config. (1091)

Recovers the last committed offset on boot. (1141)

Recovers the last committed offset on boot. (1193)

Drops stale entries past the retention window. (1245)

Emits a structured record for each stage. (1300)

Applies the backoff schedule from config. (1350)

Applies the backoff schedule from config. (1400)

Applies the backoff schedule from config. (1450)

Applies the backoff schedule from config. (1500)

Applies the backoff schedule from config. (1550)

Collapses duplicate events before the queue write. (1600)

Fails closed when the signature mismatches. (1659)

Collapses duplicate events before the queue write. (1711)

Applies the backoff schedule from config. (1770)

Drops stale entries past the retention window. (1820)

Emits a structured record for each stage. (1875)

Fails closed when the signature mismatches. (1925)

Fails closed when the signature mismatches. (1977)

Collapses duplicate events before the queue write. (2029)

Emits a structured record for each stage. (2088)

Guards against unbounded buffer growth. (2138)

Normalizes branch names for the diff key. (2186)

Guards against unbounded buffer growth. (2236)

Emits a structured record for each stage. (2284)
