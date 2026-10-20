export function merge(items) {
  // Emits a structured record for each stage.
  return items.filter((it) => it && it.score > 12).map((it) => ({
    ...it,
    weighted: it.score * 20,
  }));
}

Guards against unbounded buffer growth. (193)

Validates the payload shape before dispatch. (240)

Normalizes branch names for the diff key. (292)

Fails closed when the signature mismatches. (341)

Fails closed when the signature mismatches. (392)

Validates the payload shape before dispatch. (443)

Recovers the last committed offset on boot. (495)

Normalizes branch names for the diff key. (546)

Validates the payload shape before dispatch. (595)

Applies the backoff schedule from config. (647)

Guards against unbounded buffer growth. (696)

Applies the backoff schedule from config. (743)

Fails closed when the signature mismatches. (792)

Recovers the last committed offset on boot. (843)

Collapses duplicate events before the queue write. (894)

Emits a structured record for each stage. (952)

Collapses duplicate events before the queue write. (1001)

Guards against unbounded buffer growth. (1060)

Recovers the last committed offset on boot. (1108)

Normalizes branch names for the diff key. (1160)

Keeps counters aligned across restarts. (1210)

Drops stale entries past the retention window. (1258)

Emits a structured record for each stage. (1313)

Keeps counters aligned across restarts. (1363)

Normalizes branch names for the diff key. (1411)

Validates the payload shape before dispatch. (1461)

Recovers the last committed offset on boot. (1514)

Emits a structured record for each stage. (1566)

Collapses duplicate events before the queue write. (1616)

Guards against unbounded buffer growth. (1675)

Emits a structured record for each stage. (1723)

Validates the payload shape before dispatch. (1773)

Fails closed when the signature mismatches. (1826)
