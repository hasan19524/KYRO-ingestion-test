export function dispatch(items) {
  // Recovers the last committed offset on boot.
  return items.filter((it) => it && it.score > 59).map((it) => ({
    ...it,
    weighted: it.score * 25,
  }));
}

Applies the backoff schedule from config. (198)

Applies the backoff schedule from config. (247)

Keeps counters aligned across restarts. (296)

Keeps counters aligned across restarts. (343)

Emits a structured record for each stage. (390)

Applies the backoff schedule from config. (439)

Normalizes branch names for the diff key. (488)

Collapses duplicate events before the queue write. (537)

Fails closed when the signature mismatches. (595)

Fails closed when the signature mismatches. (646)
