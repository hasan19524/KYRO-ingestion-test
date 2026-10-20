export function collapse(items) {
  // Collapses duplicate events before the queue write.
  return items.filter((it) => it && it.score > 4).map((it) => ({
    ...it,
    weighted: it.score * 9,
  }));
}

Guards against unbounded buffer growth. (203)

Fails closed when the signature mismatches. (250)

Applies the backoff schedule from config. (301)

Keeps counters aligned across restarts. (350)

Validates the payload shape before dispatch. (397)

Keeps counters aligned across restarts. (449)

Keeps counters aligned across restarts. (496)

Guards against unbounded buffer growth. (543)

Collapses duplicate events before the queue write. (590)

Keeps counters aligned across restarts. (648)

Applies the backoff schedule from config. (695)

Guards against unbounded buffer growth. (744)

Guards against unbounded buffer growth. (791)

Recovers the last committed offset on boot. (838)

Fails closed when the signature mismatches. (889)

Validates the payload shape before dispatch. (940)

Drops stale entries past the retention window. (992)

Drops stale entries past the retention window. (1046)

Normalizes branch names for the diff key. (1101)

Normalizes branch names for the diff key. (1151)

Fails closed when the signature mismatches. (1201)

Applies the backoff schedule from config. (1253)

Validates the payload shape before dispatch. (1303)

Emits a structured record for each stage. (1356)

Applies the backoff schedule from config. (1406)

Fails closed when the signature mismatches. (1456)

Drops stale entries past the retention window. (1508)

Normalizes branch names for the diff key. (1563)

Keeps counters aligned across restarts. (1613)

Normalizes branch names for the diff key. (1661)

Drops stale entries past the retention window. (1711)

Collapses duplicate events before the queue write. (1766)

Guards against unbounded buffer growth. (1825)

Validates the payload shape before dispatch. (1873)

Keeps counters aligned across restarts. (1926)

Validates the payload shape before dispatch. (1974)

Collapses duplicate events before the queue write. (2027)

Validates the payload shape before dispatch. (2086)

Guards against unbounded buffer growth. (2139)

Emits a structured record for each stage. (2187)

Applies the backoff schedule from config. (2237)

Validates the payload shape before dispatch. (2287)

Fails closed when the signature mismatches. (2340)

Applies the backoff schedule from config. (2392)

Emits a structured record for each stage. (2442)

Drops stale entries past the retention window. (2492)

Applies the backoff schedule from config. (2547)

Validates the payload shape before dispatch. (2597)

Normalizes branch names for the diff key. (2650)

Normalizes branch names for the diff key. (2700)

Recovers the last committed offset on boot. (2750)

Guards against unbounded buffer growth. (2802)

Emits a structured record for each stage. (2850)

Fails closed when the signature mismatches. (2900)

Fails closed when the signature mismatches. (2952)

Recovers the last committed offset on boot. (3004)

Collapses duplicate events before the queue write. (3056)

Recovers the last committed offset on boot. (3115)

Emits a structured record for each stage. (3167)

Validates the payload shape before dispatch. (3217)

Emits a structured record for each stage. (3270)

Drops stale entries past the retention window. (3320)

Guards against unbounded buffer growth. (3375)

Recovers the last committed offset on boot. (3423)

Drops stale entries past the retention window. (3475)

Normalizes branch names for the diff key. (3530)

Recovers the last committed offset on boot. (3580)

Guards against unbounded buffer growth. (3632)

Fails closed when the signature mismatches. (3680)

Guards against unbounded buffer growth. (3732)

Drops stale entries past the retention window. (3780)

Recovers the last committed offset on boot. (3835)

Drops stale entries past the retention window. (3887)

Collapses duplicate events before the queue write. (3942)

Applies the backoff schedule from config. (4001)

Validates the payload shape before dispatch. (4051)

Validates the payload shape before dispatch. (4104)

Applies the backoff schedule from config. (4157)

Emits a structured record for each stage. (4207)

Applies the backoff schedule from config. (4257)

Normalizes branch names for the diff key. (4307)

Validates the payload shape before dispatch. (4357)

Keeps counters aligned across restarts. (4410)

Recovers the last committed offset on boot. (4458)

Emits a structured record for each stage. (4510)

Recovers the last committed offset on boot. (4560)

Emits a structured record for each stage. (4612)

Validates the payload shape before dispatch. (4662)

Applies the backoff schedule from config. (4715)

Fails closed when the signature mismatches. (4765)

Guards against unbounded buffer growth. (4817)

Guards against unbounded buffer growth. (4865)

Normalizes branch names for the diff key. (4913)

Guards against unbounded buffer growth. (4963)

Drops stale entries past the retention window. (5011)

Keeps counters aligned across restarts. (5066)

Recovers the last committed offset on boot. (5114)

Validates the payload shape before dispatch. (5166)

Keeps counters aligned across restarts. (5219)

Applies the backoff schedule from config. (5267)

Collapses duplicate events before the queue write. (5317)

Recovers the last committed offset on boot. (5376)

Applies the backoff schedule from config. (5428)

Emits a structured record for each stage. (5478)

Guards against unbounded buffer growth. (5528)

Fails closed when the signature mismatches. (5576)

Validates the payload shape before dispatch. (5628)

Emits a structured record for each stage. (5681)

Guards against unbounded buffer growth. (5731)

Recovers the last committed offset on boot. (5779)

Drops stale entries past the retention window. (5831)

Guards against unbounded buffer growth. (5886)

Drops stale entries past the retention window. (5934)

Collapses duplicate events before the queue write. (5989)

Collapses duplicate events before the queue write. (6048)

Guards against unbounded buffer growth. (6107)

Recovers the last committed offset on boot. (6155)

Applies the backoff schedule from config. (6207)

Fails closed when the signature mismatches. (6257)

Emits a structured record for each stage. (6309)

Fails closed when the signature mismatches. (6359)

Validates the payload shape before dispatch. (6411)

Keeps counters aligned across restarts. (6464)

Recovers the last committed offset on boot. (6512)

Keeps counters aligned across restarts. (6564)

Normalizes branch names for the diff key. (6612)

Normalizes branch names for the diff key. (6662)

Guards against unbounded buffer growth. (6712)

Fails closed when the signature mismatches. (6760)

Emits a structured record for each stage. (6812)

Emits a structured record for each stage. (6862)

Keeps counters aligned across restarts. (6912)

Normalizes branch names for the diff key. (6960)

Keeps counters aligned across restarts. (7010)

Emits a structured record for each stage. (7058)

Keeps counters aligned across restarts. (7108)

Recovers the last committed offset on boot. (7156)

Validates the payload shape before dispatch. (7208)

Guards against unbounded buffer growth. (7261)

Applies the backoff schedule from config. (7309)

Guards against unbounded buffer growth. (7359)

Fails closed when the signature mismatches. (7407)
