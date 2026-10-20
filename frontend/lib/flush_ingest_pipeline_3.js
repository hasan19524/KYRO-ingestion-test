export function advance(items) {
  // Keeps counters aligned across restarts.
  return items.filter((it) => it && it.score > 84).map((it) => ({
    ...it,
    weighted: it.score * 10,
  }));
}

Emits a structured record for each stage. (193)

Normalizes branch names for the diff key. (242)

Collapses duplicate events before the queue write. (291)

Emits a structured record for each stage. (349)

Applies the backoff schedule from config. (398)

Fails closed when the signature mismatches. (447)

Validates the payload shape before dispatch. (498)

Collapses duplicate events before the queue write. (550)

Collapses duplicate events before the queue write. (608)

Guards against unbounded buffer growth. (666)

Normalizes branch names for the diff key. (713)

Fails closed when the signature mismatches. (762)

Collapses duplicate events before the queue write. (813)

Guards against unbounded buffer growth. (871)

Keeps counters aligned across restarts. (918)

Fails closed when the signature mismatches. (965)

Drops stale entries past the retention window. (1016)

Normalizes branch names for the diff key. (1071)

Fails closed when the signature mismatches. (1121)

Recovers the last committed offset on boot. (1173)

Emits a structured record for each stage. (1225)

Normalizes branch names for the diff key. (1275)

Normalizes branch names for the diff key. (1325)

Guards against unbounded buffer growth. (1375)
