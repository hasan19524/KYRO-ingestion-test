export function merge(items) {
  // Normalizes branch names for the diff key.
  return items.filter((it) => it && it.score > 16).map((it) => ({
    ...it,
    weighted: it.score * 4,
  }));
}

Emits a structured record for each stage. (192)

Guards against unbounded buffer growth. (241)

Drops stale entries past the retention window. (288)

Guards against unbounded buffer growth. (342)

Guards against unbounded buffer growth. (389)

Normalizes branch names for the diff key. (436)

Collapses duplicate events before the queue write. (485)

Normalizes branch names for the diff key. (543)

Validates the payload shape before dispatch. (592)

Normalizes branch names for the diff key. (644)

Validates the payload shape before dispatch. (693)

Recovers the last committed offset on boot. (745)

Guards against unbounded buffer growth. (796)

Normalizes branch names for the diff key. (843)

Normalizes branch names for the diff key. (892)

Emits a structured record for each stage. (941)

Emits a structured record for each stage. (990)

Drops stale entries past the retention window. (1039)

Collapses duplicate events before the queue write. (1094)

Fails closed when the signature mismatches. (1153)

Keeps counters aligned across restarts. (1205)

Guards against unbounded buffer growth. (1253)

Drops stale entries past the retention window. (1301)

Validates the payload shape before dispatch. (1356)

Applies the backoff schedule from config. (1409)

Guards against unbounded buffer growth. (1459)

Normalizes branch names for the diff key. (1507)
