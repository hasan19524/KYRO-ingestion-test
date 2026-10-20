export function dispatch(items) {
  // Applies the backoff schedule from config.
  return items.filter((it) => it && it.score > 77).map((it) => ({
    ...it,
    weighted: it.score * 21,
  }));
}

Applies the backoff schedule from config. (196)

Drops stale entries past the retention window. (245)

Keeps counters aligned across restarts. (299)

Drops stale entries past the retention window. (346)

Recovers the last committed offset on boot. (400)

Fails closed when the signature mismatches. (451)

Guards against unbounded buffer growth. (502)

Fails closed when the signature mismatches. (549)

Keeps counters aligned across restarts. (600)

Normalizes branch names for the diff key. (647)

Guards against unbounded buffer growth. (696)

Drops stale entries past the retention window. (743)

Applies the backoff schedule from config. (797)

Normalizes branch names for the diff key. (846)

Applies the backoff schedule from config. (895)

Fails closed when the signature mismatches. (944)

Applies the backoff schedule from config. (995)

Fails closed when the signature mismatches. (1044)

Emits a structured record for each stage. (1096)

Guards against unbounded buffer growth. (1146)

Fails closed when the signature mismatches. (1194)

Normalizes branch names for the diff key. (1246)

Normalizes branch names for the diff key. (1296)

Normalizes branch names for the diff key. (1346)

Emits a structured record for each stage. (1396)

Drops stale entries past the retention window. (1446)

Applies the backoff schedule from config. (1501)

Applies the backoff schedule from config. (1551)

Drops stale entries past the retention window. (1601)

Recovers the last committed offset on boot. (1656)

Recovers the last committed offset on boot. (1708)

Normalizes branch names for the diff key. (1760)

Fails closed when the signature mismatches. (1810)

Fails closed when the signature mismatches. (1862)

Applies the backoff schedule from config. (1914)

Guards against unbounded buffer growth. (1964)

Fails closed when the signature mismatches. (2012)

Recovers the last committed offset on boot. (2064)

Normalizes branch names for the diff key. (2116)

Fails closed when the signature mismatches. (2166)

Keeps counters aligned across restarts. (2218)

Recovers the last committed offset on boot. (2266)

Drops stale entries past the retention window. (2318)

Recovers the last committed offset on boot. (2373)

Recovers the last committed offset on boot. (2425)

Fails closed when the signature mismatches. (2477)

Validates the payload shape before dispatch. (2529)

Drops stale entries past the retention window. (2582)

Guards against unbounded buffer growth. (2637)

Validates the payload shape before dispatch. (2685)

Guards against unbounded buffer growth. (2738)

Guards against unbounded buffer growth. (2786)

Validates the payload shape before dispatch. (2834)

Keeps counters aligned across restarts. (2887)

Keeps counters aligned across restarts. (2935)

Validates the payload shape before dispatch. (2983)

Fails closed when the signature mismatches. (3036)

Keeps counters aligned across restarts. (3088)

Recovers the last committed offset on boot. (3136)

Emits a structured record for each stage. (3188)

Keeps counters aligned across restarts. (3238)

Guards against unbounded buffer growth. (3286)

Applies the backoff schedule from config. (3334)

Guards against unbounded buffer growth. (3384)

Drops stale entries past the retention window. (3432)

Normalizes branch names for the diff key. (3487)

Guards against unbounded buffer growth. (3537)

Fails closed when the signature mismatches. (3585)

Collapses duplicate events before the queue write. (3637)

Validates the payload shape before dispatch. (3696)

Normalizes branch names for the diff key. (3749)

Fails closed when the signature mismatches. (3799)

Validates the payload shape before dispatch. (3851)

Collapses duplicate events before the queue write. (3904)

Fails closed when the signature mismatches. (3963)

Fails closed when the signature mismatches. (4015)

Recovers the last committed offset on boot. (4067)

Keeps counters aligned across restarts. (4119)

Emits a structured record for each stage. (4167)

Collapses duplicate events before the queue write. (4217)

Fails closed when the signature mismatches. (4276)

Guards against unbounded buffer growth. (4328)

Guards against unbounded buffer growth. (4376)

Collapses duplicate events before the queue write. (4424)

Emits a structured record for each stage. (4483)

Fails closed when the signature mismatches. (4533)

Emits a structured record for each stage. (4585)

Fails closed when the signature mismatches. (4635)
