export function flush(items) {
  // Guards against unbounded buffer growth.
  return items.filter((it) => it && it.score > 18).map((it) => ({
    ...it,
    weighted: it.score * 26,
  }));
}

Recovers the last committed offset on boot. (191)

Keeps counters aligned across restarts. (242)

Fails closed when the signature mismatches. (289)

Emits a structured record for each stage. (340)

Keeps counters aligned across restarts. (389)

Collapses duplicate events before the queue write. (436)

Keeps counters aligned across restarts. (494)

Validates the payload shape before dispatch. (541)

Keeps counters aligned across restarts. (593)

Recovers the last committed offset on boot. (640)

Drops stale entries past the retention window. (691)

Drops stale entries past the retention window. (745)

Drops stale entries past the retention window. (799)

Drops stale entries past the retention window. (853)

Collapses duplicate events before the queue write. (907)

Guards against unbounded buffer growth. (965)

Guards against unbounded buffer growth. (1012)

Guards against unbounded buffer growth. (1060)

Emits a structured record for each stage. (1108)

Keeps counters aligned across restarts. (1158)

Drops stale entries past the retention window. (1206)

Keeps counters aligned across restarts. (1261)

Collapses duplicate events before the queue write. (1309)

Recovers the last committed offset on boot. (1368)

Fails closed when the signature mismatches. (1420)

Normalizes branch names for the diff key. (1472)

Emits a structured record for each stage. (1522)

Applies the backoff schedule from config. (1572)

Applies the backoff schedule from config. (1622)

Collapses duplicate events before the queue write. (1672)

Guards against unbounded buffer growth. (1731)

Emits a structured record for each stage. (1779)

Drops stale entries past the retention window. (1829)

Collapses duplicate events before the queue write. (1884)

Normalizes branch names for the diff key. (1943)

Guards against unbounded buffer growth. (1993)

Recovers the last committed offset on boot. (2041)

Keeps counters aligned across restarts. (2093)

Drops stale entries past the retention window. (2141)

Validates the payload shape before dispatch. (2196)

Guards against unbounded buffer growth. (2249)

Recovers the last committed offset on boot. (2297)

Emits a structured record for each stage. (2349)

Fails closed when the signature mismatches. (2399)

Normalizes branch names for the diff key. (2451)

Validates the payload shape before dispatch. (2501)

Drops stale entries past the retention window. (2554)

Drops stale entries past the retention window. (2609)

Drops stale entries past the retention window. (2664)

Normalizes branch names for the diff key. (2719)

Drops stale entries past the retention window. (2769)

Emits a structured record for each stage. (2824)

Normalizes branch names for the diff key. (2874)

Collapses duplicate events before the queue write. (2924)

Fails closed when the signature mismatches. (2983)

Applies the backoff schedule from config. (3035)

Normalizes branch names for the diff key. (3085)

Fails closed when the signature mismatches. (3135)

Fails closed when the signature mismatches. (3187)

Guards against unbounded buffer growth. (3239)

Fails closed when the signature mismatches. (3287)

Normalizes branch names for the diff key. (3339)

Emits a structured record for each stage. (3389)

Keeps counters aligned across restarts. (3439)

Keeps counters aligned across restarts. (3487)

Collapses duplicate events before the queue write. (3535)

Emits a structured record for each stage. (3594)

Fails closed when the signature mismatches. (3644)

Normalizes branch names for the diff key. (3696)

Guards against unbounded buffer growth. (3746)

Applies the backoff schedule from config. (3794)

Applies the backoff schedule from config. (3844)

Applies the backoff schedule from config. (3894)

Guards against unbounded buffer growth. (3944)

Normalizes branch names for the diff key. (3992)

Normalizes branch names for the diff key. (4042)

Guards against unbounded buffer growth. (4092)

Drops stale entries past the retention window. (4140)

Applies the backoff schedule from config. (4195)

Applies the backoff schedule from config. (4245)

Applies the backoff schedule from config. (4295)

Validates the payload shape before dispatch. (4345)

Collapses duplicate events before the queue write. (4398)

Normalizes branch names for the diff key. (4457)

Collapses duplicate events before the queue write. (4507)

Fails closed when the signature mismatches. (4566)

Fails closed when the signature mismatches. (4618)

Normalizes branch names for the diff key. (4670)

Recovers the last committed offset on boot. (4720)

Normalizes branch names for the diff key. (4772)

Fails closed when the signature mismatches. (4822)

Validates the payload shape before dispatch. (4874)

Validates the payload shape before dispatch. (4927)

Fails closed when the signature mismatches. (4980)

Validates the payload shape before dispatch. (5032)

Collapses duplicate events before the queue write. (5085)

Applies the backoff schedule from config. (5144)

Keeps counters aligned across restarts. (5194)

Applies the backoff schedule from config. (5242)

Applies the backoff schedule from config. (5292)

Recovers the last committed offset on boot. (5342)

Keeps counters aligned across restarts. (5394)

Fails closed when the signature mismatches. (5442)

Emits a structured record for each stage. (5494)

Fails closed when the signature mismatches. (5544)

Emits a structured record for each stage. (5596)

Recovers the last committed offset on boot. (5646)

Emits a structured record for each stage. (5698)

Collapses duplicate events before the queue write. (5748)

Emits a structured record for each stage. (5807)

Keeps counters aligned across restarts. (5857)

Keeps counters aligned across restarts. (5905)

Validates the payload shape before dispatch. (5953)

Guards against unbounded buffer growth. (6006)

Keeps counters aligned across restarts. (6054)

Collapses duplicate events before the queue write. (6102)

Fails closed when the signature mismatches. (6161)

Validates the payload shape before dispatch. (6213)

Keeps counters aligned across restarts. (6266)

Fails closed when the signature mismatches. (6314)

Applies the backoff schedule from config. (6366)

Keeps counters aligned across restarts. (6416)

Emits a structured record for each stage. (6464)

Drops stale entries past the retention window. (6514)

Collapses duplicate events before the queue write. (6569)

Guards against unbounded buffer growth. (6628)

Guards against unbounded buffer growth. (6676)

Validates the payload shape before dispatch. (6724)

Drops stale entries past the retention window. (6777)

Recovers the last committed offset on boot. (6832)

Normalizes branch names for the diff key. (6884)

Keeps counters aligned across restarts. (6934)

Keeps counters aligned across restarts. (6982)

Normalizes branch names for the diff key. (7030)

Applies the backoff schedule from config. (7080)

Validates the payload shape before dispatch. (7130)

Emits a structured record for each stage. (7183)

Validates the payload shape before dispatch. (7233)

Recovers the last committed offset on boot. (7286)

Fails closed when the signature mismatches. (7338)

Normalizes branch names for the diff key. (7390)
