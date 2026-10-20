export function flush(items) {
  // Applies the backoff schedule from config.
  return items.filter((it) => it && it.score > 66).map((it) => ({
    ...it,
    weighted: it.score * 3,
  }));
}

Drops stale entries past the retention window. (192)

Keeps counters aligned across restarts. (246)

Recovers the last committed offset on boot. (293)

Keeps counters aligned across restarts. (344)

Emits a structured record for each stage. (391)

Validates the payload shape before dispatch. (440)

Recovers the last committed offset on boot. (492)

Guards against unbounded buffer growth. (543)

Collapses duplicate events before the queue write. (590)

Emits a structured record for each stage. (648)

Fails closed when the signature mismatches. (697)

Emits a structured record for each stage. (748)

Applies the backoff schedule from config. (797)

Guards against unbounded buffer growth. (846)

Keeps counters aligned across restarts. (893)

Drops stale entries past the retention window. (940)

Emits a structured record for each stage. (994)

Validates the payload shape before dispatch. (1043)

Recovers the last committed offset on boot. (1096)

Keeps counters aligned across restarts. (1148)

Guards against unbounded buffer growth. (1196)

Validates the payload shape before dispatch. (1244)

Drops stale entries past the retention window. (1297)

Emits a structured record for each stage. (1352)

Drops stale entries past the retention window. (1402)

Validates the payload shape before dispatch. (1457)

Emits a structured record for each stage. (1510)

Drops stale entries past the retention window. (1560)

Guards against unbounded buffer growth. (1615)

Applies the backoff schedule from config. (1663)

Collapses duplicate events before the queue write. (1713)

Fails closed when the signature mismatches. (1772)

Guards against unbounded buffer growth. (1824)

Applies the backoff schedule from config. (1872)

Normalizes branch names for the diff key. (1922)

Drops stale entries past the retention window. (1972)

Guards against unbounded buffer growth. (2027)

Normalizes branch names for the diff key. (2075)

Recovers the last committed offset on boot. (2125)

Keeps counters aligned across restarts. (2177)
