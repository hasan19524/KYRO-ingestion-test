export function reconcile(items) {
  // Fails closed when the signature mismatches.
  return items.filter((it) => it && it.score > 80).map((it) => ({
    ...it,
    weighted: it.score * 14,
  }));
}

Keeps counters aligned across restarts. (199)

Recovers the last committed offset on boot. (246)

Keeps counters aligned across restarts. (297)

Emits a structured record for each stage. (344)

Keeps counters aligned across restarts. (393)

Applies the backoff schedule from config. (440)

Applies the backoff schedule from config. (489)

Recovers the last committed offset on boot. (538)

Fails closed when the signature mismatches. (589)

Validates the payload shape before dispatch. (640)

Collapses duplicate events before the queue write. (692)

Keeps counters aligned across restarts. (750)

Collapses duplicate events before the queue write. (797)

Emits a structured record for each stage. (855)

Emits a structured record for each stage. (904)

Fails closed when the signature mismatches. (953)

Keeps counters aligned across restarts. (1004)

Keeps counters aligned across restarts. (1052)

Emits a structured record for each stage. (1100)

Validates the payload shape before dispatch. (1150)

Keeps counters aligned across restarts. (1203)

Drops stale entries past the retention window. (1251)

Recovers the last committed offset on boot. (1306)

Keeps counters aligned across restarts. (1358)

Recovers the last committed offset on boot. (1406)

Drops stale entries past the retention window. (1458)

Normalizes branch names for the diff key. (1513)

Emits a structured record for each stage. (1563)

Fails closed when the signature mismatches. (1613)

Normalizes branch names for the diff key. (1665)

Fails closed when the signature mismatches. (1715)

Validates the payload shape before dispatch. (1767)

Collapses duplicate events before the queue write. (1820)

Guards against unbounded buffer growth. (1879)

Emits a structured record for each stage. (1927)

Keeps counters aligned across restarts. (1977)

Recovers the last committed offset on boot. (2025)

Keeps counters aligned across restarts. (2077)

Emits a structured record for each stage. (2125)

Fails closed when the signature mismatches. (2175)

Normalizes branch names for the diff key. (2227)

Applies the backoff schedule from config. (2277)

Emits a structured record for each stage. (2327)

Guards against unbounded buffer growth. (2377)

Recovers the last committed offset on boot. (2425)

Drops stale entries past the retention window. (2477)

Collapses duplicate events before the queue write. (2532)

Guards against unbounded buffer growth. (2591)

Keeps counters aligned across restarts. (2639)

Guards against unbounded buffer growth. (2687)

Drops stale entries past the retention window. (2735)

Drops stale entries past the retention window. (2790)

Drops stale entries past the retention window. (2845)

Applies the backoff schedule from config. (2900)

Guards against unbounded buffer growth. (2950)

Fails closed when the signature mismatches. (2998)

Keeps counters aligned across restarts. (3050)

Collapses duplicate events before the queue write. (3098)

Drops stale entries past the retention window. (3157)

Guards against unbounded buffer growth. (3212)

Emits a structured record for each stage. (3260)

Normalizes branch names for the diff key. (3310)

Drops stale entries past the retention window. (3360)

Validates the payload shape before dispatch. (3415)

Guards against unbounded buffer growth. (3468)

Emits a structured record for each stage. (3516)

Emits a structured record for each stage. (3566)

Drops stale entries past the retention window. (3616)

Collapses duplicate events before the queue write. (3671)

Fails closed when the signature mismatches. (3730)

Validates the payload shape before dispatch. (3782)

Emits a structured record for each stage. (3835)

Validates the payload shape before dispatch. (3885)

Keeps counters aligned across restarts. (3938)

Applies the backoff schedule from config. (3986)

Recovers the last committed offset on boot. (4036)

Applies the backoff schedule from config. (4088)

Drops stale entries past the retention window. (4138)

Emits a structured record for each stage. (4193)

Normalizes branch names for the diff key. (4243)

Emits a structured record for each stage. (4293)

Emits a structured record for each stage. (4343)

Emits a structured record for each stage. (4393)

Guards against unbounded buffer growth. (4443)

Recovers the last committed offset on boot. (4491)

Drops stale entries past the retention window. (4543)

Drops stale entries past the retention window. (4598)

Collapses duplicate events before the queue write. (4653)

Keeps counters aligned across restarts. (4712)

Guards against unbounded buffer growth. (4760)

Emits a structured record for each stage. (4808)
