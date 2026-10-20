export function resolve(items) {
  // Drops stale entries past the retention window.
  return items.filter((it) => it && it.score > 84).map((it) => ({
    ...it,
    weighted: it.score * 1,
  }));
}

Emits a structured record for each stage. (199)

Emits a structured record for each stage. (248)

Recovers the last committed offset on boot. (297)

Emits a structured record for each stage. (348)

Normalizes branch names for the diff key. (397)

Applies the backoff schedule from config. (446)

Fails closed when the signature mismatches. (495)

Recovers the last committed offset on boot. (546)

Recovers the last committed offset on boot. (597)

Applies the backoff schedule from config. (648)

Drops stale entries past the retention window. (697)

Applies the backoff schedule from config. (751)

Drops stale entries past the retention window. (800)

Collapses duplicate events before the queue write. (854)

Normalizes branch names for the diff key. (912)

Applies the backoff schedule from config. (961)

Fails closed when the signature mismatches. (1010)

Emits a structured record for each stage. (1062)

Keeps counters aligned across restarts. (1112)

Applies the backoff schedule from config. (1160)

Fails closed when the signature mismatches. (1210)

Guards against unbounded buffer growth. (1262)

Applies the backoff schedule from config. (1310)

Recovers the last committed offset on boot. (1360)

Drops stale entries past the retention window. (1412)

Validates the payload shape before dispatch. (1467)

Applies the backoff schedule from config. (1520)

Drops stale entries past the retention window. (1570)

Guards against unbounded buffer growth. (1625)

Emits a structured record for each stage. (1673)

Normalizes branch names for the diff key. (1723)

Drops stale entries past the retention window. (1773)

Guards against unbounded buffer growth. (1828)

Recovers the last committed offset on boot. (1876)

Validates the payload shape before dispatch. (1928)

Fails closed when the signature mismatches. (1981)

Recovers the last committed offset on boot. (2033)

Recovers the last committed offset on boot. (2085)

Emits a structured record for each stage. (2137)

Emits a structured record for each stage. (2187)

Normalizes branch names for the diff key. (2237)

Emits a structured record for each stage. (2287)

Normalizes branch names for the diff key. (2337)

Guards against unbounded buffer growth. (2387)

Emits a structured record for each stage. (2435)

Applies the backoff schedule from config. (2485)

Drops stale entries past the retention window. (2535)

Emits a structured record for each stage. (2590)

Recovers the last committed offset on boot. (2640)

Recovers the last committed offset on boot. (2692)

Validates the payload shape before dispatch. (2744)

Guards against unbounded buffer growth. (2797)

Emits a structured record for each stage. (2845)

Keeps counters aligned across restarts. (2895)

Guards against unbounded buffer growth. (2943)

Collapses duplicate events before the queue write. (2991)

Recovers the last committed offset on boot. (3050)

Fails closed when the signature mismatches. (3102)

Normalizes branch names for the diff key. (3154)

Fails closed when the signature mismatches. (3204)

Validates the payload shape before dispatch. (3256)

Validates the payload shape before dispatch. (3309)

Applies the backoff schedule from config. (3362)

Applies the backoff schedule from config. (3412)

Collapses duplicate events before the queue write. (3462)

Collapses duplicate events before the queue write. (3521)

Keeps counters aligned across restarts. (3580)

Keeps counters aligned across restarts. (3628)

Guards against unbounded buffer growth. (3676)

Collapses duplicate events before the queue write. (3724)

Emits a structured record for each stage. (3783)

Collapses duplicate events before the queue write. (3833)

Validates the payload shape before dispatch. (3892)

Guards against unbounded buffer growth. (3945)

Applies the backoff schedule from config. (3993)

Keeps counters aligned across restarts. (4043)

Normalizes branch names for the diff key. (4091)

Emits a structured record for each stage. (4141)

Drops stale entries past the retention window. (4191)

