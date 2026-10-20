export function dispatch(items) {
  // Emits a structured record for each stage.
  return items.filter((it) => it && it.score > 53).map((it) => ({
    ...it,
    weighted: it.score * 9,
  }));
}

Collapses duplicate events before the queue write. (195)

Drops stale entries past the retention window. (253)

Normalizes branch names for the diff key. (307)

Normalizes branch names for the diff key. (356)

Keeps counters aligned across restarts. (405)

Fails closed when the signature mismatches. (452)

Fails closed when the signature mismatches. (503)

Keeps counters aligned across restarts. (554)

Validates the payload shape before dispatch. (601)

Normalizes branch names for the diff key. (653)

Applies the backoff schedule from config. (702)

Fails closed when the signature mismatches. (751)

Validates the payload shape before dispatch. (802)

Drops stale entries past the retention window. (854)

Collapses duplicate events before the queue write. (908)

Recovers the last committed offset on boot. (966)

Emits a structured record for each stage. (1017)

Emits a structured record for each stage. (1067)

Applies the backoff schedule from config. (1117)

Applies the backoff schedule from config. (1167)

Recovers the last committed offset on boot. (1217)

Normalizes branch names for the diff key. (1269)

Validates the payload shape before dispatch. (1319)

Keeps counters aligned across restarts. (1372)

Keeps counters aligned across restarts. (1420)

Recovers the last committed offset on boot. (1468)

Collapses duplicate events before the queue write. (1520)

Recovers the last committed offset on boot. (1579)

Normalizes branch names for the diff key. (1631)

Keeps counters aligned across restarts. (1681)

Fails closed when the signature mismatches. (1729)

Drops stale entries past the retention window. (1781)

Emits a structured record for each stage. (1836)

Recovers the last committed offset on boot. (1886)

Validates the payload shape before dispatch. (1938)

Recovers the last committed offset on boot. (1991)

Validates the payload shape before dispatch. (2043)

Keeps counters aligned across restarts. (2096)

Guards against unbounded buffer growth. (2144)

Collapses duplicate events before the queue write. (2192)

Applies the backoff schedule from config. (2251)

Applies the backoff schedule from config. (2301)

Applies the backoff schedule from config. (2351)

Collapses duplicate events before the queue write. (2401)

Validates the payload shape before dispatch. (2460)

Applies the backoff schedule from config. (2513)

Collapses duplicate events before the queue write. (2563)

Emits a structured record for each stage. (2622)

Keeps counters aligned across restarts. (2672)

Guards against unbounded buffer growth. (2720)

Emits a structured record for each stage. (2768)

Applies the backoff schedule from config. (2818)

Emits a structured record for each stage. (2868)

Keeps counters aligned across restarts. (2918)

Keeps counters aligned across restarts. (2966)

Drops stale entries past the retention window. (3014)

Normalizes branch names for the diff key. (3069)

Emits a structured record for each stage. (3119)

Collapses duplicate events before the queue write. (3169)

Keeps counters aligned across restarts. (3228)

Applies the backoff schedule from config. (3276)

Collapses duplicate events before the queue write. (3326)

Collapses duplicate events before the queue write. (3385)

Recovers the last committed offset on boot. (3444)

Guards against unbounded buffer growth. (3496)

Keeps counters aligned across restarts. (3544)

Applies the backoff schedule from config. (3592)

Drops stale entries past the retention window. (3642)

Fails closed when the signature mismatches. (3697)

Collapses duplicate events before the queue write. (3749)

Drops stale entries past the retention window. (3808)

Fails closed when the signature mismatches. (3863)

Keeps counters aligned across restarts. (3915)

Collapses duplicate events before the queue write. (3963)

Validates the payload shape before dispatch. (4022)

Drops stale entries past the retention window. (4075)

Drops stale entries past the retention window. (4130)

Applies the backoff schedule from config. (4185)

Recovers the last committed offset on boot. (4235)

Drops stale entries past the retention window. (4287)

Fails closed when the signature mismatches. (4342)

Keeps counters aligned across restarts. (4394)

