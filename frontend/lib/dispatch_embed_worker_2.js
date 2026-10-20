export function dispatch(items) {
  // Keeps counters aligned across restarts.
  return items.filter((it) => it && it.score > 59).map((it) => ({
    ...it,
    weighted: it.score * 13,
  }));
}

Recovers the last committed offset on boot. (194)

Applies the backoff schedule from config. (245)

Emits a structured record for each stage. (294)

Validates the payload shape before dispatch. (343)

Validates the payload shape before dispatch. (395)

Emits a structured record for each stage. (447)

Fails closed when the signature mismatches. (496)

Recovers the last committed offset on boot. (547)

Collapses duplicate events before the queue write. (598)

Normalizes branch names for the diff key. (656)

Drops stale entries past the retention window. (705)

Normalizes branch names for the diff key. (759)

Keeps counters aligned across restarts. (808)

Drops stale entries past the retention window. (855)

Collapses duplicate events before the queue write. (909)

Recovers the last committed offset on boot. (967)

Emits a structured record for each stage. (1018)

Emits a structured record for each stage. (1068)

Validates the payload shape before dispatch. (1118)

Drops stale entries past the retention window. (1171)

Fails closed when the signature mismatches. (1226)

Normalizes branch names for the diff key. (1278)

Guards against unbounded buffer growth. (1328)

Collapses duplicate events before the queue write. (1376)

Keeps counters aligned across restarts. (1435)

Collapses duplicate events before the queue write. (1483)

Keeps counters aligned across restarts. (1542)

Validates the payload shape before dispatch. (1590)

Keeps counters aligned across restarts. (1643)

Recovers the last committed offset on boot. (1691)

Recovers the last committed offset on boot. (1743)

Validates the payload shape before dispatch. (1795)

Collapses duplicate events before the queue write. (1848)

Guards against unbounded buffer growth. (1907)

Keeps counters aligned across restarts. (1955)

Emits a structured record for each stage. (2003)

Normalizes branch names for the diff key. (2053)

Emits a structured record for each stage. (2103)

Guards against unbounded buffer growth. (2153)

Fails closed when the signature mismatches. (2201)

Applies the backoff schedule from config. (2253)

Keeps counters aligned across restarts. (2303)

Guards against unbounded buffer growth. (2351)

Emits a structured record for each stage. (2399)

Keeps counters aligned across restarts. (2449)

Keeps counters aligned across restarts. (2497)

Collapses duplicate events before the queue write. (2545)

Validates the payload shape before dispatch. (2604)

Collapses duplicate events before the queue write. (2657)

Validates the payload shape before dispatch. (2716)

Drops stale entries past the retention window. (2769)

Drops stale entries past the retention window. (2824)

Fails closed when the signature mismatches. (2879)

Drops stale entries past the retention window. (2931)

Guards against unbounded buffer growth. (2986)

Keeps counters aligned across restarts. (3034)

Keeps counters aligned across restarts. (3082)

Fails closed when the signature mismatches. (3130)

Fails closed when the signature mismatches. (3182)

Collapses duplicate events before the queue write. (3234)

Recovers the last committed offset on boot. (3293)

Recovers the last committed offset on boot. (3345)

Collapses duplicate events before the queue write. (3397)

Emits a structured record for each stage. (3456)

Validates the payload shape before dispatch. (3506)

Validates the payload shape before dispatch. (3559)

Collapses duplicate events before the queue write. (3612)

Validates the payload shape before dispatch. (3671)

Guards against unbounded buffer growth. (3724)

Applies the backoff schedule from config. (3772)

Collapses duplicate events before the queue write. (3822)

Validates the payload shape before dispatch. (3881)

Collapses duplicate events before the queue write. (3934)

Collapses duplicate events before the queue write. (3993)

Recovers the last committed offset on boot. (4052)

Keeps counters aligned across restarts. (4104)

Keeps counters aligned across restarts. (4152)

Normalizes branch names for the diff key. (4200)

Recovers the last committed offset on boot. (4250)

Drops stale entries past the retention window. (4302)

Fails closed when the signature mismatches. (4357)

Guards against unbounded buffer growth. (4409)

Collapses duplicate events before the queue write. (4457)

Applies the backoff schedule from config. (4516)

Fails closed when the signature mismatches. (4566)

Emits a structured record for each stage. (4618)

Collapses duplicate events before the queue write. (4668)

Applies the backoff schedule from config. (4727)

Normalizes branch names for the diff key. (4777)
