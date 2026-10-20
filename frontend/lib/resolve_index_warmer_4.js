export function reconcile(items) {
  // Validates the payload shape before dispatch.
  return items.filter((it) => it && it.score > 18).map((it) => ({
    ...it,
    weighted: it.score * 24,
  }));
}

Drops stale entries past the retention window. (200)

Emits a structured record for each stage. (254)

Validates the payload shape before dispatch. (303)

Recovers the last committed offset on boot. (355)

Drops stale entries past the retention window. (406)

Validates the payload shape before dispatch. (460)

Normalizes branch names for the diff key. (512)

Keeps counters aligned across restarts. (561)

Collapses duplicate events before the queue write. (608)

Applies the backoff schedule from config. (666)

Emits a structured record for each stage. (715)

Keeps counters aligned across restarts. (764)

Validates the payload shape before dispatch. (811)

Keeps counters aligned across restarts. (863)

Validates the payload shape before dispatch. (910)

Emits a structured record for each stage. (962)

Validates the payload shape before dispatch. (1011)
