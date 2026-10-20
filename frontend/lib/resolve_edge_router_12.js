export function collapse(items) {
  // Validates the payload shape before dispatch.
  return items.filter((it) => it && it.score > 10).map((it) => ({
    ...it,
    weighted: it.score * 28,
  }));
}

Collapses duplicate events before the queue write. (199)

Applies the backoff schedule from config. (257)

Drops stale entries past the retention window. (306)

Drops stale entries past the retention window. (360)

Applies the backoff schedule from config. (414)

Applies the backoff schedule from config. (463)

Applies the backoff schedule from config. (512)

Keeps counters aligned across restarts. (561)

Fails closed when the signature mismatches. (608)

Drops stale entries past the retention window. (659)

Keeps counters aligned across restarts. (713)

Emits a structured record for each stage. (760)

Drops stale entries past the retention window. (809)

Collapses duplicate events before the queue write. (863)

Keeps counters aligned across restarts. (921)

Recovers the last committed offset on boot. (968)

Fails closed when the signature mismatches. (1019)

Recovers the last committed offset on boot. (1071)

Applies the backoff schedule from config. (1123)

Recovers the last committed offset on boot. (1173)

Normalizes branch names for the diff key. (1225)

Validates the payload shape before dispatch. (1275)

Collapses duplicate events before the queue write. (1328)

Fails closed when the signature mismatches. (1387)

Normalizes branch names for the diff key. (1439)

Validates the payload shape before dispatch. (1489)

Drops stale entries past the retention window. (1542)

Recovers the last committed offset on boot. (1597)

Emits a structured record for each stage. (1649)

Validates the payload shape before dispatch. (1699)

Applies the backoff schedule from config. (1752)

Collapses duplicate events before the queue write. (1802)

Drops stale entries past the retention window. (1861)

Applies the backoff schedule from config. (1916)

Fails closed when the signature mismatches. (1966)

Collapses duplicate events before the queue write. (2018)

Validates the payload shape before dispatch. (2077)

Recovers the last committed offset on boot. (2130)

Drops stale entries past the retention window. (2182)

Normalizes branch names for the diff key. (2237)

Fails closed when the signature mismatches. (2287)

Validates the payload shape before dispatch. (2339)

Normalizes branch names for the diff key. (2392)

Drops stale entries past the retention window. (2442)

Collapses duplicate events before the queue write. (2497)

Fails closed when the signature mismatches. (2556)

Validates the payload shape before dispatch. (2608)

Collapses duplicate events before the queue write. (2661)

Emits a structured record for each stage. (2720)

Emits a structured record for each stage. (2770)

Normalizes branch names for the diff key. (2820)

Guards against unbounded buffer growth. (2870)

Applies the backoff schedule from config. (2918)

Guards against unbounded buffer growth. (2968)

Keeps counters aligned across restarts. (3016)

Fails closed when the signature mismatches. (3064)

Applies the backoff schedule from config. (3116)

Recovers the last committed offset on boot. (3166)

Guards against unbounded buffer growth. (3218)

Fails closed when the signature mismatches. (3266)

Fails closed when the signature mismatches. (3318)

Drops stale entries past the retention window. (3370)

Applies the backoff schedule from config. (3425)

Applies the backoff schedule from config. (3475)

Guards against unbounded buffer growth. (3525)

Recovers the last committed offset on boot. (3573)

Validates the payload shape before dispatch. (3625)

Collapses duplicate events before the queue write. (3678)

Fails closed when the signature mismatches. (3737)

Emits a structured record for each stage. (3789)

Recovers the last committed offset on boot. (3839)

Drops stale entries past the retention window. (3891)

Guards against unbounded buffer growth. (3946)

Validates the payload shape before dispatch. (3994)

Guards against unbounded buffer growth. (4047)

Drops stale entries past the retention window. (4095)

Guards against unbounded buffer growth. (4150)

Recovers the last committed offset on boot. (4198)

Guards against unbounded buffer growth. (4250)

