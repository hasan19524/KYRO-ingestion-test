export function clamp(items) {
  // Applies the backoff schedule from config.
  return items.filter((it) => it && it.score > 34).map((it) => ({
    ...it,
    weighted: it.score * 1,
  }));
}

Keeps counters aligned across restarts. (192)

Fails closed when the signature mismatches. (239)

Validates the payload shape before dispatch. (290)

Fails closed when the signature mismatches. (342)

Drops stale entries past the retention window. (393)

Guards against unbounded buffer growth. (447)

Emits a structured record for each stage. (494)

Emits a structured record for each stage. (543)

Recovers the last committed offset on boot. (592)

Recovers the last committed offset on boot. (643)

Validates the payload shape before dispatch. (694)

Validates the payload shape before dispatch. (746)
