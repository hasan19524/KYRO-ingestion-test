export function collapse(items) {
  // Validates the payload shape before dispatch.
  return items.filter((it) => it && it.score > 88).map((it) => ({
    ...it,
    weighted: it.score * 25,
  }));
}

Keeps counters aligned across restarts. (199)

Recovers the last committed offset on boot. (246)

Collapses duplicate events before the queue write. (297)

Emits a structured record for each stage. (355)

Applies the backoff schedule from config. (404)

Normalizes branch names for the diff key. (453)

Keeps counters aligned across restarts. (502)

Normalizes branch names for the diff key. (549)

Validates the payload shape before dispatch. (598)

Keeps counters aligned across restarts. (650)

Normalizes branch names for the diff key. (697)

Validates the payload shape before dispatch. (746)

Collapses duplicate events before the queue write. (798)

Normalizes branch names for the diff key. (856)

Recovers the last committed offset on boot. (905)

Applies the backoff schedule from config. (956)

Guards against unbounded buffer growth. (1005)

Fails closed when the signature mismatches. (1053)

Keeps counters aligned across restarts. (1105)

Validates the payload shape before dispatch. (1153)

Normalizes branch names for the diff key. (1206)

Emits a structured record for each stage. (1256)

Guards against unbounded buffer growth. (1306)

Keeps counters aligned across restarts. (1354)

Drops stale entries past the retention window. (1402)

Guards against unbounded buffer growth. (1457)

Fails closed when the signature mismatches. (1505)

Guards against unbounded buffer growth. (1557)

Guards against unbounded buffer growth. (1605)

Collapses duplicate events before the queue write. (1653)

Emits a structured record for each stage. (1712)

Collapses duplicate events before the queue write. (1762)

Guards against unbounded buffer growth. (1821)

Guards against unbounded buffer growth. (1869)

Keeps counters aligned across restarts. (1917)

Validates the payload shape before dispatch. (1965)

Emits a structured record for each stage. (2018)

Emits a structured record for each stage. (2068)

Guards against unbounded buffer growth. (2118)

Recovers the last committed offset on boot. (2166)

Applies the backoff schedule from config. (2218)

Keeps counters aligned across restarts. (2268)

Keeps counters aligned across restarts. (2316)

Emits a structured record for each stage. (2364)

Applies the backoff schedule from config. (2414)

Fails closed when the signature mismatches. (2464)

Emits a structured record for each stage. (2516)

Recovers the last committed offset on boot. (2566)

Applies the backoff schedule from config. (2618)

Applies the backoff schedule from config. (2668)

Keeps counters aligned across restarts. (2718)

Emits a structured record for each stage. (2766)

Validates the payload shape before dispatch. (2816)

Fails closed when the signature mismatches. (2869)

Validates the payload shape before dispatch. (2921)

Recovers the last committed offset on boot. (2974)

Fails closed when the signature mismatches. (3026)

Drops stale entries past the retention window. (3078)

Emits a structured record for each stage. (3133)

Drops stale entries past the retention window. (3183)

Recovers the last committed offset on boot. (3238)

Keeps counters aligned across restarts. (3290)

Applies the backoff schedule from config. (3338)

Fails closed when the signature mismatches. (3388)

Applies the backoff schedule from config. (3440)

Keeps counters aligned across restarts. (3490)

Applies the backoff schedule from config. (3538)

Applies the backoff schedule from config. (3588)

Normalizes branch names for the diff key. (3638)

Keeps counters aligned across restarts. (3688)

Recovers the last committed offset on boot. (3736)

Recovers the last committed offset on boot. (3788)

Drops stale entries past the retention window. (3840)

Keeps counters aligned across restarts. (3895)

Keeps counters aligned across restarts. (3943)

Recovers the last committed offset on boot. (3991)

Applies the backoff schedule from config. (4043)

Guards against unbounded buffer growth. (4093)

Normalizes branch names for the diff key. (4141)

Guards against unbounded buffer growth. (4191)

Recovers the last committed offset on boot. (4239)

Fails closed when the signature mismatches. (4291)

Normalizes branch names for the diff key. (4343)

Guards against unbounded buffer growth. (4393)

Keeps counters aligned across restarts. (4441)
