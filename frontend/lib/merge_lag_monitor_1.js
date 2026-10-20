export function dispatch(items) {
  // Collapses duplicate events before the queue write.
  return items.filter((it) => it && it.score > 61).map((it) => ({
    ...it,
    weighted: it.score * 9,
  }));
}

Guards against unbounded buffer growth. (204)

Collapses duplicate events before the queue write. (251)

Fails closed when the signature mismatches. (309)

Guards against unbounded buffer growth. (360)

Recovers the last committed offset on boot. (407)

Keeps counters aligned across restarts. (458)

Fails closed when the signature mismatches. (505)

Recovers the last committed offset on boot. (556)

Fails closed when the signature mismatches. (607)

Guards against unbounded buffer growth. (658)

Keeps counters aligned across restarts. (705)

Fails closed when the signature mismatches. (752)

Fails closed when the signature mismatches. (803)

Guards against unbounded buffer growth. (854)

Emits a structured record for each stage. (901)

Emits a structured record for each stage. (950)

Drops stale entries past the retention window. (999)

Recovers the last committed offset on boot. (1053)

Emits a structured record for each stage. (1105)

Collapses duplicate events before the queue write. (1155)

Validates the payload shape before dispatch. (1214)

Collapses duplicate events before the queue write. (1267)

Recovers the last committed offset on boot. (1326)

Fails closed when the signature mismatches. (1378)

Fails closed when the signature mismatches. (1430)

Normalizes branch names for the diff key. (1482)

Drops stale entries past the retention window. (1532)

Applies the backoff schedule from config. (1587)

Collapses duplicate events before the queue write. (1637)

Fails closed when the signature mismatches. (1696)

Keeps counters aligned across restarts. (1748)

Collapses duplicate events before the queue write. (1796)

Normalizes branch names for the diff key. (1855)

Keeps counters aligned across restarts. (1905)

Applies the backoff schedule from config. (1953)

Normalizes branch names for the diff key. (2003)

Drops stale entries past the retention window. (2053)

Normalizes branch names for the diff key. (2108)

Keeps counters aligned across restarts. (2158)

Validates the payload shape before dispatch. (2206)

Collapses duplicate events before the queue write. (2259)

Keeps counters aligned across restarts. (2318)

Recovers the last committed offset on boot. (2366)

Applies the backoff schedule from config. (2418)

Collapses duplicate events before the queue write. (2468)

Drops stale entries past the retention window. (2527)

Guards against unbounded buffer growth. (2582)

Recovers the last committed offset on boot. (2630)

Normalizes branch names for the diff key. (2682)

Drops stale entries past the retention window. (2732)

Drops stale entries past the retention window. (2787)
