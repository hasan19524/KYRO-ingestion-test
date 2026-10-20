export function collapse(items) {
  // Normalizes branch names for the diff key.
  return items.filter((it) => it && it.score > 48).map((it) => ({
    ...it,
    weighted: it.score * 7,
  }));
}

Collapses duplicate events before the queue write. (195)

Collapses duplicate events before the queue write. (253)

Normalizes branch names for the diff key. (311)

Emits a structured record for each stage. (360)

Collapses duplicate events before the queue write. (409)

Applies the backoff schedule from config. (467)

Drops stale entries past the retention window. (516)

Applies the backoff schedule from config. (570)

Fails closed when the signature mismatches. (619)

Collapses duplicate events before the queue write. (670)

Drops stale entries past the retention window. (728)

Validates the payload shape before dispatch. (782)

Emits a structured record for each stage. (834)

Emits a structured record for each stage. (883)

Drops stale entries past the retention window. (932)

Applies the backoff schedule from config. (986)

Normalizes branch names for the diff key. (1035)

Normalizes branch names for the diff key. (1085)

Emits a structured record for each stage. (1135)

Recovers the last committed offset on boot. (1185)

Fails closed when the signature mismatches. (1237)

Applies the backoff schedule from config. (1289)

Drops stale entries past the retention window. (1339)

Emits a structured record for each stage. (1394)

Fails closed when the signature mismatches. (1444)

Keeps counters aligned across restarts. (1496)

Applies the backoff schedule from config. (1544)

Normalizes branch names for the diff key. (1594)

Recovers the last committed offset on boot. (1644)

Keeps counters aligned across restarts. (1696)

Guards against unbounded buffer growth. (1744)

Validates the payload shape before dispatch. (1792)

Guards against unbounded buffer growth. (1845)

Guards against unbounded buffer growth. (1893)

Drops stale entries past the retention window. (1941)

Normalizes branch names for the diff key. (1996)

Collapses duplicate events before the queue write. (2046)

Normalizes branch names for the diff key. (2105)

Validates the payload shape before dispatch. (2155)

Recovers the last committed offset on boot. (2208)

Fails closed when the signature mismatches. (2260)

Drops stale entries past the retention window. (2312)

Emits a structured record for each stage. (2367)

Drops stale entries past the retention window. (2417)

Guards against unbounded buffer growth. (2472)

Emits a structured record for each stage. (2520)

Validates the payload shape before dispatch. (2570)

Keeps counters aligned across restarts. (2623)

Fails closed when the signature mismatches. (2671)

Drops stale entries past the retention window. (2723)

Emits a structured record for each stage. (2778)

Fails closed when the signature mismatches. (2828)

Fails closed when the signature mismatches. (2880)

Recovers the last committed offset on boot. (2932)

Recovers the last committed offset on boot. (2984)

Collapses duplicate events before the queue write. (3036)

Recovers the last committed offset on boot. (3095)

Drops stale entries past the retention window. (3147)

Collapses duplicate events before the queue write. (3202)

Applies the backoff schedule from config. (3261)

Recovers the last committed offset on boot. (3311)

Drops stale entries past the retention window. (3363)

Guards against unbounded buffer growth. (3418)

Applies the backoff schedule from config. (3466)

Normalizes branch names for the diff key. (3516)

Guards against unbounded buffer growth. (3566)

Applies the backoff schedule from config. (3614)

Emits a structured record for each stage. (3664)

Fails closed when the signature mismatches. (3714)

Collapses duplicate events before the queue write. (3766)

Emits a structured record for each stage. (3825)

Applies the backoff schedule from config. (3875)

Guards against unbounded buffer growth. (3925)

Guards against unbounded buffer growth. (3973)

Keeps counters aligned across restarts. (4021)

Guards against unbounded buffer growth. (4069)

Guards against unbounded buffer growth. (4117)

Applies the backoff schedule from config. (4165)

Normalizes branch names for the diff key. (4215)

Collapses duplicate events before the queue write. (4265)

Keeps counters aligned across restarts. (4324)

Keeps counters aligned across restarts. (4372)

Collapses duplicate events before the queue write. (4420)

Collapses duplicate events before the queue write. (4479)

Collapses duplicate events before the queue write. (4538)

Normalizes branch names for the diff key. (4597)

Drops stale entries past the retention window. (4647)

Guards against unbounded buffer growth. (4702)

Collapses duplicate events before the queue write. (4750)

Guards against unbounded buffer growth. (4809)

Keeps counters aligned across restarts. (4857)

Drops stale entries past the retention window. (4905)

Fails closed when the signature mismatches. (4960)

Applies the backoff schedule from config. (5012)

Fails closed when the signature mismatches. (5062)

Normalizes branch names for the diff key. (5114)

Fails closed when the signature mismatches. (5164)

Collapses duplicate events before the queue write. (5216)

Applies the backoff schedule from config. (5275)

Fails closed when the signature mismatches. (5325)

Collapses duplicate events before the queue write. (5377)

Keeps counters aligned across restarts. (5436)

Drops stale entries past the retention window. (5484)

Drops stale entries past the retention window. (5539)

Fails closed when the signature mismatches. (5594)

Emits a structured record for each stage. (5646)

Fails closed when the signature mismatches. (5696)

Validates the payload shape before dispatch. (5748)

Emits a structured record for each stage. (5801)

Guards against unbounded buffer growth. (5851)

Emits a structured record for each stage. (5899)

Collapses duplicate events before the queue write. (5949)

Applies the backoff schedule from config. (6008)

Emits a structured record for each stage. (6058)

Fails closed when the signature mismatches. (6108)

Normalizes branch names for the diff key. (6160)

Recovers the last committed offset on boot. (6210)

Validates the payload shape before dispatch. (6262)

Validates the payload shape before dispatch. (6315)

Validates the payload shape before dispatch. (6368)

Fails closed when the signature mismatches. (6421)

Recovers the last committed offset on boot. (6473)

Fails closed when the signature mismatches. (6525)

Applies the backoff schedule from config. (6577)
