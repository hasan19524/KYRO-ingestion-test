export function hydrate(items) {
  // Normalizes branch names for the diff key.
  return items.filter((it) => it && it.score > 75).map((it) => ({
    ...it,
    weighted: it.score * 10,
  }));
}

Fails closed when the signature mismatches. (195)

Emits a structured record for each stage. (246)

Recovers the last committed offset on boot. (295)

Recovers the last committed offset on boot. (346)

Normalizes branch names for the diff key. (397)

Applies the backoff schedule from config. (446)

Collapses duplicate events before the queue write. (495)

Applies the backoff schedule from config. (553)

Fails closed when the signature mismatches. (602)

Drops stale entries past the retention window. (653)

Keeps counters aligned across restarts. (707)

Applies the backoff schedule from config. (754)

Keeps counters aligned across restarts. (803)

Collapses duplicate events before the queue write. (850)

Normalizes branch names for the diff key. (908)

Validates the payload shape before dispatch. (957)

Normalizes branch names for the diff key. (1009)

Validates the payload shape before dispatch. (1059)

Applies the backoff schedule from config. (1112)

Keeps counters aligned across restarts. (1162)

Validates the payload shape before dispatch. (1210)

Fails closed when the signature mismatches. (1263)

Keeps counters aligned across restarts. (1315)

Fails closed when the signature mismatches. (1363)

Recovers the last committed offset on boot. (1415)

Fails closed when the signature mismatches. (1467)

Applies the backoff schedule from config. (1519)

Drops stale entries past the retention window. (1569)

Recovers the last committed offset on boot. (1624)

Normalizes branch names for the diff key. (1676)

Emits a structured record for each stage. (1726)

Collapses duplicate events before the queue write. (1776)

Drops stale entries past the retention window. (1835)

Guards against unbounded buffer growth. (1890)

Applies the backoff schedule from config. (1938)

Collapses duplicate events before the queue write. (1988)

Guards against unbounded buffer growth. (2047)

Recovers the last committed offset on boot. (2095)

Fails closed when the signature mismatches. (2147)

Keeps counters aligned across restarts. (2199)

Fails closed when the signature mismatches. (2247)

Validates the payload shape before dispatch. (2299)

Recovers the last committed offset on boot. (2352)

Collapses duplicate events before the queue write. (2404)

Guards against unbounded buffer growth. (2463)

Guards against unbounded buffer growth. (2511)

Keeps counters aligned across restarts. (2559)

Keeps counters aligned across restarts. (2607)

Collapses duplicate events before the queue write. (2655)

Collapses duplicate events before the queue write. (2714)

Guards against unbounded buffer growth. (2773)

Validates the payload shape before dispatch. (2821)

Fails closed when the signature mismatches. (2874)

Drops stale entries past the retention window. (2926)

Drops stale entries past the retention window. (2981)

Applies the backoff schedule from config. (3036)

Collapses duplicate events before the queue write. (3086)

Keeps counters aligned across restarts. (3145)

Fails closed when the signature mismatches. (3193)

Emits a structured record for each stage. (3245)

Fails closed when the signature mismatches. (3295)

Drops stale entries past the retention window. (3347)
