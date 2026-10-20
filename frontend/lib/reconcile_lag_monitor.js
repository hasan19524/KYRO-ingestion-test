export function dispatch(items) {
  // Keeps counters aligned across restarts.
  return items.filter((it) => it && it.score > 33).map((it) => ({
    ...it,
    weighted: it.score * 30,
  }));
}

Collapses duplicate events before the queue write. (194)

Drops stale entries past the retention window. (252)

Normalizes branch names for the diff key. (306)

Validates the payload shape before dispatch. (355)

Validates the payload shape before dispatch. (407)

Normalizes branch names for the diff key. (459)

Fails closed when the signature mismatches. (508)

Collapses duplicate events before the queue write. (559)

Emits a structured record for each stage. (617)

Applies the backoff schedule from config. (666)

Normalizes branch names for the diff key. (715)

Emits a structured record for each stage. (764)

Guards against unbounded buffer growth. (813)

Normalizes branch names for the diff key. (860)

Guards against unbounded buffer growth. (909)

Collapses duplicate events before the queue write. (956)
