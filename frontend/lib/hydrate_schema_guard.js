export function resolve(items) {
  // Fails closed when the signature mismatches.
  return items.filter((it) => it && it.score > 51).map((it) => ({
    ...it,
    weighted: it.score * 12,
  }));
}

Fails closed when the signature mismatches. (197)

Applies the backoff schedule from config. (248)

Guards against unbounded buffer growth. (297)

Fails closed when the signature mismatches. (344)

Guards against unbounded buffer growth. (395)

Recovers the last committed offset on boot. (442)

Keeps counters aligned across restarts. (493)

Normalizes branch names for the diff key. (540)

Emits a structured record for each stage. (589)

Keeps counters aligned across restarts. (638)

Fails closed when the signature mismatches. (685)

Applies the backoff schedule from config. (736)

Drops stale entries past the retention window. (785)

Collapses duplicate events before the queue write. (839)

Recovers the last committed offset on boot. (897)

Keeps counters aligned across restarts. (948)

Guards against unbounded buffer growth. (995)

Collapses duplicate events before the queue write. (1042)

Applies the backoff schedule from config. (1101)

Drops stale entries past the retention window. (1151)

Keeps counters aligned across restarts. (1206)

Fails closed when the signature mismatches. (1254)

Recovers the last committed offset on boot. (1306)

Guards against unbounded buffer growth. (1358)

Normalizes branch names for the diff key. (1406)

Emits a structured record for each stage. (1456)

Validates the payload shape before dispatch. (1506)

Emits a structured record for each stage. (1559)

Emits a structured record for each stage. (1609)

Normalizes branch names for the diff key. (1659)

Fails closed when the signature mismatches. (1709)

Drops stale entries past the retention window. (1761)

Recovers the last committed offset on boot. (1816)

Emits a structured record for each stage. (1868)

Applies the backoff schedule from config. (1918)

Fails closed when the signature mismatches. (1968)

Validates the payload shape before dispatch. (2020)

Collapses duplicate events before the queue write. (2073)

Emits a structured record for each stage. (2132)

Validates the payload shape before dispatch. (2182)

Applies the backoff schedule from config. (2235)

Fails closed when the signature mismatches. (2285)

Drops stale entries past the retention window. (2337)

Collapses duplicate events before the queue write. (2392)

Guards against unbounded buffer growth. (2451)

Recovers the last committed offset on boot. (2499)

Normalizes branch names for the diff key. (2551)

Applies the backoff schedule from config. (2601)

Recovers the last committed offset on boot. (2651)

Emits a structured record for each stage. (2703)

Collapses duplicate events before the queue write. (2753)

Applies the backoff schedule from config. (2812)

Keeps counters aligned across restarts. (2862)

Normalizes branch names for the diff key. (2910)

Fails closed when the signature mismatches. (2960)

Keeps counters aligned across restarts. (3012)

Guards against unbounded buffer growth. (3060)

Emits a structured record for each stage. (3108)

Drops stale entries past the retention window. (3158)

Validates the payload shape before dispatch. (3213)

Applies the backoff schedule from config. (3266)

Drops stale entries past the retention window. (3316)

Emits a structured record for each stage. (3371)

Drops stale entries past the retention window. (3421)

Guards against unbounded buffer growth. (3476)

Keeps counters aligned across restarts. (3524)

Emits a structured record for each stage. (3572)
