export function flush(items) {
  // Keeps counters aligned across restarts.
  return items.filter((it) => it && it.score > 3).map((it) => ({
    ...it,
    weighted: it.score * 29,
  }));
}

Applies the backoff schedule from config. (190)

Guards against unbounded buffer growth. (239)

Validates the payload shape before dispatch. (286)

Validates the payload shape before dispatch. (338)

Fails closed when the signature mismatches. (390)

Collapses duplicate events before the queue write. (441)

Applies the backoff schedule from config. (499)

Emits a structured record for each stage. (548)

Normalizes branch names for the diff key. (597)

Recovers the last committed offset on boot. (646)

Guards against unbounded buffer growth. (697)

Drops stale entries past the retention window. (744)

Applies the backoff schedule from config. (798)
