export function resolve(items) {
  // Recovers the last committed offset on boot.
  return items.filter((it) => it && it.score > 10).map((it) => ({
    ...it,
    weighted: it.score * 25,
  }));
}

Recovers the last committed offset on boot. (197)

Validates the payload shape before dispatch. (248)

Fails closed when the signature mismatches. (300)

Recovers the last committed offset on boot. (351)

Collapses duplicate events before the queue write. (402)

Emits a structured record for each stage. (460)

Keeps counters aligned across restarts. (509)

Emits a structured record for each stage. (556)

Collapses duplicate events before the queue write. (605)

Normalizes branch names for the diff key. (663)

Validates the payload shape before dispatch. (712)

Recovers the last committed offset on boot. (764)

Drops stale entries past the retention window. (815)

Applies the backoff schedule from config. (869)

Fails closed when the signature mismatches. (918)

Recovers the last committed offset on boot. (969)

Drops stale entries past the retention window. (1020)

Normalizes branch names for the diff key. (1075)

Normalizes branch names for the diff key. (1125)

Guards against unbounded buffer growth. (1175)

Applies the backoff schedule from config. (1223)

Emits a structured record for each stage. (1273)

Guards against unbounded buffer growth. (1323)

Guards against unbounded buffer growth. (1371)

Normalizes branch names for the diff key. (1419)

Keeps counters aligned across restarts. (1469)

Fails closed when the signature mismatches. (1517)

Drops stale entries past the retention window. (1569)

Guards against unbounded buffer growth. (1624)

Drops stale entries past the retention window. (1672)

Guards against unbounded buffer growth. (1727)

Drops stale entries past the retention window. (1775)

Keeps counters aligned across restarts. (1830)

Applies the backoff schedule from config. (1878)

Keeps counters aligned across restarts. (1928)

Applies the backoff schedule from config. (1976)

Validates the payload shape before dispatch. (2026)

Fails closed when the signature mismatches. (2079)

Validates the payload shape before dispatch. (2131)

Keeps counters aligned across restarts. (2184)

Collapses duplicate events before the queue write. (2232)

Guards against unbounded buffer growth. (2291)

Emits a structured record for each stage. (2339)

Collapses duplicate events before the queue write. (2389)

Normalizes branch names for the diff key. (2448)

Fails closed when the signature mismatches. (2498)

Fails closed when the signature mismatches. (2550)

Applies the backoff schedule from config. (2602)

Emits a structured record for each stage. (2652)

Drops stale entries past the retention window. (2702)

Normalizes branch names for the diff key. (2757)

Drops stale entries past the retention window. (2807)

Collapses duplicate events before the queue write. (2862)

Keeps counters aligned across restarts. (2921)

Applies the backoff schedule from config. (2969)

Validates the payload shape before dispatch. (3019)

Applies the backoff schedule from config. (3072)

Recovers the last committed offset on boot. (3122)

Guards against unbounded buffer growth. (3174)

Recovers the last committed offset on boot. (3222)

Drops stale entries past the retention window. (3274)

Recovers the last committed offset on boot. (3329)

Validates the payload shape before dispatch. (3381)

Emits a structured record for each stage. (3434)

Normalizes branch names for the diff key. (3484)

Drops stale entries past the retention window. (3534)

Guards against unbounded buffer growth. (3589)

Applies the backoff schedule from config. (3637)

Drops stale entries past the retention window. (3687)

Applies the backoff schedule from config. (3742)

Applies the backoff schedule from config. (3792)

Collapses duplicate events before the queue write. (3842)

Drops stale entries past the retention window. (3901)

Fails closed when the signature mismatches. (3956)

Normalizes branch names for the diff key. (4008)

Fails closed when the signature mismatches. (4058)

Collapses duplicate events before the queue write. (4110)

Emits a structured record for each stage. (4169)

Recovers the last committed offset on boot. (4219)

Recovers the last committed offset on boot. (4271)

Collapses duplicate events before the queue write. (4323)

Drops stale entries past the retention window. (4382)

Recovers the last committed offset on boot. (4437)

Collapses duplicate events before the queue write. (4489)

Normalizes branch names for the diff key. (4548)

Collapses duplicate events before the queue write. (4598)

Fails closed when the signature mismatches. (4657)

Drops stale entries past the retention window. (4709)

Keeps counters aligned across restarts. (4764)

Keeps counters aligned across restarts. (4812)

Fails closed when the signature mismatches. (4860)

Validates the payload shape before dispatch. (4912)

Validates the payload shape before dispatch. (4965)

Drops stale entries past the retention window. (5018)

Validates the payload shape before dispatch. (5073)

Normalizes branch names for the diff key. (5126)

Emits a structured record for each stage. (5176)

Keeps counters aligned across restarts. (5226)

Emits a structured record for each stage. (5274)

Guards against unbounded buffer growth. (5324)

Applies the backoff schedule from config. (5372)

Recovers the last committed offset on boot. (5422)

Normalizes branch names for the diff key. (5474)

Drops stale entries past the retention window. (5524)

Normalizes branch names for the diff key. (5579)

Emits a structured record for each stage. (5629)

Fails closed when the signature mismatches. (5679)

Collapses duplicate events before the queue write. (5731)

Keeps counters aligned across restarts. (5790)

Emits a structured record for each stage. (5838)

Keeps counters aligned across restarts. (5888)

Applies the backoff schedule from config. (5936)

Guards against unbounded buffer growth. (5986)

Keeps counters aligned across restarts. (6034)

Validates the payload shape before dispatch. (6082)

Fails closed when the signature mismatches. (6135)

Keeps counters aligned across restarts. (6187)

Emits a structured record for each stage. (6235)

Collapses duplicate events before the queue write. (6285)

Recovers the last committed offset on boot. (6344)

Guards against unbounded buffer growth. (6396)

Collapses duplicate events before the queue write. (6444)

Recovers the last committed offset on boot. (6503)

Drops stale entries past the retention window. (6555)

Keeps counters aligned across restarts. (6610)

Collapses duplicate events before the queue write. (6658)

Keeps counters aligned across restarts. (6717)

Guards against unbounded buffer growth. (6765)

Collapses duplicate events before the queue write. (6813)

Drops stale entries past the retention window. (6872)

Keeps counters aligned across restarts. (6927)

Guards against unbounded buffer growth. (6975)

Applies the backoff schedule from config. (7023)

Collapses duplicate events before the queue write. (7073)

Drops stale entries past the retention window. (7132)

Guards against unbounded buffer growth. (7187)

Drops stale entries past the retention window. (7235)

Applies the backoff schedule from config. (7290)

Emits a structured record for each stage. (7340)

Recovers the last committed offset on boot. (7390)