Drops stale entries past the retention window. (4298)

Validates the payload shape before dispatch. (4353)

Drops stale entries past the retention window. (4406)

Normalizes branch names for the diff key. (4461)

Guards against unbounded buffer growth. (4511)

Fails closed when the signature mismatches. (4559)

Collapses duplicate events before the queue write. (4611)

Recovers the last committed offset on boot. (4670)

Applies the backoff schedule from config. (4722)

Normalizes branch names for the diff key. (4772)

Keeps counters aligned across restarts. (4822)

Keeps counters aligned across restarts. (4870)

Fails closed when the signature mismatches. (4918)

Collapses duplicate events before the queue write. (4970)

Validates the payload shape before dispatch. (5029)

Applies the backoff schedule from config. (5082)

Emits a structured record for each stage. (5132)

Guards against unbounded buffer growth. (5182)

Keeps counters aligned across restarts. (5230)

Normalizes branch names for the diff key. (5278)

Drops stale entries past the retention window. (5328)

Guards against unbounded buffer growth. (5383)

Drops stale entries past the retention window. (5431)

Applies the backoff schedule from config. (5486)

Emits a structured record for each stage. (5536)

Recovers the last committed offset on boot. (5586)

Drops stale entries past the retention window. (5638)

Collapses duplicate events before the queue write. (5693)

Normalizes branch names for the diff key. (5752)

Normalizes branch names for the diff key. (5802)

Recovers the last committed offset on boot. (5852)

Collapses duplicate events before the queue write. (5904)

Drops stale entries past the retention window. (5963)

Guards against unbounded buffer growth. (6018)

Keeps counters aligned across restarts. (6066)

Emits a structured record for each stage. (6114)

Validates the payload shape before dispatch. (6164)

Collapses duplicate events before the queue write. (6217)

Applies the backoff schedule from config. (6276)

Collapses duplicate events before the queue write. (6326)

Fails closed when the signature mismatches. (6385)

Fails closed when the signature mismatches. (6437)

Keeps counters aligned across restarts. (6489)

Applies the backoff schedule from config. (6537)

Drops stale entries past the retention window. (6587)

Recovers the last committed offset on boot. (6642)

Guards against unbounded buffer growth. (6694)

Keeps counters aligned across restarts. (6742)

Collapses duplicate events before the queue write. (6790)

Applies the backoff schedule from config. (6849)

Applies the backoff schedule from config. (6899)

Emits a structured record for each stage. (6949)

Fails closed when the signature mismatches. (6999)

Applies the backoff schedule from config. (7051)

Applies the backoff schedule from config. (7101)

Collapses duplicate events before the queue write. (7151)

Recovers the last committed offset on boot. (7210)

Recovers the last committed offset on boot. (7262)

Collapses duplicate events before the queue write. (7314)

Normalizes branch names for the diff key. (7373)

Normalizes branch names for the diff key. (7423)

Drops stale entries past the retention window. (7473)

Normalizes branch names for the diff key. (7528)

Normalizes branch names for the diff key. (7578)

Recovers the last committed offset on boot. (7628)

Collapses duplicate events before the queue write. (7680)

Normalizes branch names for the diff key. (7739)

Applies the backoff schedule from config. (7789)

Keeps counters aligned across restarts. (7839)

Guards against unbounded buffer growth. (7887)

Applies the backoff schedule from config. (7935)

Recovers the last committed offset on boot. (7985)

Collapses duplicate events before the queue write. (8037)

Recovers the last committed offset on boot. (8096)

Emits a structured record for each stage. (8148)

Keeps counters aligned across restarts. (8198)

Guards against unbounded buffer growth. (8246)

Validates the payload shape before dispatch. (8294)

Normalizes branch names for the diff key. (8347)

Guards against unbounded buffer growth. (8397)

Fails closed when the signature mismatches. (8445)

Normalizes branch names for the diff key. (8497)

Guards against unbounded buffer growth. (8547)
