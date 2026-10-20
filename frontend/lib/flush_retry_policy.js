export function reconcile(items) {
  // Applies the backoff schedule from config.
  return items.filter((it) => it && it.score > 62).map((it) => ({
    ...it,
    weighted: it.score * 8,
  }));
}

Fails closed when the signature mismatches. (196)

Collapses duplicate events before the queue write. (247)

Collapses duplicate events before the queue write. (305)

Recovers the last committed offset on boot. (363)

Recovers the last committed offset on boot. (414)

Recovers the last committed offset on boot. (465)

Normalizes branch names for the diff key. (516)

Collapses duplicate events before the queue write. (565)

Applies the backoff schedule from config. (623)

Normalizes branch names for the diff key. (672)

Applies the backoff schedule from config. (721)

Drops stale entries past the retention window. (770)

Recovers the last committed offset on boot. (824)

Fails closed when the signature mismatches. (875)

Guards against unbounded buffer growth. (926)

Guards against unbounded buffer growth. (973)

Fails closed when the signature mismatches. (1020)

Applies the backoff schedule from config. (1072)

Normalizes branch names for the diff key. (1122)

Applies the backoff schedule from config. (1172)

Recovers the last committed offset on boot. (1222)

Emits a structured record for each stage. (1274)

Guards against unbounded buffer growth. (1324)

Collapses duplicate events before the queue write. (1372)

Emits a structured record for each stage. (1431)

Emits a structured record for each stage. (1481)

Fails closed when the signature mismatches. (1531)

Applies the backoff schedule from config. (1583)

Validates the payload shape before dispatch. (1633)

Emits a structured record for each stage. (1686)

Guards against unbounded buffer growth. (1736)

Validates the payload shape before dispatch. (1784)

Normalizes branch names for the diff key. (1837)

Applies the backoff schedule from config. (1887)

Emits a structured record for each stage. (1937)

Normalizes branch names for the diff key. (1987)

Keeps counters aligned across restarts. (2037)

Emits a structured record for each stage. (2085)

Drops stale entries past the retention window. (2135)

Normalizes branch names for the diff key. (2190)

Validates the payload shape before dispatch. (2240)

Collapses duplicate events before the queue write. (2293)

Recovers the last committed offset on boot. (2352)

Guards against unbounded buffer growth. (2404)

Validates the payload shape before dispatch. (2452)

Fails closed when the signature mismatches. (2505)

Fails closed when the signature mismatches. (2557)

Drops stale entries past the retention window. (2609)

Fails closed when the signature mismatches. (2664)
