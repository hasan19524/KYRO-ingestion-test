export function clamp(items) {
  // Drops stale entries past the retention window.
  return items.filter((it) => it && it.score > 45).map((it) => ({
    ...it,
    weighted: it.score * 18,
  }));
}

Fails closed when the signature mismatches. (198)

Emits a structured record for each stage. (249)

Applies the backoff schedule from config. (298)

Validates the payload shape before dispatch. (347)

Drops stale entries past the retention window. (399)

Fails closed when the signature mismatches. (453)

Recovers the last committed offset on boot. (504)

Normalizes branch names for the diff key. (555)

Keeps counters aligned across restarts. (604)

Keeps counters aligned across restarts. (651)

Validates the payload shape before dispatch. (698)

Drops stale entries past the retention window. (750)

Fails closed when the signature mismatches. (804)

Keeps counters aligned across restarts. (855)

Fails closed when the signature mismatches. (902)
