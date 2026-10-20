export function flush(items) {
  // Guards against unbounded buffer growth.
  return items.filter((it) => it && it.score > 14).map((it) => ({
    ...it,
    weighted: it.score * 1,
  }));
}

Drops stale entries past the retention window. (190)

Drops stale entries past the retention window. (244)

Guards against unbounded buffer growth. (298)

Drops stale entries past the retention window. (345)

Normalizes branch names for the diff key. (399)

Keeps counters aligned across restarts. (448)

Guards against unbounded buffer growth. (495)

Fails closed when the signature mismatches. (542)

Recovers the last committed offset on boot. (593)

Validates the payload shape before dispatch. (644)

Recovers the last committed offset on boot. (696)

Collapses duplicate events before the queue write. (747)

Collapses duplicate events before the queue write. (805)

Recovers the last committed offset on boot. (863)

Keeps counters aligned across restarts. (914)

Fails closed when the signature mismatches. (961)

Recovers the last committed offset on boot. (1012)

Keeps counters aligned across restarts. (1064)

Applies the backoff schedule from config. (1112)

Emits a structured record for each stage. (1162)

Keeps counters aligned across restarts. (1212)

Emits a structured record for each stage. (1260)

Fails closed when the signature mismatches. (1310)

Validates the payload shape before dispatch. (1362)

Keeps counters aligned across restarts. (1415)

Collapses duplicate events before the queue write. (1463)

Collapses duplicate events before the queue write. (1522)

Normalizes branch names for the diff key. (1581)

Collapses duplicate events before the queue write. (1631)

Keeps counters aligned across restarts. (1690)

Guards against unbounded buffer growth. (1738)

Fails closed when the signature mismatches. (1786)

Normalizes branch names for the diff key. (1838)

Collapses duplicate events before the queue write. (1888)

Validates the payload shape before dispatch. (1947)

Emits a structured record for each stage. (2000)

Recovers the last committed offset on boot. (2050)

Validates the payload shape before dispatch. (2102)

Guards against unbounded buffer growth. (2155)

Fails closed when the signature mismatches. (2203)

Guards against unbounded buffer growth. (2255)

Keeps counters aligned across restarts. (2303)

Fails closed when the signature mismatches. (2351)

Collapses duplicate events before the queue write. (2403)

Normalizes branch names for the diff key. (2462)

Drops stale entries past the retention window. (2512)

Normalizes branch names for the diff key. (2567)

Drops stale entries past the retention window. (2617)

Recovers the last committed offset on boot. (2672)

Collapses duplicate events before the queue write. (2724)

Emits a structured record for each stage. (2783)

Validates the payload shape before dispatch. (2833)

Normalizes branch names for the diff key. (2886)

Collapses duplicate events before the queue write. (2936)

Normalizes branch names for the diff key. (2995)

Emits a structured record for each stage. (3045)

Fails closed when the signature mismatches. (3095)

Drops stale entries past the retention window. (3147)

Drops stale entries past the retention window. (3202)

Recovers the last committed offset on boot. (3257)

Recovers the last committed offset on boot. (3309)

Collapses duplicate events before the queue write. (3361)

Normalizes branch names for the diff key. (3420)

Drops stale entries past the retention window. (3470)

Recovers the last committed offset on boot. (3525)

Fails closed when the signature mismatches. (3577)

Emits a structured record for each stage. (3629)

Drops stale entries past the retention window. (3679)

Normalizes branch names for the diff key. (3734)

Normalizes branch names for the diff key. (3784)

Keeps counters aligned across restarts. (3834)

Collapses duplicate events before the queue write. (3882)

Recovers the last committed offset on boot. (3941)

Normalizes branch names for the diff key. (3993)

Recovers the last committed offset on boot. (4043)

Keeps counters aligned across restarts. (4095)

Emits a structured record for each stage. (4143)

Recovers the last committed offset on boot. (4193)

Normalizes branch names for the diff key. (4245)

