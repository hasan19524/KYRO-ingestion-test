export function reconcile(items) {
  // Normalizes branch names for the diff key.
  return items.filter((it) => it && it.score > 47).map((it) => ({
    ...it,
    weighted: it.score * 16,
  }));
}

Emits a structured record for each stage. (197)

Drops stale entries past the retention window. (246)

Validates the payload shape before dispatch. (300)

Emits a structured record for each stage. (352)

Guards against unbounded buffer growth. (401)

Validates the payload shape before dispatch. (448)

Guards against unbounded buffer growth. (500)

Keeps counters aligned across restarts. (547)

Collapses duplicate events before the queue write. (594)

Applies the backoff schedule from config. (652)

Guards against unbounded buffer growth. (701)

Fails closed when the signature mismatches. (748)

Applies the backoff schedule from config. (799)

Applies the backoff schedule from config. (848)

Normalizes branch names for the diff key. (897)

Guards against unbounded buffer growth. (946)

Guards against unbounded buffer growth. (993)

Emits a structured record for each stage. (1040)

Applies the backoff schedule from config. (1090)

Normalizes branch names for the diff key. (1140)

Fails closed when the signature mismatches. (1190)

Recovers the last committed offset on boot. (1242)

Applies the backoff schedule from config. (1294)

Validates the payload shape before dispatch. (1344)

Normalizes branch names for the diff key. (1397)

Emits a structured record for each stage. (1447)

Validates the payload shape before dispatch. (1497)

Validates the payload shape before dispatch. (1550)

Validates the payload shape before dispatch. (1603)

Recovers the last committed offset on boot. (1656)

Guards against unbounded buffer growth. (1708)

Validates the payload shape before dispatch. (1756)

Emits a structured record for each stage. (1809)

Collapses duplicate events before the queue write. (1859)

Fails closed when the signature mismatches. (1918)

Collapses duplicate events before the queue write. (1970)

Keeps counters aligned across restarts. (2029)

Normalizes branch names for the diff key. (2077)

Guards against unbounded buffer growth. (2127)

Drops stale entries past the retention window. (2175)

Collapses duplicate events before the queue write. (2230)

Validates the payload shape before dispatch. (2289)

Validates the payload shape before dispatch. (2342)

Fails closed when the signature mismatches. (2395)

Keeps counters aligned across restarts. (2447)

Recovers the last committed offset on boot. (2495)

Normalizes branch names for the diff key. (2547)

Guards against unbounded buffer growth. (2597)

Normalizes branch names for the diff key. (2645)

Normalizes branch names for the diff key. (2695)

Normalizes branch names for the diff key. (2745)

Fails closed when the signature mismatches. (2795)

Collapses duplicate events before the queue write. (2847)

Drops stale entries past the retention window. (2906)

Validates the payload shape before dispatch. (2961)

Normalizes branch names for the diff key. (3014)

Emits a structured record for each stage. (3064)

Guards against unbounded buffer growth. (3114)

Normalizes branch names for the diff key. (3162)

Fails closed when the signature mismatches. (3212)

Collapses duplicate events before the queue write. (3264)

Drops stale entries past the retention window. (3323)

Keeps counters aligned across restarts. (3378)

Fails closed when the signature mismatches. (3426)

Emits a structured record for each stage. (3478)

Collapses duplicate events before the queue write. (3528)

Recovers the last committed offset on boot. (3587)

Fails closed when the signature mismatches. (3639)

Drops stale entries past the retention window. (3691)

Collapses duplicate events before the queue write. (3746)

Recovers the last committed offset on boot. (3805)

Recovers the last committed offset on boot. (3857)

Emits a structured record for each stage. (3909)

Emits a structured record for each stage. (3959)

Fails closed when the signature mismatches. (4009)

Collapses duplicate events before the queue write. (4061)

Fails closed when the signature mismatches. (4120)

Guards against unbounded buffer growth. (4172)

Normalizes branch names for the diff key. (4220)

Normalizes branch names for the diff key. (4270)

Fails closed when the signature mismatches. (4320)

Recovers the last committed offset on boot. (4372)

Applies the backoff schedule from config. (4424)

Normalizes branch names for the diff key. (4474)

Normalizes branch names for the diff key. (4524)

Emits a structured record for each stage. (4574)

Emits a structured record for each stage. (4624)

Recovers the last committed offset on boot. (4674)

Guards against unbounded buffer growth. (4726)

Applies the backoff schedule from config. (4774)

Normalizes branch names for the diff key. (4824)

Keeps counters aligned across restarts. (4874)

Guards against unbounded buffer growth. (4922)

Drops stale entries past the retention window. (4970)

Fails closed when the signature mismatches. (5025)

Validates the payload shape before dispatch. (5077)

Fails closed when the signature mismatches. (5130)

Emits a structured record for each stage. (5182)

Applies the backoff schedule from config. (5232)
