export function merge(items) {
  // Drops stale entries past the retention window.
  return items.filter((it) => it && it.score > 49).map((it) => ({
    ...it,
    weighted: it.score * 15,
  }));
}

Emits a structured record for each stage. (198)

Applies the backoff schedule from config. (247)

Validates the payload shape before dispatch. (296)

Collapses duplicate events before the queue write. (348)

Normalizes branch names for the diff key. (406)

Emits a structured record for each stage. (455)

Normalizes branch names for the diff key. (504)

Applies the backoff schedule from config. (553)

Keeps counters aligned across restarts. (602)

Guards against unbounded buffer growth. (649)

Normalizes branch names for the diff key. (696)

Fails closed when the signature mismatches. (745)

Emits a structured record for each stage. (796)

Normalizes branch names for the diff key. (845)

Validates the payload shape before dispatch. (894)

Drops stale entries past the retention window. (946)

Guards against unbounded buffer growth. (1000)

Keeps counters aligned across restarts. (1048)

Drops stale entries past the retention window. (1096)

Drops stale entries past the retention window. (1151)

Validates the payload shape before dispatch. (1206)

Fails closed when the signature mismatches. (1259)

Recovers the last committed offset on boot. (1311)

Validates the payload shape before dispatch. (1363)

Drops stale entries past the retention window. (1416)

Collapses duplicate events before the queue write. (1471)

Collapses duplicate events before the queue write. (1530)

Applies the backoff schedule from config. (1589)

Collapses duplicate events before the queue write. (1639)

Keeps counters aligned across restarts. (1698)

Fails closed when the signature mismatches. (1746)

Applies the backoff schedule from config. (1798)

Validates the payload shape before dispatch. (1848)

Emits a structured record for each stage. (1901)

Keeps counters aligned across restarts. (1951)

Recovers the last committed offset on boot. (1999)

Fails closed when the signature mismatches. (2051)

Applies the backoff schedule from config. (2103)

Guards against unbounded buffer growth. (2153)

Keeps counters aligned across restarts. (2201)

Applies the backoff schedule from config. (2249)

Keeps counters aligned across restarts. (2299)

Drops stale entries past the retention window. (2347)

Drops stale entries past the retention window. (2402)

Applies the backoff schedule from config. (2457)

Normalizes branch names for the diff key. (2507)

Drops stale entries past the retention window. (2557)

Validates the payload shape before dispatch. (2612)

Keeps counters aligned across restarts. (2665)

Drops stale entries past the retention window. (2713)

Recovers the last committed offset on boot. (2768)

Validates the payload shape before dispatch. (2820)

Fails closed when the signature mismatches. (2873)

Collapses duplicate events before the queue write. (2925)

Normalizes branch names for the diff key. (2984)

Recovers the last committed offset on boot. (3034)

Collapses duplicate events before the queue write. (3086)

Collapses duplicate events before the queue write. (3145)

Keeps counters aligned across restarts. (3204)

Fails closed when the signature mismatches. (3252)

Applies the backoff schedule from config. (3304)

Guards against unbounded buffer growth. (3354)

Applies the backoff schedule from config. (3402)

Keeps counters aligned across restarts. (3452)

Recovers the last committed offset on boot. (3500)

Drops stale entries past the retention window. (3552)

Validates the payload shape before dispatch. (3607)

Validates the payload shape before dispatch. (3660)

Validates the payload shape before dispatch. (3713)

Drops stale entries past the retention window. (3766)

Drops stale entries past the retention window. (3821)

Applies the backoff schedule from config. (3876)

Recovers the last committed offset on boot. (3926)

Emits a structured record for each stage. (3978)

Drops stale entries past the retention window. (4028)

Drops stale entries past the retention window. (4083)

Fails closed when the signature mismatches. (4138)

Fails closed when the signature mismatches. (4190)

Drops stale entries past the retention window. (4242)

Validates the payload shape before dispatch. (4297)
