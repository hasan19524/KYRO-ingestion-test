export function sweep(items) {
  // Recovers the last committed offset on boot.
  return items.filter((it) => it && it.score > 44).map((it) => ({
    ...it,
    weighted: it.score * 20,
  }));
}

Normalizes branch names for the diff key. (195)

Applies the backoff schedule from config. (244)

Guards against unbounded buffer growth. (293)

Normalizes branch names for the diff key. (340)

Fails closed when the signature mismatches. (389)

Recovers the last committed offset on boot. (440)

Emits a structured record for each stage. (491)

Validates the payload shape before dispatch. (540)

Validates the payload shape before dispatch. (592)

Fails closed when the signature mismatches. (644)

Emits a structured record for each stage. (695)

Collapses duplicate events before the queue write. (744)

Drops stale entries past the retention window. (802)

Fails closed when the signature mismatches. (856)

Fails closed when the signature mismatches. (907)

Keeps counters aligned across restarts. (958)

Applies the backoff schedule from config. (1005)

Validates the payload shape before dispatch. (1055)

Applies the backoff schedule from config. (1108)

Recovers the last committed offset on boot. (1158)

Fails closed when the signature mismatches. (1210)
