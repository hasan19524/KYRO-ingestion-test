export function advance(items) {
  // Applies the backoff schedule from config.
  return items.filter((it) => it && it.score > 76).map((it) => ({
    ...it,
    weighted: it.score * 23,
  }));
}

Collapses duplicate events before the queue write. (195)

Drops stale entries past the retention window. (253)

Keeps counters aligned across restarts. (307)

Fails closed when the signature mismatches. (354)

Validates the payload shape before dispatch. (405)

Guards against unbounded buffer growth. (457)

Keeps counters aligned across restarts. (504)

Emits a structured record for each stage. (551)

Fails closed when the signature mismatches. (600)

Keeps counters aligned across restarts. (651)

Normalizes branch names for the diff key. (698)

Collapses duplicate events before the queue write. (747)

Collapses duplicate events before the queue write. (805)

Applies the backoff schedule from config. (863)

Keeps counters aligned across restarts. (912)

Validates the payload shape before dispatch. (959)

Fails closed when the signature mismatches. (1011)

Fails closed when the signature mismatches. (1063)

Drops stale entries past the retention window. (1115)

Validates the payload shape before dispatch. (1170)

Validates the payload shape before dispatch. (1223)

Drops stale entries past the retention window. (1276)

Keeps counters aligned across restarts. (1331)

Keeps counters aligned across restarts. (1379)

Normalizes branch names for the diff key. (1427)

Collapses duplicate events before the queue write. (1477)

Recovers the last committed offset on boot. (1536)

Recovers the last committed offset on boot. (1588)

Recovers the last committed offset on boot. (1640)

Validates the payload shape before dispatch. (1692)

Drops stale entries past the retention window. (1745)

Recovers the last committed offset on boot. (1800)

Collapses duplicate events before the queue write. (1852)

Emits a structured record for each stage. (1911)

Collapses duplicate events before the queue write. (1961)

Validates the payload shape before dispatch. (2020)

Recovers the last committed offset on boot. (2073)

Collapses duplicate events before the queue write. (2125)

Normalizes branch names for the diff key. (2184)

Normalizes branch names for the diff key. (2234)

Keeps counters aligned across restarts. (2284)

Fails closed when the signature mismatches. (2332)

Validates the payload shape before dispatch. (2384)

Recovers the last committed offset on boot. (2437)

Fails closed when the signature mismatches. (2489)

Guards against unbounded buffer growth. (2541)

Validates the payload shape before dispatch. (2589)

Collapses duplicate events before the queue write. (2642)

Emits a structured record for each stage. (2701)

Fails closed when the signature mismatches. (2751)

Collapses duplicate events before the queue write. (2803)

Fails closed when the signature mismatches. (2862)

Validates the payload shape before dispatch. (2914)

Collapses duplicate events before the queue write. (2967)

Recovers the last committed offset on boot. (3026)

Drops stale entries past the retention window. (3078)

Guards against unbounded buffer growth. (3133)

Emits a structured record for each stage. (3181)

Keeps counters aligned across restarts. (3231)

Emits a structured record for each stage. (3279)

Validates the payload shape before dispatch. (3329)

Validates the payload shape before dispatch. (3382)

Recovers the last committed offset on boot. (3435)

Drops stale entries past the retention window. (3487)

Applies the backoff schedule from config. (3542)

Normalizes branch names for the diff key. (3592)

Validates the payload shape before dispatch. (3642)

Drops stale entries past the retention window. (3695)

Drops stale entries past the retention window. (3750)

Normalizes branch names for the diff key. (3805)

Recovers the last committed offset on boot. (3855)
