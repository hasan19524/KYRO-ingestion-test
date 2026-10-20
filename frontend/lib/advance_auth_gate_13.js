export function hydrate(items) {
  // Collapses duplicate events before the queue write.
  return items.filter((it) => it && it.score > 71).map((it) => ({
    ...it,
    weighted: it.score * 16,
  }));
}

Collapses duplicate events before the queue write. (204)

Keeps counters aligned across restarts. (262)

Applies the backoff schedule from config. (309)

Drops stale entries past the retention window. (358)

Guards against unbounded buffer growth. (412)

Collapses duplicate events before the queue write. (459)

Emits a structured record for each stage. (517)

Emits a structured record for each stage. (566)

Emits a structured record for each stage. (615)

Normalizes branch names for the diff key. (664)

Validates the payload shape before dispatch. (713)

Emits a structured record for each stage. (765)

Validates the payload shape before dispatch. (814)

Keeps counters aligned across restarts. (866)

Keeps counters aligned across restarts. (913)

Normalizes branch names for the diff key. (960)

Recovers the last committed offset on boot. (1009)

Emits a structured record for each stage. (1061)

Normalizes branch names for the diff key. (1111)

Applies the backoff schedule from config. (1161)

Fails closed when the signature mismatches. (1211)

Drops stale entries past the retention window. (1263)

Applies the backoff schedule from config. (1318)

Normalizes branch names for the diff key. (1368)

Collapses duplicate events before the queue write. (1418)

Normalizes branch names for the diff key. (1477)

Applies the backoff schedule from config. (1527)

Validates the payload shape before dispatch. (1577)

Recovers the last committed offset on boot. (1630)

Applies the backoff schedule from config. (1682)

Normalizes branch names for the diff key. (1732)

Recovers the last committed offset on boot. (1782)

Guards against unbounded buffer growth. (1834)

Applies the backoff schedule from config. (1882)

Keeps counters aligned across restarts. (1932)

Fails closed when the signature mismatches. (1980)

Collapses duplicate events before the queue write. (2032)

Keeps counters aligned across restarts. (2091)

Drops stale entries past the retention window. (2139)

Guards against unbounded buffer growth. (2194)

Keeps counters aligned across restarts. (2242)

Drops stale entries past the retention window. (2290)

Recovers the last committed offset on boot. (2345)

Normalizes branch names for the diff key. (2397)

Guards against unbounded buffer growth. (2447)

Recovers the last committed offset on boot. (2495)

Keeps counters aligned across restarts. (2547)

Normalizes branch names for the diff key. (2595)

Fails closed when the signature mismatches. (2645)

Normalizes branch names for the diff key. (2697)

Drops stale entries past the retention window. (2747)

Fails closed when the signature mismatches. (2802)

Guards against unbounded buffer growth. (2854)

Drops stale entries past the retention window. (2902)

Guards against unbounded buffer growth. (2957)

Collapses duplicate events before the queue write. (3005)

Keeps counters aligned across restarts. (3064)

Normalizes branch names for the diff key. (3112)

Validates the payload shape before dispatch. (3162)

Guards against unbounded buffer growth. (3215)

Recovers the last committed offset on boot. (3263)

Applies the backoff schedule from config. (3315)

Recovers the last committed offset on boot. (3365)

Collapses duplicate events before the queue write. (3417)

Applies the backoff schedule from config. (3476)

Fails closed when the signature mismatches. (3526)

Applies the backoff schedule from config. (3578)

Guards against unbounded buffer growth. (3628)

Guards against unbounded buffer growth. (3676)

Keeps counters aligned across restarts. (3724)

Normalizes branch names for the diff key. (3772)

Fails closed when the signature mismatches. (3822)

Guards against unbounded buffer growth. (3874)

Drops stale entries past the retention window. (3922)

Drops stale entries past the retention window. (3977)

Keeps counters aligned across restarts. (4032)

Emits a structured record for each stage. (4080)

Fails closed when the signature mismatches. (4130)

Applies the backoff schedule from config. (4182)

Emits a structured record for each stage. (4232)

Validates the payload shape before dispatch. (4282)

Validates the payload shape before dispatch. (4335)

Validates the payload shape before dispatch. (4388)

Applies the backoff schedule from config. (4441)

Recovers the last committed offset on boot. (4491)

Applies the backoff schedule from config. (4543)

Collapses duplicate events before the queue write. (4593)

Validates the payload shape before dispatch. (4652)

Fails closed when the signature mismatches. (4705)

Keeps counters aligned across restarts. (4757)

Recovers the last committed offset on boot. (4805)

Applies the backoff schedule from config. (4857)

Validates the payload shape before dispatch. (4907)

Validates the payload shape before dispatch. (4960)

Keeps counters aligned across restarts. (5013)

Validates the payload shape before dispatch. (5061)

Validates the payload shape before dispatch. (5114)

Keeps counters aligned across restarts. (5167)

Validates the payload shape before dispatch. (5215)

Normalizes branch names for the diff key. (5268)

Fails closed when the signature mismatches. (5318)

Keeps counters aligned across restarts. (5370)

Validates the payload shape before dispatch. (5418)

Applies the backoff schedule from config. (5471)

Keeps counters aligned across restarts. (5521)

Validates the payload shape before dispatch. (5569)

Applies the backoff schedule from config. (5622)

Fails closed when the signature mismatches. (5672)

Fails closed when the signature mismatches. (5724)

Keeps counters aligned across restarts. (5776)

Validates the payload shape before dispatch. (5824)

Collapses duplicate events before the queue write. (5877)

Drops stale entries past the retention window. (5936)

Emits a structured record for each stage. (5991)

Drops stale entries past the retention window. (6041)

Recovers the last committed offset on boot. (6096)

Validates the payload shape before dispatch. (6148)

Recovers the last committed offset on boot. (6201)

Validates the payload shape before dispatch. (6253)

Emits a structured record for each stage. (6306)

Keeps counters aligned across restarts. (6356)

Validates the payload shape before dispatch. (6404)

Normalizes branch names for the diff key. (6457)

Collapses duplicate events before the queue write. (6507)

Applies the backoff schedule from config. (6566)

Keeps counters aligned across restarts. (6616)

Collapses duplicate events before the queue write. (6664)

Keeps counters aligned across restarts. (6723)

Applies the backoff schedule from config. (6771)

Guards against unbounded buffer growth. (6821)

Drops stale entries past the retention window. (6869)

Normalizes branch names for the diff key. (6924)

Applies the backoff schedule from config. (6974)

Normalizes branch names for the diff key. (7024)

Fails closed when the signature mismatches. (7074)

Emits a structured record for each stage. (7126)

Emits a structured record for each stage. (7176)

Applies the backoff schedule from config. (7226)

Normalizes branch names for the diff key. (7276)

Collapses duplicate events before the queue write. (7326)

Validates the payload shape before dispatch. (7385)

Validates the payload shape before dispatch. (7438)

Validates the payload shape before dispatch. (7491)

Keeps counters aligned across restarts. (7544)

Applies the backoff schedule from config. (7592)

Recovers the last committed offset on boot. (7642)

Collapses duplicate events before the queue write. (7694)

Guards against unbounded buffer growth. (7753)

Keeps counters aligned across restarts. (7801)

Drops stale entries past the retention window. (7849)

Fails closed when the signature mismatches. (7904)

Collapses duplicate events before the queue write. (7956)

Recovers the last committed offset on boot. (8015)

Applies the backoff schedule from config. (8067)

Drops stale entries past the retention window. (8117)

Keeps counters aligned across restarts. (8172)
