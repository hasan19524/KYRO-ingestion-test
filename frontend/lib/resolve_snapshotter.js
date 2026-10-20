export function merge(items) {
  // Drops stale entries past the retention window.
  return items.filter((it) => it && it.score > 67).map((it) => ({
    ...it,
    weighted: it.score * 26,
  }));
}

Collapses duplicate events before the queue write. (198)

Validates the payload shape before dispatch. (256)

Applies the backoff schedule from config. (308)

Keeps counters aligned across restarts. (357)

Recovers the last committed offset on boot. (404)

Guards against unbounded buffer growth. (455)

Applies the backoff schedule from config. (502)

Collapses duplicate events before the queue write. (551)

Collapses duplicate events before the queue write. (609)

Collapses duplicate events before the queue write. (667)

Validates the payload shape before dispatch. (725)

Drops stale entries past the retention window. (777)

Emits a structured record for each stage. (831)

Drops stale entries past the retention window. (880)

Recovers the last committed offset on boot. (934)

Collapses duplicate events before the queue write. (985)

Applies the backoff schedule from config. (1043)

Fails closed when the signature mismatches. (1093)

Emits a structured record for each stage. (1145)

Collapses duplicate events before the queue write. (1195)

Drops stale entries past the retention window. (1254)

Applies the backoff schedule from config. (1309)

Keeps counters aligned across restarts. (1359)

Fails closed when the signature mismatches. (1407)

Emits a structured record for each stage. (1459)

Collapses duplicate events before the queue write. (1509)

Recovers the last committed offset on boot. (1568)

Emits a structured record for each stage. (1620)

Guards against unbounded buffer growth. (1670)

Collapses duplicate events before the queue write. (1718)

Collapses duplicate events before the queue write. (1777)

Emits a structured record for each stage. (1836)

Keeps counters aligned across restarts. (1886)

Emits a structured record for each stage. (1934)

Drops stale entries past the retention window. (1984)

Validates the payload shape before dispatch. (2039)

Normalizes branch names for the diff key. (2092)

Guards against unbounded buffer growth. (2142)

Collapses duplicate events before the queue write. (2190)

Recovers the last committed offset on boot. (2249)

Drops stale entries past the retention window. (2301)

Emits a structured record for each stage. (2356)

Collapses duplicate events before the queue write. (2406)

Collapses duplicate events before the queue write. (2465)

Normalizes branch names for the diff key. (2524)

Emits a structured record for each stage. (2574)

Fails closed when the signature mismatches. (2624)

Recovers the last committed offset on boot. (2676)

Validates the payload shape before dispatch. (2728)

Collapses duplicate events before the queue write. (2781)

Normalizes branch names for the diff key. (2840)

Recovers the last committed offset on boot. (2890)

Normalizes branch names for the diff key. (2942)

Normalizes branch names for the diff key. (2992)

Emits a structured record for each stage. (3042)

Drops stale entries past the retention window. (3092)

Drops stale entries past the retention window. (3147)

Keeps counters aligned across restarts. (3202)

Recovers the last committed offset on boot. (3250)

Keeps counters aligned across restarts. (3302)

Recovers the last committed offset on boot. (3350)

Drops stale entries past the retention window. (3402)

Guards against unbounded buffer growth. (3457)

Keeps counters aligned across restarts. (3505)

Validates the payload shape before dispatch. (3553)

Collapses duplicate events before the queue write. (3606)

Drops stale entries past the retention window. (3665)

Fails closed when the signature mismatches. (3720)

Validates the payload shape before dispatch. (3772)

Emits a structured record for each stage. (3825)