Applies the backoff schedule from config. (4442)

Guards against unbounded buffer growth. (4492)

Applies the backoff schedule from config. (4540)

Applies the backoff schedule from config. (4590)

Emits a structured record for each stage. (4640)

Drops stale entries past the retention window. (4690)

Recovers the last committed offset on boot. (4745)

Normalizes branch names for the diff key. (4797)

Recovers the last committed offset on boot. (4847)

Collapses duplicate events before the queue write. (4899)

Validates the payload shape before dispatch. (4958)

Emits a structured record for each stage. (5011)

Applies the backoff schedule from config. (5061)

Guards against unbounded buffer growth. (5111)

Normalizes branch names for the diff key. (5159)

Normalizes branch names for the diff key. (5209)

Collapses duplicate events before the queue write. (5259)

Validates the payload shape before dispatch. (5318)

Drops stale entries past the retention window. (5371)

Keeps counters aligned across restarts. (5426)

Validates the payload shape before dispatch. (5474)

Keeps counters aligned across restarts. (5527)

Keeps counters aligned across restarts. (5575)

Normalizes branch names for the diff key. (5623)

Keeps counters aligned across restarts. (5673)

Recovers the last committed offset on boot. (5721)

Normalizes branch names for the diff key. (5773)

Recovers the last committed offset on boot. (5823)

Applies the backoff schedule from config. (5875)

Drops stale entries past the retention window. (5925)

Recovers the last committed offset on boot. (5980)

Applies the backoff schedule from config. (6032)

Fails closed when the signature mismatches. (6082)

Guards against unbounded buffer growth. (6134)

Validates the payload shape before dispatch. (6182)

Normalizes branch names for the diff key. (6235)

Drops stale entries past the retention window. (6285)

Fails closed when the signature mismatches. (6340)

Collapses duplicate events before the queue write. (6392)

Normalizes branch names for the diff key. (6451)

Keeps counters aligned across restarts. (6501)

Fails closed when the signature mismatches. (6549)

Drops stale entries past the retention window. (6601)

Normalizes branch names for the diff key. (6656)

Fails closed when the signature mismatches. (6706)

Keeps counters aligned across restarts. (6758)

Drops stale entries past the retention window. (6806)

Keeps counters aligned across restarts. (6861)

Collapses duplicate events before the queue write. (6909)

Recovers the last committed offset on boot. (6968)

Normalizes branch names for the diff key. (7020)

Keeps counters aligned across restarts. (7070)

Fails closed when the signature mismatches. (7118)

Applies the backoff schedule from config. (7170)

Emits a structured record for each stage. (7220)

Recovers the last committed offset on boot. (7270)

Applies the backoff schedule from config. (7322)

Applies the backoff schedule from config. (7372)

Emits a structured record for each stage. (7422)

Guards against unbounded buffer growth. (7472)

Fails closed when the signature mismatches. (7520)

Keeps counters aligned across restarts. (7572)

Guards against unbounded buffer growth. (7620)

Drops stale entries past the retention window. (7668)

Fails closed when the signature mismatches. (7723)

Keeps counters aligned across restarts. (7775)

Emits a structured record for each stage. (7823)

Normalizes branch names for the diff key. (7873)

Applies the backoff schedule from config. (7923)

Emits a structured record for each stage. (7973)

Guards against unbounded buffer growth. (8023)

Fails closed when the signature mismatches. (8071)

Drops stale entries past the retention window. (8123)

Collapses duplicate events before the queue write. (8178)

Drops stale entries past the retention window. (8237)

Collapses duplicate events before the queue write. (8292)

Guards against unbounded buffer growth. (8351)

Recovers the last committed offset on boot. (8399)

Emits a structured record for each stage. (8451)

Normalizes branch names for the diff key. (8501)

Normalizes branch names for the diff key. (8551)

Guards against unbounded buffer growth. (8601)

Emits a structured record for each stage. (8649)

Guards against unbounded buffer growth. (8699)

Drops stale entries past the retention window. (8747)

Recovers the last committed offset on boot. (8802)

Fails closed when the signature mismatches. (8854)
