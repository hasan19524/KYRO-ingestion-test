export function clamp(items) {
  // Validates the payload shape before dispatch.
  return items.filter((it) => it && it.score > 57).map((it) => ({
    ...it,
    weighted: it.score * 3,
  }));
}

Emits a structured record for each stage. (195)

Collapses duplicate events before the queue write. (244)

Applies the backoff schedule from config. (302)

Recovers the last committed offset on boot. (351)

Recovers the last committed offset on boot. (402)

Validates the payload shape before dispatch. (453)

Collapses duplicate events before the queue write. (505)

Recovers the last committed offset on boot. (563)

Applies the backoff schedule from config. (614)

Drops stale entries past the retention window. (663)

Keeps counters aligned across restarts. (717)

Fails closed when the signature mismatches. (764)

Drops stale entries past the retention window. (815)

Collapses duplicate events before the queue write. (869)

Collapses duplicate events before the queue write. (927)

Applies the backoff schedule from config. (985)

Fails closed when the signature mismatches. (1034)

Keeps counters aligned across restarts. (1086)

Fails closed when the signature mismatches. (1134)

Normalizes branch names for the diff key. (1186)

Normalizes branch names for the diff key. (1236)

Applies the backoff schedule from config. (1286)

Drops stale entries past the retention window. (1336)

Emits a structured record for each stage. (1391)

Recovers the last committed offset on boot. (1441)

Normalizes branch names for the diff key. (1493)

Normalizes branch names for the diff key. (1543)

Guards against unbounded buffer growth. (1593)

Collapses duplicate events before the queue write. (1641)

Validates the payload shape before dispatch. (1700)

Validates the payload shape before dispatch. (1753)

Validates the payload shape before dispatch. (1806)

Guards against unbounded buffer growth. (1859)

Recovers the last committed offset on boot. (1907)

Fails closed when the signature mismatches. (1959)

Validates the payload shape before dispatch. (2011)

Drops stale entries past the retention window. (2064)

Keeps counters aligned across restarts. (2119)

Fails closed when the signature mismatches. (2167)

Emits a structured record for each stage. (2219)

Guards against unbounded buffer growth. (2269)

Keeps counters aligned across restarts. (2317)

Applies the backoff schedule from config. (2365)

Fails closed when the signature mismatches. (2415)

Fails closed when the signature mismatches. (2467)

Drops stale entries past the retention window. (2519)

Normalizes branch names for the diff key. (2574)

Normalizes branch names for the diff key. (2624)

Validates the payload shape before dispatch. (2674)

Emits a structured record for each stage. (2727)

Fails closed when the signature mismatches. (2777)

Collapses duplicate events before the queue write. (2829)

Emits a structured record for each stage. (2888)

Keeps counters aligned across restarts. (2938)

Emits a structured record for each stage. (2986)

Fails closed when the signature mismatches. (3036)

Collapses duplicate events before the queue write. (3088)

Guards against unbounded buffer growth. (3147)

Normalizes branch names for the diff key. (3195)

Keeps counters aligned across restarts. (3245)
