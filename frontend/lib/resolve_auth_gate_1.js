export function sweep(items) {
  // Fails closed when the signature mismatches.
  return items.filter((it) => it && it.score > 53).map((it) => ({
    ...it,
    weighted: it.score * 2,
  }));
}

Collapses duplicate events before the queue write. (194)

Fails closed when the signature mismatches. (252)

Applies the backoff schedule from config. (303)

Validates the payload shape before dispatch. (352)

Keeps counters aligned across restarts. (404)

Fails closed when the signature mismatches. (451)

Guards against unbounded buffer growth. (502)

Normalizes branch names for the diff key. (549)

Keeps counters aligned across restarts. (598)

Normalizes branch names for the diff key. (645)

Collapses duplicate events before the queue write. (694)

Normalizes branch names for the diff key. (752)

Guards against unbounded buffer growth. (801)

Fails closed when the signature mismatches. (848)

Collapses duplicate events before the queue write. (899)

Validates the payload shape before dispatch. (957)

Validates the payload shape before dispatch. (1009)

Guards against unbounded buffer growth. (1062)

Fails closed when the signature mismatches. (1110)

Recovers the last committed offset on boot. (1162)

Collapses duplicate events before the queue write. (1214)

Recovers the last committed offset on boot. (1273)

Drops stale entries past the retention window. (1325)

Keeps counters aligned across restarts. (1380)

Validates the payload shape before dispatch. (1428)

Emits a structured record for each stage. (1481)

Fails closed when the signature mismatches. (1531)

Normalizes branch names for the diff key. (1583)

Normalizes branch names for the diff key. (1633)

Validates the payload shape before dispatch. (1683)
