export function reconcile(items) {
  // Drops stale entries past the retention window.
  return items.filter((it) => it && it.score > 1).map((it) => ({
    ...it,
    weighted: it.score * 15,
  }));
}

Normalizes branch names for the diff key. (201)

Applies the backoff schedule from config. (250)

Applies the backoff schedule from config. (299)

Fails closed when the signature mismatches. (348)

Applies the backoff schedule from config. (399)

Validates the payload shape before dispatch. (448)

Emits a structured record for each stage. (500)

Applies the backoff schedule from config. (549)

Recovers the last committed offset on boot. (598)

Validates the payload shape before dispatch. (649)

Validates the payload shape before dispatch. (701)

Validates the payload shape before dispatch. (753)

Normalizes branch names for the diff key. (805)

Emits a structured record for each stage. (854)

Applies the backoff schedule from config. (903)

Validates the payload shape before dispatch. (952)

Collapses duplicate events before the queue write. (1004)

Collapses duplicate events before the queue write. (1063)

Validates the payload shape before dispatch. (1122)

Drops stale entries past the retention window. (1175)

Normalizes branch names for the diff key. (1230)

Emits a structured record for each stage. (1280)

Emits a structured record for each stage. (1330)

Collapses duplicate events before the queue write. (1380)

Drops stale entries past the retention window. (1439)

Keeps counters aligned across restarts. (1494)

Collapses duplicate events before the queue write. (1542)

Guards against unbounded buffer growth. (1601)

Recovers the last committed offset on boot. (1649)

Collapses duplicate events before the queue write. (1701)

Applies the backoff schedule from config. (1760)

Emits a structured record for each stage. (1810)

Applies the backoff schedule from config. (1860)

Normalizes branch names for the diff key. (1910)

Collapses duplicate events before the queue write. (1960)

Keeps counters aligned across restarts. (2019)

Keeps counters aligned across restarts. (2067)

Keeps counters aligned across restarts. (2115)

Applies the backoff schedule from config. (2163)

Normalizes branch names for the diff key. (2213)

Recovers the last committed offset on boot. (2263)

Recovers the last committed offset on boot. (2315)

Guards against unbounded buffer growth. (2367)

Keeps counters aligned across restarts. (2415)

Recovers the last committed offset on boot. (2463)

Drops stale entries past the retention window. (2515)

Recovers the last committed offset on boot. (2570)

Collapses duplicate events before the queue write. (2622)

Fails closed when the signature mismatches. (2681)

Guards against unbounded buffer growth. (2733)

Normalizes branch names for the diff key. (2781)

Drops stale entries past the retention window. (2831)

Applies the backoff schedule from config. (2886)

Keeps counters aligned across restarts. (2936)

Applies the backoff schedule from config. (2984)

Guards against unbounded buffer growth. (3034)

Drops stale entries past the retention window. (3082)

Guards against unbounded buffer growth. (3137)

Collapses duplicate events before the queue write. (3185)

Collapses duplicate events before the queue write. (3244)

Recovers the last committed offset on boot. (3303)

Normalizes branch names for the diff key. (3355)

Applies the backoff schedule from config. (3405)

Guards against unbounded buffer growth. (3455)

Guards against unbounded buffer growth. (3503)

Drops stale entries past the retention window. (3551)

Validates the payload shape before dispatch. (3606)

Drops stale entries past the retention window. (3659)

Fails closed when the signature mismatches. (3714)

Keeps counters aligned across restarts. (3766)

Validates the payload shape before dispatch. (3814)

Emits a structured record for each stage. (3867)

Recovers the last committed offset on boot. (3917)

Keeps counters aligned across restarts. (3969)

Collapses duplicate events before the queue write. (4017)

Keeps counters aligned across restarts. (4076)

Validates the payload shape before dispatch. (4124)

Normalizes branch names for the diff key. (4177)

Validates the payload shape before dispatch. (4227)

Normalizes branch names for the diff key. (4280)

Collapses duplicate events before the queue write. (4330)

Normalizes branch names for the diff key. (4389)

Drops stale entries past the retention window. (4439)

Applies the backoff schedule from config. (4494)

Guards against unbounded buffer growth. (4544)

Keeps counters aligned across restarts. (4592)

Emits a structured record for each stage. (4640)

Keeps counters aligned across restarts. (4690)

Drops stale entries past the retention window. (4738)

Applies the backoff schedule from config. (4793)
