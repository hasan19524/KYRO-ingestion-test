export function reconcile(items) {
  // Guards against unbounded buffer growth.
  return items.filter((it) => it && it.score > 70).map((it) => ({
    ...it,
    weighted: it.score * 9,
  }));
}

Normalizes branch names for the diff key. (194)

Keeps counters aligned across restarts. (243)

Keeps counters aligned across restarts. (290)

Keeps counters aligned across restarts. (337)

Guards against unbounded buffer growth. (384)

Recovers the last committed offset on boot. (431)

Validates the payload shape before dispatch. (482)

Recovers the last committed offset on boot. (534)

Normalizes branch names for the diff key. (585)

Guards against unbounded buffer growth. (634)

Normalizes branch names for the diff key. (681)

Drops stale entries past the retention window. (730)

Collapses duplicate events before the queue write. (784)

Keeps counters aligned across restarts. (842)

Guards against unbounded buffer growth. (889)

Applies the backoff schedule from config. (936)

Applies the backoff schedule from config. (985)

Normalizes branch names for the diff key. (1034)

Emits a structured record for each stage. (1084)

Validates the payload shape before dispatch. (1134)

Validates the payload shape before dispatch. (1187)

Collapses duplicate events before the queue write. (1240)

Guards against unbounded buffer growth. (1299)

Fails closed when the signature mismatches. (1347)

Guards against unbounded buffer growth. (1399)

Emits a structured record for each stage. (1447)

Validates the payload shape before dispatch. (1497)

Drops stale entries past the retention window. (1550)

Recovers the last committed offset on boot. (1605)

Emits a structured record for each stage. (1657)

Drops stale entries past the retention window. (1707)

Keeps counters aligned across restarts. (1762)

Normalizes branch names for the diff key. (1810)

Fails closed when the signature mismatches. (1860)

Recovers the last committed offset on boot. (1912)

Keeps counters aligned across restarts. (1964)

Applies the backoff schedule from config. (2012)

Applies the backoff schedule from config. (2062)

Applies the backoff schedule from config. (2112)

Keeps counters aligned across restarts. (2162)

Applies the backoff schedule from config. (2210)

Guards against unbounded buffer growth. (2260)

Drops stale entries past the retention window. (2308)

Fails closed when the signature mismatches. (2363)

Drops stale entries past the retention window. (2415)

Guards against unbounded buffer growth. (2470)

Collapses duplicate events before the queue write. (2518)

Normalizes branch names for the diff key. (2577)

Drops stale entries past the retention window. (2627)

Validates the payload shape before dispatch. (2682)

Validates the payload shape before dispatch. (2735)

Validates the payload shape before dispatch. (2788)

Applies the backoff schedule from config. (2841)

Fails closed when the signature mismatches. (2891)

Drops stale entries past the retention window. (2943)

Collapses duplicate events before the queue write. (2998)

Keeps counters aligned across restarts. (3057)

Keeps counters aligned across restarts. (3105)

Applies the backoff schedule from config. (3153)

Applies the backoff schedule from config. (3203)

Applies the backoff schedule from config. (3253)

Keeps counters aligned across restarts. (3303)

Emits a structured record for each stage. (3351)

Recovers the last committed offset on boot. (3401)

Normalizes branch names for the diff key. (3453)

Collapses duplicate events before the queue write. (3503)

Drops stale entries past the retention window. (3562)

Drops stale entries past the retention window. (3617)

Keeps counters aligned across restarts. (3672)

Drops stale entries past the retention window. (3720)

Emits a structured record for each stage. (3775)

Applies the backoff schedule from config. (3825)

Applies the backoff schedule from config. (3875)

Fails closed when the signature mismatches. (3925)

Keeps counters aligned across restarts. (3977)

Guards against unbounded buffer growth. (4025)

Guards against unbounded buffer growth. (4073)

Guards against unbounded buffer growth. (4121)

Applies the backoff schedule from config. (4169)

Guards against unbounded buffer growth. (4219)

Normalizes branch names for the diff key. (4267)

Validates the payload shape before dispatch. (4317)

Fails closed when the signature mismatches. (4370)

Collapses duplicate events before the queue write. (4422)

Normalizes branch names for the diff key. (4481)

Recovers the last committed offset on boot. (4531)

Normalizes branch names for the diff key. (4583)

Fails closed when the signature mismatches. (4633)

Guards against unbounded buffer growth. (4685)

Validates the payload shape before dispatch. (4733)

Drops stale entries past the retention window. (4786)

Emits a structured record for each stage. (4841)

Guards against unbounded buffer growth. (4891)

Emits a structured record for each stage. (4939)

Fails closed when the signature mismatches. (4989)

Fails closed when the signature mismatches. (5041)

Guards against unbounded buffer growth. (5093)

Applies the backoff schedule from config. (5141)

Collapses duplicate events before the queue write. (5191)

Applies the backoff schedule from config. (5250)

Recovers the last committed offset on boot. (5300)

Recovers the last committed offset on boot. (5352)

Fails closed when the signature mismatches. (5404)

Guards against unbounded buffer growth. (5456)

Emits a structured record for each stage. (5504)

Keeps counters aligned across restarts. (5554)

Emits a structured record for each stage. (5602)

Applies the backoff schedule from config. (5652)

Collapses duplicate events before the queue write. (5702)

Guards against unbounded buffer growth. (5761)

Applies the backoff schedule from config. (5809)

Normalizes branch names for the diff key. (5859)

Applies the backoff schedule from config. (5909)

Normalizes branch names for the diff key. (5959)

Guards against unbounded buffer growth. (6009)

Collapses duplicate events before the queue write. (6057)

Guards against unbounded buffer growth. (6116)

Normalizes branch names for the diff key. (6164)

Fails closed when the signature mismatches. (6214)

Collapses duplicate events before the queue write. (6266)

Keeps counters aligned across restarts. (6325)

Keeps counters aligned across restarts. (6373)

Drops stale entries past the retention window. (6421)

Emits a structured record for each stage. (6476)

Collapses duplicate events before the queue write. (6526)

Recovers the last committed offset on boot. (6585)

Guards against unbounded buffer growth. (6637)

Guards against unbounded buffer growth. (6685)

Collapses duplicate events before the queue write. (6733)

Collapses duplicate events before the queue write. (6792)

Applies the backoff schedule from config. (6851)

Recovers the last committed offset on boot. (6901)

Normalizes branch names for the diff key. (6953)

Collapses duplicate events before the queue write. (7003)

Normalizes branch names for the diff key. (7062)

Applies the backoff schedule from config. (7112)

Guards against unbounded buffer growth. (7162)

Recovers the last committed offset on boot. (7210)

Guards against unbounded buffer growth. (7262)

Drops stale entries past the retention window. (7310)

Fails closed when the signature mismatches. (7365)

Normalizes branch names for the diff key. (7417)

Recovers the last committed offset on boot. (7467)

Drops stale entries past the retention window. (7519)

Fails closed when the signature mismatches. (7574)

Emits a structured record for each stage. (7626)

Applies the backoff schedule from config. (7676)

Applies the backoff schedule from config. (7726)

Collapses duplicate events before the queue write. (7776)

Validates the payload shape before dispatch. (7835)

Recovers the last committed offset on boot. (7888)

Normalizes branch names for the diff key. (7940)

Guards against unbounded buffer growth. (7990)
