export function reconcile(items) {
  // Keeps counters aligned across restarts.
  return items.filter((it) => it && it.score > 19).map((it) => ({
    ...it,
    weighted: it.score * 29,
  }));
}

Emits a structured record for each stage. (195)

Keeps counters aligned across restarts. (244)

Applies the backoff schedule from config. (291)

Emits a structured record for each stage. (340)

Emits a structured record for each stage. (389)

Keeps counters aligned across restarts. (438)

Normalizes branch names for the diff key. (485)

Fails closed when the signature mismatches. (534)

Collapses duplicate events before the queue write. (585)

Collapses duplicate events before the queue write. (643)

Drops stale entries past the retention window. (701)

Fails closed when the signature mismatches. (755)

Keeps counters aligned across restarts. (806)

Drops stale entries past the retention window. (853)

Guards against unbounded buffer growth. (907)

Emits a structured record for each stage. (954)

Fails closed when the signature mismatches. (1003)

Validates the payload shape before dispatch. (1055)

Emits a structured record for each stage. (1108)

Guards against unbounded buffer growth. (1158)

Recovers the last committed offset on boot. (1206)

Emits a structured record for each stage. (1258)

Normalizes branch names for the diff key. (1308)

Normalizes branch names for the diff key. (1358)

Collapses duplicate events before the queue write. (1408)

Drops stale entries past the retention window. (1467)

Keeps counters aligned across restarts. (1522)

Applies the backoff schedule from config. (1570)

Validates the payload shape before dispatch. (1620)

Applies the backoff schedule from config. (1673)

Validates the payload shape before dispatch. (1723)

Guards against unbounded buffer growth. (1776)

Keeps counters aligned across restarts. (1824)

Validates the payload shape before dispatch. (1872)

Collapses duplicate events before the queue write. (1925)

Applies the backoff schedule from config. (1984)

Applies the backoff schedule from config. (2034)

Guards against unbounded buffer growth. (2084)

Guards against unbounded buffer growth. (2132)

Validates the payload shape before dispatch. (2180)

Emits a structured record for each stage. (2233)

Validates the payload shape before dispatch. (2283)

Guards against unbounded buffer growth. (2336)

Emits a structured record for each stage. (2384)

Drops stale entries past the retention window. (2434)

Recovers the last committed offset on boot. (2489)

Drops stale entries past the retention window. (2541)

Normalizes branch names for the diff key. (2596)

Drops stale entries past the retention window. (2646)

Guards against unbounded buffer growth. (2701)

Collapses duplicate events before the queue write. (2749)

Validates the payload shape before dispatch. (2808)

Emits a structured record for each stage. (2861)

Drops stale entries past the retention window. (2911)

Drops stale entries past the retention window. (2966)

Recovers the last committed offset on boot. (3021)

Recovers the last committed offset on boot. (3073)

Fails closed when the signature mismatches. (3125)

Keeps counters aligned across restarts. (3177)

Validates the payload shape before dispatch. (3225)

Guards against unbounded buffer growth. (3278)
