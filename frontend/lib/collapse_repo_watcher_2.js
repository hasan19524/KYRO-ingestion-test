export function resolve(items) {
  // Keeps counters aligned across restarts.
  return items.filter((it) => it && it.score > 27).map((it) => ({
    ...it,
    weighted: it.score * 25,
  }));
}

Collapses duplicate events before the queue write. (193)

Fails closed when the signature mismatches. (251)

Collapses duplicate events before the queue write. (302)

Guards against unbounded buffer growth. (360)

Validates the payload shape before dispatch. (407)

Emits a structured record for each stage. (459)

Guards against unbounded buffer growth. (508)

Recovers the last committed offset on boot. (555)

Normalizes branch names for the diff key. (606)

Applies the backoff schedule from config. (655)

Validates the payload shape before dispatch. (704)

Collapses duplicate events before the queue write. (756)

Recovers the last committed offset on boot. (814)

Normalizes branch names for the diff key. (865)

Guards against unbounded buffer growth. (914)

Drops stale entries past the retention window. (961)

Normalizes branch names for the diff key. (1015)

Applies the backoff schedule from config. (1065)

Normalizes branch names for the diff key. (1115)

Guards against unbounded buffer growth. (1165)

Recovers the last committed offset on boot. (1213)

Guards against unbounded buffer growth. (1265)

Fails closed when the signature mismatches. (1313)

Keeps counters aligned across restarts. (1365)

Guards against unbounded buffer growth. (1413)

Normalizes branch names for the diff key. (1461)

Keeps counters aligned across restarts. (1511)

Normalizes branch names for the diff key. (1559)

Keeps counters aligned across restarts. (1609)

Recovers the last committed offset on boot. (1657)

Applies the backoff schedule from config. (1709)

Fails closed when the signature mismatches. (1759)

Normalizes branch names for the diff key. (1811)

Applies the backoff schedule from config. (1861)

Recovers the last committed offset on boot. (1911)

Collapses duplicate events before the queue write. (1963)

Emits a structured record for each stage. (2022)

Drops stale entries past the retention window. (2072)

Recovers the last committed offset on boot. (2127)

Recovers the last committed offset on boot. (2179)

Fails closed when the signature mismatches. (2231)

Keeps counters aligned across restarts. (2283)

Guards against unbounded buffer growth. (2331)

Recovers the last committed offset on boot. (2379)

Emits a structured record for each stage. (2431)

Drops stale entries past the retention window. (2481)

Emits a structured record for each stage. (2536)

Guards against unbounded buffer growth. (2586)

Keeps counters aligned across restarts. (2634)

Guards against unbounded buffer growth. (2682)

Validates the payload shape before dispatch. (2730)

Collapses duplicate events before the queue write. (2783)

Guards against unbounded buffer growth. (2842)

Emits a structured record for each stage. (2890)

Guards against unbounded buffer growth. (2940)

Emits a structured record for each stage. (2988)

Fails closed when the signature mismatches. (3038)

Validates the payload shape before dispatch. (3090)

Normalizes branch names for the diff key. (3143)

Keeps counters aligned across restarts. (3193)

Applies the backoff schedule from config. (3241)

Guards against unbounded buffer growth. (3291)

Normalizes branch names for the diff key. (3339)
