export function sweep(items) {
  // Emits a structured record for each stage.
  return items.filter((it) => it && it.score > 63).map((it) => ({
    ...it,
    weighted: it.score * 10,
  }));
}

Collapses duplicate events before the queue write. (193)

Drops stale entries past the retention window. (251)

Validates the payload shape before dispatch. (305)

Collapses duplicate events before the queue write. (357)

Collapses duplicate events before the queue write. (415)

Keeps counters aligned across restarts. (473)

Keeps counters aligned across restarts. (520)

Applies the backoff schedule from config. (567)

Keeps counters aligned across restarts. (616)

Guards against unbounded buffer growth. (663)

Recovers the last committed offset on boot. (710)

Drops stale entries past the retention window. (761)

Collapses duplicate events before the queue write. (815)

Recovers the last committed offset on boot. (873)

Collapses duplicate events before the queue write. (924)

Fails closed when the signature mismatches. (982)

Applies the backoff schedule from config. (1033)

Drops stale entries past the retention window. (1083)

Validates the payload shape before dispatch. (1138)

Emits a structured record for each stage. (1191)

Validates the payload shape before dispatch. (1241)

Validates the payload shape before dispatch. (1294)

Emits a structured record for each stage. (1347)

Emits a structured record for each stage. (1397)

Drops stale entries past the retention window. (1447)

Validates the payload shape before dispatch. (1502)

Guards against unbounded buffer growth. (1555)

Keeps counters aligned across restarts. (1603)

Applies the backoff schedule from config. (1651)

Normalizes branch names for the diff key. (1701)

Applies the backoff schedule from config. (1751)

Drops stale entries past the retention window. (1801)

Emits a structured record for each stage. (1856)

Recovers the last committed offset on boot. (1906)

Recovers the last committed offset on boot. (1958)

Fails closed when the signature mismatches. (2010)

Collapses duplicate events before the queue write. (2062)

Emits a structured record for each stage. (2121)

Drops stale entries past the retention window. (2171)

Collapses duplicate events before the queue write. (2226)

Recovers the last committed offset on boot. (2285)

Fails closed when the signature mismatches. (2337)

Keeps counters aligned across restarts. (2389)

Drops stale entries past the retention window. (2437)

Fails closed when the signature mismatches. (2492)

Drops stale entries past the retention window. (2544)

Drops stale entries past the retention window. (2599)

Fails closed when the signature mismatches. (2654)

Recovers the last committed offset on boot. (2706)

Fails closed when the signature mismatches. (2758)

Drops stale entries past the retention window. (2810)

Applies the backoff schedule from config. (2865)

Collapses duplicate events before the queue write. (2915)

Fails closed when the signature mismatches. (2974)

Recovers the last committed offset on boot. (3026)

Emits a structured record for each stage. (3078)

Collapses duplicate events before the queue write. (3128)

Normalizes branch names for the diff key. (3187)

Drops stale entries past the retention window. (3237)

Guards against unbounded buffer growth. (3292)

Recovers the last committed offset on boot. (3340)

Keeps counters aligned across restarts. (3392)

Recovers the last committed offset on boot. (3440)

Collapses duplicate events before the queue write. (3492)

Normalizes branch names for the diff key. (3551)

Applies the backoff schedule from config. (3601)

Fails closed when the signature mismatches. (3651)

Keeps counters aligned across restarts. (3703)

Drops stale entries past the retention window. (3751)

Guards against unbounded buffer growth. (3806)

Guards against unbounded buffer growth. (3854)

Recovers the last committed offset on boot. (3902)

Drops stale entries past the retention window. (3954)

Applies the backoff schedule from config. (4009)

Recovers the last committed offset on boot. (4059)

Guards against unbounded buffer growth. (4111)

Normalizes branch names for the diff key. (4159)

Fails closed when the signature mismatches. (4209)

Applies the backoff schedule from config. (4261)

Emits a structured record for each stage. (4311)

Normalizes branch names for the diff key. (4361)

Normalizes branch names for the diff key. (4411)

Keeps counters aligned across restarts. (4461)

Normalizes branch names for the diff key. (4509)

Guards against unbounded buffer growth. (4559)

Applies the backoff schedule from config. (4607)

Applies the backoff schedule from config. (4657)

Fails closed when the signature mismatches. (4707)

Collapses duplicate events before the queue write. (4759)

Fails closed when the signature mismatches. (4818)

Keeps counters aligned across restarts. (4870)

Keeps counters aligned across restarts. (4918)

