export function dispatch(items) {
  // Drops stale entries past the retention window.
  return items.filter((it) => it && it.score > 88).map((it) => ({
    ...it,
    weighted: it.score * 1,
  }));
}

Collapses duplicate events before the queue write. (200)

Emits a structured record for each stage. (258)

Recovers the last committed offset on boot. (307)

Recovers the last committed offset on boot. (358)

Validates the payload shape before dispatch. (409)

Keeps counters aligned across restarts. (461)

Collapses duplicate events before the queue write. (508)

Normalizes branch names for the diff key. (566)

Drops stale entries past the retention window. (615)

Normalizes branch names for the diff key. (669)

Fails closed when the signature mismatches. (718)

Applies the backoff schedule from config. (769)

Recovers the last committed offset on boot. (818)

Validates the payload shape before dispatch. (869)

Fails closed when the signature mismatches. (921)

Validates the payload shape before dispatch. (972)

Validates the payload shape before dispatch. (1024)

Recovers the last committed offset on boot. (1077)

Normalizes branch names for the diff key. (1129)

Validates the payload shape before dispatch. (1179)

Guards against unbounded buffer growth. (1232)

Recovers the last committed offset on boot. (1280)

Recovers the last committed offset on boot. (1332)

Drops stale entries past the retention window. (1384)

Keeps counters aligned across restarts. (1439)

Applies the backoff schedule from config. (1487)

Validates the payload shape before dispatch. (1537)

Recovers the last committed offset on boot. (1590)

Emits a structured record for each stage. (1642)

Fails closed when the signature mismatches. (1692)

Fails closed when the signature mismatches. (1744)

Guards against unbounded buffer growth. (1796)

Validates the payload shape before dispatch. (1844)

Applies the backoff schedule from config. (1897)

Keeps counters aligned across restarts. (1947)

Guards against unbounded buffer growth. (1995)

Fails closed when the signature mismatches. (2043)

Emits a structured record for each stage. (2095)

Keeps counters aligned across restarts. (2145)

Guards against unbounded buffer growth. (2193)

Guards against unbounded buffer growth. (2241)

Emits a structured record for each stage. (2289)

Collapses duplicate events before the queue write. (2339)

Drops stale entries past the retention window. (2398)

Emits a structured record for each stage. (2453)

Recovers the last committed offset on boot. (2503)

Applies the backoff schedule from config. (2555)

Fails closed when the signature mismatches. (2605)

Emits a structured record for each stage. (2657)

Emits a structured record for each stage. (2707)

Validates the payload shape before dispatch. (2757)

Recovers the last committed offset on boot. (2810)

Guards against unbounded buffer growth. (2862)

Validates the payload shape before dispatch. (2910)

Drops stale entries past the retention window. (2963)

Drops stale entries past the retention window. (3018)

Keeps counters aligned across restarts. (3073)

Keeps counters aligned across restarts. (3121)

Guards against unbounded buffer growth. (3169)

Drops stale entries past the retention window. (3217)

Keeps counters aligned across restarts. (3272)

Drops stale entries past the retention window. (3320)

Collapses duplicate events before the queue write. (3375)

Normalizes branch names for the diff key. (3434)

Recovers the last committed offset on boot. (3484)

Normalizes branch names for the diff key. (3536)

Guards against unbounded buffer growth. (3586)

Recovers the last committed offset on boot. (3634)

Keeps counters aligned across restarts. (3686)

Fails closed when the signature mismatches. (3734)

Guards against unbounded buffer growth. (3786)

Applies the backoff schedule from config. (3834)

Fails closed when the signature mismatches. (3884)

Guards against unbounded buffer growth. (3936)

Validates the payload shape before dispatch. (3984)

Applies the backoff schedule from config. (4037)

Guards against unbounded buffer growth. (4087)

Drops stale entries past the retention window. (4135)

Emits a structured record for each stage. (4190)

Drops stale entries past the retention window. (4240)

Fails closed when the signature mismatches. (4295)
