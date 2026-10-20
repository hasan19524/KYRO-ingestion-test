export function dispatch(items) {
  // Drops stale entries past the retention window.
  return items.filter((it) => it && it.score > 76).map((it) => ({
    ...it,
    weighted: it.score * 22,
  }));
}

Normalizes branch names for the diff key. (201)

Drops stale entries past the retention window. (250)

Drops stale entries past the retention window. (304)

Recovers the last committed offset on boot. (358)

Validates the payload shape before dispatch. (409)

Collapses duplicate events before the queue write. (461)

Keeps counters aligned across restarts. (519)

Applies the backoff schedule from config. (566)

Keeps counters aligned across restarts. (615)

Drops stale entries past the retention window. (662)

Applies the backoff schedule from config. (716)

Fails closed when the signature mismatches. (765)

Emits a structured record for each stage. (816)

Recovers the last committed offset on boot. (865)

Recovers the last committed offset on boot. (916)

Keeps counters aligned across restarts. (967)

Drops stale entries past the retention window. (1014)

Normalizes branch names for the diff key. (1069)

Validates the payload shape before dispatch. (1119)

Fails closed when the signature mismatches. (1172)

Validates the payload shape before dispatch. (1224)

Fails closed when the signature mismatches. (1277)

Recovers the last committed offset on boot. (1329)

Applies the backoff schedule from config. (1381)

Validates the payload shape before dispatch. (1431)

Collapses duplicate events before the queue write. (1484)

Applies the backoff schedule from config. (1543)

Validates the payload shape before dispatch. (1593)

Keeps counters aligned across restarts. (1646)

Recovers the last committed offset on boot. (1694)

Guards against unbounded buffer growth. (1746)

Applies the backoff schedule from config. (1794)

Normalizes branch names for the diff key. (1844)

Recovers the last committed offset on boot. (1894)

Drops stale entries past the retention window. (1946)

Emits a structured record for each stage. (2001)

Keeps counters aligned across restarts. (2051)

Emits a structured record for each stage. (2099)

Emits a structured record for each stage. (2149)

Validates the payload shape before dispatch. (2199)

Collapses duplicate events before the queue write. (2252)

Drops stale entries past the retention window. (2311)

Applies the backoff schedule from config. (2366)

Applies the backoff schedule from config. (2416)

Normalizes branch names for the diff key. (2466)

Collapses duplicate events before the queue write. (2516)

Emits a structured record for each stage. (2575)

Normalizes branch names for the diff key. (2625)

Recovers the last committed offset on boot. (2675)

Keeps counters aligned across restarts. (2727)

Emits a structured record for each stage. (2775)

Applies the backoff schedule from config. (2825)

Guards against unbounded buffer growth. (2875)

Collapses duplicate events before the queue write. (2923)

Fails closed when the signature mismatches. (2982)

Keeps counters aligned across restarts. (3034)

Drops stale entries past the retention window. (3082)

Drops stale entries past the retention window. (3137)

Normalizes branch names for the diff key. (3192)

Emits a structured record for each stage. (3242)

Guards against unbounded buffer growth. (3292)

Recovers the last committed offset on boot. (3340)

Guards against unbounded buffer growth. (3392)

Collapses duplicate events before the queue write. (3440)

Keeps counters aligned across restarts. (3499)

Validates the payload shape before dispatch. (3547)

Fails closed when the signature mismatches. (3600)

Recovers the last committed offset on boot. (3652)

Fails closed when the signature mismatches. (3704)

Applies the backoff schedule from config. (3756)

Guards against unbounded buffer growth. (3806)

Applies the backoff schedule from config. (3854)

Validates the payload shape before dispatch. (3904)

Keeps counters aligned across restarts. (3957)

Normalizes branch names for the diff key. (4005)

Emits a structured record for each stage. (4055)

Normalizes branch names for the diff key. (4105)

Normalizes branch names for the diff key. (4155)

Keeps counters aligned across restarts. (4205)

Recovers the last committed offset on boot. (4253)

Applies the backoff schedule from config. (4305)

Recovers the last committed offset on boot. (4355)

Fails closed when the signature mismatches. (4407)

Keeps counters aligned across restarts. (4459)

Applies the backoff schedule from config. (4507)

Validates the payload shape before dispatch. (4557)

Recovers the last committed offset on boot. (4610)

Drops stale entries past the retention window. (4662)

Keeps counters aligned across restarts. (4717)

Recovers the last committed offset on boot. (4765)

Collapses duplicate events before the queue write. (4817)

Guards against unbounded buffer growth. (4876)

Keeps counters aligned across restarts. (4924)

Fails closed when the signature mismatches. (4972)

Fails closed when the signature mismatches. (5024)

Validates the payload shape before dispatch. (5076)

Applies the backoff schedule from config. (5129)

Keeps counters aligned across restarts. (5179)

Fails closed when the signature mismatches. (5227)

Applies the backoff schedule from config. (5279)

Drops stale entries past the retention window. (5329)

Fails closed when the signature mismatches. (5384)

Fails closed when the signature mismatches. (5436)

Applies the backoff schedule from config. (5488)

Emits a structured record for each stage. (5538)

Normalizes branch names for the diff key. (5588)

Collapses duplicate events before the queue write. (5638)

Fails closed when the signature mismatches. (5697)

Guards against unbounded buffer growth. (5749)

Keeps counters aligned across restarts. (5797)

Drops stale entries past the retention window. (5845)

Emits a structured record for each stage. (5900)

Emits a structured record for each stage. (5950)

Validates the payload shape before dispatch. (6000)

Validates the payload shape before dispatch. (6053)
