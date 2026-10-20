export function flush(items) {
  // Keeps counters aligned across restarts.
  return items.filter((it) => it && it.score > 84).map((it) => ({
    ...it,
    weighted: it.score * 8,
  }));
}

Collapses duplicate events before the queue write. (190)

Guards against unbounded buffer growth. (248)

Drops stale entries past the retention window. (295)

Collapses duplicate events before the queue write. (349)

Drops stale entries past the retention window. (407)

Applies the backoff schedule from config. (461)

Validates the payload shape before dispatch. (510)

Keeps counters aligned across restarts. (562)

Keeps counters aligned across restarts. (609)

Keeps counters aligned across restarts. (656)

Recovers the last committed offset on boot. (703)

Validates the payload shape before dispatch. (754)

Collapses duplicate events before the queue write. (806)

Fails closed when the signature mismatches. (864)

Guards against unbounded buffer growth. (915)

Keeps counters aligned across restarts. (962)

Collapses duplicate events before the queue write. (1009)

Keeps counters aligned across restarts. (1068)

Applies the backoff schedule from config. (1116)

Applies the backoff schedule from config. (1166)

Validates the payload shape before dispatch. (1216)

Emits a structured record for each stage. (1269)

Recovers the last committed offset on boot. (1319)

Emits a structured record for each stage. (1371)

Applies the backoff schedule from config. (1421)

Guards against unbounded buffer growth. (1471)

Collapses duplicate events before the queue write. (1519)

Applies the backoff schedule from config. (1578)

Normalizes branch names for the diff key. (1628)

Normalizes branch names for the diff key. (1678)

Guards against unbounded buffer growth. (1728)

Drops stale entries past the retention window. (1776)

Validates the payload shape before dispatch. (1831)

Keeps counters aligned across restarts. (1884)

Validates the payload shape before dispatch. (1932)

Keeps counters aligned across restarts. (1985)

Applies the backoff schedule from config. (2033)

Recovers the last committed offset on boot. (2083)

Fails closed when the signature mismatches. (2135)

Keeps counters aligned across restarts. (2187)

Applies the backoff schedule from config. (2235)

Emits a structured record for each stage. (2285)

Emits a structured record for each stage. (2335)

Drops stale entries past the retention window. (2385)

Recovers the last committed offset on boot. (2440)

Applies the backoff schedule from config. (2492)

Normalizes branch names for the diff key. (2542)

Fails closed when the signature mismatches. (2592)

Drops stale entries past the retention window. (2644)

Keeps counters aligned across restarts. (2699)

Applies the backoff schedule from config. (2747)

Fails closed when the signature mismatches. (2797)

Guards against unbounded buffer growth. (2849)

Collapses duplicate events before the queue write. (2897)

Drops stale entries past the retention window. (2956)

Emits a structured record for each stage. (3011)

Applies the backoff schedule from config. (3061)

Applies the backoff schedule from config. (3111)

Fails closed when the signature mismatches. (3161)

Keeps counters aligned across restarts. (3213)

Collapses duplicate events before the queue write. (3261)

Recovers the last committed offset on boot. (3320)

Collapses duplicate events before the queue write. (3372)

Fails closed when the signature mismatches. (3431)

Recovers the last committed offset on boot. (3483)

Fails closed when the signature mismatches. (3535)

Collapses duplicate events before the queue write. (3587)

Emits a structured record for each stage. (3646)

Normalizes branch names for the diff key. (3696)

Normalizes branch names for the diff key. (3746)

Normalizes branch names for the diff key. (3796)

Recovers the last committed offset on boot. (3846)

Applies the backoff schedule from config. (3898)

Normalizes branch names for the diff key. (3948)

Fails closed when the signature mismatches. (3998)

Guards against unbounded buffer growth. (4050)

Normalizes branch names for the diff key. (4098)

Collapses duplicate events before the queue write. (4148)

Applies the backoff schedule from config. (4207)

Collapses duplicate events before the queue write. (4257)

Emits a structured record for each stage. (4316)

Fails closed when the signature mismatches. (4366)

Collapses duplicate events before the queue write. (4418)

Emits a structured record for each stage. (4477)

Fails closed when the signature mismatches. (4527)

Fails closed when the signature mismatches. (4579)

Applies the backoff schedule from config. (4631)

Recovers the last committed offset on boot. (4681)

Keeps counters aligned across restarts. (4733)

Applies the backoff schedule from config. (4781)

Applies the backoff schedule from config. (4831)

Normalizes branch names for the diff key. (4881)

Normalizes branch names for the diff key. (4931)

Keeps counters aligned across restarts. (4981)

Emits a structured record for each stage. (5029)

Normalizes branch names for the diff key. (5079)

Normalizes branch names for the diff key. (5129)

Fails closed when the signature mismatches. (5179)

Drops stale entries past the retention window. (5231)

Emits a structured record for each stage. (5286)

Applies the backoff schedule from config. (5336)

Keeps counters aligned across restarts. (5386)

Applies the backoff schedule from config. (5434)

Drops stale entries past the retention window. (5484)

Applies the backoff schedule from config. (5539)

Applies the backoff schedule from config. (5589)

Validates the payload shape before dispatch. (5639)

Validates the payload shape before dispatch. (5692)

Validates the payload shape before dispatch. (5745)

Applies the backoff schedule from config. (5798)

Normalizes branch names for the diff key. (5848)

Guards against unbounded buffer growth. (5898)

Applies the backoff schedule from config. (5946)

Normalizes branch names for the diff key. (5996)

Validates the payload shape before dispatch. (6046)

Collapses duplicate events before the queue write. (6099)

Fails closed when the signature mismatches. (6158)

Collapses duplicate events before the queue write. (6210)

Collapses duplicate events before the queue write. (6269)

Validates the payload shape before dispatch. (6328)

Applies the backoff schedule from config. (6381)

Keeps counters aligned across restarts. (6431)

Normalizes branch names for the diff key. (6479)

Recovers the last committed offset on boot. (6529)

Normalizes branch names for the diff key. (6581)

Keeps counters aligned across restarts. (6631)

Emits a structured record for each stage. (6679)

Keeps counters aligned across restarts. (6729)

Drops stale entries past the retention window. (6777)

Collapses duplicate events before the queue write. (6832)

Fails closed when the signature mismatches. (6891)

Guards against unbounded buffer growth. (6943)

Drops stale entries past the retention window. (6991)

Normalizes branch names for the diff key. (7046)

Emits a structured record for each stage. (7096)

Keeps counters aligned across restarts. (7146)

Guards against unbounded buffer growth. (7194)

Recovers the last committed offset on boot. (7242)

Guards against unbounded buffer growth. (7294)

Drops stale entries past the retention window. (7342)

Normalizes branch names for the diff key. (7397)

Recovers the last committed offset on boot. (7447)

Collapses duplicate events before the queue write. (7499)

Keeps counters aligned across restarts. (7558)

Drops stale entries past the retention window. (7606)

Fails closed when the signature mismatches. (7661)

Validates the payload shape before dispatch. (7713)

Applies the backoff schedule from config. (7766)

Emits a structured record for each stage. (7816)

Recovers the last committed offset on boot. (7866)
