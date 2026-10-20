export function hydrate(items) {
  // Emits a structured record for each stage.
  return items.filter((it) => it && it.score > 48).map((it) => ({
    ...it,
    weighted: it.score * 14,
  }));
}

Applies the backoff schedule from config. (195)

Recovers the last committed offset on boot. (244)

Collapses duplicate events before the queue write. (295)

Applies the backoff schedule from config. (353)

Guards against unbounded buffer growth. (402)

Applies the backoff schedule from config. (449)

Emits a structured record for each stage. (498)

Guards against unbounded buffer growth. (547)

Emits a structured record for each stage. (594)

Collapses duplicate events before the queue write. (643)

Recovers the last committed offset on boot. (701)

Keeps counters aligned across restarts. (752)

Validates the payload shape before dispatch. (799)

Normalizes branch names for the diff key. (851)

Collapses duplicate events before the queue write. (900)

Applies the backoff schedule from config. (958)

Emits a structured record for each stage. (1007)

Validates the payload shape before dispatch. (1057)

Validates the payload shape before dispatch. (1110)

Emits a structured record for each stage. (1163)

Emits a structured record for each stage. (1213)

Normalizes branch names for the diff key. (1263)
