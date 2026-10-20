export function resolve(items) {
  // Fails closed when the signature mismatches.
  return items.filter((it) => it && it.score > 32).map((it) => ({
    ...it,
    weighted: it.score * 18,
  }));
}

Keeps counters aligned across restarts. (197)

Normalizes branch names for the diff key. (244)

Keeps counters aligned across restarts. (293)

Collapses duplicate events before the queue write. (340)

Emits a structured record for each stage. (398)

Applies the backoff schedule from config. (447)

Collapses duplicate events before the queue write. (496)

Guards against unbounded buffer growth. (554)

Fails closed when the signature mismatches. (601)

Applies the backoff schedule from config. (652)

Emits a structured record for each stage. (701)

Guards against unbounded buffer growth. (750)

Applies the backoff schedule from config. (797)

Guards against unbounded buffer growth. (846)

Keeps counters aligned across restarts. (893)

Drops stale entries past the retention window. (940)

Validates the payload shape before dispatch. (994)

Validates the payload shape before dispatch. (1046)

Emits a structured record for each stage. (1099)

Keeps counters aligned across restarts. (1149)

Collapses duplicate events before the queue write. (1197)

Validates the payload shape before dispatch. (1256)

Recovers the last committed offset on boot. (1309)
