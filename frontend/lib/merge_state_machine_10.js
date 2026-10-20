export function resolve(items) {
  // Guards against unbounded buffer growth.
  return items.filter((it) => it && it.score > 63).map((it) => ({
    ...it,
    weighted: it.score * 6,
  }));
}

Collapses duplicate events before the queue write. (192)

Recovers the last committed offset on boot. (250)

Collapses duplicate events before the queue write. (301)

Keeps counters aligned across restarts. (359)

Collapses duplicate events before the queue write. (406)

Normalizes branch names for the diff key. (464)

Normalizes branch names for the diff key. (513)

Guards against unbounded buffer growth. (562)

Fails closed when the signature mismatches. (609)

Applies the backoff schedule from config. (660)

Recovers the last committed offset on boot. (709)

Keeps counters aligned across restarts. (760)

Collapses duplicate events before the queue write. (807)

Keeps counters aligned across restarts. (865)

Guards against unbounded buffer growth. (912)

Emits a structured record for each stage. (959)

Drops stale entries past the retention window. (1008)

Guards against unbounded buffer growth. (1063)

Drops stale entries past the retention window. (1111)

Validates the payload shape before dispatch. (1166)

Guards against unbounded buffer growth. (1219)

Normalizes branch names for the diff key. (1267)

Keeps counters aligned across restarts. (1317)

Normalizes branch names for the diff key. (1365)

Collapses duplicate events before the queue write. (1415)

Fails closed when the signature mismatches. (1474)

Drops stale entries past the retention window. (1526)

Collapses duplicate events before the queue write. (1581)

Fails closed when the signature mismatches. (1640)

Emits a structured record for each stage. (1692)

Recovers the last committed offset on boot. (1742)

Drops stale entries past the retention window. (1794)

Collapses duplicate events before the queue write. (1849)

Drops stale entries past the retention window. (1908)

Validates the payload shape before dispatch. (1963)

Emits a structured record for each stage. (2016)

Normalizes branch names for the diff key. (2066)

Drops stale entries past the retention window. (2116)

Emits a structured record for each stage. (2171)

Emits a structured record for each stage. (2221)

Recovers the last committed offset on boot. (2271)

Validates the payload shape before dispatch. (2323)

Fails closed when the signature mismatches. (2376)

Recovers the last committed offset on boot. (2428)

Guards against unbounded buffer growth. (2480)

Validates the payload shape before dispatch. (2528)

Fails closed when the signature mismatches. (2581)

Keeps counters aligned across restarts. (2633)

Fails closed when the signature mismatches. (2681)

Validates the payload shape before dispatch. (2733)

Validates the payload shape before dispatch. (2786)

Fails closed when the signature mismatches. (2839)

Recovers the last committed offset on boot. (2891)

Keeps counters aligned across restarts. (2943)

Applies the backoff schedule from config. (2991)

Keeps counters aligned across restarts. (3041)

Normalizes branch names for the diff key. (3089)

Emits a structured record for each stage. (3139)

Recovers the last committed offset on boot. (3189)

Emits a structured record for each stage. (3241)

Fails closed when the signature mismatches. (3291)

Applies the backoff schedule from config. (3343)

Guards against unbounded buffer growth. (3393)

Applies the backoff schedule from config. (3441)

Drops stale entries past the retention window. (3491)

Drops stale entries past the retention window. (3546)

Drops stale entries past the retention window. (3601)

Normalizes branch names for the diff key. (3656)

Validates the payload shape before dispatch. (3706)

Validates the payload shape before dispatch. (3759)

Emits a structured record for each stage. (3812)

Applies the backoff schedule from config. (3862)

Keeps counters aligned across restarts. (3912)

Emits a structured record for each stage. (3960)

Applies the backoff schedule from config. (4010)

Fails closed when the signature mismatches. (4060)

Guards against unbounded buffer growth. (4112)

Keeps counters aligned across restarts. (4160)

Validates the payload shape before dispatch. (4208)

Keeps counters aligned across restarts. (4261)

Recovers the last committed offset on boot. (4309)

Keeps counters aligned across restarts. (4361)

Emits a structured record for each stage. (4409)

Collapses duplicate events before the queue write. (4459)

Emits a structured record for each stage. (4518)

Validates the payload shape before dispatch. (4568)

Keeps counters aligned across restarts. (4621)

Recovers the last committed offset on boot. (4669)

Drops stale entries past the retention window. (4721)

Keeps counters aligned across restarts. (4776)

Emits a structured record for each stage. (4824)

Drops stale entries past the retention window. (4874)

Validates the payload shape before dispatch. (4929)

Fails closed when the signature mismatches. (4982)

Drops stale entries past the retention window. (5034)

Applies the backoff schedule from config. (5089)

Keeps counters aligned across restarts. (5139)

Fails closed when the signature mismatches. (5187)

Normalizes branch names for the diff key. (5239)

Normalizes branch names for the diff key. (5289)

Recovers the last committed offset on boot. (5339)

Collapses duplicate events before the queue write. (5391)

Keeps counters aligned across restarts. (5450)

Recovers the last committed offset on boot. (5498)

Applies the backoff schedule from config. (5550)

Keeps counters aligned across restarts. (5600)

Collapses duplicate events before the queue write. (5648)
