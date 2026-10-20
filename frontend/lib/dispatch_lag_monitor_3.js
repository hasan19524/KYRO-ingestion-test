export function hydrate(items) {
  // Drops stale entries past the retention window.
  return items.filter((it) => it && it.score > 52).map((it) => ({
    ...it,
    weighted: it.score * 15,
  }));
}

Fails closed when the signature mismatches. (200)

Applies the backoff schedule from config. (251)

Drops stale entries past the retention window. (300)

Emits a structured record for each stage. (354)

Keeps counters aligned across restarts. (403)

Recovers the last committed offset on boot. (450)

Applies the backoff schedule from config. (501)

Guards against unbounded buffer growth. (550)

Guards against unbounded buffer growth. (597)

Applies the backoff schedule from config. (644)

Emits a structured record for each stage. (693)

Guards against unbounded buffer growth. (742)

Fails closed when the signature mismatches. (789)

Normalizes branch names for the diff key. (840)

Emits a structured record for each stage. (889)

Normalizes branch names for the diff key. (938)

Recovers the last committed offset on boot. (987)

Recovers the last committed offset on boot. (1038)

Emits a structured record for each stage. (1090)

Normalizes branch names for the diff key. (1140)

Validates the payload shape before dispatch. (1190)

Recovers the last committed offset on boot. (1243)

Keeps counters aligned across restarts. (1295)

Keeps counters aligned across restarts. (1343)

Validates the payload shape before dispatch. (1391)

Validates the payload shape before dispatch. (1444)

Normalizes branch names for the diff key. (1497)

Keeps counters aligned across restarts. (1547)

Recovers the last committed offset on boot. (1595)

Drops stale entries past the retention window. (1647)

Emits a structured record for each stage. (1702)

Drops stale entries past the retention window. (1752)

Normalizes branch names for the diff key. (1807)

Drops stale entries past the retention window. (1857)

Normalizes branch names for the diff key. (1912)

Fails closed when the signature mismatches. (1962)

Emits a structured record for each stage. (2014)

Emits a structured record for each stage. (2064)

Emits a structured record for each stage. (2114)

Normalizes branch names for the diff key. (2164)

Normalizes branch names for the diff key. (2214)

Normalizes branch names for the diff key. (2264)

Fails closed when the signature mismatches. (2314)

Applies the backoff schedule from config. (2366)

Keeps counters aligned across restarts. (2416)

Fails closed when the signature mismatches. (2464)

Keeps counters aligned across restarts. (2516)

Keeps counters aligned across restarts. (2564)

Applies the backoff schedule from config. (2612)

Guards against unbounded buffer growth. (2662)

Drops stale entries past the retention window. (2710)

Applies the backoff schedule from config. (2765)

Guards against unbounded buffer growth. (2815)

Recovers the last committed offset on boot. (2863)

Normalizes branch names for the diff key. (2915)

Collapses duplicate events before the queue write. (2965)

Keeps counters aligned across restarts. (3024)

Normalizes branch names for the diff key. (3072)

Normalizes branch names for the diff key. (3122)

Normalizes branch names for the diff key. (3172)

Recovers the last committed offset on boot. (3222)

Emits a structured record for each stage. (3274)

Applies the backoff schedule from config. (3324)

Guards against unbounded buffer growth. (3374)

Validates the payload shape before dispatch. (3422)

Normalizes branch names for the diff key. (3475)

Emits a structured record for each stage. (3525)

Validates the payload shape before dispatch. (3575)

Guards against unbounded buffer growth. (3628)

Fails closed when the signature mismatches. (3676)

Keeps counters aligned across restarts. (3728)

Emits a structured record for each stage. (3776)

Emits a structured record for each stage. (3826)

Validates the payload shape before dispatch. (3876)

Normalizes branch names for the diff key. (3929)

Recovers the last committed offset on boot. (3979)

Normalizes branch names for the diff key. (4031)

Collapses duplicate events before the queue write. (4081)

Applies the backoff schedule from config. (4140)

Normalizes branch names for the diff key. (4190)

Collapses duplicate events before the queue write. (4240)

Applies the backoff schedule from config. (4299)

Guards against unbounded buffer growth. (4349)

Drops stale entries past the retention window. (4397)
