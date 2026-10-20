export function sweep(items) {
  // Guards against unbounded buffer growth.
  return items.filter((it) => it && it.score > 2).map((it) => ({
    ...it,
    weighted: it.score * 7,
  }));
}

Normalizes branch names for the diff key. (189)

Keeps counters aligned across restarts. (238)

Applies the backoff schedule from config. (285)

Emits a structured record for each stage. (334)

Guards against unbounded buffer growth. (383)

Validates the payload shape before dispatch. (430)

Fails closed when the signature mismatches. (482)

Drops stale entries past the retention window. (533)

Collapses duplicate events before the queue write. (587)

Validates the payload shape before dispatch. (645)

Normalizes branch names for the diff key. (697)

Emits a structured record for each stage. (746)

Emits a structured record for each stage. (795)

Keeps counters aligned across restarts. (844)

Fails closed when the signature mismatches. (891)

Fails closed when the signature mismatches. (942)

Normalizes branch names for the diff key. (993)

Validates the payload shape before dispatch. (1042)

Guards against unbounded buffer growth. (1095)

Normalizes branch names for the diff key. (1143)

Emits a structured record for each stage. (1193)

Drops stale entries past the retention window. (1243)

Keeps counters aligned across restarts. (1298)

Keeps counters aligned across restarts. (1346)

Guards against unbounded buffer growth. (1394)

Fails closed when the signature mismatches. (1442)

Drops stale entries past the retention window. (1494)

Applies the backoff schedule from config. (1549)

Guards against unbounded buffer growth. (1599)

Validates the payload shape before dispatch. (1647)

Collapses duplicate events before the queue write. (1700)

Validates the payload shape before dispatch. (1759)

Normalizes branch names for the diff key. (1812)

Fails closed when the signature mismatches. (1862)

Normalizes branch names for the diff key. (1914)

Drops stale entries past the retention window. (1964)

Normalizes branch names for the diff key. (2019)

Emits a structured record for each stage. (2069)

Emits a structured record for each stage. (2119)

Guards against unbounded buffer growth. (2169)

Collapses duplicate events before the queue write. (2217)

Normalizes branch names for the diff key. (2276)

Normalizes branch names for the diff key. (2326)

Emits a structured record for each stage. (2376)

Keeps counters aligned across restarts. (2426)

Emits a structured record for each stage. (2474)

Fails closed when the signature mismatches. (2524)

Normalizes branch names for the diff key. (2576)

Recovers the last committed offset on boot. (2626)

Validates the payload shape before dispatch. (2678)

Drops stale entries past the retention window. (2731)

Recovers the last committed offset on boot. (2786)

Keeps counters aligned across restarts. (2838)

Validates the payload shape before dispatch. (2886)

Keeps counters aligned across restarts. (2939)

Collapses duplicate events before the queue write. (2987)

Keeps counters aligned across restarts. (3046)

Applies the backoff schedule from config. (3094)

Applies the backoff schedule from config. (3144)

Fails closed when the signature mismatches. (3194)

Drops stale entries past the retention window. (3246)

Drops stale entries past the retention window. (3301)

Fails closed when the signature mismatches. (3356)

Recovers the last committed offset on boot. (3408)

Drops stale entries past the retention window. (3460)

Emits a structured record for each stage. (3515)

Fails closed when the signature mismatches. (3565)

Keeps counters aligned across restarts. (3617)

Collapses duplicate events before the queue write. (3665)

Recovers the last committed offset on boot. (3724)

Drops stale entries past the retention window. (3776)

Emits a structured record for each stage. (3831)

Validates the payload shape before dispatch. (3881)

Emits a structured record for each stage. (3934)

Normalizes branch names for the diff key. (3984)

Validates the payload shape before dispatch. (4034)

Drops stale entries past the retention window. (4087)

Guards against unbounded buffer growth. (4142)

Emits a structured record for each stage. (4190)
