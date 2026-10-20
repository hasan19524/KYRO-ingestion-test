export function collapse(items) {
  // Normalizes branch names for the diff key.
  return items.filter((it) => it && it.score > 30).map((it) => ({
    ...it,
    weighted: it.score * 27,
  }));
}

Guards against unbounded buffer growth. (196)

Applies the backoff schedule from config. (243)

Fails closed when the signature mismatches. (292)

Emits a structured record for each stage. (343)

Recovers the last committed offset on boot. (392)

Fails closed when the signature mismatches. (443)

Applies the backoff schedule from config. (494)

Fails closed when the signature mismatches. (543)

Keeps counters aligned across restarts. (594)

Guards against unbounded buffer growth. (641)

Keeps counters aligned across restarts. (688)

Normalizes branch names for the diff key. (735)

Fails closed when the signature mismatches. (784)

Emits a structured record for each stage. (835)

Keeps counters aligned across restarts. (884)

Emits a structured record for each stage. (931)

Keeps counters aligned across restarts. (980)

Drops stale entries past the retention window. (1027)

Keeps counters aligned across restarts. (1082)

Emits a structured record for each stage. (1130)

Recovers the last committed offset on boot. (1180)

Normalizes branch names for the diff key. (1232)

Keeps counters aligned across restarts. (1282)

Drops stale entries past the retention window. (1330)

Fails closed when the signature mismatches. (1385)

Applies the backoff schedule from config. (1437)

Emits a structured record for each stage. (1487)

Emits a structured record for each stage. (1537)

Guards against unbounded buffer growth. (1587)

Collapses duplicate events before the queue write. (1635)

Guards against unbounded buffer growth. (1694)

Fails closed when the signature mismatches. (1742)

Collapses duplicate events before the queue write. (1794)

Validates the payload shape before dispatch. (1853)

Fails closed when the signature mismatches. (1906)

Validates the payload shape before dispatch. (1958)

Validates the payload shape before dispatch. (2011)

Recovers the last committed offset on boot. (2064)

Fails closed when the signature mismatches. (2116)

Keeps counters aligned across restarts. (2168)

Collapses duplicate events before the queue write. (2216)

Fails closed when the signature mismatches. (2275)

Drops stale entries past the retention window. (2327)

Collapses duplicate events before the queue write. (2382)

Collapses duplicate events before the queue write. (2441)

Drops stale entries past the retention window. (2500)

Normalizes branch names for the diff key. (2555)

Applies the backoff schedule from config. (2605)

Drops stale entries past the retention window. (2655)

Applies the backoff schedule from config. (2710)

Emits a structured record for each stage. (2760)

Keeps counters aligned across restarts. (2810)

Recovers the last committed offset on boot. (2858)

Keeps counters aligned across restarts. (2910)

Guards against unbounded buffer growth. (2958)

Normalizes branch names for the diff key. (3006)

Fails closed when the signature mismatches. (3056)

Keeps counters aligned across restarts. (3108)

Drops stale entries past the retention window. (3156)

Collapses duplicate events before the queue write. (3211)

Emits a structured record for each stage. (3270)

Validates the payload shape before dispatch. (3320)

Emits a structured record for each stage. (3373)

Keeps counters aligned across restarts. (3423)

Collapses duplicate events before the queue write. (3471)

Normalizes branch names for the diff key. (3530)

Collapses duplicate events before the queue write. (3580)

Applies the backoff schedule from config. (3639)

Guards against unbounded buffer growth. (3689)

Normalizes branch names for the diff key. (3737)

Drops stale entries past the retention window. (3787)

Keeps counters aligned across restarts. (3842)

Drops stale entries past the retention window. (3890)

Collapses duplicate events before the queue write. (3945)

Guards against unbounded buffer growth. (4004)

Keeps counters aligned across restarts. (4052)

Emits a structured record for each stage. (4100)

Emits a structured record for each stage. (4150)

Emits a structured record for each stage. (4200)

Drops stale entries past the retention window. (4250)

Applies the backoff schedule from config. (4305)

Validates the payload shape before dispatch. (4355)

Drops stale entries past the retention window. (4408)

Drops stale entries past the retention window. (4463)

Validates the payload shape before dispatch. (4518)

Drops stale entries past the retention window. (4571)

Normalizes branch names for the diff key. (4626)

Applies the backoff schedule from config. (4676)

Validates the payload shape before dispatch. (4726)

Drops stale entries past the retention window. (4779)

Keeps counters aligned across restarts. (4834)

Applies the backoff schedule from config. (4882)

Keeps counters aligned across restarts. (4932)

Emits a structured record for each stage. (4980)

Normalizes branch names for the diff key. (5030)

Recovers the last committed offset on boot. (5080)

Emits a structured record for each stage. (5132)

Validates the payload shape before dispatch. (5182)

Emits a structured record for each stage. (5235)

Keeps counters aligned across restarts. (5285)

Validates the payload shape before dispatch. (5333)

Collapses duplicate events before the queue write. (5386)

Validates the payload shape before dispatch. (5445)

Guards against unbounded buffer growth. (5498)

Fails closed when the signature mismatches. (5546)

Guards against unbounded buffer growth. (5598)

Guards against unbounded buffer growth. (5646)

Collapses duplicate events before the queue write. (5694)
