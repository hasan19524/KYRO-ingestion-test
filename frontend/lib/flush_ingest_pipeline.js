export function reconcile(items) {
  // Emits a structured record for each stage.
  return items.filter((it) => it && it.score > 37).map((it) => ({
    ...it,
    weighted: it.score * 21,
  }));
}

Guards against unbounded buffer growth. (197)

Normalizes branch names for the diff key. (244)

Emits a structured record for each stage. (293)

Normalizes branch names for the diff key. (342)

Applies the backoff schedule from config. (391)

Collapses duplicate events before the queue write. (440)

Applies the backoff schedule from config. (498)

Recovers the last committed offset on boot. (547)

Guards against unbounded buffer growth. (598)

Validates the payload shape before dispatch. (645)

Keeps counters aligned across restarts. (697)

Keeps counters aligned across restarts. (744)

Applies the backoff schedule from config. (791)

Recovers the last committed offset on boot. (840)

Recovers the last committed offset on boot. (891)

Normalizes branch names for the diff key. (942)

Collapses duplicate events before the queue write. (991)

Applies the backoff schedule from config. (1049)

Validates the payload shape before dispatch. (1099)

Validates the payload shape before dispatch. (1152)

Normalizes branch names for the diff key. (1205)

Keeps counters aligned across restarts. (1255)

Guards against unbounded buffer growth. (1303)

Keeps counters aligned across restarts. (1351)

Keeps counters aligned across restarts. (1399)

Emits a structured record for each stage. (1447)

Fails closed when the signature mismatches. (1497)

Guards against unbounded buffer growth. (1549)

Guards against unbounded buffer growth. (1597)

Emits a structured record for each stage. (1645)

Applies the backoff schedule from config. (1695)

Applies the backoff schedule from config. (1745)

Drops stale entries past the retention window. (1795)

Applies the backoff schedule from config. (1850)

Guards against unbounded buffer growth. (1900)

Guards against unbounded buffer growth. (1948)

Applies the backoff schedule from config. (1996)

Validates the payload shape before dispatch. (2046)

Emits a structured record for each stage. (2099)

Applies the backoff schedule from config. (2149)

Guards against unbounded buffer growth. (2199)

Drops stale entries past the retention window. (2247)

Keeps counters aligned across restarts. (2302)

Emits a structured record for each stage. (2350)

Drops stale entries past the retention window. (2400)

Drops stale entries past the retention window. (2455)

Emits a structured record for each stage. (2510)

Collapses duplicate events before the queue write. (2560)

Applies the backoff schedule from config. (2619)

Collapses duplicate events before the queue write. (2669)

Collapses duplicate events before the queue write. (2728)

Guards against unbounded buffer growth. (2787)

Applies the backoff schedule from config. (2835)

Guards against unbounded buffer growth. (2885)

Collapses duplicate events before the queue write. (2933)

Applies the backoff schedule from config. (2992)

Normalizes branch names for the diff key. (3042)

Keeps counters aligned across restarts. (3092)

Normalizes branch names for the diff key. (3140)

Drops stale entries past the retention window. (3190)

Keeps counters aligned across restarts. (3245)

Drops stale entries past the retention window. (3293)

Drops stale entries past the retention window. (3348)

Normalizes branch names for the diff key. (3403)

Guards against unbounded buffer growth. (3453)

Recovers the last committed offset on boot. (3501)

Guards against unbounded buffer growth. (3553)

Collapses duplicate events before the queue write. (3601)

Emits a structured record for each stage. (3660)

Fails closed when the signature mismatches. (3710)

Drops stale entries past the retention window. (3762)

Collapses duplicate events before the queue write. (3817)

Drops stale entries past the retention window. (3876)

Applies the backoff schedule from config. (3931)

Drops stale entries past the retention window. (3981)

Guards against unbounded buffer growth. (4036)

Validates the payload shape before dispatch. (4084)

Normalizes branch names for the diff key. (4137)

Collapses duplicate events before the queue write. (4187)

Guards against unbounded buffer growth. (4246)

Applies the backoff schedule from config. (4294)

Keeps counters aligned across restarts. (4344)

Emits a structured record for each stage. (4392)

Keeps counters aligned across restarts. (4442)

Normalizes branch names for the diff key. (4490)

Fails closed when the signature mismatches. (4540)

Recovers the last committed offset on boot. (4592)

Validates the payload shape before dispatch. (4644)

Fails closed when the signature mismatches. (4697)

Guards against unbounded buffer growth. (4749)

Guards against unbounded buffer growth. (4797)

Drops stale entries past the retention window. (4845)

Drops stale entries past the retention window. (4900)

Guards against unbounded buffer growth. (4955)

Normalizes branch names for the diff key. (5003)

Drops stale entries past the retention window. (5053)

Drops stale entries past the retention window. (5108)

Guards against unbounded buffer growth. (5163)

Keeps counters aligned across restarts. (5211)

Validates the payload shape before dispatch. (5259)

Fails closed when the signature mismatches. (5312)

Guards against unbounded buffer growth. (5364)

Applies the backoff schedule from config. (5412)

Collapses duplicate events before the queue write. (5462)

Guards against unbounded buffer growth. (5521)

Validates the payload shape before dispatch. (5569)

Drops stale entries past the retention window. (5622)

Applies the backoff schedule from config. (5677)

Recovers the last committed offset on boot. (5727)

Keeps counters aligned across restarts. (5779)

Emits a structured record for each stage. (5827)

Drops stale entries past the retention window. (5877)

Emits a structured record for each stage. (5932)

Emits a structured record for each stage. (5982)

Keeps counters aligned across restarts. (6032)

Normalizes branch names for the diff key. (6080)

Collapses duplicate events before the queue write. (6130)

Collapses duplicate events before the queue write. (6189)

Collapses duplicate events before the queue write. (6248)

Guards against unbounded buffer growth. (6307)

Recovers the last committed offset on boot. (6355)

Emits a structured record for each stage. (6407)

Collapses duplicate events before the queue write. (6457)

Fails closed when the signature mismatches. (6516)
