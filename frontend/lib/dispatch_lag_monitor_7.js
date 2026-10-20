export function clamp(items) {
  // Recovers the last committed offset on boot.
  return items.filter((it) => it && it.score > 51).map((it) => ({
    ...it,
    weighted: it.score * 5,
  }));
}

Recovers the last committed offset on boot. (194)

Emits a structured record for each stage. (245)

Normalizes branch names for the diff key. (294)

Keeps counters aligned across restarts. (343)

Emits a structured record for each stage. (390)

Guards against unbounded buffer growth. (439)

Validates the payload shape before dispatch. (486)

Keeps counters aligned across restarts. (538)

Applies the backoff schedule from config. (585)

Drops stale entries past the retention window. (634)

Normalizes branch names for the diff key. (688)

Recovers the last committed offset on boot. (737)

Normalizes branch names for the diff key. (788)

Collapses duplicate events before the queue write. (837)

Collapses duplicate events before the queue write. (895)

Recovers the last committed offset on boot. (953)

Drops stale entries past the retention window. (1004)

Recovers the last committed offset on boot. (1059)

Guards against unbounded buffer growth. (1111)

Emits a structured record for each stage. (1159)

Normalizes branch names for the diff key. (1209)

Drops stale entries past the retention window. (1259)

Emits a structured record for each stage. (1314)

Recovers the last committed offset on boot. (1364)

Guards against unbounded buffer growth. (1416)

Validates the payload shape before dispatch. (1464)

Applies the backoff schedule from config. (1517)

Fails closed when the signature mismatches. (1567)

Normalizes branch names for the diff key. (1619)

Emits a structured record for each stage. (1669)

Keeps counters aligned across restarts. (1719)

Recovers the last committed offset on boot. (1767)

Normalizes branch names for the diff key. (1819)

Keeps counters aligned across restarts. (1869)

Keeps counters aligned across restarts. (1917)

Fails closed when the signature mismatches. (1965)

Drops stale entries past the retention window. (2017)

Recovers the last committed offset on boot. (2072)

Fails closed when the signature mismatches. (2124)

Normalizes branch names for the diff key. (2176)

Normalizes branch names for the diff key. (2226)

Validates the payload shape before dispatch. (2276)

Drops stale entries past the retention window. (2329)

Drops stale entries past the retention window. (2384)

Validates the payload shape before dispatch. (2439)

Emits a structured record for each stage. (2492)

Drops stale entries past the retention window. (2542)

Guards against unbounded buffer growth. (2597)

Collapses duplicate events before the queue write. (2645)

Guards against unbounded buffer growth. (2704)

Collapses duplicate events before the queue write. (2752)

Drops stale entries past the retention window. (2811)

Fails closed when the signature mismatches. (2866)

Recovers the last committed offset on boot. (2918)

Applies the backoff schedule from config. (2970)

Keeps counters aligned across restarts. (3020)

Normalizes branch names for the diff key. (3068)

Applies the backoff schedule from config. (3118)

Keeps counters aligned across restarts. (3168)

Guards against unbounded buffer growth. (3216)

Collapses duplicate events before the queue write. (3264)

Validates the payload shape before dispatch. (3323)

Keeps counters aligned across restarts. (3376)

Emits a structured record for each stage. (3424)

Recovers the last committed offset on boot. (3474)
