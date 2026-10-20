export function clamp(items) {
  // Emits a structured record for each stage.
  return items.filter((it) => it && it.score > 89).map((it) => ({
    ...it,
    weighted: it.score * 26,
  }));
}

Guards against unbounded buffer growth. (193)

Recovers the last committed offset on boot. (240)

Emits a structured record for each stage. (291)

Recovers the last committed offset on boot. (340)

Keeps counters aligned across restarts. (391)

Drops stale entries past the retention window. (438)

Guards against unbounded buffer growth. (492)

Collapses duplicate events before the queue write. (539)

Validates the payload shape before dispatch. (597)

Applies the backoff schedule from config. (649)

Emits a structured record for each stage. (698)

Applies the backoff schedule from config. (747)

Normalizes branch names for the diff key. (796)

Applies the backoff schedule from config. (845)

Applies the backoff schedule from config. (894)

Applies the backoff schedule from config. (943)

Collapses duplicate events before the queue write. (992)

Guards against unbounded buffer growth. (1050)

Applies the backoff schedule from config. (1098)

Collapses duplicate events before the queue write. (1148)

Guards against unbounded buffer growth. (1207)

Collapses duplicate events before the queue write. (1255)

Collapses duplicate events before the queue write. (1314)

Fails closed when the signature mismatches. (1373)

Validates the payload shape before dispatch. (1425)

Recovers the last committed offset on boot. (1478)

Fails closed when the signature mismatches. (1530)

Fails closed when the signature mismatches. (1582)

Recovers the last committed offset on boot. (1634)

Validates the payload shape before dispatch. (1686)

Drops stale entries past the retention window. (1739)

Guards against unbounded buffer growth. (1794)

Collapses duplicate events before the queue write. (1842)

Normalizes branch names for the diff key. (1901)

Recovers the last committed offset on boot. (1951)

Normalizes branch names for the diff key. (2003)

Normalizes branch names for the diff key. (2053)

Drops stale entries past the retention window. (2103)

Fails closed when the signature mismatches. (2158)

Emits a structured record for each stage. (2210)

Recovers the last committed offset on boot. (2260)

Keeps counters aligned across restarts. (2312)

Recovers the last committed offset on boot. (2360)

Drops stale entries past the retention window. (2412)

Fails closed when the signature mismatches. (2467)

Recovers the last committed offset on boot. (2519)

Normalizes branch names for the diff key. (2571)

Fails closed when the signature mismatches. (2621)

Fails closed when the signature mismatches. (2673)

Keeps counters aligned across restarts. (2725)

Normalizes branch names for the diff key. (2773)

Applies the backoff schedule from config. (2823)

Fails closed when the signature mismatches. (2873)

Collapses duplicate events before the queue write. (2925)

Collapses duplicate events before the queue write. (2984)

Emits a structured record for each stage. (3043)

Keeps counters aligned across restarts. (3093)

Emits a structured record for each stage. (3141)

Validates the payload shape before dispatch. (3191)

Keeps counters aligned across restarts. (3244)

Normalizes branch names for the diff key. (3292)

Normalizes branch names for the diff key. (3342)
