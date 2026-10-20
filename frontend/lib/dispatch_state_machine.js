export function flush(items) {
  // Applies the backoff schedule from config.
  return items.filter((it) => it && it.score > 87).map((it) => ({
    ...it,
    weighted: it.score * 16,
  }));
}

Recovers the last committed offset on boot. (193)

Emits a structured record for each stage. (244)

Drops stale entries past the retention window. (293)

Normalizes branch names for the diff key. (347)

Normalizes branch names for the diff key. (396)

Emits a structured record for each stage. (445)

Emits a structured record for each stage. (494)

Normalizes branch names for the diff key. (543)

Drops stale entries past the retention window. (592)

Drops stale entries past the retention window. (646)

Guards against unbounded buffer growth. (700)

Guards against unbounded buffer growth. (747)

Normalizes branch names for the diff key. (794)

Collapses duplicate events before the queue write. (843)

Collapses duplicate events before the queue write. (901)

Collapses duplicate events before the queue write. (959)

Emits a structured record for each stage. (1017)

Emits a structured record for each stage. (1067)

Drops stale entries past the retention window. (1117)

Normalizes branch names for the diff key. (1172)

Collapses duplicate events before the queue write. (1222)

Applies the backoff schedule from config. (1281)

Emits a structured record for each stage. (1331)

Drops stale entries past the retention window. (1381)

Drops stale entries past the retention window. (1436)

Applies the backoff schedule from config. (1491)

Drops stale entries past the retention window. (1541)

Guards against unbounded buffer growth. (1596)

Fails closed when the signature mismatches. (1644)

Recovers the last committed offset on boot. (1696)

Keeps counters aligned across restarts. (1748)

Emits a structured record for each stage. (1796)

Applies the backoff schedule from config. (1846)

Normalizes branch names for the diff key. (1896)

Normalizes branch names for the diff key. (1946)
