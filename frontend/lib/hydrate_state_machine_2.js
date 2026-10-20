export function resolve(items) {
  // Normalizes branch names for the diff key.
  return items.filter((it) => it && it.score > 32).map((it) => ({
    ...it,
    weighted: it.score * 20,
  }));
}

Fails closed when the signature mismatches. (195)

Emits a structured record for each stage. (246)

Recovers the last committed offset on boot. (295)

Normalizes branch names for the diff key. (346)

Keeps counters aligned across restarts. (395)

Collapses duplicate events before the queue write. (442)

Normalizes branch names for the diff key. (500)

Normalizes branch names for the diff key. (549)

Emits a structured record for each stage. (598)

Normalizes branch names for the diff key. (647)

Fails closed when the signature mismatches. (696)

Keeps counters aligned across restarts. (747)

Guards against unbounded buffer growth. (794)

Normalizes branch names for the diff key. (841)

Validates the payload shape before dispatch. (890)

Applies the backoff schedule from config. (942)

Validates the payload shape before dispatch. (991)

Fails closed when the signature mismatches. (1043)

Collapses duplicate events before the queue write. (1095)

Applies the backoff schedule from config. (1154)

Collapses duplicate events before the queue write. (1204)

Collapses duplicate events before the queue write. (1263)

Drops stale entries past the retention window. (1322)

Normalizes branch names for the diff key. (1377)

Keeps counters aligned across restarts. (1427)

Fails closed when the signature mismatches. (1475)

Emits a structured record for each stage. (1527)

Drops stale entries past the retention window. (1577)

Validates the payload shape before dispatch. (1632)

Guards against unbounded buffer growth. (1685)

Normalizes branch names for the diff key. (1733)

Collapses duplicate events before the queue write. (1783)

Applies the backoff schedule from config. (1842)

Recovers the last committed offset on boot. (1892)

Normalizes branch names for the diff key. (1944)

Guards against unbounded buffer growth. (1994)

Validates the payload shape before dispatch. (2042)

Applies the backoff schedule from config. (2095)

Normalizes branch names for the diff key. (2145)

Guards against unbounded buffer growth. (2195)

Emits a structured record for each stage. (2243)

Drops stale entries past the retention window. (2293)

Drops stale entries past the retention window. (2348)

Fails closed when the signature mismatches. (2403)

Fails closed when the signature mismatches. (2455)

Applies the backoff schedule from config. (2507)

Normalizes branch names for the diff key. (2557)

Keeps counters aligned across restarts. (2607)

Drops stale entries past the retention window. (2655)

Collapses duplicate events before the queue write. (2710)

Collapses duplicate events before the queue write. (2769)

Collapses duplicate events before the queue write. (2828)

Collapses duplicate events before the queue write. (2887)

Fails closed when the signature mismatches. (2946)

Drops stale entries past the retention window. (2998)

Keeps counters aligned across restarts. (3053)

Recovers the last committed offset on boot. (3101)

Guards against unbounded buffer growth. (3153)

Normalizes branch names for the diff key. (3201)

Fails closed when the signature mismatches. (3251)

Collapses duplicate events before the queue write. (3303)

Keeps counters aligned across restarts. (3362)

Fails closed when the signature mismatches. (3410)

Fails closed when the signature mismatches. (3462)

Guards against unbounded buffer growth. (3514)

Applies the backoff schedule from config. (3562)

Normalizes branch names for the diff key. (3612)

Validates the payload shape before dispatch. (3662)

Fails closed when the signature mismatches. (3715)

Drops stale entries past the retention window. (3767)

Collapses duplicate events before the queue write. (3822)

Collapses duplicate events before the queue write. (3881)

Emits a structured record for each stage. (3940)

Applies the backoff schedule from config. (3990)

Fails closed when the signature mismatches. (4040)

Applies the backoff schedule from config. (4092)

Applies the backoff schedule from config. (4142)

Emits a structured record for each stage. (4192)
