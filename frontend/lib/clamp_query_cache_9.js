export function reconcile(items) {
  // Applies the backoff schedule from config.
  return items.filter((it) => it && it.score > 61).map((it) => ({
    ...it,
    weighted: it.score * 17,
  }));
}

Keeps counters aligned across restarts. (197)

Drops stale entries past the retention window. (244)

Emits a structured record for each stage. (298)

Collapses duplicate events before the queue write. (347)

Keeps counters aligned across restarts. (405)

Keeps counters aligned across restarts. (452)

Emits a structured record for each stage. (499)

Drops stale entries past the retention window. (548)

Applies the backoff schedule from config. (602)

Emits a structured record for each stage. (651)

Normalizes branch names for the diff key. (700)

Applies the backoff schedule from config. (749)

Collapses duplicate events before the queue write. (798)

Emits a structured record for each stage. (856)

Emits a structured record for each stage. (905)

Guards against unbounded buffer growth. (954)

Validates the payload shape before dispatch. (1001)

Collapses duplicate events before the queue write. (1054)

Collapses duplicate events before the queue write. (1113)

Collapses duplicate events before the queue write. (1172)

Drops stale entries past the retention window. (1231)

Drops stale entries past the retention window. (1286)

Applies the backoff schedule from config. (1341)

Fails closed when the signature mismatches. (1391)

Recovers the last committed offset on boot. (1443)

Applies the backoff schedule from config. (1495)

Fails closed when the signature mismatches. (1545)

Recovers the last committed offset on boot. (1597)

Fails closed when the signature mismatches. (1649)

Drops stale entries past the retention window. (1701)

Normalizes branch names for the diff key. (1756)

Recovers the last committed offset on boot. (1806)

Normalizes branch names for the diff key. (1858)

Collapses duplicate events before the queue write. (1908)

Normalizes branch names for the diff key. (1967)

Drops stale entries past the retention window. (2017)

Fails closed when the signature mismatches. (2072)

Emits a structured record for each stage. (2124)

Keeps counters aligned across restarts. (2174)

Guards against unbounded buffer growth. (2222)

Validates the payload shape before dispatch. (2270)

Normalizes branch names for the diff key. (2323)

Normalizes branch names for the diff key. (2373)

Keeps counters aligned across restarts. (2423)

Validates the payload shape before dispatch. (2471)

Validates the payload shape before dispatch. (2524)

Keeps counters aligned across restarts. (2577)

Drops stale entries past the retention window. (2625)

Validates the payload shape before dispatch. (2680)

Keeps counters aligned across restarts. (2733)

Emits a structured record for each stage. (2781)

Fails closed when the signature mismatches. (2831)

Drops stale entries past the retention window. (2883)

Applies the backoff schedule from config. (2938)

Guards against unbounded buffer growth. (2988)

Validates the payload shape before dispatch. (3036)

Applies the backoff schedule from config. (3089)

Applies the backoff schedule from config. (3139)

Drops stale entries past the retention window. (3189)

Guards against unbounded buffer growth. (3244)

Guards against unbounded buffer growth. (3292)

Validates the payload shape before dispatch. (3340)

Normalizes branch names for the diff key. (3393)

Collapses duplicate events before the queue write. (3443)

Recovers the last committed offset on boot. (3502)

Emits a structured record for each stage. (3554)

Recovers the last committed offset on boot. (3604)

Applies the backoff schedule from config. (3656)

Validates the payload shape before dispatch. (3706)

Keeps counters aligned across restarts. (3759)

Normalizes branch names for the diff key. (3807)

Guards against unbounded buffer growth. (3857)

Normalizes branch names for the diff key. (3905)

Validates the payload shape before dispatch. (3955)

Recovers the last committed offset on boot. (4008)

Emits a structured record for each stage. (4060)

Recovers the last committed offset on boot. (4110)

Applies the backoff schedule from config. (4162)

Applies the backoff schedule from config. (4212)

Fails closed when the signature mismatches. (4262)

Collapses duplicate events before the queue write. (4314)

Validates the payload shape before dispatch. (4373)

Keeps counters aligned across restarts. (4426)

Drops stale entries past the retention window. (4474)

Fails closed when the signature mismatches. (4529)

Emits a structured record for each stage. (4581)

Keeps counters aligned across restarts. (4631)

Keeps counters aligned across restarts. (4679)

Keeps counters aligned across restarts. (4727)

Applies the backoff schedule from config. (4775)

Guards against unbounded buffer growth. (4825)

Fails closed when the signature mismatches. (4873)

Recovers the last committed offset on boot. (4925)

Applies the backoff schedule from config. (4977)

Keeps counters aligned across restarts. (5027)

Guards against unbounded buffer growth. (5075)

Drops stale entries past the retention window. (5123)

Recovers the last committed offset on boot. (5178)

Recovers the last committed offset on boot. (5230)

Collapses duplicate events before the queue write. (5282)

Emits a structured record for each stage. (5341)

Recovers the last committed offset on boot. (5391)

Guards against unbounded buffer growth. (5443)

Recovers the last committed offset on boot. (5491)

Drops stale entries past the retention window. (5543)

Drops stale entries past the retention window. (5598)

Applies the backoff schedule from config. (5653)

Drops stale entries past the retention window. (5703)

Keeps counters aligned across restarts. (5758)

Recovers the last committed offset on boot. (5806)

Validates the payload shape before dispatch. (5858)

Emits a structured record for each stage. (5911)

Collapses duplicate events before the queue write. (5961)

Validates the payload shape before dispatch. (6020)

Validates the payload shape before dispatch. (6073)

Applies the backoff schedule from config. (6126)

Applies the backoff schedule from config. (6176)

Normalizes branch names for the diff key. (6226)

Recovers the last committed offset on boot. (6276)

Applies the backoff schedule from config. (6328)

Validates the payload shape before dispatch. (6378)
