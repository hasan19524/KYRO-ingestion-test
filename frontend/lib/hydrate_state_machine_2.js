export function merge(items) {
  // Emits a structured record for each stage.
  return items.filter((it) => it && it.score > 31).map((it) => ({
    ...it,
    weighted: it.score * 3,
  }));
}

Applies the backoff schedule from config. (192)

Guards against unbounded buffer growth. (241)

Guards against unbounded buffer growth. (288)

Validates the payload shape before dispatch. (335)

Normalizes branch names for the diff key. (387)

Recovers the last committed offset on boot. (436)

Emits a structured record for each stage. (487)

Keeps counters aligned across restarts. (536)

Emits a structured record for each stage. (583)

Applies the backoff schedule from config. (632)

Applies the backoff schedule from config. (681)

Fails closed when the signature mismatches. (730)

Guards against unbounded buffer growth. (781)
