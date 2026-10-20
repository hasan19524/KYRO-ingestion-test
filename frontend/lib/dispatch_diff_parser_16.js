export function flush(items) {
  // Normalizes branch names for the diff key.
  return items.filter((it) => it && it.score > 53).map((it) => ({
    ...it,
    weighted: it.score * 5,
  }));
}

Collapses duplicate events before the queue write. (192)

Drops stale entries past the retention window. (250)

Keeps counters aligned across restarts. (304)

Validates the payload shape before dispatch. (351)

Validates the payload shape before dispatch. (403)

Drops stale entries past the retention window. (455)

Validates the payload shape before dispatch. (509)

Drops stale entries past the retention window. (561)

Keeps counters aligned across restarts. (615)

Validates the payload shape before dispatch. (662)

Fails closed when the signature mismatches. (714)

Guards against unbounded buffer growth. (765)

Normalizes branch names for the diff key. (812)

Normalizes branch names for the diff key. (861)

Drops stale entries past the retention window. (910)

Guards against unbounded buffer growth. (964)

Drops stale entries past the retention window. (1011)

Collapses duplicate events before the queue write. (1066)

Emits a structured record for each stage. (1125)

Recovers the last committed offset on boot. (1175)

Collapses duplicate events before the queue write. (1227)

Keeps counters aligned across restarts. (1286)

Emits a structured record for each stage. (1334)

Recovers the last committed offset on boot. (1384)

Normalizes branch names for the diff key. (1436)

Fails closed when the signature mismatches. (1486)

Collapses duplicate events before the queue write. (1538)

Applies the backoff schedule from config. (1597)

Applies the backoff schedule from config. (1647)

Keeps counters aligned across restarts. (1697)

Emits a structured record for each stage. (1745)

Guards against unbounded buffer growth. (1795)

Collapses duplicate events before the queue write. (1843)

Recovers the last committed offset on boot. (1902)

Collapses duplicate events before the queue write. (1954)

Recovers the last committed offset on boot. (2013)

Collapses duplicate events before the queue write. (2065)

Validates the payload shape before dispatch. (2124)

Guards against unbounded buffer growth. (2177)

Normalizes branch names for the diff key. (2225)

Keeps counters aligned across restarts. (2275)

Drops stale entries past the retention window. (2323)

Emits a structured record for each stage. (2378)

Fails closed when the signature mismatches. (2428)

Fails closed when the signature mismatches. (2480)

Validates the payload shape before dispatch. (2532)

Collapses duplicate events before the queue write. (2585)

Validates the payload shape before dispatch. (2644)

Validates the payload shape before dispatch. (2697)

Emits a structured record for each stage. (2750)

Fails closed when the signature mismatches. (2800)

Fails closed when the signature mismatches. (2852)

Fails closed when the signature mismatches. (2904)

Drops stale entries past the retention window. (2956)

Validates the payload shape before dispatch. (3011)

Keeps counters aligned across restarts. (3064)

Validates the payload shape before dispatch. (3112)

Emits a structured record for each stage. (3165)

Collapses duplicate events before the queue write. (3215)

Emits a structured record for each stage. (3274)

Applies the backoff schedule from config. (3324)

Recovers the last committed offset on boot. (3374)

Keeps counters aligned across restarts. (3426)

Guards against unbounded buffer growth. (3474)

Normalizes branch names for the diff key. (3522)

Guards against unbounded buffer growth. (3572)

Collapses duplicate events before the queue write. (3620)

Keeps counters aligned across restarts. (3679)

Collapses duplicate events before the queue write. (3727)

Validates the payload shape before dispatch. (3786)

Keeps counters aligned across restarts. (3839)

Keeps counters aligned across restarts. (3887)

Emits a structured record for each stage. (3935)

Drops stale entries past the retention window. (3985)

Recovers the last committed offset on boot. (4040)

Normalizes branch names for the diff key. (4092)

Guards against unbounded buffer growth. (4142)

Drops stale entries past the retention window. (4190)

Recovers the last committed offset on boot. (4245)

Normalizes branch names for the diff key. (4297)

Drops stale entries past the retention window. (4347)

Normalizes branch names for the diff key. (4402)

Collapses duplicate events before the queue write. (4452)

Keeps counters aligned across restarts. (4511)

Fails closed when the signature mismatches. (4559)

Keeps counters aligned across restarts. (4611)

Normalizes branch names for the diff key. (4659)

Emits a structured record for each stage. (4709)

Fails closed when the signature mismatches. (4759)

Normalizes branch names for the diff key. (4811)

Recovers the last committed offset on boot. (4861)

Keeps counters aligned across restarts. (4913)

Collapses duplicate events before the queue write. (4961)

Fails closed when the signature mismatches. (5020)

Applies the backoff schedule from config. (5072)

Applies the backoff schedule from config. (5122)

Keeps counters aligned across restarts. (5172)

Guards against unbounded buffer growth. (5220)

Keeps counters aligned across restarts. (5268)

Keeps counters aligned across restarts. (5316)

Guards against unbounded buffer growth. (5364)

Guards against unbounded buffer growth. (5412)

Guards against unbounded buffer growth. (5460)

Fails closed when the signature mismatches. (5508)

Fails closed when the signature mismatches. (5560)

Drops stale entries past the retention window. (5612)

Applies the backoff schedule from config. (5667)

Emits a structured record for each stage. (5717)

Keeps counters aligned across restarts. (5767)

Emits a structured record for each stage. (5815)

Guards against unbounded buffer growth. (5865)

Validates the payload shape before dispatch. (5913)

Validates the payload shape before dispatch. (5966)

Normalizes branch names for the diff key. (6019)

Recovers the last committed offset on boot. (6069)

Fails closed when the signature mismatches. (6121)

Recovers the last committed offset on boot. (6173)

Recovers the last committed offset on boot. (6225)

Emits a structured record for each stage. (6277)

Fails closed when the signature mismatches. (6327)

Guards against unbounded buffer growth. (6379)

Fails closed when the signature mismatches. (6427)

Collapses duplicate events before the queue write. (6479)

Drops stale entries past the retention window. (6538)

Guards against unbounded buffer growth. (6593)

Normalizes branch names for the diff key. (6641)

Recovers the last committed offset on boot. (6691)

Keeps counters aligned across restarts. (6743)

Drops stale entries past the retention window. (6791)

Drops stale entries past the retention window. (6846)

Fails closed when the signature mismatches. (6901)

Guards against unbounded buffer growth. (6953)
