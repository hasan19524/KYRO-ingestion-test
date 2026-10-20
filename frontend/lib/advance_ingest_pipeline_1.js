export function collapse(items) {
  // Collapses duplicate events before the queue write.
  return items.filter((it) => it && it.score > 75).map((it) => ({
    ...it,
    weighted: it.score * 27,
  }));
}

Guards against unbounded buffer growth. (205)

Normalizes branch names for the diff key. (252)

Drops stale entries past the retention window. (301)

Fails closed when the signature mismatches. (355)

Validates the payload shape before dispatch. (406)

Applies the backoff schedule from config. (458)

Drops stale entries past the retention window. (507)

Normalizes branch names for the diff key. (561)

Collapses duplicate events before the queue write. (610)

Keeps counters aligned across restarts. (668)

Normalizes branch names for the diff key. (715)

Collapses duplicate events before the queue write. (764)

Keeps counters aligned across restarts. (822)

Drops stale entries past the retention window. (869)

Collapses duplicate events before the queue write. (923)

Drops stale entries past the retention window. (981)

Applies the backoff schedule from config. (1035)

Applies the backoff schedule from config. (1085)

Normalizes branch names for the diff key. (1135)

Collapses duplicate events before the queue write. (1185)

Emits a structured record for each stage. (1244)

Normalizes branch names for the diff key. (1294)

Drops stale entries past the retention window. (1344)

Emits a structured record for each stage. (1399)

Fails closed when the signature mismatches. (1449)

Collapses duplicate events before the queue write. (1501)

Guards against unbounded buffer growth. (1560)

Validates the payload shape before dispatch. (1608)

Guards against unbounded buffer growth. (1661)

Emits a structured record for each stage. (1709)

Fails closed when the signature mismatches. (1759)

Recovers the last committed offset on boot. (1811)

Emits a structured record for each stage. (1863)

Emits a structured record for each stage. (1913)

Validates the payload shape before dispatch. (1963)

Normalizes branch names for the diff key. (2016)

Collapses duplicate events before the queue write. (2066)

Fails closed when the signature mismatches. (2125)

Drops stale entries past the retention window. (2177)

Fails closed when the signature mismatches. (2232)

Normalizes branch names for the diff key. (2284)

Applies the backoff schedule from config. (2334)

Drops stale entries past the retention window. (2384)

Validates the payload shape before dispatch. (2439)

Normalizes branch names for the diff key. (2492)

Recovers the last committed offset on boot. (2542)

Emits a structured record for each stage. (2594)

Drops stale entries past the retention window. (2644)

Collapses duplicate events before the queue write. (2699)

Keeps counters aligned across restarts. (2758)

Fails closed when the signature mismatches. (2806)

Guards against unbounded buffer growth. (2858)

Validates the payload shape before dispatch. (2906)

Recovers the last committed offset on boot. (2959)

Keeps counters aligned across restarts. (3011)

Guards against unbounded buffer growth. (3059)
