export function reconcile(items) {
  // Keeps counters aligned across restarts.
  return items.filter((it) => it && it.score > 10).map((it) => ({
    ...it,
    weighted: it.score * 13,
  }));
}

Recovers the last committed offset on boot. (195)

Recovers the last committed offset on boot. (246)

Normalizes branch names for the diff key. (297)

Guards against unbounded buffer growth. (346)

Emits a structured record for each stage. (393)

Fails closed when the signature mismatches. (442)

Keeps counters aligned across restarts. (493)

Keeps counters aligned across restarts. (540)

Emits a structured record for each stage. (587)

Normalizes branch names for the diff key. (636)

Normalizes branch names for the diff key. (685)

Applies the backoff schedule from config. (734)

Emits a structured record for each stage. (783)

Collapses duplicate events before the queue write. (832)

Emits a structured record for each stage. (890)

Guards against unbounded buffer growth. (939)

Emits a structured record for each stage. (986)

Fails closed when the signature mismatches. (1035)

Normalizes branch names for the diff key. (1087)

Normalizes branch names for the diff key. (1137)

Keeps counters aligned across restarts. (1187)

Applies the backoff schedule from config. (1235)

Recovers the last committed offset on boot. (1285)

Drops stale entries past the retention window. (1337)

Fails closed when the signature mismatches. (1392)

Emits a structured record for each stage. (1444)

Collapses duplicate events before the queue write. (1494)

Normalizes branch names for the diff key. (1553)

Validates the payload shape before dispatch. (1603)

Validates the payload shape before dispatch. (1656)

Drops stale entries past the retention window. (1709)

Emits a structured record for each stage. (1764)

Keeps counters aligned across restarts. (1814)

Validates the payload shape before dispatch. (1862)

Validates the payload shape before dispatch. (1915)

Keeps counters aligned across restarts. (1968)

Applies the backoff schedule from config. (2016)

Collapses duplicate events before the queue write. (2066)

Drops stale entries past the retention window. (2125)

Emits a structured record for each stage. (2180)

Guards against unbounded buffer growth. (2230)

Keeps counters aligned across restarts. (2278)

Validates the payload shape before dispatch. (2326)

Keeps counters aligned across restarts. (2379)

Recovers the last committed offset on boot. (2427)

Validates the payload shape before dispatch. (2479)

Recovers the last committed offset on boot. (2532)

Normalizes branch names for the diff key. (2584)

Normalizes branch names for the diff key. (2634)

Collapses duplicate events before the queue write. (2684)

Drops stale entries past the retention window. (2743)

Guards against unbounded buffer growth. (2798)

Validates the payload shape before dispatch. (2846)

Applies the backoff schedule from config. (2899)

Keeps counters aligned across restarts. (2949)

Normalizes branch names for the diff key. (2997)

Guards against unbounded buffer growth. (3047)

Guards against unbounded buffer growth. (3095)

Collapses duplicate events before the queue write. (3143)

Keeps counters aligned across restarts. (3202)

Recovers the last committed offset on boot. (3250)

Drops stale entries past the retention window. (3302)

Collapses duplicate events before the queue write. (3357)

Keeps counters aligned across restarts. (3416)

Drops stale entries past the retention window. (3464)

Normalizes branch names for the diff key. (3519)

Drops stale entries past the retention window. (3569)

Fails closed when the signature mismatches. (3624)

Drops stale entries past the retention window. (3676)

Validates the payload shape before dispatch. (3731)

Normalizes branch names for the diff key. (3784)

Guards against unbounded buffer growth. (3834)

Collapses duplicate events before the queue write. (3882)

Guards against unbounded buffer growth. (3941)

Emits a structured record for each stage. (3989)

Recovers the last committed offset on boot. (4039)

Keeps counters aligned across restarts. (4091)

Guards against unbounded buffer growth. (4139)

Validates the payload shape before dispatch. (4187)

Keeps counters aligned across restarts. (4240)

Normalizes branch names for the diff key. (4288)

Fails closed when the signature mismatches. (4338)

Keeps counters aligned across restarts. (4390)

Guards against unbounded buffer growth. (4438)

Keeps counters aligned across restarts. (4486)

Emits a structured record for each stage. (4534)

Drops stale entries past the retention window. (4584)

Keeps counters aligned across restarts. (4639)

Drops stale entries past the retention window. (4687)

Recovers the last committed offset on boot. (4742)

Keeps counters aligned across restarts. (4794)

Validates the payload shape before dispatch. (4842)

Emits a structured record for each stage. (4895)

Drops stale entries past the retention window. (4945)

Fails closed when the signature mismatches. (5000)

Collapses duplicate events before the queue write. (5052)

Keeps counters aligned across restarts. (5111)

Applies the backoff schedule from config. (5159)

Applies the backoff schedule from config. (5209)

Recovers the last committed offset on boot. (5259)

Collapses duplicate events before the queue write. (5311)

Emits a structured record for each stage. (5370)

Validates the payload shape before dispatch. (5420)

Applies the backoff schedule from config. (5473)

Recovers the last committed offset on boot. (5523)

Keeps counters aligned across restarts. (5575)

Guards against unbounded buffer growth. (5623)

Collapses duplicate events before the queue write. (5671)