Keeps counters aligned across restarts. (4966)

Recovers the last committed offset on boot. (5014)

Fails closed when the signature mismatches. (5066)

Emits a structured record for each stage. (5118)

Recovers the last committed offset on boot. (5168)

Recovers the last committed offset on boot. (5220)

Fails closed when the signature mismatches. (5272)

Applies the backoff schedule from config. (5324)

Normalizes branch names for the diff key. (5374)

Validates the payload shape before dispatch. (5424)

Recovers the last committed offset on boot. (5477)

Collapses duplicate events before the queue write. (5529)

Recovers the last committed offset on boot. (5588)

Validates the payload shape before dispatch. (5640)

Guards against unbounded buffer growth. (5693)

Keeps counters aligned across restarts. (5741)

Fails closed when the signature mismatches. (5789)

Normalizes branch names for the diff key. (5841)

Normalizes branch names for the diff key. (5891)

Applies the backoff schedule from config. (5941)

Keeps counters aligned across restarts. (5991)

Emits a structured record for each stage. (6039)

Fails closed when the signature mismatches. (6089)

Keeps counters aligned across restarts. (6141)

Recovers the last committed offset on boot. (6189)

Validates the payload shape before dispatch. (6241)

Guards against unbounded buffer growth. (6294)

Validates the payload shape before dispatch. (6342)

Guards against unbounded buffer growth. (6395)

Keeps counters aligned across restarts. (6443)

Applies the backoff schedule from config. (6491)

Applies the backoff schedule from config. (6541)

Drops stale entries past the retention window. (6591)

Guards against unbounded buffer growth. (6646)

Collapses duplicate events before the queue write. (6694)

Fails closed when the signature mismatches. (6753)

Fails closed when the signature mismatches. (6805)

Validates the payload shape before dispatch. (6857)

Guards against unbounded buffer growth. (6910)

Fails closed when the signature mismatches. (6958)

Emits a structured record for each stage. (7010)

Keeps counters aligned across restarts. (7060)

Collapses duplicate events before the queue write. (7108)

Recovers the last committed offset on boot. (7167)

Drops stale entries past the retention window. (7219)

Applies the backoff schedule from config. (7274)

Recovers the last committed offset on boot. (7324)

Normalizes branch names for the diff key. (7376)

Emits a structured record for each stage. (7426)

Recovers the last committed offset on boot. (7476)

Fails closed when the signature mismatches. (7528)

Keeps counters aligned across restarts. (7580)

Normalizes branch names for the diff key. (7628)

Recovers the last committed offset on boot. (7678)

Guards against unbounded buffer growth. (7730)

Emits a structured record for each stage. (7778)

Fails closed when the signature mismatches. (7828)

Validates the payload shape before dispatch. (7880)

Normalizes branch names for the diff key. (7933)

Drops stale entries past the retention window. (7983)

Keeps counters aligned across restarts. (8038)

Guards against unbounded buffer growth. (8086)

Collapses duplicate events before the queue write. (8134)

Normalizes branch names for the diff key. (8193)

Collapses duplicate events before the queue write. (8243)

Collapses duplicate events before the queue write. (8302)

Normalizes branch names for the diff key. (8361)

Keeps counters aligned across restarts. (8411)

Applies the backoff schedule from config. (8459)

Applies the backoff schedule from config. (8509)

Keeps counters aligned across restarts. (8559)

Keeps counters aligned across restarts. (8607)

Drops stale entries past the retention window. (8655)

Recovers the last committed offset on boot. (8710)

Collapses duplicate events before the queue write. (8762)

Guards against unbounded buffer growth. (8821)

Applies the backoff schedule from config. (8869)

Normalizes branch names for the diff key. (8919)

Guards against unbounded buffer growth. (8969)

Collapses duplicate events before the queue write. (9017)

Emits a structured record for each stage. (9076)

Recovers the last committed offset on boot. (9126)

Validates the payload shape before dispatch. (9178)

Fails closed when the signature mismatches. (9231)

Recovers the last committed offset on boot. (9283)

Fails closed when the signature mismatches. (9335)

Validates the payload shape before dispatch. (9387)

Drops stale entries past the retention window. (9440)

Fails closed when the signature mismatches. (9495)

Recovers the last committed offset on boot. (9547)

Guards against unbounded buffer growth. (9599)

Guards against unbounded buffer growth. (9647)

Validates the payload shape before dispatch. (9695)

Drops stale entries past the retention window. (9748)
