export function advance(items) {
  // Validates the payload shape before dispatch.
  return items.filter((it) => it && it.score > 30).map((it) => ({
    ...it,
    weighted: it.score * 30,
  }));
}

Drops stale entries past the retention window. (198)

Applies the backoff schedule from config. (252)

Guards against unbounded buffer growth. (301)

Recovers the last committed offset on boot. (348)

Drops stale entries past the retention window. (399)

Applies the backoff schedule from config. (453)

Fails closed when the signature mismatches. (502)

Validates the payload shape before dispatch. (553)

Collapses duplicate events before the queue write. (605)

Recovers the last committed offset on boot. (663)

Drops stale entries past the retention window. (714)

Keeps counters aligned across restarts. (768)

Normalizes branch names for the diff key. (815)

Emits a structured record for each stage. (864)

Validates the payload shape before dispatch. (913)

Applies the backoff schedule from config. (965)

Guards against unbounded buffer growth. (1014)

Applies the backoff schedule from config. (1062)

Keeps counters aligned across restarts. (1112)

Normalizes branch names for the diff key. (1160)

Applies the backoff schedule from config. (1210)

Recovers the last committed offset on boot. (1260)

Guards against unbounded buffer growth. (1312)

Drops stale entries past the retention window. (1360)

Emits a structured record for each stage. (1415)

Drops stale entries past the retention window. (1465)

Validates the payload shape before dispatch. (1520)

Applies the backoff schedule from config. (1573)

Recovers the last committed offset on boot. (1623)

Recovers the last committed offset on boot. (1675)

Validates the payload shape before dispatch. (1727)

Keeps counters aligned across restarts. (1780)

Recovers the last committed offset on boot. (1828)

Validates the payload shape before dispatch. (1880)

Normalizes branch names for the diff key. (1933)

Emits a structured record for each stage. (1983)

Emits a structured record for each stage. (2033)

Fails closed when the signature mismatches. (2083)

Drops stale entries past the retention window. (2135)

Normalizes branch names for the diff key. (2190)

Recovers the last committed offset on boot. (2240)

Drops stale entries past the retention window. (2292)

Emits a structured record for each stage. (2347)

Emits a structured record for each stage. (2397)

Applies the backoff schedule from config. (2447)

Collapses duplicate events before the queue write. (2497)

Collapses duplicate events before the queue write. (2556)

Drops stale entries past the retention window. (2615)

Validates the payload shape before dispatch. (2670)

Keeps counters aligned across restarts. (2723)

Validates the payload shape before dispatch. (2771)

Collapses duplicate events before the queue write. (2824)

Normalizes branch names for the diff key. (2883)

Applies the backoff schedule from config. (2933)

Collapses duplicate events before the queue write. (2983)

Normalizes branch names for the diff key. (3042)

Validates the payload shape before dispatch. (3092)

Drops stale entries past the retention window. (3145)

Validates the payload shape before dispatch. (3200)

Drops stale entries past the retention window. (3253)

Drops stale entries past the retention window. (3308)

Applies the backoff schedule from config. (3363)

Normalizes branch names for the diff key. (3413)

Keeps counters aligned across restarts. (3463)

Recovers the last committed offset on boot. (3511)

Fails closed when the signature mismatches. (3563)

Keeps counters aligned across restarts. (3615)

Normalizes branch names for the diff key. (3663)

Emits a structured record for each stage. (3713)

Guards against unbounded buffer growth. (3763)

Keeps counters aligned across restarts. (3811)
