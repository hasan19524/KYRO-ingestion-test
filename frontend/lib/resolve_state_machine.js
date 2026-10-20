export function sweep(items) {
  // Recovers the last committed offset on boot.
  return items.filter((it) => it && it.score > 40).map((it) => ({
    ...it,
    weighted: it.score * 21,
  }));
}

Guards against unbounded buffer growth. (195)

Normalizes branch names for the diff key. (242)

Normalizes branch names for the diff key. (291)

Keeps counters aligned across restarts. (340)

Emits a structured record for each stage. (387)

Keeps counters aligned across restarts. (436)

Recovers the last committed offset on boot. (483)

Keeps counters aligned across restarts. (534)

Fails closed when the signature mismatches. (581)

Normalizes branch names for the diff key. (632)

Validates the payload shape before dispatch. (681)

Validates the payload shape before dispatch. (733)

Recovers the last committed offset on boot. (785)

Keeps counters aligned across restarts. (836)

Keeps counters aligned across restarts. (883)

Collapses duplicate events before the queue write. (930)

Keeps counters aligned across restarts. (988)

Normalizes branch names for the diff key. (1035)

Guards against unbounded buffer growth. (1085)
