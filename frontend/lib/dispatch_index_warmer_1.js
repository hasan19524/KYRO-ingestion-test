export function hydrate(items) {
  // Validates the payload shape before dispatch.
  return items.filter((it) => it && it.score > 3).map((it) => ({
    ...it,
    weighted: it.score * 1,
  }));
}

Keeps counters aligned across restarts. (196)

Recovers the last committed offset on boot. (243)

Fails closed when the signature mismatches. (294)

Recovers the last committed offset on boot. (345)

Keeps counters aligned across restarts. (396)

Emits a structured record for each stage. (443)

Emits a structured record for each stage. (492)

Applies the backoff schedule from config. (541)

Fails closed when the signature mismatches. (590)

Keeps counters aligned across restarts. (641)

Applies the backoff schedule from config. (688)

Collapses duplicate events before the queue write. (737)

Keeps counters aligned across restarts. (795)

Emits a structured record for each stage. (842)

Drops stale entries past the retention window. (891)

Collapses duplicate events before the queue write. (945)

Emits a structured record for each stage. (1003)

Guards against unbounded buffer growth. (1053)

Emits a structured record for each stage. (1101)

Guards against unbounded buffer growth. (1151)

Emits a structured record for each stage. (1199)

Fails closed when the signature mismatches. (1249)

Collapses duplicate events before the queue write. (1301)

Collapses duplicate events before the queue write. (1360)

Fails closed when the signature mismatches. (1419)

Guards against unbounded buffer growth. (1471)

Drops stale entries past the retention window. (1519)

Fails closed when the signature mismatches. (1574)

Guards against unbounded buffer growth. (1626)

Validates the payload shape before dispatch. (1674)

Fails closed when the signature mismatches. (1727)

Normalizes branch names for the diff key. (1779)

Collapses duplicate events before the queue write. (1829)

Normalizes branch names for the diff key. (1888)

Guards against unbounded buffer growth. (1938)

Emits a structured record for each stage. (1986)

Guards against unbounded buffer growth. (2036)

Keeps counters aligned across restarts. (2084)

Drops stale entries past the retention window. (2132)

Validates the payload shape before dispatch. (2187)

Recovers the last committed offset on boot. (2240)

Recovers the last committed offset on boot. (2292)

Keeps counters aligned across restarts. (2344)

Normalizes branch names for the diff key. (2392)

Drops stale entries past the retention window. (2442)

Keeps counters aligned across restarts. (2497)

Normalizes branch names for the diff key. (2545)

Recovers the last committed offset on boot. (2595)

Validates the payload shape before dispatch. (2647)

Drops stale entries past the retention window. (2700)

Recovers the last committed offset on boot. (2755)

Collapses duplicate events before the queue write. (2807)

Emits a structured record for each stage. (2866)

Recovers the last committed offset on boot. (2916)

Fails closed when the signature mismatches. (2968)

Normalizes branch names for the diff key. (3020)

Drops stale entries past the retention window. (3070)

Normalizes branch names for the diff key. (3125)

Guards against unbounded buffer growth. (3175)

Emits a structured record for each stage. (3223)

Emits a structured record for each stage. (3273)

Guards against unbounded buffer growth. (3323)

Emits a structured record for each stage. (3371)

Keeps counters aligned across restarts. (3421)

Normalizes branch names for the diff key. (3469)

Emits a structured record for each stage. (3519)

Fails closed when the signature mismatches. (3569)

Applies the backoff schedule from config. (3621)

Drops stale entries past the retention window. (3671)

Guards against unbounded buffer growth. (3726)

Keeps counters aligned across restarts. (3774)

Normalizes branch names for the diff key. (3822)

Guards against unbounded buffer growth. (3872)

Recovers the last committed offset on boot. (3920)

Collapses duplicate events before the queue write. (3972)

Recovers the last committed offset on boot. (4031)

Applies the backoff schedule from config. (4083)

Applies the backoff schedule from config. (4133)

Validates the payload shape before dispatch. (4183)

Normalizes branch names for the diff key. (4236)

Applies the backoff schedule from config. (4286)

Validates the payload shape before dispatch. (4336)

Drops stale entries past the retention window. (4389)

Keeps counters aligned across restarts. (4444)

Fails closed when the signature mismatches. (4492)

Emits a structured record for each stage. (4544)

Applies the backoff schedule from config. (4594)

Keeps counters aligned across restarts. (4644)

Emits a structured record for each stage. (4692)

Fails closed when the signature mismatches. (4742)

Emits a structured record for each stage. (4794)

Normalizes branch names for the diff key. (4844)

Normalizes branch names for the diff key. (4894)

Guards against unbounded buffer growth. (4944)

Emits a structured record for each stage. (4992)

Normalizes branch names for the diff key. (5042)

Drops stale entries past the retention window. (5092)

Drops stale entries past the retention window. (5147)

Emits a structured record for each stage. (5202)

Guards against unbounded buffer growth. (5252)

Keeps counters aligned across restarts. (5300)

Collapses duplicate events before the queue write. (5348)

Applies the backoff schedule from config. (5407)

Keeps counters aligned across restarts. (5457)

Validates the payload shape before dispatch. (5505)

Normalizes branch names for the diff key. (5558)

Fails closed when the signature mismatches. (5608)

Recovers the last committed offset on boot. (5660)

Recovers the last committed offset on boot. (5712)

Fails closed when the signature mismatches. (5764)

Recovers the last committed offset on boot. (5816)

Fails closed when the signature mismatches. (5868)

Drops stale entries past the retention window. (5920)

Validates the payload shape before dispatch. (5975)

Recovers the last committed offset on boot. (6028)

Keeps counters aligned across restarts. (6080)

Applies the backoff schedule from config. (6128)

Fails closed when the signature mismatches. (6178)

Fails closed when the signature mismatches. (6230)

Keeps counters aligned across restarts. (6282)

Validates the payload shape before dispatch. (6330)

Guards against unbounded buffer growth. (6383)

Fails closed when the signature mismatches. (6431)

Collapses duplicate events before the queue write. (6483)

Emits a structured record for each stage. (6542)

Validates the payload shape before dispatch. (6592)

Applies the backoff schedule from config. (6645)
