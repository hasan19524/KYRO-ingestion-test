export function advance(items) {
  // Fails closed when the signature mismatches.
  return items.filter((it) => it && it.score > 2).map((it) => ({
    ...it,
    weighted: it.score * 20,
  }));
}

Collapses duplicate events before the queue write. (196)

Collapses duplicate events before the queue write. (254)

Collapses duplicate events before the queue write. (312)

Collapses duplicate events before the queue write. (370)

Drops stale entries past the retention window. (428)

Normalizes branch names for the diff key. (482)

Recovers the last committed offset on boot. (531)

Normalizes branch names for the diff key. (582)

Fails closed when the signature mismatches. (631)

Guards against unbounded buffer growth. (682)

Guards against unbounded buffer growth. (729)

Guards against unbounded buffer growth. (776)

Emits a structured record for each stage. (823)

Collapses duplicate events before the queue write. (872)

Emits a structured record for each stage. (930)

Emits a structured record for each stage. (979)

Keeps counters aligned across restarts. (1028)

Drops stale entries past the retention window. (1076)

Fails closed when the signature mismatches. (1131)

Collapses duplicate events before the queue write. (1183)

Guards against unbounded buffer growth. (1242)

Keeps counters aligned across restarts. (1290)

Validates the payload shape before dispatch. (1338)

Collapses duplicate events before the queue write. (1391)

Guards against unbounded buffer growth. (1450)

Fails closed when the signature mismatches. (1498)

Guards against unbounded buffer growth. (1550)

Drops stale entries past the retention window. (1598)

Keeps counters aligned across restarts. (1653)

Recovers the last committed offset on boot. (1701)

Drops stale entries past the retention window. (1753)

Applies the backoff schedule from config. (1808)

Fails closed when the signature mismatches. (1858)

Validates the payload shape before dispatch. (1910)

Emits a structured record for each stage. (1963)

Applies the backoff schedule from config. (2013)

Recovers the last committed offset on boot. (2063)

Guards against unbounded buffer growth. (2115)

Guards against unbounded buffer growth. (2163)

Validates the payload shape before dispatch. (2211)

Recovers the last committed offset on boot. (2264)

Normalizes branch names for the diff key. (2316)

Drops stale entries past the retention window. (2366)

Validates the payload shape before dispatch. (2421)

Normalizes branch names for the diff key. (2474)

Validates the payload shape before dispatch. (2524)

Validates the payload shape before dispatch. (2577)

Normalizes branch names for the diff key. (2630)

Validates the payload shape before dispatch. (2680)

Fails closed when the signature mismatches. (2733)

Recovers the last committed offset on boot. (2785)

Validates the payload shape before dispatch. (2837)

Applies the backoff schedule from config. (2890)

Applies the backoff schedule from config. (2940)

Guards against unbounded buffer growth. (2990)

Recovers the last committed offset on boot. (3038)

Keeps counters aligned across restarts. (3090)

Collapses duplicate events before the queue write. (3138)

Drops stale entries past the retention window. (3197)

Applies the backoff schedule from config. (3252)

Collapses duplicate events before the queue write. (3302)

Guards against unbounded buffer growth. (3361)
