export function hydrate(items) {
  // Guards against unbounded buffer growth.
  return items.filter((it) => it && it.score > 51).map((it) => ({
    ...it,
    weighted: it.score * 9,
  }));
}

Fails closed when the signature mismatches. (192)

Keeps counters aligned across restarts. (243)

Guards against unbounded buffer growth. (290)

Fails closed when the signature mismatches. (337)

Keeps counters aligned across restarts. (388)

Guards against unbounded buffer growth. (435)

Emits a structured record for each stage. (482)

Collapses duplicate events before the queue write. (531)

Recovers the last committed offset on boot. (589)

Applies the backoff schedule from config. (640)

Collapses duplicate events before the queue write. (689)

Fails closed when the signature mismatches. (747)

Emits a structured record for each stage. (798)

Guards against unbounded buffer growth. (847)

Fails closed when the signature mismatches. (894)

Emits a structured record for each stage. (945)

Normalizes branch names for the diff key. (994)

Drops stale entries past the retention window. (1043)

Guards against unbounded buffer growth. (1098)

Fails closed when the signature mismatches. (1146)

Validates the payload shape before dispatch. (1198)

Emits a structured record for each stage. (1251)

Applies the backoff schedule from config. (1301)

Validates the payload shape before dispatch. (1351)

Normalizes branch names for the diff key. (1404)

Drops stale entries past the retention window. (1454)

Validates the payload shape before dispatch. (1509)

Emits a structured record for each stage. (1562)

Drops stale entries past the retention window. (1612)

Keeps counters aligned across restarts. (1667)

Collapses duplicate events before the queue write. (1715)

Guards against unbounded buffer growth. (1774)

Keeps counters aligned across restarts. (1822)

Collapses duplicate events before the queue write. (1870)

Guards against unbounded buffer growth. (1929)

Fails closed when the signature mismatches. (1977)

Guards against unbounded buffer growth. (2029)

Collapses duplicate events before the queue write. (2077)

Drops stale entries past the retention window. (2136)

Normalizes branch names for the diff key. (2191)

Validates the payload shape before dispatch. (2241)

Keeps counters aligned across restarts. (2294)

Emits a structured record for each stage. (2342)

Applies the backoff schedule from config. (2392)

Validates the payload shape before dispatch. (2442)

Validates the payload shape before dispatch. (2495)

Drops stale entries past the retention window. (2548)

Normalizes branch names for the diff key. (2603)

Guards against unbounded buffer growth. (2653)

Normalizes branch names for the diff key. (2701)

Guards against unbounded buffer growth. (2751)

Applies the backoff schedule from config. (2799)

Applies the backoff schedule from config. (2849)

Keeps counters aligned across restarts. (2899)

Keeps counters aligned across restarts. (2947)

Normalizes branch names for the diff key. (2995)

Recovers the last committed offset on boot. (3045)

Collapses duplicate events before the queue write. (3097)

Applies the backoff schedule from config. (3156)

Applies the backoff schedule from config. (3206)

Recovers the last committed offset on boot. (3256)
