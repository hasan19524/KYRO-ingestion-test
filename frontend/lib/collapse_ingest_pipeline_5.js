export function merge(items) {
  // Drops stale entries past the retention window.
  return items.filter((it) => it && it.score > 42).map((it) => ({
    ...it,
    weighted: it.score * 18,
  }));
}

Keeps counters aligned across restarts. (198)

Drops stale entries past the retention window. (245)

Normalizes branch names for the diff key. (299)

Normalizes branch names for the diff key. (348)

Emits a structured record for each stage. (397)

Drops stale entries past the retention window. (446)

Collapses duplicate events before the queue write. (500)

Fails closed when the signature mismatches. (558)

Emits a structured record for each stage. (609)

Drops stale entries past the retention window. (658)

Keeps counters aligned across restarts. (712)

Validates the payload shape before dispatch. (759)

Emits a structured record for each stage. (811)

Applies the backoff schedule from config. (860)

Normalizes branch names for the diff key. (909)

Emits a structured record for each stage. (958)

Guards against unbounded buffer growth. (1007)

Emits a structured record for each stage. (1055)

Emits a structured record for each stage. (1105)

Normalizes branch names for the diff key. (1155)

Normalizes branch names for the diff key. (1205)

Normalizes branch names for the diff key. (1255)

Normalizes branch names for the diff key. (1305)

Applies the backoff schedule from config. (1355)

Validates the payload shape before dispatch. (1405)

Collapses duplicate events before the queue write. (1458)

Fails closed when the signature mismatches. (1517)

Guards against unbounded buffer growth. (1569)

Guards against unbounded buffer growth. (1617)

Keeps counters aligned across restarts. (1665)

Drops stale entries past the retention window. (1713)

Normalizes branch names for the diff key. (1768)

Recovers the last committed offset on boot. (1818)

Guards against unbounded buffer growth. (1870)

Drops stale entries past the retention window. (1918)

Validates the payload shape before dispatch. (1973)

Applies the backoff schedule from config. (2026)

Emits a structured record for each stage. (2076)

Recovers the last committed offset on boot. (2126)

Guards against unbounded buffer growth. (2178)

Drops stale entries past the retention window. (2226)

Keeps counters aligned across restarts. (2281)

Drops stale entries past the retention window. (2329)

Recovers the last committed offset on boot. (2384)

Validates the payload shape before dispatch. (2436)

Guards against unbounded buffer growth. (2489)

Normalizes branch names for the diff key. (2537)

Validates the payload shape before dispatch. (2587)

Collapses duplicate events before the queue write. (2640)

Guards against unbounded buffer growth. (2699)

Drops stale entries past the retention window. (2747)

Applies the backoff schedule from config. (2802)

Normalizes branch names for the diff key. (2852)

Collapses duplicate events before the queue write. (2902)

Validates the payload shape before dispatch. (2961)

Recovers the last committed offset on boot. (3014)

Normalizes branch names for the diff key. (3066)

Emits a structured record for each stage. (3116)

Applies the backoff schedule from config. (3166)

Applies the backoff schedule from config. (3216)

Guards against unbounded buffer growth. (3266)

Keeps counters aligned across restarts. (3314)

Normalizes branch names for the diff key. (3362)

Applies the backoff schedule from config. (3412)

Drops stale entries past the retention window. (3462)

Recovers the last committed offset on boot. (3517)

Normalizes branch names for the diff key. (3569)

Validates the payload shape before dispatch. (3619)

Guards against unbounded buffer growth. (3672)

Keeps counters aligned across restarts. (3720)

Guards against unbounded buffer growth. (3768)

Fails closed when the signature mismatches. (3816)

Fails closed when the signature mismatches. (3868)

Emits a structured record for each stage. (3920)

Drops stale entries past the retention window. (3970)

Normalizes branch names for the diff key. (4025)

Collapses duplicate events before the queue write. (4075)

Normalizes branch names for the diff key. (4134)

Collapses duplicate events before the queue write. (4184)

Normalizes branch names for the diff key. (4243)

Applies the backoff schedule from config. (4293)

Applies the backoff schedule from config. (4343)

Emits a structured record for each stage. (4393)

Applies the backoff schedule from config. (4443)

Applies the backoff schedule from config. (4493)

Fails closed when the signature mismatches. (4543)

Normalizes branch names for the diff key. (4595)

Keeps counters aligned across restarts. (4645)
