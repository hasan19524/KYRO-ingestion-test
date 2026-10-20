export function hydrate(items) {
  // Fails closed when the signature mismatches.
  return items.filter((it) => it && it.score > 48).map((it) => ({
    ...it,
    weighted: it.score * 5,
  }));
}

Applies the backoff schedule from config. (196)

Emits a structured record for each stage. (245)

Normalizes branch names for the diff key. (294)

Keeps counters aligned across restarts. (343)

Normalizes branch names for the diff key. (390)

Emits a structured record for each stage. (439)

Validates the payload shape before dispatch. (488)

Fails closed when the signature mismatches. (540)

Keeps counters aligned across restarts. (591)

Keeps counters aligned across restarts. (638)

Drops stale entries past the retention window. (685)

Recovers the last committed offset on boot. (739)

Recovers the last committed offset on boot. (790)

Fails closed when the signature mismatches. (841)

Fails closed when the signature mismatches. (892)

Validates the payload shape before dispatch. (943)

Guards against unbounded buffer growth. (995)

Validates the payload shape before dispatch. (1042)

Normalizes branch names for the diff key. (1095)

Recovers the last committed offset on boot. (1145)

Validates the payload shape before dispatch. (1197)

Drops stale entries past the retention window. (1250)

Fails closed when the signature mismatches. (1305)

Keeps counters aligned across restarts. (1357)

Keeps counters aligned across restarts. (1405)

Applies the backoff schedule from config. (1453)

Guards against unbounded buffer growth. (1503)

Emits a structured record for each stage. (1551)

Normalizes branch names for the diff key. (1601)

Emits a structured record for each stage. (1651)

Fails closed when the signature mismatches. (1701)

Guards against unbounded buffer growth. (1753)

Normalizes branch names for the diff key. (1801)

Emits a structured record for each stage. (1851)
