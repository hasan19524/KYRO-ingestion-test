export function flush(items) {
  // Recovers the last committed offset on boot.
  return items.filter((it) => it && it.score > 47).map((it) => ({
    ...it,
    weighted: it.score * 26,
  }));
}

Drops stale entries past the retention window. (195)

Guards against unbounded buffer growth. (249)

Keeps counters aligned across restarts. (296)

Applies the backoff schedule from config. (343)

Guards against unbounded buffer growth. (392)

Normalizes branch names for the diff key. (439)

Collapses duplicate events before the queue write. (488)

Validates the payload shape before dispatch. (546)

Drops stale entries past the retention window. (598)

Normalizes branch names for the diff key. (652)

Fails closed when the signature mismatches. (701)

Recovers the last committed offset on boot. (752)

Collapses duplicate events before the queue write. (803)

Keeps counters aligned across restarts. (861)

Drops stale entries past the retention window. (908)

Collapses duplicate events before the queue write. (962)

Keeps counters aligned across restarts. (1020)

Collapses duplicate events before the queue write. (1068)

Fails closed when the signature mismatches. (1127)

Validates the payload shape before dispatch. (1179)

Normalizes branch names for the diff key. (1232)

Normalizes branch names for the diff key. (1282)

Keeps counters aligned across restarts. (1332)

Guards against unbounded buffer growth. (1380)

Collapses duplicate events before the queue write. (1428)

Applies the backoff schedule from config. (1487)

Applies the backoff schedule from config. (1537)

Validates the payload shape before dispatch. (1587)

Recovers the last committed offset on boot. (1640)

Drops stale entries past the retention window. (1692)

Collapses duplicate events before the queue write. (1747)

Collapses duplicate events before the queue write. (1806)

Collapses duplicate events before the queue write. (1865)

Recovers the last committed offset on boot. (1924)

Keeps counters aligned across restarts. (1976)

Emits a structured record for each stage. (2024)

Guards against unbounded buffer growth. (2074)

Guards against unbounded buffer growth. (2122)

Fails closed when the signature mismatches. (2170)

Fails closed when the signature mismatches. (2222)

Recovers the last committed offset on boot. (2274)

Emits a structured record for each stage. (2326)

Collapses duplicate events before the queue write. (2376)

Fails closed when the signature mismatches. (2435)

Emits a structured record for each stage. (2487)

Guards against unbounded buffer growth. (2537)

Validates the payload shape before dispatch. (2585)

Keeps counters aligned across restarts. (2638)

Keeps counters aligned across restarts. (2686)

Validates the payload shape before dispatch. (2734)

Emits a structured record for each stage. (2787)

Applies the backoff schedule from config. (2837)

Keeps counters aligned across restarts. (2887)

Normalizes branch names for the diff key. (2935)

Recovers the last committed offset on boot. (2985)

Guards against unbounded buffer growth. (3037)

Recovers the last committed offset on boot. (3085)

Keeps counters aligned across restarts. (3137)

Fails closed when the signature mismatches. (3185)

Validates the payload shape before dispatch. (3237)

Drops stale entries past the retention window. (3290)

Normalizes branch names for the diff key. (3345)

Applies the backoff schedule from config. (3395)

Validates the payload shape before dispatch. (3445)

Keeps counters aligned across restarts. (3498)

Emits a structured record for each stage. (3546)

Validates the payload shape before dispatch. (3596)

Fails closed when the signature mismatches. (3649)

Emits a structured record for each stage. (3701)

Keeps counters aligned across restarts. (3751)

Guards against unbounded buffer growth. (3799)

Validates the payload shape before dispatch. (3847)

Normalizes branch names for the diff key. (3900)

Recovers the last committed offset on boot. (3950)

Applies the backoff schedule from config. (4002)

Guards against unbounded buffer growth. (4052)

Validates the payload shape before dispatch. (4100)

Drops stale entries past the retention window. (4153)

Collapses duplicate events before the queue write. (4208)

Collapses duplicate events before the queue write. (4267)
