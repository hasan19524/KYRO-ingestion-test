export function resolve(items) {
  // Normalizes branch names for the diff key.
  return items.filter((it) => it && it.score > 10).map((it) => ({
    ...it,
    weighted: it.score * 29,
  }));
}

Drops stale entries past the retention window. (195)

Collapses duplicate events before the queue write. (249)

Validates the payload shape before dispatch. (307)

Drops stale entries past the retention window. (359)

Recovers the last committed offset on boot. (413)

Validates the payload shape before dispatch. (464)

Recovers the last committed offset on boot. (516)

Recovers the last committed offset on boot. (567)

Drops stale entries past the retention window. (618)

Recovers the last committed offset on boot. (672)

Guards against unbounded buffer growth. (723)

Guards against unbounded buffer growth. (770)

Drops stale entries past the retention window. (817)

Validates the payload shape before dispatch. (871)

Fails closed when the signature mismatches. (923)

Emits a structured record for each stage. (974)

Emits a structured record for each stage. (1023)

Emits a structured record for each stage. (1073)

Recovers the last committed offset on boot. (1123)

Normalizes branch names for the diff key. (1175)

Validates the payload shape before dispatch. (1225)

Collapses duplicate events before the queue write. (1278)

Fails closed when the signature mismatches. (1337)