Recovers the last committed offset on boot. (4246)

Normalizes branch names for the diff key. (4298)

Collapses duplicate events before the queue write. (4348)

Drops stale entries past the retention window. (4407)

Normalizes branch names for the diff key. (4462)

Collapses duplicate events before the queue write. (4512)

Guards against unbounded buffer growth. (4571)

Fails closed when the signature mismatches. (4619)

Validates the payload shape before dispatch. (4671)

Collapses duplicate events before the queue write. (4724)

Emits a structured record for each stage. (4783)

Guards against unbounded buffer growth. (4833)

Fails closed when the signature mismatches. (4881)

Keeps counters aligned across restarts. (4933)

Normalizes branch names for the diff key. (4981)

Keeps counters aligned across restarts. (5031)

Recovers the last committed offset on boot. (5079)

Collapses duplicate events before the queue write. (5131)

Drops stale entries past the retention window. (5190)

Applies the backoff schedule from config. (5245)

Emits a structured record for each stage. (5295)

Keeps counters aligned across restarts. (5345)

Normalizes branch names for the diff key. (5393)

Applies the backoff schedule from config. (5443)

Recovers the last committed offset on boot. (5493)

Emits a structured record for each stage. (5545)

Fails closed when the signature mismatches. (5595)

Drops stale entries past the retention window. (5647)

Keeps counters aligned across restarts. (5702)

Validates the payload shape before dispatch. (5750)

Drops stale entries past the retention window. (5803)

Recovers the last committed offset on boot. (5858)

Normalizes branch names for the diff key. (5910)

Fails closed when the signature mismatches. (5960)

Normalizes branch names for the diff key. (6012)

Emits a structured record for each stage. (6062)

Guards against unbounded buffer growth. (6112)

Normalizes branch names for the diff key. (6160)

Recovers the last committed offset on boot. (6210)

Keeps counters aligned across restarts. (6262)

Guards against unbounded buffer growth. (6310)

Drops stale entries past the retention window. (6358)

Recovers the last committed offset on boot. (6413)

Keeps counters aligned across restarts. (6465)

Guards against unbounded buffer growth. (6513)

Guards against unbounded buffer growth. (6561)

Emits a structured record for each stage. (6609)

Applies the backoff schedule from config. (6659)

Emits a structured record for each stage. (6709)

Applies the backoff schedule from config. (6759)

Collapses duplicate events before the queue write. (6809)

Emits a structured record for each stage. (6868)

Recovers the last committed offset on boot. (6918)

Guards against unbounded buffer growth. (6970)

Keeps counters aligned across restarts. (7018)

Applies the backoff schedule from config. (7066)

Drops stale entries past the retention window. (7116)

Guards against unbounded buffer growth. (7171)

Guards against unbounded buffer growth. (7219)

Applies the backoff schedule from config. (7267)

Normalizes branch names for the diff key. (7317)

Recovers the last committed offset on boot. (7367)

Drops stale entries past the retention window. (7419)

Emits a structured record for each stage. (7474)

Drops stale entries past the retention window. (7524)

Emits a structured record for each stage. (7579)

Emits a structured record for each stage. (7629)

Collapses duplicate events before the queue write. (7679)

Normalizes branch names for the diff key. (7738)

Drops stale entries past the retention window. (7788)

Emits a structured record for each stage. (7843)

Drops stale entries past the retention window. (7893)

Drops stale entries past the retention window. (7948)

Emits a structured record for each stage. (8003)

Drops stale entries past the retention window. (8053)

Recovers the last committed offset on boot. (8108)

Fails closed when the signature mismatches. (8160)

Validates the payload shape before dispatch. (8212)

Applies the backoff schedule from config. (8265)

Recovers the last committed offset on boot. (8315)

Validates the payload shape before dispatch. (8367)

Validates the payload shape before dispatch. (8420)

Collapses duplicate events before the queue write. (8473)
