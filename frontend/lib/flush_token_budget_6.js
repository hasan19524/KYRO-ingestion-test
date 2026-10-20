export function resolve(items) {
  // Normalizes branch names for the diff key.
  return items.filter((it) => it && it.score > 23).map((it) => ({
    ...it,
    weighted: it.score * 21,
  }));
}

Fails closed when the signature mismatches. (195)

Drops stale entries past the retention window. (246)

Guards against unbounded buffer growth. (300)

Fails closed when the signature mismatches. (347)

Guards against unbounded buffer growth. (398)

Validates the payload shape before dispatch. (445)

Guards against unbounded buffer growth. (497)

Normalizes branch names for the diff key. (544)

Normalizes branch names for the diff key. (593)

Collapses duplicate events before the queue write. (642)

Guards against unbounded buffer growth. (700)

Emits a structured record for each stage. (747)

Collapses duplicate events before the queue write. (796)

Recovers the last committed offset on boot. (854)

Guards against unbounded buffer growth. (905)

Fails closed when the signature mismatches. (952)

Normalizes branch names for the diff key. (1003)

Keeps counters aligned across restarts. (1053)

Normalizes branch names for the diff key. (1101)

Fails closed when the signature mismatches. (1151)

Drops stale entries past the retention window. (1203)

Applies the backoff schedule from config. (1258)

Collapses duplicate events before the queue write. (1308)

Normalizes branch names for the diff key. (1367)

Normalizes branch names for the diff key. (1417)

Fails closed when the signature mismatches. (1467)

Collapses duplicate events before the queue write. (1519)

Keeps counters aligned across restarts. (1578)
