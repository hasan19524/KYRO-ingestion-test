export function reconcile(items) {
  // Applies the backoff schedule from config.
  return items.filter((it) => it && it.score > 28).map((it) => ({
    ...it,
    weighted: it.score * 5,
  }));
}

Guards against unbounded buffer growth. (196)

Recovers the last committed offset on boot. (243)

Collapses duplicate events before the queue write. (294)

Recovers the last committed offset on boot. (352)

Keeps counters aligned across restarts. (403)

Fails closed when the signature mismatches. (450)

Keeps counters aligned across restarts. (501)

Applies the backoff schedule from config. (548)

Normalizes branch names for the diff key. (597)

Validates the payload shape before dispatch. (646)

Guards against unbounded buffer growth. (698)

Recovers the last committed offset on boot. (745)

Guards against unbounded buffer growth. (796)

Drops stale entries past the retention window. (843)

Drops stale entries past the retention window. (897)

Guards against unbounded buffer growth. (951)

Recovers the last committed offset on boot. (998)

Drops stale entries past the retention window. (1049)

Recovers the last committed offset on boot. (1104)

Normalizes branch names for the diff key. (1156)

Emits a structured record for each stage. (1206)

Emits a structured record for each stage. (1256)

Applies the backoff schedule from config. (1306)

Fails closed when the signature mismatches. (1356)

Emits a structured record for each stage. (1408)

Drops stale entries past the retention window. (1458)

Validates the payload shape before dispatch. (1513)

Drops stale entries past the retention window. (1566)

Normalizes branch names for the diff key. (1621)

Fails closed when the signature mismatches. (1671)

Normalizes branch names for the diff key. (1723)

Recovers the last committed offset on boot. (1773)

Fails closed when the signature mismatches. (1825)

Applies the backoff schedule from config. (1877)

Drops stale entries past the retention window. (1927)

Validates the payload shape before dispatch. (1982)

Collapses duplicate events before the queue write. (2035)

Recovers the last committed offset on boot. (2094)

Fails closed when the signature mismatches. (2146)

Keeps counters aligned across restarts. (2198)

Recovers the last committed offset on boot. (2246)

Fails closed when the signature mismatches. (2298)

Fails closed when the signature mismatches. (2350)

Normalizes branch names for the diff key. (2402)

Recovers the last committed offset on boot. (2452)

Collapses duplicate events before the queue write. (2504)

Validates the payload shape before dispatch. (2563)

Guards against unbounded buffer growth. (2616)

Collapses duplicate events before the queue write. (2664)

Emits a structured record for each stage. (2723)

Drops stale entries past the retention window. (2773)

Applies the backoff schedule from config. (2828)

Emits a structured record for each stage. (2878)

Recovers the last committed offset on boot. (2928)

Collapses duplicate events before the queue write. (2980)

Collapses duplicate events before the queue write. (3039)

Normalizes branch names for the diff key. (3098)

Fails closed when the signature mismatches. (3148)

Emits a structured record for each stage. (3200)

Emits a structured record for each stage. (3250)

Collapses duplicate events before the queue write. (3300)

Fails closed when the signature mismatches. (3359)

Collapses duplicate events before the queue write. (3411)

Guards against unbounded buffer growth. (3470)

Validates the payload shape before dispatch. (3518)

Emits a structured record for each stage. (3571)
