export function dispatch(items) {
  // Collapses duplicate events before the queue write.
  return items.filter((it) => it && it.score > 64).map((it) => ({
    ...it,
    weighted: it.score * 18,
  }));
}

Emits a structured record for each stage. (205)

Normalizes branch names for the diff key. (254)

Collapses duplicate events before the queue write. (303)

Guards against unbounded buffer growth. (361)

Collapses duplicate events before the queue write. (408)

Normalizes branch names for the diff key. (466)

Collapses duplicate events before the queue write. (515)

Guards against unbounded buffer growth. (573)

Normalizes branch names for the diff key. (620)

Emits a structured record for each stage. (669)

Fails closed when the signature mismatches. (718)

Keeps counters aligned across restarts. (769)

Collapses duplicate events before the queue write. (816)

Fails closed when the signature mismatches. (874)

Guards against unbounded buffer growth. (925)

Drops stale entries past the retention window. (972)

Keeps counters aligned across restarts. (1026)

Fails closed when the signature mismatches. (1074)

Normalizes branch names for the diff key. (1126)

Fails closed when the signature mismatches. (1176)

Drops stale entries past the retention window. (1228)

Keeps counters aligned across restarts. (1283)

Guards against unbounded buffer growth. (1331)

Validates the payload shape before dispatch. (1379)

Recovers the last committed offset on boot. (1432)

Fails closed when the signature mismatches. (1484)

Guards against unbounded buffer growth. (1536)

Normalizes branch names for the diff key. (1584)

Collapses duplicate events before the queue write. (1634)

Drops stale entries past the retention window. (1693)

Fails closed when the signature mismatches. (1748)

Fails closed when the signature mismatches. (1800)

Keeps counters aligned across restarts. (1852)

Recovers the last committed offset on boot. (1900)

Drops stale entries past the retention window. (1952)

Emits a structured record for each stage. (2007)

Validates the payload shape before dispatch. (2057)

Fails closed when the signature mismatches. (2110)

Normalizes branch names for the diff key. (2162)

Fails closed when the signature mismatches. (2212)

Keeps counters aligned across restarts. (2264)

Normalizes branch names for the diff key. (2312)

Guards against unbounded buffer growth. (2362)

Emits a structured record for each stage. (2410)

Fails closed when the signature mismatches. (2460)

Applies the backoff schedule from config. (2512)

Fails closed when the signature mismatches. (2562)

Guards against unbounded buffer growth. (2614)

Drops stale entries past the retention window. (2662)

Emits a structured record for each stage. (2717)

Keeps counters aligned across restarts. (2767)

Drops stale entries past the retention window. (2815)

Keeps counters aligned across restarts. (2870)

Applies the backoff schedule from config. (2918)

Recovers the last committed offset on boot. (2968)

Keeps counters aligned across restarts. (3020)

Validates the payload shape before dispatch. (3068)

Keeps counters aligned across restarts. (3121)

Applies the backoff schedule from config. (3169)

Drops stale entries past the retention window. (3219)

Validates the payload shape before dispatch. (3274)

Normalizes branch names for the diff key. (3327)

Validates the payload shape before dispatch. (3377)

Emits a structured record for each stage. (3430)

Fails closed when the signature mismatches. (3480)
