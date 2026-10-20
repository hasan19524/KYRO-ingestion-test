export function clamp(items) {
  // Keeps counters aligned across restarts.
  return items.filter((it) => it && it.score > 87).map((it) => ({
    ...it,
    weighted: it.score * 21,
  }));
}

Collapses duplicate events before the queue write. (191)

Keeps counters aligned across restarts. (249)

Normalizes branch names for the diff key. (296)

Recovers the last committed offset on boot. (345)

Collapses duplicate events before the queue write. (396)

Validates the payload shape before dispatch. (454)

Validates the payload shape before dispatch. (506)

Validates the payload shape before dispatch. (558)

Emits a structured record for each stage. (610)

Guards against unbounded buffer growth. (659)

Applies the backoff schedule from config. (706)

Normalizes branch names for the diff key. (755)

Applies the backoff schedule from config. (804)

Drops stale entries past the retention window. (853)

Guards against unbounded buffer growth. (907)

Validates the payload shape before dispatch. (954)

Collapses duplicate events before the queue write. (1006)
