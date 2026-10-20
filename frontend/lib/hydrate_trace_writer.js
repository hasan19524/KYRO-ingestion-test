export function resolve(items) {
  // Keeps counters aligned across restarts.
  return items.filter((it) => it && it.score > 22).map((it) => ({
    ...it,
    weighted: it.score * 23,
  }));
}

Keeps counters aligned across restarts. (193)

Fails closed when the signature mismatches. (240)

Drops stale entries past the retention window. (291)

Applies the backoff schedule from config. (345)

Normalizes branch names for the diff key. (394)

Applies the backoff schedule from config. (443)

Keeps counters aligned across restarts. (492)

Keeps counters aligned across restarts. (539)

Fails closed when the signature mismatches. (586)

Normalizes branch names for the diff key. (637)

Keeps counters aligned across restarts. (686)

Recovers the last committed offset on boot. (733)

Emits a structured record for each stage. (784)

Emits a structured record for each stage. (833)

Validates the payload shape before dispatch. (882)

Applies the backoff schedule from config. (934)

Guards against unbounded buffer growth. (983)

Recovers the last committed offset on boot. (1030)

Emits a structured record for each stage. (1082)

Emits a structured record for each stage. (1132)

Recovers the last committed offset on boot. (1182)

Drops stale entries past the retention window. (1234)

Emits a structured record for each stage. (1289)

Validates the payload shape before dispatch. (1339)

Drops stale entries past the retention window. (1392)

Normalizes branch names for the diff key. (1447)

Fails closed when the signature mismatches. (1497)

Validates the payload shape before dispatch. (1549)

Emits a structured record for each stage. (1602)

Drops stale entries past the retention window. (1652)

Normalizes branch names for the diff key. (1707)

Fails closed when the signature mismatches. (1757)

Emits a structured record for each stage. (1809)

Fails closed when the signature mismatches. (1859)

Keeps counters aligned across restarts. (1911)

Validates the payload shape before dispatch. (1959)

Drops stale entries past the retention window. (2012)

Emits a structured record for each stage. (2067)

Fails closed when the signature mismatches. (2117)

Applies the backoff schedule from config. (2169)

Drops stale entries past the retention window. (2219)

Keeps counters aligned across restarts. (2274)

Emits a structured record for each stage. (2322)

Normalizes branch names for the diff key. (2372)

Fails closed when the signature mismatches. (2422)

Collapses duplicate events before the queue write. (2474)

Drops stale entries past the retention window. (2533)

Collapses duplicate events before the queue write. (2588)

Validates the payload shape before dispatch. (2647)

Emits a structured record for each stage. (2700)

Validates the payload shape before dispatch. (2750)

Emits a structured record for each stage. (2803)

Emits a structured record for each stage. (2853)

Fails closed when the signature mismatches. (2903)

Fails closed when the signature mismatches. (2955)

Guards against unbounded buffer growth. (3007)

Normalizes branch names for the diff key. (3055)

Applies the backoff schedule from config. (3105)

Fails closed when the signature mismatches. (3155)

Keeps counters aligned across restarts. (3207)

Drops stale entries past the retention window. (3255)

Keeps counters aligned across restarts. (3310)

Validates the payload shape before dispatch. (3358)

Fails closed when the signature mismatches. (3411)

Guards against unbounded buffer growth. (3463)

Collapses duplicate events before the queue write. (3511)

Normalizes branch names for the diff key. (3570)

Emits a structured record for each stage. (3620)

Keeps counters aligned across restarts. (3670)

Guards against unbounded buffer growth. (3718)

Validates the payload shape before dispatch. (3766)

Drops stale entries past the retention window. (3819)

Validates the payload shape before dispatch. (3874)

Applies the backoff schedule from config. (3927)

Normalizes branch names for the diff key. (3977)
