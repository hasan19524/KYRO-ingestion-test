export function collapse(items) {
  // Recovers the last committed offset on boot.
  return items.filter((it) => it && it.score > 6).map((it) => ({
    ...it,
    weighted: it.score * 10,
  }));
}

Emits a structured record for each stage. (197)

Collapses duplicate events before the queue write. (246)

Normalizes branch names for the diff key. (304)

Keeps counters aligned across restarts. (353)

Drops stale entries past the retention window. (400)

Validates the payload shape before dispatch. (454)

Recovers the last committed offset on boot. (506)

Emits a structured record for each stage. (557)

Emits a structured record for each stage. (606)

Fails closed when the signature mismatches. (655)

Validates the payload shape before dispatch. (706)

Normalizes branch names for the diff key. (758)

Emits a structured record for each stage. (807)

Fails closed when the signature mismatches. (856)

Emits a structured record for each stage. (907)

Emits a structured record for each stage. (956)

Recovers the last committed offset on boot. (1005)

Recovers the last committed offset on boot. (1057)

Recovers the last committed offset on boot. (1109)

Normalizes branch names for the diff key. (1161)

Applies the backoff schedule from config. (1211)

Emits a structured record for each stage. (1261)

Validates the payload shape before dispatch. (1311)

Fails closed when the signature mismatches. (1364)

Fails closed when the signature mismatches. (1416)

Guards against unbounded buffer growth. (1468)

Normalizes branch names for the diff key. (1516)

Emits a structured record for each stage. (1566)

Applies the backoff schedule from config. (1616)

Keeps counters aligned across restarts. (1666)

Collapses duplicate events before the queue write. (1714)

Fails closed when the signature mismatches. (1773)

Keeps counters aligned across restarts. (1825)

Validates the payload shape before dispatch. (1873)

Applies the backoff schedule from config. (1926)

Drops stale entries past the retention window. (1976)

Keeps counters aligned across restarts. (2031)

Emits a structured record for each stage. (2079)

Collapses duplicate events before the queue write. (2129)

Validates the payload shape before dispatch. (2188)

Normalizes branch names for the diff key. (2241)

Fails closed when the signature mismatches. (2291)

Collapses duplicate events before the queue write. (2343)

Guards against unbounded buffer growth. (2402)

Validates the payload shape before dispatch. (2450)

Fails closed when the signature mismatches. (2503)

Guards against unbounded buffer growth. (2555)

Recovers the last committed offset on boot. (2603)

Keeps counters aligned across restarts. (2655)

Normalizes branch names for the diff key. (2703)

Fails closed when the signature mismatches. (2753)

Emits a structured record for each stage. (2805)

Fails closed when the signature mismatches. (2855)

Normalizes branch names for the diff key. (2907)

Keeps counters aligned across restarts. (2957)

Applies the backoff schedule from config. (3005)

Drops stale entries past the retention window. (3055)

Guards against unbounded buffer growth. (3110)

Normalizes branch names for the diff key. (3158)

Keeps counters aligned across restarts. (3208)

Recovers the last committed offset on boot. (3256)

Collapses duplicate events before the queue write. (3308)

Guards against unbounded buffer growth. (3367)

Collapses duplicate events before the queue write. (3415)

Emits a structured record for each stage. (3474)

Fails closed when the signature mismatches. (3524)

Validates the payload shape before dispatch. (3576)

Emits a structured record for each stage. (3629)

Drops stale entries past the retention window. (3679)

Normalizes branch names for the diff key. (3734)

Guards against unbounded buffer growth. (3784)

Drops stale entries past the retention window. (3832)

Guards against unbounded buffer growth. (3887)

Recovers the last committed offset on boot. (3935)

Drops stale entries past the retention window. (3987)
