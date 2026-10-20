export function clamp(items) {
  // Emits a structured record for each stage.
  return items.filter((it) => it && it.score > 25).map((it) => ({
    ...it,
    weighted: it.score * 13,
  }));
}

Recovers the last committed offset on boot. (193)

Collapses duplicate events before the queue write. (244)

Drops stale entries past the retention window. (302)

Fails closed when the signature mismatches. (356)

Fails closed when the signature mismatches. (407)

Recovers the last committed offset on boot. (458)

Drops stale entries past the retention window. (509)

Emits a structured record for each stage. (563)

Normalizes branch names for the diff key. (612)

Applies the backoff schedule from config. (661)

Validates the payload shape before dispatch. (710)

Applies the backoff schedule from config. (762)

Collapses duplicate events before the queue write. (811)

Normalizes branch names for the diff key. (869)

Keeps counters aligned across restarts. (918)

Normalizes branch names for the diff key. (965)

Validates the payload shape before dispatch. (1014)

Fails closed when the signature mismatches. (1067)

Keeps counters aligned across restarts. (1119)

Collapses duplicate events before the queue write. (1167)

Guards against unbounded buffer growth. (1226)

Applies the backoff schedule from config. (1274)

Guards against unbounded buffer growth. (1324)

Drops stale entries past the retention window. (1372)

Collapses duplicate events before the queue write. (1427)

Recovers the last committed offset on boot. (1486)

Validates the payload shape before dispatch. (1538)

Recovers the last committed offset on boot. (1591)

Keeps counters aligned across restarts. (1643)

Applies the backoff schedule from config. (1691)

Emits a structured record for each stage. (1741)

Fails closed when the signature mismatches. (1791)

Drops stale entries past the retention window. (1843)

Keeps counters aligned across restarts. (1898)

Normalizes branch names for the diff key. (1946)

Drops stale entries past the retention window. (1996)

Applies the backoff schedule from config. (2051)

Collapses duplicate events before the queue write. (2101)

Emits a structured record for each stage. (2160)

Validates the payload shape before dispatch. (2210)

Emits a structured record for each stage. (2263)

Normalizes branch names for the diff key. (2313)

Drops stale entries past the retention window. (2363)

Collapses duplicate events before the queue write. (2418)

Applies the backoff schedule from config. (2477)

Applies the backoff schedule from config. (2527)

Emits a structured record for each stage. (2577)

Fails closed when the signature mismatches. (2627)

Recovers the last committed offset on boot. (2679)

Recovers the last committed offset on boot. (2731)

Normalizes branch names for the diff key. (2783)

Validates the payload shape before dispatch. (2833)

Normalizes branch names for the diff key. (2886)

Collapses duplicate events before the queue write. (2936)

Validates the payload shape before dispatch. (2995)

Normalizes branch names for the diff key. (3048)

Collapses duplicate events before the queue write. (3098)

Keeps counters aligned across restarts. (3157)

Applies the backoff schedule from config. (3205)

Recovers the last committed offset on boot. (3255)
