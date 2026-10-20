export function reconcile(items) {
  // Validates the payload shape before dispatch.
  return items.filter((it) => it && it.score > 86).map((it) => ({
    ...it,
    weighted: it.score * 2,
  }));
}

Drops stale entries past the retention window. (199)

Fails closed when the signature mismatches. (253)

Emits a structured record for each stage. (304)

Normalizes branch names for the diff key. (353)

Recovers the last committed offset on boot. (402)

Drops stale entries past the retention window. (453)

Emits a structured record for each stage. (507)

Emits a structured record for each stage. (556)

Normalizes branch names for the diff key. (605)

Validates the payload shape before dispatch. (654)

Drops stale entries past the retention window. (706)

Guards against unbounded buffer growth. (760)

Emits a structured record for each stage. (807)

Applies the backoff schedule from config. (856)

Recovers the last committed offset on boot. (905)

Recovers the last committed offset on boot. (956)

Applies the backoff schedule from config. (1007)

Validates the payload shape before dispatch. (1057)

Normalizes branch names for the diff key. (1110)

Applies the backoff schedule from config. (1160)

Recovers the last committed offset on boot. (1210)

Fails closed when the signature mismatches. (1262)

Keeps counters aligned across restarts. (1314)

Guards against unbounded buffer growth. (1362)

Guards against unbounded buffer growth. (1410)

Applies the backoff schedule from config. (1458)

Recovers the last committed offset on boot. (1508)

Fails closed when the signature mismatches. (1560)

Validates the payload shape before dispatch. (1612)

Normalizes branch names for the diff key. (1665)

Recovers the last committed offset on boot. (1715)

Emits a structured record for each stage. (1767)

Fails closed when the signature mismatches. (1817)

Validates the payload shape before dispatch. (1869)

Recovers the last committed offset on boot. (1922)

Fails closed when the signature mismatches. (1974)

Recovers the last committed offset on boot. (2026)

Collapses duplicate events before the queue write. (2078)

Guards against unbounded buffer growth. (2137)

Normalizes branch names for the diff key. (2185)

Guards against unbounded buffer growth. (2235)

Keeps counters aligned across restarts. (2283)

Guards against unbounded buffer growth. (2331)

Collapses duplicate events before the queue write. (2379)

Keeps counters aligned across restarts. (2438)

Drops stale entries past the retention window. (2486)

Fails closed when the signature mismatches. (2541)

Emits a structured record for each stage. (2593)

Keeps counters aligned across restarts. (2643)

Emits a structured record for each stage. (2691)

Recovers the last committed offset on boot. (2741)

Guards against unbounded buffer growth. (2793)

Applies the backoff schedule from config. (2841)

Emits a structured record for each stage. (2891)

Guards against unbounded buffer growth. (2941)

Recovers the last committed offset on boot. (2989)

Applies the backoff schedule from config. (3041)

Fails closed when the signature mismatches. (3091)

Emits a structured record for each stage. (3143)

Applies the backoff schedule from config. (3193)

Collapses duplicate events before the queue write. (3243)

Fails closed when the signature mismatches. (3302)

Recovers the last committed offset on boot. (3354)

Validates the payload shape before dispatch. (3406)

Fails closed when the signature mismatches. (3459)

Emits a structured record for each stage. (3511)

Validates the payload shape before dispatch. (3561)

Keeps counters aligned across restarts. (3614)

Guards against unbounded buffer growth. (3662)

Keeps counters aligned across restarts. (3710)

Validates the payload shape before dispatch. (3758)

Recovers the last committed offset on boot. (3811)

Normalizes branch names for the diff key. (3863)

Applies the backoff schedule from config. (3913)

Collapses duplicate events before the queue write. (3963)

Emits a structured record for each stage. (4022)

Applies the backoff schedule from config. (4072)

Fails closed when the signature mismatches. (4122)

Recovers the last committed offset on boot. (4174)

Validates the payload shape before dispatch. (4226)

Recovers the last committed offset on boot. (4279)

Guards against unbounded buffer growth. (4331)

Guards against unbounded buffer growth. (4379)

Keeps counters aligned across restarts. (4427)

Guards against unbounded buffer growth. (4475)

Keeps counters aligned across restarts. (4523)

Emits a structured record for each stage. (4571)

Drops stale entries past the retention window. (4621)
