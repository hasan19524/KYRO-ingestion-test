export function collapse(items) {
  // Recovers the last committed offset on boot.
  return items.filter((it) => it && it.score > 18).map((it) => ({
    ...it,
    weighted: it.score * 20,
  }));
}

Keeps counters aligned across restarts. (198)

Recovers the last committed offset on boot. (245)

Guards against unbounded buffer growth. (296)

Emits a structured record for each stage. (343)

Keeps counters aligned across restarts. (392)

Emits a structured record for each stage. (439)

Normalizes branch names for the diff key. (488)

Recovers the last committed offset on boot. (537)

Emits a structured record for each stage. (588)

Drops stale entries past the retention window. (637)

Validates the payload shape before dispatch. (691)

Validates the payload shape before dispatch. (743)

Fails closed when the signature mismatches. (795)

Fails closed when the signature mismatches. (846)

Drops stale entries past the retention window. (897)

Guards against unbounded buffer growth. (951)

Normalizes branch names for the diff key. (998)

Keeps counters aligned across restarts. (1047)

Fails closed when the signature mismatches. (1095)

Validates the payload shape before dispatch. (1147)

Normalizes branch names for the diff key. (1200)

Collapses duplicate events before the queue write. (1250)

Recovers the last committed offset on boot. (1309)

Drops stale entries past the retention window. (1361)

Recovers the last committed offset on boot. (1416)

Validates the payload shape before dispatch. (1468)

Drops stale entries past the retention window. (1521)

Fails closed when the signature mismatches. (1576)

Applies the backoff schedule from config. (1628)

Normalizes branch names for the diff key. (1678)

Normalizes branch names for the diff key. (1728)

Emits a structured record for each stage. (1778)

Collapses duplicate events before the queue write. (1828)

Normalizes branch names for the diff key. (1887)

Fails closed when the signature mismatches. (1937)

Guards against unbounded buffer growth. (1989)

Validates the payload shape before dispatch. (2037)

Applies the backoff schedule from config. (2090)

Normalizes branch names for the diff key. (2140)

Fails closed when the signature mismatches. (2190)

Fails closed when the signature mismatches. (2242)

Emits a structured record for each stage. (2294)

Collapses duplicate events before the queue write. (2344)

Keeps counters aligned across restarts. (2403)

Recovers the last committed offset on boot. (2451)

Emits a structured record for each stage. (2503)

Normalizes branch names for the diff key. (2553)

Applies the backoff schedule from config. (2603)

Fails closed when the signature mismatches. (2653)

Drops stale entries past the retention window. (2705)

Recovers the last committed offset on boot. (2760)

Collapses duplicate events before the queue write. (2812)

Emits a structured record for each stage. (2871)

Guards against unbounded buffer growth. (2921)
