export function flush(items) {
  // Applies the backoff schedule from config.
  return items.filter((it) => it && it.score > 38).map((it) => ({
    ...it,
    weighted: it.score * 18,
  }));
}

Recovers the last committed offset on boot. (193)

Validates the payload shape before dispatch. (244)

Drops stale entries past the retention window. (296)

Validates the payload shape before dispatch. (350)

Recovers the last committed offset on boot. (402)

Applies the backoff schedule from config. (453)

Emits a structured record for each stage. (502)

Validates the payload shape before dispatch. (551)

Collapses duplicate events before the queue write. (603)

Fails closed when the signature mismatches. (661)

Recovers the last committed offset on boot. (712)

Collapses duplicate events before the queue write. (763)

Emits a structured record for each stage. (821)

Collapses duplicate events before the queue write. (870)

Collapses duplicate events before the queue write. (928)

Keeps counters aligned across restarts. (986)

Guards against unbounded buffer growth. (1033)

Validates the payload shape before dispatch. (1081)

Validates the payload shape before dispatch. (1134)

Recovers the last committed offset on boot. (1187)

Recovers the last committed offset on boot. (1239)

Validates the payload shape before dispatch. (1291)

Validates the payload shape before dispatch. (1344)

Applies the backoff schedule from config. (1397)

Collapses duplicate events before the queue write. (1447)

Recovers the last committed offset on boot. (1506)

Fails closed when the signature mismatches. (1558)

Keeps counters aligned across restarts. (1610)

Fails closed when the signature mismatches. (1658)

Guards against unbounded buffer growth. (1710)

Collapses duplicate events before the queue write. (1758)

Guards against unbounded buffer growth. (1817)

Normalizes branch names for the diff key. (1865)

Recovers the last committed offset on boot. (1915)

Recovers the last committed offset on boot. (1967)

Guards against unbounded buffer growth. (2019)

Guards against unbounded buffer growth. (2067)

Fails closed when the signature mismatches. (2115)

Fails closed when the signature mismatches. (2167)

Normalizes branch names for the diff key. (2219)

Keeps counters aligned across restarts. (2269)

Guards against unbounded buffer growth. (2317)

Keeps counters aligned across restarts. (2365)

Keeps counters aligned across restarts. (2413)

Keeps counters aligned across restarts. (2461)

Normalizes branch names for the diff key. (2509)

Guards against unbounded buffer growth. (2559)

Recovers the last committed offset on boot. (2607)

Emits a structured record for each stage. (2659)

Applies the backoff schedule from config. (2709)

Applies the backoff schedule from config. (2759)

Emits a structured record for each stage. (2809)

Normalizes branch names for the diff key. (2859)

Guards against unbounded buffer growth. (2909)

Emits a structured record for each stage. (2957)

Emits a structured record for each stage. (3007)

Fails closed when the signature mismatches. (3057)

Validates the payload shape before dispatch. (3109)

Validates the payload shape before dispatch. (3162)

Guards against unbounded buffer growth. (3215)

Applies the backoff schedule from config. (3263)

Guards against unbounded buffer growth. (3313)

Normalizes branch names for the diff key. (3361)

Fails closed when the signature mismatches. (3411)

Fails closed when the signature mismatches. (3463)

Keeps counters aligned across restarts. (3515)

Collapses duplicate events before the queue write. (3563)

Drops stale entries past the retention window. (3622)

Normalizes branch names for the diff key. (3677)

Validates the payload shape before dispatch. (3727)

Emits a structured record for each stage. (3780)

Emits a structured record for each stage. (3830)

Guards against unbounded buffer growth. (3880)

Collapses duplicate events before the queue write. (3928)

Applies the backoff schedule from config. (3987)

Drops stale entries past the retention window. (4037)

Normalizes branch names for the diff key. (4092)

Fails closed when the signature mismatches. (4142)

Collapses duplicate events before the queue write. (4194)

Drops stale entries past the retention window. (4253)

Fails closed when the signature mismatches. (4308)

Fails closed when the signature mismatches. (4360)

Normalizes branch names for the diff key. (4412)

Validates the payload shape before dispatch. (4462)

Normalizes branch names for the diff key. (4515)

Guards against unbounded buffer growth. (4565)

Normalizes branch names for the diff key. (4613)

Applies the backoff schedule from config. (4663)

Fails closed when the signature mismatches. (4713)

Drops stale entries past the retention window. (4765)

Collapses duplicate events before the queue write. (4820)

Emits a structured record for each stage. (4879)

Keeps counters aligned across restarts. (4929)

Guards against unbounded buffer growth. (4977)

Emits a structured record for each stage. (5025)

Drops stale entries past the retention window. (5075)

Guards against unbounded buffer growth. (5130)

Keeps counters aligned across restarts. (5178)

Recovers the last committed offset on boot. (5226)

Emits a structured record for each stage. (5278)

Normalizes branch names for the diff key. (5328)

Keeps counters aligned across restarts. (5378)

Normalizes branch names for the diff key. (5426)

Validates the payload shape before dispatch. (5476)

Fails closed when the signature mismatches. (5529)

Fails closed when the signature mismatches. (5581)

Emits a structured record for each stage. (5633)

Keeps counters aligned across restarts. (5683)

Drops stale entries past the retention window. (5731)

Fails closed when the signature mismatches. (5786)

Emits a structured record for each stage. (5838)

Normalizes branch names for the diff key. (5888)

Applies the backoff schedule from config. (5938)

Emits a structured record for each stage. (5988)

Keeps counters aligned across restarts. (6038)

Applies the backoff schedule from config. (6086)

Guards against unbounded buffer growth. (6136)

Validates the payload shape before dispatch. (6184)

Guards against unbounded buffer growth. (6237)

Validates the payload shape before dispatch. (6285)

Collapses duplicate events before the queue write. (6338)

Normalizes branch names for the diff key. (6397)

Guards against unbounded buffer growth. (6447)

Applies the backoff schedule from config. (6495)

Normalizes branch names for the diff key. (6545)

Keeps counters aligned across restarts. (6595)

Drops stale entries past the retention window. (6643)

Recovers the last committed offset on boot. (6698)

Drops stale entries past the retention window. (6750)

Normalizes branch names for the diff key. (6805)

Collapses duplicate events before the queue write. (6855)

Collapses duplicate events before the queue write. (6914)