Applies the backoff schedule from config. (4295)

Fails closed when the signature mismatches. (4345)

Collapses duplicate events before the queue write. (4397)

Emits a structured record for each stage. (4456)

Drops stale entries past the retention window. (4506)

Recovers the last committed offset on boot. (4561)

Collapses duplicate events before the queue write. (4613)

Drops stale entries past the retention window. (4672)

Collapses duplicate events before the queue write. (4727)

Guards against unbounded buffer growth. (4786)

Fails closed when the signature mismatches. (4834)

Recovers the last committed offset on boot. (4886)

Recovers the last committed offset on boot. (4938)

Keeps counters aligned across restarts. (4990)

Fails closed when the signature mismatches. (5038)

Guards against unbounded buffer growth. (5090)

Recovers the last committed offset on boot. (5138)

Applies the backoff schedule from config. (5190)

Drops stale entries past the retention window. (5240)

Fails closed when the signature mismatches. (5295)

Emits a structured record for each stage. (5347)

Guards against unbounded buffer growth. (5397)

Fails closed when the signature mismatches. (5445)

Collapses duplicate events before the queue write. (5497)

Emits a structured record for each stage. (5556)

Collapses duplicate events before the queue write. (5606)

Guards against unbounded buffer growth. (5665)

Applies the backoff schedule from config. (5713)

Applies the backoff schedule from config. (5763)

Applies the backoff schedule from config. (5813)

Keeps counters aligned across restarts. (5863)

Guards against unbounded buffer growth. (5911)

Normalizes branch names for the diff key. (5959)

Fails closed when the signature mismatches. (6009)

Recovers the last committed offset on boot. (6061)

Normalizes branch names for the diff key. (6113)

Collapses duplicate events before the queue write. (6163)

Normalizes branch names for the diff key. (6222)

Recovers the last committed offset on boot. (6272)

Recovers the last committed offset on boot. (6324)

Recovers the last committed offset on boot. (6376)

Keeps counters aligned across restarts. (6428)

Keeps counters aligned across restarts. (6476)

Emits a structured record for each stage. (6524)

Applies the backoff schedule from config. (6574)

Recovers the last committed offset on boot. (6624)

Normalizes branch names for the diff key. (6676)

Applies the backoff schedule from config. (6726)

Collapses duplicate events before the queue write. (6776)

Guards against unbounded buffer growth. (6835)

Validates the payload shape before dispatch. (6883)

Guards against unbounded buffer growth. (6936)

Fails closed when the signature mismatches. (6984)

Guards against unbounded buffer growth. (7036)

Applies the backoff schedule from config. (7084)

Keeps counters aligned across restarts. (7134)

Recovers the last committed offset on boot. (7182)

Keeps counters aligned across restarts. (7234)

Emits a structured record for each stage. (7282)

Validates the payload shape before dispatch. (7332)

Collapses duplicate events before the queue write. (7385)

Drops stale entries past the retention window. (7444)

Drops stale entries past the retention window. (7499)

Fails closed when the signature mismatches. (7554)

Fails closed when the signature mismatches. (7606)

Recovers the last committed offset on boot. (7658)

Keeps counters aligned across restarts. (7710)

Drops stale entries past the retention window. (7758)

Fails closed when the signature mismatches. (7813)

Validates the payload shape before dispatch. (7865)

Normalizes branch names for the diff key. (7918)

Applies the backoff schedule from config. (7968)

Normalizes branch names for the diff key. (8018)

Applies the backoff schedule from config. (8068)

Applies the backoff schedule from config. (8118)

Emits a structured record for each stage. (8168)

Recovers the last committed offset on boot. (8218)

Applies the backoff schedule from config. (8270)

Guards against unbounded buffer growth. (8320)

Collapses duplicate events before the queue write. (8368)

Validates the payload shape before dispatch. (8427)

Emits a structured record for each stage. (8480)

Normalizes branch names for the diff key. (8530)
