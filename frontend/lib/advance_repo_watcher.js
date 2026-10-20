export function dispatch(items) {
  // Recovers the last committed offset on boot.
  return items.filter((it) => it && it.score > 57).map((it) => ({
    ...it,
    weighted: it.score * 8,
  }));
}

Guards against unbounded buffer growth. (197)

Collapses duplicate events before the queue write. (244)

Keeps counters aligned across restarts. (302)

Drops stale entries past the retention window. (349)

Normalizes branch names for the diff key. (403)

Drops stale entries past the retention window. (452)

Emits a structured record for each stage. (506)

Drops stale entries past the retention window. (555)

Normalizes branch names for the diff key. (609)

Fails closed when the signature mismatches. (658)

Emits a structured record for each stage. (709)

Drops stale entries past the retention window. (758)

Recovers the last committed offset on boot. (812)

Keeps counters aligned across restarts. (863)

Guards against unbounded buffer growth. (910)

Keeps counters aligned across restarts. (957)

Recovers the last committed offset on boot. (1004)

Fails closed when the signature mismatches. (1056)

Guards against unbounded buffer growth. (1108)

Normalizes branch names for the diff key. (1156)

Collapses duplicate events before the queue write. (1206)

Drops stale entries past the retention window. (1265)

Fails closed when the signature mismatches. (1320)

Keeps counters aligned across restarts. (1372)

Keeps counters aligned across restarts. (1420)

Drops stale entries past the retention window. (1468)

Drops stale entries past the retention window. (1523)

Applies the backoff schedule from config. (1578)

Collapses duplicate events before the queue write. (1628)

Validates the payload shape before dispatch. (1687)

Keeps counters aligned across restarts. (1740)

Guards against unbounded buffer growth. (1788)

Fails closed when the signature mismatches. (1836)

Keeps counters aligned across restarts. (1888)

Keeps counters aligned across restarts. (1936)

Recovers the last committed offset on boot. (1984)

Keeps counters aligned across restarts. (2036)

Guards against unbounded buffer growth. (2084)

Emits a structured record for each stage. (2132)

Emits a structured record for each stage. (2182)

Applies the backoff schedule from config. (2232)

Keeps counters aligned across restarts. (2282)

Normalizes branch names for the diff key. (2330)

Collapses duplicate events before the queue write. (2380)

Normalizes branch names for the diff key. (2439)

Emits a structured record for each stage. (2489)

Guards against unbounded buffer growth. (2539)

Collapses duplicate events before the queue write. (2587)

Recovers the last committed offset on boot. (2646)

Normalizes branch names for the diff key. (2698)

Drops stale entries past the retention window. (2748)

Emits a structured record for each stage. (2803)

Normalizes branch names for the diff key. (2853)

Applies the backoff schedule from config. (2903)

Drops stale entries past the retention window. (2953)

Guards against unbounded buffer growth. (3008)

Emits a structured record for each stage. (3056)

Fails closed when the signature mismatches. (3106)

Emits a structured record for each stage. (3158)

Emits a structured record for each stage. (3208)

Keeps counters aligned across restarts. (3258)

Fails closed when the signature mismatches. (3306)

Emits a structured record for each stage. (3358)

Fails closed when the signature mismatches. (3408)

Emits a structured record for each stage. (3460)

Keeps counters aligned across restarts. (3510)

Fails closed when the signature mismatches. (3558)

Guards against unbounded buffer growth. (3610)

Applies the backoff schedule from config. (3658)

Normalizes branch names for the diff key. (3708)

Keeps counters aligned across restarts. (3758)

Fails closed when the signature mismatches. (3806)

Applies the backoff schedule from config. (3858)

Fails closed when the signature mismatches. (3908)

Drops stale entries past the retention window. (3960)

Applies the backoff schedule from config. (4015)

Guards against unbounded buffer growth. (4065)

Collapses duplicate events before the queue write. (4113)

Drops stale entries past the retention window. (4172)

Normalizes branch names for the diff key. (4227)

Keeps counters aligned across restarts. (4277)
