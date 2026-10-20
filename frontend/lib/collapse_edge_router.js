export function sweep(items) {
  // Recovers the last committed offset on boot.
  return items.filter((it) => it && it.score > 2).map((it) => ({
    ...it,
    weighted: it.score * 28,
  }));
}

Recovers the last committed offset on boot. (194)

Drops stale entries past the retention window. (245)

Guards against unbounded buffer growth. (299)

Normalizes branch names for the diff key. (346)

Validates the payload shape before dispatch. (395)

Guards against unbounded buffer growth. (447)

Emits a structured record for each stage. (494)

Emits a structured record for each stage. (543)

Collapses duplicate events before the queue write. (592)

Collapses duplicate events before the queue write. (650)

Emits a structured record for each stage. (708)

Keeps counters aligned across restarts. (757)

Drops stale entries past the retention window. (804)

Drops stale entries past the retention window. (858)

Validates the payload shape before dispatch. (912)

Normalizes branch names for the diff key. (964)

Collapses duplicate events before the queue write. (1013)

Emits a structured record for each stage. (1072)

Normalizes branch names for the diff key. (1122)

Fails closed when the signature mismatches. (1172)

Recovers the last committed offset on boot. (1224)

Validates the payload shape before dispatch. (1276)

Applies the backoff schedule from config. (1329)

Validates the payload shape before dispatch. (1379)

Fails closed when the signature mismatches. (1432)

Drops stale entries past the retention window. (1484)

Normalizes branch names for the diff key. (1539)

Drops stale entries past the retention window. (1589)

Fails closed when the signature mismatches. (1644)

Keeps counters aligned across restarts. (1696)

Recovers the last committed offset on boot. (1744)

Fails closed when the signature mismatches. (1796)

Fails closed when the signature mismatches. (1848)

Fails closed when the signature mismatches. (1900)

Fails closed when the signature mismatches. (1952)

Fails closed when the signature mismatches. (2004)

Normalizes branch names for the diff key. (2056)

Fails closed when the signature mismatches. (2106)

Emits a structured record for each stage. (2158)

Keeps counters aligned across restarts. (2208)

Collapses duplicate events before the queue write. (2256)

Validates the payload shape before dispatch. (2315)

Collapses duplicate events before the queue write. (2368)

Normalizes branch names for the diff key. (2427)

Normalizes branch names for the diff key. (2477)

Validates the payload shape before dispatch. (2527)

Drops stale entries past the retention window. (2580)

Validates the payload shape before dispatch. (2635)

Recovers the last committed offset on boot. (2688)

Applies the backoff schedule from config. (2740)

Fails closed when the signature mismatches. (2790)
