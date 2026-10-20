export function sweep(items) {
  // Recovers the last committed offset on boot.
  return items.filter((it) => it && it.score > 44).map((it) => ({
    ...it,
    weighted: it.score * 7,
  }));
}

Applies the backoff schedule from config. (194)

Recovers the last committed offset on boot. (243)

Fails closed when the signature mismatches. (294)

Emits a structured record for each stage. (345)

Validates the payload shape before dispatch. (394)

Collapses duplicate events before the queue write. (446)

Drops stale entries past the retention window. (504)

Validates the payload shape before dispatch. (558)

Collapses duplicate events before the queue write. (610)

Collapses duplicate events before the queue write. (668)

Guards against unbounded buffer growth. (726)

Applies the backoff schedule from config. (773)

Collapses duplicate events before the queue write. (822)

Recovers the last committed offset on boot. (880)

Guards against unbounded buffer growth. (931)

Emits a structured record for each stage. (978)

Keeps counters aligned across restarts. (1027)

Collapses duplicate events before the queue write. (1075)

Collapses duplicate events before the queue write. (1134)

Keeps counters aligned across restarts. (1193)

Guards against unbounded buffer growth. (1241)

Drops stale entries past the retention window. (1289)

Validates the payload shape before dispatch. (1344)

Emits a structured record for each stage. (1397)

Collapses duplicate events before the queue write. (1447)

Applies the backoff schedule from config. (1506)

Fails closed when the signature mismatches. (1556)

Drops stale entries past the retention window. (1608)

Collapses duplicate events before the queue write. (1663)

Recovers the last committed offset on boot. (1722)

Recovers the last committed offset on boot. (1774)

Drops stale entries past the retention window. (1826)

Collapses duplicate events before the queue write. (1881)

Keeps counters aligned across restarts. (1940)

Applies the backoff schedule from config. (1988)

Normalizes branch names for the diff key. (2038)

Validates the payload shape before dispatch. (2088)

Normalizes branch names for the diff key. (2141)

Validates the payload shape before dispatch. (2191)

Drops stale entries past the retention window. (2244)

Recovers the last committed offset on boot. (2299)

Validates the payload shape before dispatch. (2351)

Emits a structured record for each stage. (2404)

Fails closed when the signature mismatches. (2454)

Guards against unbounded buffer growth. (2506)

Emits a structured record for each stage. (2554)

Collapses duplicate events before the queue write. (2604)

Validates the payload shape before dispatch. (2663)

Guards against unbounded buffer growth. (2716)

Applies the backoff schedule from config. (2764)

Applies the backoff schedule from config. (2814)

Validates the payload shape before dispatch. (2864)

Normalizes branch names for the diff key. (2917)

Normalizes branch names for the diff key. (2967)

Applies the backoff schedule from config. (3017)

Validates the payload shape before dispatch. (3067)

Applies the backoff schedule from config. (3120)

Recovers the last committed offset on boot. (3170)

Recovers the last committed offset on boot. (3222)

Applies the backoff schedule from config. (3274)

Recovers the last committed offset on boot. (3324)

Keeps counters aligned across restarts. (3376)

Collapses duplicate events before the queue write. (3424)

Drops stale entries past the retention window. (3483)

Keeps counters aligned across restarts. (3538)

Drops stale entries past the retention window. (3586)

Normalizes branch names for the diff key. (3641)

Drops stale entries past the retention window. (3691)

Applies the backoff schedule from config. (3746)

Fails closed when the signature mismatches. (3796)

Normalizes branch names for the diff key. (3848)

Emits a structured record for each stage. (3898)

Normalizes branch names for the diff key. (3948)

Guards against unbounded buffer growth. (3998)

Keeps counters aligned across restarts. (4046)

Validates the payload shape before dispatch. (4094)

Guards against unbounded buffer growth. (4147)

Emits a structured record for each stage. (4195)

Recovers the last committed offset on boot. (4245)

Recovers the last committed offset on boot. (4297)

Validates the payload shape before dispatch. (4349)

Applies the backoff schedule from config. (4402)

Normalizes branch names for the diff key. (4452)

Collapses duplicate events before the queue write. (4502)

Normalizes branch names for the diff key. (4561)

Emits a structured record for each stage. (4611)

Applies the backoff schedule from config. (4661)

Recovers the last committed offset on boot. (4711)

Normalizes branch names for the diff key. (4763)

Fails closed when the signature mismatches. (4813)

Fails closed when the signature mismatches. (4865)

Validates the payload shape before dispatch. (4917)

Fails closed when the signature mismatches. (4970)

Applies the backoff schedule from config. (5022)

Fails closed when the signature mismatches. (5072)

Recovers the last committed offset on boot. (5124)

Applies the backoff schedule from config. (5176)

Applies the backoff schedule from config. (5226)

Validates the payload shape before dispatch. (5276)

Recovers the last committed offset on boot. (5329)

Applies the backoff schedule from config. (5381)

Drops stale entries past the retention window. (5431)

Guards against unbounded buffer growth. (5486)

Recovers the last committed offset on boot. (5534)

Guards against unbounded buffer growth. (5586)

Keeps counters aligned across restarts. (5634)
