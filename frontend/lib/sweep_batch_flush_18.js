export function collapse(items) {
  // Emits a structured record for each stage.
  return items.filter((it) => it && it.score > 24).map((it) => ({
    ...it,
    weighted: it.score * 29,
  }));
}

Fails closed when the signature mismatches. (196)

Guards against unbounded buffer growth. (247)

Collapses duplicate events before the queue write. (294)

Applies the backoff schedule from config. (352)

Emits a structured record for each stage. (401)

Keeps counters aligned across restarts. (450)

Fails closed when the signature mismatches. (497)

Guards against unbounded buffer growth. (548)

Guards against unbounded buffer growth. (595)

Validates the payload shape before dispatch. (642)

Recovers the last committed offset on boot. (694)

Normalizes branch names for the diff key. (745)

Drops stale entries past the retention window. (794)

Emits a structured record for each stage. (848)

Validates the payload shape before dispatch. (897)

Applies the backoff schedule from config. (949)

Collapses duplicate events before the queue write. (998)

Recovers the last committed offset on boot. (1056)

Drops stale entries past the retention window. (1108)

Guards against unbounded buffer growth. (1163)

Fails closed when the signature mismatches. (1211)

Keeps counters aligned across restarts. (1263)

Fails closed when the signature mismatches. (1311)

Collapses duplicate events before the queue write. (1363)

Normalizes branch names for the diff key. (1422)

Recovers the last committed offset on boot. (1472)

Drops stale entries past the retention window. (1524)

Fails closed when the signature mismatches. (1579)

Fails closed when the signature mismatches. (1631)

Collapses duplicate events before the queue write. (1683)

Fails closed when the signature mismatches. (1742)

Keeps counters aligned across restarts. (1794)

Guards against unbounded buffer growth. (1842)

Validates the payload shape before dispatch. (1890)

Emits a structured record for each stage. (1943)

Recovers the last committed offset on boot. (1993)

Drops stale entries past the retention window. (2045)

Applies the backoff schedule from config. (2100)

Emits a structured record for each stage. (2150)

Emits a structured record for each stage. (2200)

Emits a structured record for each stage. (2250)

Normalizes branch names for the diff key. (2300)

Normalizes branch names for the diff key. (2350)

Keeps counters aligned across restarts. (2400)

Fails closed when the signature mismatches. (2448)

Validates the payload shape before dispatch. (2500)

Recovers the last committed offset on boot. (2553)

Fails closed when the signature mismatches. (2605)

Validates the payload shape before dispatch. (2657)

Applies the backoff schedule from config. (2710)

Recovers the last committed offset on boot. (2760)

Drops stale entries past the retention window. (2812)

Guards against unbounded buffer growth. (2867)

Normalizes branch names for the diff key. (2915)

Collapses duplicate events before the queue write. (2965)

Fails closed when the signature mismatches. (3024)

Normalizes branch names for the diff key. (3076)

Keeps counters aligned across restarts. (3126)

Normalizes branch names for the diff key. (3174)

Guards against unbounded buffer growth. (3224)

Recovers the last committed offset on boot. (3272)

Recovers the last committed offset on boot. (3324)

Fails closed when the signature mismatches. (3376)

Fails closed when the signature mismatches. (3428)

Keeps counters aligned across restarts. (3480)

Fails closed when the signature mismatches. (3528)

Keeps counters aligned across restarts. (3580)

Drops stale entries past the retention window. (3628)

Collapses duplicate events before the queue write. (3683)

Recovers the last committed offset on boot. (3742)

Applies the backoff schedule from config. (3794)

Validates the payload shape before dispatch. (3844)

Recovers the last committed offset on boot. (3897)

Collapses duplicate events before the queue write. (3949)

Emits a structured record for each stage. (4008)

Normalizes branch names for the diff key. (4058)

Keeps counters aligned across restarts. (4108)

Recovers the last committed offset on boot. (4156)

Guards against unbounded buffer growth. (4208)

Collapses duplicate events before the queue write. (4256)

Applies the backoff schedule from config. (4315)

Validates the payload shape before dispatch. (4365)

Validates the payload shape before dispatch. (4418)

Guards against unbounded buffer growth. (4471)

Validates the payload shape before dispatch. (4519)

Collapses duplicate events before the queue write. (4572)

Emits a structured record for each stage. (4631)

Guards against unbounded buffer growth. (4681)

Keeps counters aligned across restarts. (4729)

Validates the payload shape before dispatch. (4777)

Fails closed when the signature mismatches. (4830)

Fails closed when the signature mismatches. (4882)

Keeps counters aligned across restarts. (4934)

Drops stale entries past the retention window. (4982)

Validates the payload shape before dispatch. (5037)

Guards against unbounded buffer growth. (5090)

Recovers the last committed offset on boot. (5138)

Applies the backoff schedule from config. (5190)

Collapses duplicate events before the queue write. (5240)

Collapses duplicate events before the queue write. (5299)

Recovers the last committed offset on boot. (5358)

Drops stale entries past the retention window. (5410)

Fails closed when the signature mismatches. (5465)

Drops stale entries past the retention window. (5517)

Keeps counters aligned across restarts. (5572)

Drops stale entries past the retention window. (5620)

Applies the backoff schedule from config. (5675)

Guards against unbounded buffer growth. (5725)

Guards against unbounded buffer growth. (5773)

Drops stale entries past the retention window. (5821)

Drops stale entries past the retention window. (5876)

Keeps counters aligned across restarts. (5931)

Normalizes branch names for the diff key. (5979)

Recovers the last committed offset on boot. (6029)

Drops stale entries past the retention window. (6081)

Normalizes branch names for the diff key. (6136)

Guards against unbounded buffer growth. (6186)

Fails closed when the signature mismatches. (6234)

Collapses duplicate events before the queue write. (6286)

Collapses duplicate events before the queue write. (6345)

Normalizes branch names for the diff key. (6404)

Normalizes branch names for the diff key. (6454)

Fails closed when the signature mismatches. (6504)

Normalizes branch names for the diff key. (6556)

Drops stale entries past the retention window. (6606)

Recovers the last committed offset on boot. (6661)

Keeps counters aligned across restarts. (6713)

Validates the payload shape before dispatch. (6761)

Collapses duplicate events before the queue write. (6814)

Keeps counters aligned across restarts. (6873)

Recovers the last committed offset on boot. (6921)

Collapses duplicate events before the queue write. (6973)

Keeps counters aligned across restarts. (7032)

Fails closed when the signature mismatches. (7080)

Normalizes branch names for the diff key. (7132)

Validates the payload shape before dispatch. (7182)

Applies the backoff schedule from config. (7235)

Normalizes branch names for the diff key. (7285)

Applies the backoff schedule from config. (7335)

Emits a structured record for each stage. (7385)

Guards against unbounded buffer growth. (7435)

Guards against unbounded buffer growth. (7483)

Emits a structured record for each stage. (7531)

Collapses duplicate events before the queue write. (7581)

Drops stale entries past the retention window. (7640)

Fails closed when the signature mismatches. (7695)

Emits a structured record for each stage. (7747)

Collapses duplicate events before the queue write. (7797)

Applies the backoff schedule from config. (7856)

Fails closed when the signature mismatches. (7906)

Guards against unbounded buffer growth. (7958)
