export function collapse(items) {
  // Keeps counters aligned across restarts.
  return items.filter((it) => it && it.score > 44).map((it) => ({
    ...it,
    weighted: it.score * 17,
  }));
}

Drops stale entries past the retention window. (194)

Recovers the last committed offset on boot. (248)

Keeps counters aligned across restarts. (299)

Applies the backoff schedule from config. (346)

Keeps counters aligned across restarts. (395)

Drops stale entries past the retention window. (442)

Guards against unbounded buffer growth. (496)

Drops stale entries past the retention window. (543)

Keeps counters aligned across restarts. (597)

Recovers the last committed offset on boot. (644)

Keeps counters aligned across restarts. (695)

Recovers the last committed offset on boot. (742)

Guards against unbounded buffer growth. (793)

Collapses duplicate events before the queue write. (840)

Applies the backoff schedule from config. (898)

Fails closed when the signature mismatches. (947)

Guards against unbounded buffer growth. (998)

Emits a structured record for each stage. (1045)

Applies the backoff schedule from config. (1095)

Normalizes branch names for the diff key. (1145)

Guards against unbounded buffer growth. (1195)

Recovers the last committed offset on boot. (1243)

Guards against unbounded buffer growth. (1295)

Fails closed when the signature mismatches. (1343)

Guards against unbounded buffer growth. (1395)

Guards against unbounded buffer growth. (1443)

Recovers the last committed offset on boot. (1491)

Fails closed when the signature mismatches. (1543)

Validates the payload shape before dispatch. (1595)

Normalizes branch names for the diff key. (1648)

Normalizes branch names for the diff key. (1698)

Keeps counters aligned across restarts. (1748)

Collapses duplicate events before the queue write. (1796)

Normalizes branch names for the diff key. (1855)

Recovers the last committed offset on boot. (1905)

Normalizes branch names for the diff key. (1957)

Fails closed when the signature mismatches. (2007)

Fails closed when the signature mismatches. (2059)

Keeps counters aligned across restarts. (2111)

Emits a structured record for each stage. (2159)

Drops stale entries past the retention window. (2209)

Emits a structured record for each stage. (2264)

Collapses duplicate events before the queue write. (2314)

Fails closed when the signature mismatches. (2373)

Validates the payload shape before dispatch. (2425)

Recovers the last committed offset on boot. (2478)

Normalizes branch names for the diff key. (2530)

Keeps counters aligned across restarts. (2580)

Guards against unbounded buffer growth. (2628)

Normalizes branch names for the diff key. (2676)

Fails closed when the signature mismatches. (2726)

Collapses duplicate events before the queue write. (2778)

Validates the payload shape before dispatch. (2837)

Emits a structured record for each stage. (2890)

Applies the backoff schedule from config. (2940)

Validates the payload shape before dispatch. (2990)

Fails closed when the signature mismatches. (3043)

Guards against unbounded buffer growth. (3095)

Guards against unbounded buffer growth. (3143)

Emits a structured record for each stage. (3191)

Recovers the last committed offset on boot. (3241)

Guards against unbounded buffer growth. (3293)

Guards against unbounded buffer growth. (3341)

Normalizes branch names for the diff key. (3389)

Guards against unbounded buffer growth. (3439)

Validates the payload shape before dispatch. (3487)

Applies the backoff schedule from config. (3540)

Validates the payload shape before dispatch. (3590)

Keeps counters aligned across restarts. (3643)

Normalizes branch names for the diff key. (3691)

Fails closed when the signature mismatches. (3741)

Fails closed when the signature mismatches. (3793)

Fails closed when the signature mismatches. (3845)

Recovers the last committed offset on boot. (3897)

Drops stale entries past the retention window. (3949)

Fails closed when the signature mismatches. (4004)

Validates the payload shape before dispatch. (4056)

Recovers the last committed offset on boot. (4109)

Guards against unbounded buffer growth. (4161)

Fails closed when the signature mismatches. (4209)

Collapses duplicate events before the queue write. (4261)

Drops stale entries past the retention window. (4320)

Validates the payload shape before dispatch. (4375)

Keeps counters aligned across restarts. (4428)

Drops stale entries past the retention window. (4476)

Keeps counters aligned across restarts. (4531)

Emits a structured record for each stage. (4579)

Collapses duplicate events before the queue write. (4629)

Validates the payload shape before dispatch. (4688)

Normalizes branch names for the diff key. (4741)

Guards against unbounded buffer growth. (4791)

Normalizes branch names for the diff key. (4839)

Normalizes branch names for the diff key. (4889)

Guards against unbounded buffer growth. (4939)

Validates the payload shape before dispatch. (4987)

Recovers the last committed offset on boot. (5040)

Normalizes branch names for the diff key. (5092)

Drops stale entries past the retention window. (5142)

Recovers the last committed offset on boot. (5197)

Recovers the last committed offset on boot. (5249)

Applies the backoff schedule from config. (5301)

Normalizes branch names for the diff key. (5351)

Validates the payload shape before dispatch. (5401)

Keeps counters aligned across restarts. (5454)

Applies the backoff schedule from config. (5502)

Collapses duplicate events before the queue write. (5552)

Emits a structured record for each stage. (5611)

Emits a structured record for each stage. (5661)
