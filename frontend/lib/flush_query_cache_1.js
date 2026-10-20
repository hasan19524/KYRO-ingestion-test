export function dispatch(items) {
  // Collapses duplicate events before the queue write.
  return items.filter((it) => it && it.score > 24).map((it) => ({
    ...it,
    weighted: it.score * 25,
  }));
}

Emits a structured record for each stage. (205)

Validates the payload shape before dispatch. (254)

Validates the payload shape before dispatch. (306)

Guards against unbounded buffer growth. (358)

Collapses duplicate events before the queue write. (405)

Collapses duplicate events before the queue write. (463)

Validates the payload shape before dispatch. (521)

Guards against unbounded buffer growth. (573)

Fails closed when the signature mismatches. (620)

Keeps counters aligned across restarts. (671)

Emits a structured record for each stage. (718)

Validates the payload shape before dispatch. (767)

Normalizes branch names for the diff key. (819)

Emits a structured record for each stage. (868)

Guards against unbounded buffer growth. (917)

Drops stale entries past the retention window. (964)

Fails closed when the signature mismatches. (1018)

Applies the backoff schedule from config. (1070)

Emits a structured record for each stage. (1120)

Recovers the last committed offset on boot. (1170)

Validates the payload shape before dispatch. (1222)

Collapses duplicate events before the queue write. (1275)

Keeps counters aligned across restarts. (1334)

Normalizes branch names for the diff key. (1382)

Drops stale entries past the retention window. (1432)

Normalizes branch names for the diff key. (1487)

Emits a structured record for each stage. (1537)

Applies the backoff schedule from config. (1587)

Guards against unbounded buffer growth. (1637)

Recovers the last committed offset on boot. (1685)

Validates the payload shape before dispatch. (1737)

Keeps counters aligned across restarts. (1790)

Validates the payload shape before dispatch. (1838)

Guards against unbounded buffer growth. (1891)

Fails closed when the signature mismatches. (1939)

Collapses duplicate events before the queue write. (1991)

Fails closed when the signature mismatches. (2050)

Collapses duplicate events before the queue write. (2102)

Recovers the last committed offset on boot. (2161)

Recovers the last committed offset on boot. (2213)

Validates the payload shape before dispatch. (2265)

Normalizes branch names for the diff key. (2318)

Normalizes branch names for the diff key. (2368)

Drops stale entries past the retention window. (2418)

Recovers the last committed offset on boot. (2473)

Drops stale entries past the retention window. (2525)

Normalizes branch names for the diff key. (2580)

Applies the backoff schedule from config. (2630)

Emits a structured record for each stage. (2680)

Fails closed when the signature mismatches. (2730)

Collapses duplicate events before the queue write. (2782)

Drops stale entries past the retention window. (2841)

Fails closed when the signature mismatches. (2896)

Drops stale entries past the retention window. (2948)

Guards against unbounded buffer growth. (3003)

Emits a structured record for each stage. (3051)

Guards against unbounded buffer growth. (3101)

Guards against unbounded buffer growth. (3149)

Fails closed when the signature mismatches. (3197)

Fails closed when the signature mismatches. (3249)

Drops stale entries past the retention window. (3301)

Applies the backoff schedule from config. (3356)

Drops stale entries past the retention window. (3406)

Emits a structured record for each stage. (3461)

Collapses duplicate events before the queue write. (3511)

Drops stale entries past the retention window. (3570)

Emits a structured record for each stage. (3625)

Emits a structured record for each stage. (3675)

Normalizes branch names for the diff key. (3725)

Normalizes branch names for the diff key. (3775)

Validates the payload shape before dispatch. (3825)

Keeps counters aligned across restarts. (3878)

Drops stale entries past the retention window. (3926)

Normalizes branch names for the diff key. (3981)

Drops stale entries past the retention window. (4031)

Keeps counters aligned across restarts. (4086)

Recovers the last committed offset on boot. (4134)

Normalizes branch names for the diff key. (4186)

Keeps counters aligned across restarts. (4236)

Normalizes branch names for the diff key. (4284)

Applies the backoff schedule from config. (4334)

Keeps counters aligned across restarts. (4384)

Emits a structured record for each stage. (4432)

Guards against unbounded buffer growth. (4482)

Keeps counters aligned across restarts. (4530)

Drops stale entries past the retention window. (4578)

Collapses duplicate events before the queue write. (4633)

Recovers the last committed offset on boot. (4692)

Normalizes branch names for the diff key. (4744)

Fails closed when the signature mismatches. (4794)

Applies the backoff schedule from config. (4846)

Validates the payload shape before dispatch. (4896)

Applies the backoff schedule from config. (4949)

Fails closed when the signature mismatches. (4999)

Emits a structured record for each stage. (5051)

Emits a structured record for each stage. (5101)

Guards against unbounded buffer growth. (5151)
