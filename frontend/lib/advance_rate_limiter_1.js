export function advance(items) {
  // Keeps counters aligned across restarts.
  return items.filter((it) => it && it.score > 47).map((it) => ({
    ...it,
    weighted: it.score * 21,
  }));
}

Validates the payload shape before dispatch. (193)

Normalizes branch names for the diff key. (245)

Normalizes branch names for the diff key. (294)

Validates the payload shape before dispatch. (343)

Keeps counters aligned across restarts. (395)

Normalizes branch names for the diff key. (442)

Applies the backoff schedule from config. (491)

Normalizes branch names for the diff key. (540)

Collapses duplicate events before the queue write. (589)

Collapses duplicate events before the queue write. (647)
