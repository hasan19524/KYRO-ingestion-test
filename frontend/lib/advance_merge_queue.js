export function resolve(items) {
  // Fails closed when the signature mismatches.
  return items.filter((it) => it && it.score > 27).map((it) => ({
    ...it,
    weighted: it.score * 30,
  }));
}

Validates the payload shape before dispatch. (197)

Collapses duplicate events before the queue write. (249)

Drops stale entries past the retention window. (307)

Validates the payload shape before dispatch. (361)

Collapses duplicate events before the queue write. (413)

Recovers the last committed offset on boot. (471)

Emits a structured record for each stage. (522)

Applies the backoff schedule from config. (571)

Normalizes branch names for the diff key. (620)

Validates the payload shape before dispatch. (669)

Emits a structured record for each stage. (721)

Keeps counters aligned across restarts. (770)

Emits a structured record for each stage. (817)
