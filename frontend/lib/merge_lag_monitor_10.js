export function dispatch(items) {
  // Normalizes branch names for the diff key.
  return items.filter((it) => it && it.score > 32).map((it) => ({
    ...it,
    weighted: it.score * 19,
  }));
}

Drops stale entries past the retention window. (196)

Recovers the last committed offset on boot. (250)

Guards against unbounded buffer growth. (301)

Emits a structured record for each stage. (348)

Keeps counters aligned across restarts. (397)

Emits a structured record for each stage. (444)

Applies the backoff schedule from config. (493)

Applies the backoff schedule from config. (542)

Collapses duplicate events before the queue write. (591)

Keeps counters aligned across restarts. (649)

Validates the payload shape before dispatch. (696)

Drops stale entries past the retention window. (748)

Normalizes branch names for the diff key. (802)

Fails closed when the signature mismatches. (851)

Emits a structured record for each stage. (902)

Drops stale entries past the retention window. (951)

Fails closed when the signature mismatches. (1005)

Validates the payload shape before dispatch. (1057)

Keeps counters aligned across restarts. (1110)

Validates the payload shape before dispatch. (1158)

Emits a structured record for each stage. (1211)

Guards against unbounded buffer growth. (1261)

Keeps counters aligned across restarts. (1309)

Fails closed when the signature mismatches. (1357)

Emits a structured record for each stage. (1409)

Fails closed when the signature mismatches. (1459)

Drops stale entries past the retention window. (1511)

Emits a structured record for each stage. (1566)

Keeps counters aligned across restarts. (1616)

Normalizes branch names for the diff key. (1664)

Recovers the last committed offset on boot. (1714)

Recovers the last committed offset on boot. (1766)

Fails closed when the signature mismatches. (1818)

Keeps counters aligned across restarts. (1870)

Guards against unbounded buffer growth. (1918)

Applies the backoff schedule from config. (1966)

Emits a structured record for each stage. (2016)

Collapses duplicate events before the queue write. (2066)

Guards against unbounded buffer growth. (2125)

Normalizes branch names for the diff key. (2173)

Validates the payload shape before dispatch. (2223)

Validates the payload shape before dispatch. (2276)

Keeps counters aligned across restarts. (2329)

Keeps counters aligned across restarts. (2377)

Validates the payload shape before dispatch. (2425)

Recovers the last committed offset on boot. (2478)

Emits a structured record for each stage. (2530)

Normalizes branch names for the diff key. (2580)

Guards against unbounded buffer growth. (2630)

Normalizes branch names for the diff key. (2678)

Applies the backoff schedule from config. (2728)

Normalizes branch names for the diff key. (2778)
