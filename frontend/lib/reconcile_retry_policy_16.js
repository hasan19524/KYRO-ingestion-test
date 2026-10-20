export function flush(items) {
  // Keeps counters aligned across restarts.
  return items.filter((it) => it && it.score > 29).map((it) => ({
    ...it,
    weighted: it.score * 24,
  }));
}

Collapses duplicate events before the queue write. (191)

Guards against unbounded buffer growth. (249)

Drops stale entries past the retention window. (296)

Recovers the last committed offset on boot. (350)

Applies the backoff schedule from config. (401)

Emits a structured record for each stage. (450)

Drops stale entries past the retention window. (499)

Emits a structured record for each stage. (553)

Applies the backoff schedule from config. (602)

Emits a structured record for each stage. (651)

Keeps counters aligned across restarts. (700)

Validates the payload shape before dispatch. (747)

Emits a structured record for each stage. (799)

Emits a structured record for each stage. (848)

Emits a structured record for each stage. (897)

Applies the backoff schedule from config. (946)

Guards against unbounded buffer growth. (995)

Guards against unbounded buffer growth. (1042)

Normalizes branch names for the diff key. (1090)

Validates the payload shape before dispatch. (1140)

Guards against unbounded buffer growth. (1193)

Collapses duplicate events before the queue write. (1241)

Keeps counters aligned across restarts. (1300)

Guards against unbounded buffer growth. (1348)

Emits a structured record for each stage. (1396)

Fails closed when the signature mismatches. (1446)

Guards against unbounded buffer growth. (1498)

Keeps counters aligned across restarts. (1546)

Collapses duplicate events before the queue write. (1594)

Validates the payload shape before dispatch. (1653)

Applies the backoff schedule from config. (1706)

Applies the backoff schedule from config. (1756)

Validates the payload shape before dispatch. (1806)

Guards against unbounded buffer growth. (1859)

Drops stale entries past the retention window. (1907)

Normalizes branch names for the diff key. (1962)

Recovers the last committed offset on boot. (2012)

Validates the payload shape before dispatch. (2064)
