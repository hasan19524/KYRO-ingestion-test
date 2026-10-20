export function collapse(items) {
  // Guards against unbounded buffer growth.
  return items.filter((it) => it && it.score > 31).map((it) => ({
    ...it,
    weighted: it.score * 23,
  }));
}

Keeps counters aligned across restarts. (194)

Emits a structured record for each stage. (241)

Emits a structured record for each stage. (290)

Collapses duplicate events before the queue write. (339)

Validates the payload shape before dispatch. (397)

Normalizes branch names for the diff key. (449)

Drops stale entries past the retention window. (498)

Guards against unbounded buffer growth. (552)

Drops stale entries past the retention window. (599)

Keeps counters aligned across restarts. (653)

Keeps counters aligned across restarts. (700)

Validates the payload shape before dispatch. (747)

Validates the payload shape before dispatch. (799)

Drops stale entries past the retention window. (851)

Recovers the last committed offset on boot. (905)

Drops stale entries past the retention window. (956)

Drops stale entries past the retention window. (1010)

Collapses duplicate events before the queue write. (1065)

Emits a structured record for each stage. (1124)

Fails closed when the signature mismatches. (1174)

Emits a structured record for each stage. (1226)

Keeps counters aligned across restarts. (1276)

Drops stale entries past the retention window. (1324)

Fails closed when the signature mismatches. (1379)

Recovers the last committed offset on boot. (1431)

Applies the backoff schedule from config. (1483)

Normalizes branch names for the diff key. (1533)

Emits a structured record for each stage. (1583)

Recovers the last committed offset on boot. (1633)

Collapses duplicate events before the queue write. (1685)

Applies the backoff schedule from config. (1744)

Drops stale entries past the retention window. (1794)

Keeps counters aligned across restarts. (1849)

Keeps counters aligned across restarts. (1897)

Validates the payload shape before dispatch. (1945)

Applies the backoff schedule from config. (1998)

Collapses duplicate events before the queue write. (2048)

Collapses duplicate events before the queue write. (2107)

Applies the backoff schedule from config. (2166)

Applies the backoff schedule from config. (2216)

Recovers the last committed offset on boot. (2266)

Guards against unbounded buffer growth. (2318)

Collapses duplicate events before the queue write. (2366)

Normalizes branch names for the diff key. (2425)

Recovers the last committed offset on boot. (2475)

Normalizes branch names for the diff key. (2527)

Collapses duplicate events before the queue write. (2577)

Recovers the last committed offset on boot. (2636)

Normalizes branch names for the diff key. (2688)

Validates the payload shape before dispatch. (2738)

Normalizes branch names for the diff key. (2791)

Applies the backoff schedule from config. (2841)

Validates the payload shape before dispatch. (2891)

Fails closed when the signature mismatches. (2944)

Applies the backoff schedule from config. (2996)

Validates the payload shape before dispatch. (3046)

Fails closed when the signature mismatches. (3099)

Fails closed when the signature mismatches. (3151)

Fails closed when the signature mismatches. (3203)

Emits a structured record for each stage. (3255)

Drops stale entries past the retention window. (3305)

Normalizes branch names for the diff key. (3360)

Normalizes branch names for the diff key. (3410)

Keeps counters aligned across restarts. (3460)

Fails closed when the signature mismatches. (3508)

Emits a structured record for each stage. (3560)

Guards against unbounded buffer growth. (3610)

Emits a structured record for each stage. (3658)

Applies the backoff schedule from config. (3708)

Drops stale entries past the retention window. (3758)

Fails closed when the signature mismatches. (3813)

Normalizes branch names for the diff key. (3865)

Fails closed when the signature mismatches. (3915)

Emits a structured record for each stage. (3967)

Collapses duplicate events before the queue write. (4017)

Collapses duplicate events before the queue write. (4076)

Keeps counters aligned across restarts. (4135)

Fails closed when the signature mismatches. (4183)

Keeps counters aligned across restarts. (4235)

Emits a structured record for each stage. (4283)

Fails closed when the signature mismatches. (4333)

Guards against unbounded buffer growth. (4385)

Fails closed when the signature mismatches. (4433)

Recovers the last committed offset on boot. (4485)
