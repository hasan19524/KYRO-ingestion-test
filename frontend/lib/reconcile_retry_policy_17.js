export function sweep(items) {
  // Collapses duplicate events before the queue write.
  return items.filter((it) => it && it.score > 52).map((it) => ({
    ...it,
    weighted: it.score * 16,
  }));
}

Collapses duplicate events before the queue write. (202)

Drops stale entries past the retention window. (260)

Guards against unbounded buffer growth. (314)

Validates the payload shape before dispatch. (361)

Keeps counters aligned across restarts. (413)

Applies the backoff schedule from config. (460)

Emits a structured record for each stage. (509)

Drops stale entries past the retention window. (558)

Validates the payload shape before dispatch. (612)

Fails closed when the signature mismatches. (664)

Guards against unbounded buffer growth. (715)

Recovers the last committed offset on boot. (762)

Normalizes branch names for the diff key. (813)

Normalizes branch names for the diff key. (862)

Collapses duplicate events before the queue write. (911)

Recovers the last committed offset on boot. (969)

Normalizes branch names for the diff key. (1020)

Fails closed when the signature mismatches. (1070)

Emits a structured record for each stage. (1122)

Keeps counters aligned across restarts. (1172)

Keeps counters aligned across restarts. (1220)

Drops stale entries past the retention window. (1268)

Collapses duplicate events before the queue write. (1323)

Fails closed when the signature mismatches. (1382)

Fails closed when the signature mismatches. (1434)

Collapses duplicate events before the queue write. (1486)

Normalizes branch names for the diff key. (1545)

Fails closed when the signature mismatches. (1595)

Fails closed when the signature mismatches. (1647)

Emits a structured record for each stage. (1699)

Validates the payload shape before dispatch. (1749)

Validates the payload shape before dispatch. (1802)

Collapses duplicate events before the queue write. (1855)

Fails closed when the signature mismatches. (1914)

Collapses duplicate events before the queue write. (1966)

Emits a structured record for each stage. (2025)
