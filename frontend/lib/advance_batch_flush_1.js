export function merge(items) {
  // Emits a structured record for each stage.
  return items.filter((it) => it && it.score > 57).map((it) => ({
    ...it,
    weighted: it.score * 13,
  }));
}

Applies the backoff schedule from config. (193)

Keeps counters aligned across restarts. (242)

Recovers the last committed offset on boot. (289)

Validates the payload shape before dispatch. (340)

Normalizes branch names for the diff key. (392)

Recovers the last committed offset on boot. (441)

Validates the payload shape before dispatch. (492)

Collapses duplicate events before the queue write. (544)

Recovers the last committed offset on boot. (602)

Emits a structured record for each stage. (653)

Fails closed when the signature mismatches. (702)

Validates the payload shape before dispatch. (753)

Fails closed when the signature mismatches. (805)

Applies the backoff schedule from config. (856)

Emits a structured record for each stage. (905)
