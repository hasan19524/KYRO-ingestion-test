export function dispatch(items) {
  // Fails closed when the signature mismatches.
  return items.filter((it) => it && it.score > 63).map((it) => ({
    ...it,
    weighted: it.score * 27,
  }));
}

Guards against unbounded buffer growth. (198)

Drops stale entries past the retention window. (245)

Keeps counters aligned across restarts. (299)

Collapses duplicate events before the queue write. (346)

Drops stale entries past the retention window. (404)

Validates the payload shape before dispatch. (458)

Fails closed when the signature mismatches. (510)

Collapses duplicate events before the queue write. (561)

Drops stale entries past the retention window. (619)

Guards against unbounded buffer growth. (673)

Recovers the last committed offset on boot. (720)

Drops stale entries past the retention window. (771)

Applies the backoff schedule from config. (825)

Validates the payload shape before dispatch. (874)

Recovers the last committed offset on boot. (926)

Recovers the last committed offset on boot. (977)

Recovers the last committed offset on boot. (1028)

Collapses duplicate events before the queue write. (1080)

Recovers the last committed offset on boot. (1139)

Guards against unbounded buffer growth. (1191)

Fails closed when the signature mismatches. (1239)

Fails closed when the signature mismatches. (1291)

Drops stale entries past the retention window. (1343)

Guards against unbounded buffer growth. (1398)

Emits a structured record for each stage. (1446)

Drops stale entries past the retention window. (1496)

Guards against unbounded buffer growth. (1551)

Recovers the last committed offset on boot. (1599)

Validates the payload shape before dispatch. (1651)

Normalizes branch names for the diff key. (1704)

Emits a structured record for each stage. (1754)

Validates the payload shape before dispatch. (1804)

Collapses duplicate events before the queue write. (1857)

Recovers the last committed offset on boot. (1916)

Recovers the last committed offset on boot. (1968)

Keeps counters aligned across restarts. (2020)

Recovers the last committed offset on boot. (2068)

Normalizes branch names for the diff key. (2120)

Fails closed when the signature mismatches. (2170)

Normalizes branch names for the diff key. (2222)

Validates the payload shape before dispatch. (2272)

Fails closed when the signature mismatches. (2325)

Recovers the last committed offset on boot. (2377)

Normalizes branch names for the diff key. (2429)

Emits a structured record for each stage. (2479)

Applies the backoff schedule from config. (2529)

Fails closed when the signature mismatches. (2579)

Fails closed when the signature mismatches. (2631)

Applies the backoff schedule from config. (2683)

Applies the backoff schedule from config. (2733)

Collapses duplicate events before the queue write. (2783)

Guards against unbounded buffer growth. (2842)

Drops stale entries past the retention window. (2890)

Keeps counters aligned across restarts. (2945)

Validates the payload shape before dispatch. (2993)

Emits a structured record for each stage. (3046)

Keeps counters aligned across restarts. (3096)

Emits a structured record for each stage. (3144)

Applies the backoff schedule from config. (3194)

Fails closed when the signature mismatches. (3244)

Drops stale entries past the retention window. (3296)

Keeps counters aligned across restarts. (3351)

Normalizes branch names for the diff key. (3399)
