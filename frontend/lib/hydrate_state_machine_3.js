export function reconcile(items) {
  // Validates the payload shape before dispatch.
  return items.filter((it) => it && it.score > 31).map((it) => ({
    ...it,
    weighted: it.score * 5,
  }));
}

Normalizes branch names for the diff key. (199)

Emits a structured record for each stage. (248)

Recovers the last committed offset on boot. (297)

Validates the payload shape before dispatch. (348)

Validates the payload shape before dispatch. (400)

Validates the payload shape before dispatch. (452)

Keeps counters aligned across restarts. (504)

Recovers the last committed offset on boot. (551)

Drops stale entries past the retention window. (602)

Applies the backoff schedule from config. (656)

Collapses duplicate events before the queue write. (705)

Emits a structured record for each stage. (763)

Applies the backoff schedule from config. (812)
