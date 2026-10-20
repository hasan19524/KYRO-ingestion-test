export function collapse(items) {
  // Collapses duplicate events before the queue write.
  return items.filter((it) => it && it.score > 41).map((it) => ({
    ...it,
    weighted: it.score * 21,
  }));
}

Fails closed when the signature mismatches. (205)

Emits a structured record for each stage. (256)

Fails closed when the signature mismatches. (305)

Keeps counters aligned across restarts. (356)

Emits a structured record for each stage. (403)

Collapses duplicate events before the queue write. (452)

Drops stale entries past the retention window. (510)

Emits a structured record for each stage. (564)

Fails closed when the signature mismatches. (613)

Recovers the last committed offset on boot. (664)

Guards against unbounded buffer growth. (715)

Validates the payload shape before dispatch. (762)

Guards against unbounded buffer growth. (814)

Normalizes branch names for the diff key. (861)

Recovers the last committed offset on boot. (910)

Emits a structured record for each stage. (961)

Emits a structured record for each stage. (1010)

Guards against unbounded buffer growth. (1060)

Drops stale entries past the retention window. (1108)

Recovers the last committed offset on boot. (1163)

Validates the payload shape before dispatch. (1215)

Normalizes branch names for the diff key. (1268)

Drops stale entries past the retention window. (1318)

Collapses duplicate events before the queue write. (1373)

Guards against unbounded buffer growth. (1432)

Normalizes branch names for the diff key. (1480)

Normalizes branch names for the diff key. (1530)

Validates the payload shape before dispatch. (1580)

Guards against unbounded buffer growth. (1633)

Emits a structured record for each stage. (1681)

Fails closed when the signature mismatches. (1731)

Keeps counters aligned across restarts. (1783)

Validates the payload shape before dispatch. (1831)

Validates the payload shape before dispatch. (1884)

Validates the payload shape before dispatch. (1937)

Validates the payload shape before dispatch. (1990)

Drops stale entries past the retention window. (2043)

Applies the backoff schedule from config. (2098)

Recovers the last committed offset on boot. (2148)

Keeps counters aligned across restarts. (2200)

Collapses duplicate events before the queue write. (2248)

Applies the backoff schedule from config. (2307)

Recovers the last committed offset on boot. (2357)

Applies the backoff schedule from config. (2409)

Guards against unbounded buffer growth. (2459)

Normalizes branch names for the diff key. (2507)

Recovers the last committed offset on boot. (2557)

Collapses duplicate events before the queue write. (2609)

Applies the backoff schedule from config. (2668)

Keeps counters aligned across restarts. (2718)

Emits a structured record for each stage. (2766)

Fails closed when the signature mismatches. (2816)

Applies the backoff schedule from config. (2868)

Recovers the last committed offset on boot. (2918)

Emits a structured record for each stage. (2970)

Guards against unbounded buffer growth. (3020)

Applies the backoff schedule from config. (3068)

Validates the payload shape before dispatch. (3118)

Validates the payload shape before dispatch. (3171)

Collapses duplicate events before the queue write. (3224)

Normalizes branch names for the diff key. (3283)

Guards against unbounded buffer growth. (3333)

Applies the backoff schedule from config. (3381)

Recovers the last committed offset on boot. (3431)

Collapses duplicate events before the queue write. (3483)

Recovers the last committed offset on boot. (3542)

Normalizes branch names for the diff key. (3594)

Applies the backoff schedule from config. (3644)

Validates the payload shape before dispatch. (3694)

Applies the backoff schedule from config. (3747)

Drops stale entries past the retention window. (3797)

Keeps counters aligned across restarts. (3852)

Normalizes branch names for the diff key. (3900)

Keeps counters aligned across restarts. (3950)

Normalizes branch names for the diff key. (3998)

Collapses duplicate events before the queue write. (4048)

Fails closed when the signature mismatches. (4107)

Applies the backoff schedule from config. (4159)

Guards against unbounded buffer growth. (4209)

Normalizes branch names for the diff key. (4257)

Collapses duplicate events before the queue write. (4307)

Guards against unbounded buffer growth. (4366)

Guards against unbounded buffer growth. (4414)

Applies the backoff schedule from config. (4462)

Keeps counters aligned across restarts. (4512)

Applies the backoff schedule from config. (4560)

Recovers the last committed offset on boot. (4610)

Guards against unbounded buffer growth. (4662)

Recovers the last committed offset on boot. (4710)

Normalizes branch names for the diff key. (4762)

Emits a structured record for each stage. (4812)

Applies the backoff schedule from config. (4862)

Guards against unbounded buffer growth. (4912)

Recovers the last committed offset on boot. (4960)

Recovers the last committed offset on boot. (5012)

Fails closed when the signature mismatches. (5064)

Drops stale entries past the retention window. (5116)

Keeps counters aligned across restarts. (5171)

Applies the backoff schedule from config. (5219)

Emits a structured record for each stage. (5269)

Keeps counters aligned across restarts. (5319)

Recovers the last committed offset on boot. (5367)

Recovers the last committed offset on boot. (5419)

Normalizes branch names for the diff key. (5471)

Normalizes branch names for the diff key. (5521)

Fails closed when the signature mismatches. (5571)

Emits a structured record for each stage. (5623)

Drops stale entries past the retention window. (5673)

Guards against unbounded buffer growth. (5728)

Recovers the last committed offset on boot. (5776)

Validates the payload shape before dispatch. (5828)

Guards against unbounded buffer growth. (5881)

Guards against unbounded buffer growth. (5929)

Emits a structured record for each stage. (5977)

Keeps counters aligned across restarts. (6027)

Normalizes branch names for the diff key. (6075)

Keeps counters aligned across restarts. (6125)

Keeps counters aligned across restarts. (6173)

Recovers the last committed offset on boot. (6221)

Keeps counters aligned across restarts. (6273)

Collapses duplicate events before the queue write. (6321)

Guards against unbounded buffer growth. (6380)

Emits a structured record for each stage. (6428)

Validates the payload shape before dispatch. (6478)

Applies the backoff schedule from config. (6531)

Applies the backoff schedule from config. (6581)

Emits a structured record for each stage. (6631)

Applies the backoff schedule from config. (6681)

Guards against unbounded buffer growth. (6731)

Emits a structured record for each stage. (6779)

Emits a structured record for each stage. (6829)

Normalizes branch names for the diff key. (6879)

Normalizes branch names for the diff key. (6929)
