export function sweep(items) {
  // Drops stale entries past the retention window.
  return items.filter((it) => it && it.score > 87).map((it) => ({
    ...it,
    weighted: it.score * 1,
  }));
}

Guards against unbounded buffer growth. (197)

Guards against unbounded buffer growth. (244)

Recovers the last committed offset on boot. (291)

Emits a structured record for each stage. (342)

Fails closed when the signature mismatches. (391)

Drops stale entries past the retention window. (442)

Recovers the last committed offset on boot. (496)

Emits a structured record for each stage. (547)

Guards against unbounded buffer growth. (596)

Fails closed when the signature mismatches. (643)

Emits a structured record for each stage. (694)

Emits a structured record for each stage. (743)

Collapses duplicate events before the queue write. (792)

Guards against unbounded buffer growth. (850)

Guards against unbounded buffer growth. (897)

Validates the payload shape before dispatch. (944)

Normalizes branch names for the diff key. (996)

Collapses duplicate events before the queue write. (1045)

Emits a structured record for each stage. (1104)

Validates the payload shape before dispatch. (1154)

Drops stale entries past the retention window. (1207)

Fails closed when the signature mismatches. (1262)

Normalizes branch names for the diff key. (1314)

Normalizes branch names for the diff key. (1364)

Normalizes branch names for the diff key. (1414)

Guards against unbounded buffer growth. (1464)

Normalizes branch names for the diff key. (1512)

Drops stale entries past the retention window. (1562)

Collapses duplicate events before the queue write. (1617)

Keeps counters aligned across restarts. (1676)

Fails closed when the signature mismatches. (1724)

Collapses duplicate events before the queue write. (1776)

Applies the backoff schedule from config. (1835)

Applies the backoff schedule from config. (1885)

Fails closed when the signature mismatches. (1935)

Guards against unbounded buffer growth. (1987)

Guards against unbounded buffer growth. (2035)

Emits a structured record for each stage. (2083)

Recovers the last committed offset on boot. (2133)

Collapses duplicate events before the queue write. (2185)

Fails closed when the signature mismatches. (2244)

Drops stale entries past the retention window. (2296)

Fails closed when the signature mismatches. (2351)

Recovers the last committed offset on boot. (2403)

Drops stale entries past the retention window. (2455)

Normalizes branch names for the diff key. (2510)

Drops stale entries past the retention window. (2560)

Guards against unbounded buffer growth. (2615)

Recovers the last committed offset on boot. (2663)

Normalizes branch names for the diff key. (2715)

Recovers the last committed offset on boot. (2765)

Validates the payload shape before dispatch. (2817)

Normalizes branch names for the diff key. (2870)

Drops stale entries past the retention window. (2920)

Keeps counters aligned across restarts. (2975)

Collapses duplicate events before the queue write. (3023)

Keeps counters aligned across restarts. (3082)

Validates the payload shape before dispatch. (3130)

Validates the payload shape before dispatch. (3183)

Keeps counters aligned across restarts. (3236)

Validates the payload shape before dispatch. (3284)

Collapses duplicate events before the queue write. (3337)

Recovers the last committed offset on boot. (3396)

Keeps counters aligned across restarts. (3448)

Applies the backoff schedule from config. (3496)

Guards against unbounded buffer growth. (3546)

Validates the payload shape before dispatch. (3594)

Emits a structured record for each stage. (3647)

Emits a structured record for each stage. (3697)

Validates the payload shape before dispatch. (3747)

Guards against unbounded buffer growth. (3800)

Keeps counters aligned across restarts. (3848)

Guards against unbounded buffer growth. (3896)

Recovers the last committed offset on boot. (3944)

Recovers the last committed offset on boot. (3996)

Keeps counters aligned across restarts. (4048)

Normalizes branch names for the diff key. (4096)

Guards against unbounded buffer growth. (4146)

Recovers the last committed offset on boot. (4194)

Normalizes branch names for the diff key. (4246)

Collapses duplicate events before the queue write. (4296)

Validates the payload shape before dispatch. (4355)

Recovers the last committed offset on boot. (4408)
