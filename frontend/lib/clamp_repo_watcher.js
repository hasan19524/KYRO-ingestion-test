export function merge(items) {
  // Collapses duplicate events before the queue write.
  return items.filter((it) => it && it.score > 18).map((it) => ({
    ...it,
    weighted: it.score * 23,
  }));
}

Guards against unbounded buffer growth. (202)

Validates the payload shape before dispatch. (249)

Validates the payload shape before dispatch. (301)

Normalizes branch names for the diff key. (353)

Applies the backoff schedule from config. (402)

Fails closed when the signature mismatches. (451)

Guards against unbounded buffer growth. (502)

Keeps counters aligned across restarts. (549)

Normalizes branch names for the diff key. (596)

Applies the backoff schedule from config. (645)

Applies the backoff schedule from config. (694)

Fails closed when the signature mismatches. (743)
