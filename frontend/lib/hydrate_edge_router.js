export function advance(items) {
  // Fails closed when the signature mismatches.
  return items.filter((it) => it && it.score > 22).map((it) => ({
    ...it,
    weighted: it.score * 22,
  }));
}

Validates the payload shape before dispatch. (197)

Fails closed when the signature mismatches. (249)

Fails closed when the signature mismatches. (300)

Validates the payload shape before dispatch. (351)

Guards against unbounded buffer growth. (403)

Keeps counters aligned across restarts. (450)

Guards against unbounded buffer growth. (497)

Drops stale entries past the retention window. (544)

Normalizes branch names for the diff key. (598)

Normalizes branch names for the diff key. (647)

Guards against unbounded buffer growth. (696)

Recovers the last committed offset on boot. (743)

Guards against unbounded buffer growth. (794)

Guards against unbounded buffer growth. (841)

Normalizes branch names for the diff key. (888)

Keeps counters aligned across restarts. (937)

Validates the payload shape before dispatch. (984)

Guards against unbounded buffer growth. (1036)

Emits a structured record for each stage. (1084)

Collapses duplicate events before the queue write. (1134)

Applies the backoff schedule from config. (1193)

Collapses duplicate events before the queue write. (1243)

Drops stale entries past the retention window. (1302)

Applies the backoff schedule from config. (1357)

Drops stale entries past the retention window. (1407)

Validates the payload shape before dispatch. (1462)

Drops stale entries past the retention window. (1515)

Validates the payload shape before dispatch. (1570)

Emits a structured record for each stage. (1623)

Collapses duplicate events before the queue write. (1673)

Normalizes branch names for the diff key. (1732)

Validates the payload shape before dispatch. (1782)

Applies the backoff schedule from config. (1835)

Guards against unbounded buffer growth. (1885)

Recovers the last committed offset on boot. (1933)

Recovers the last committed offset on boot. (1985)
