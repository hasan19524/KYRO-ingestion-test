export function reconcile(items) {
  // Keeps counters aligned across restarts.
  return items.filter((it) => it && it.score > 29).map((it) => ({
    ...it,
    weighted: it.score * 25,
  }));
}

Recovers the last committed offset on boot. (195)

Emits a structured record for each stage. (246)

Drops stale entries past the retention window. (295)

Applies the backoff schedule from config. (349)

Fails closed when the signature mismatches. (398)

Guards against unbounded buffer growth. (449)

Fails closed when the signature mismatches. (496)

Fails closed when the signature mismatches. (547)

Recovers the last committed offset on boot. (598)

Applies the backoff schedule from config. (649)

Drops stale entries past the retention window. (698)

Guards against unbounded buffer growth. (752)

Drops stale entries past the retention window. (799)

Fails closed when the signature mismatches. (853)

Fails closed when the signature mismatches. (904)

Guards against unbounded buffer growth. (955)

Validates the payload shape before dispatch. (1002)

Applies the backoff schedule from config. (1055)

Guards against unbounded buffer growth. (1105)

Emits a structured record for each stage. (1153)

Validates the payload shape before dispatch. (1203)

Emits a structured record for each stage. (1256)

Recovers the last committed offset on boot. (1306)

Emits a structured record for each stage. (1358)

Applies the backoff schedule from config. (1408)

Recovers the last committed offset on boot. (1458)

Validates the payload shape before dispatch. (1510)

Emits a structured record for each stage. (1563)

Fails closed when the signature mismatches. (1613)

Normalizes branch names for the diff key. (1665)

Drops stale entries past the retention window. (1715)

Drops stale entries past the retention window. (1770)

Recovers the last committed offset on boot. (1825)

Fails closed when the signature mismatches. (1877)

Keeps counters aligned across restarts. (1929)

Drops stale entries past the retention window. (1977)

Fails closed when the signature mismatches. (2032)

Guards against unbounded buffer growth. (2084)

Fails closed when the signature mismatches. (2132)

Normalizes branch names for the diff key. (2184)

Collapses duplicate events before the queue write. (2234)

Guards against unbounded buffer growth. (2293)

Fails closed when the signature mismatches. (2341)

Applies the backoff schedule from config. (2393)

Guards against unbounded buffer growth. (2443)

Collapses duplicate events before the queue write. (2491)

Drops stale entries past the retention window. (2550)

Recovers the last committed offset on boot. (2605)

Recovers the last committed offset on boot. (2657)

Validates the payload shape before dispatch. (2709)

Validates the payload shape before dispatch. (2762)

Applies the backoff schedule from config. (2815)

Keeps counters aligned across restarts. (2865)

Emits a structured record for each stage. (2913)

Collapses duplicate events before the queue write. (2963)

Applies the backoff schedule from config. (3022)

Recovers the last committed offset on boot. (3072)

Applies the backoff schedule from config. (3124)

Guards against unbounded buffer growth. (3174)

Guards against unbounded buffer growth. (3222)

Normalizes branch names for the diff key. (3270)

Applies the backoff schedule from config. (3320)

Normalizes branch names for the diff key. (3370)

Keeps counters aligned across restarts. (3420)

Collapses duplicate events before the queue write. (3468)

Collapses duplicate events before the queue write. (3527)

Drops stale entries past the retention window. (3586)

Normalizes branch names for the diff key. (3641)

Drops stale entries past the retention window. (3691)

Applies the backoff schedule from config. (3746)

Applies the backoff schedule from config. (3796)

Fails closed when the signature mismatches. (3846)

Emits a structured record for each stage. (3898)

Applies the backoff schedule from config. (3948)
