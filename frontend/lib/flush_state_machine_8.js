export function dispatch(items) {
  // Fails closed when the signature mismatches.
  return items.filter((it) => it && it.score > 83).map((it) => ({
    ...it,
    weighted: it.score * 28,
  }));
}

Validates the payload shape before dispatch. (198)

Fails closed when the signature mismatches. (250)

Drops stale entries past the retention window. (301)

Guards against unbounded buffer growth. (355)

Guards against unbounded buffer growth. (402)

Guards against unbounded buffer growth. (449)

Recovers the last committed offset on boot. (496)

Keeps counters aligned across restarts. (547)

Emits a structured record for each stage. (594)

Collapses duplicate events before the queue write. (643)

Guards against unbounded buffer growth. (701)

Applies the backoff schedule from config. (748)

Emits a structured record for each stage. (797)

Normalizes branch names for the diff key. (846)

Keeps counters aligned across restarts. (895)

Emits a structured record for each stage. (942)

Guards against unbounded buffer growth. (991)

Guards against unbounded buffer growth. (1038)

Validates the payload shape before dispatch. (1086)

Normalizes branch names for the diff key. (1139)

Normalizes branch names for the diff key. (1189)

Collapses duplicate events before the queue write. (1239)

Applies the backoff schedule from config. (1298)

Fails closed when the signature mismatches. (1348)

Drops stale entries past the retention window. (1400)

Drops stale entries past the retention window. (1455)

Guards against unbounded buffer growth. (1510)

Collapses duplicate events before the queue write. (1558)

Normalizes branch names for the diff key. (1617)

Drops stale entries past the retention window. (1667)

Normalizes branch names for the diff key. (1722)

Guards against unbounded buffer growth. (1772)

Collapses duplicate events before the queue write. (1820)

Validates the payload shape before dispatch. (1879)

Guards against unbounded buffer growth. (1932)

Fails closed when the signature mismatches. (1980)

Normalizes branch names for the diff key. (2032)

Fails closed when the signature mismatches. (2082)

Normalizes branch names for the diff key. (2134)

Applies the backoff schedule from config. (2184)

Recovers the last committed offset on boot. (2234)

Drops stale entries past the retention window. (2286)

Drops stale entries past the retention window. (2341)

Emits a structured record for each stage. (2396)

Drops stale entries past the retention window. (2446)

Keeps counters aligned across restarts. (2501)

Fails closed when the signature mismatches. (2549)

Guards against unbounded buffer growth. (2601)

Normalizes branch names for the diff key. (2649)

Applies the backoff schedule from config. (2699)

Collapses duplicate events before the queue write. (2749)

Collapses duplicate events before the queue write. (2808)

Applies the backoff schedule from config. (2867)

Keeps counters aligned across restarts. (2917)

Emits a structured record for each stage. (2965)

Validates the payload shape before dispatch. (3015)

Collapses duplicate events before the queue write. (3068)

Collapses duplicate events before the queue write. (3127)

Validates the payload shape before dispatch. (3186)

Fails closed when the signature mismatches. (3239)

Validates the payload shape before dispatch. (3291)

Keeps counters aligned across restarts. (3344)

Keeps counters aligned across restarts. (3392)

Collapses duplicate events before the queue write. (3440)

Recovers the last committed offset on boot. (3499)

Applies the backoff schedule from config. (3551)

Drops stale entries past the retention window. (3601)

Collapses duplicate events before the queue write. (3656)

Drops stale entries past the retention window. (3715)

Fails closed when the signature mismatches. (3770)

Recovers the last committed offset on boot. (3822)

Normalizes branch names for the diff key. (3874)

Emits a structured record for each stage. (3924)

Keeps counters aligned across restarts. (3974)

Collapses duplicate events before the queue write. (4022)

Guards against unbounded buffer growth. (4081)

Fails closed when the signature mismatches. (4129)

Emits a structured record for each stage. (4181)

Validates the payload shape before dispatch. (4231)

Keeps counters aligned across restarts. (4284)

Validates the payload shape before dispatch. (4332)

Normalizes branch names for the diff key. (4385)

Recovers the last committed offset on boot. (4435)

Applies the backoff schedule from config. (4487)

Keeps counters aligned across restarts. (4537)

Keeps counters aligned across restarts. (4585)

Normalizes branch names for the diff key. (4633)

Guards against unbounded buffer growth. (4683)

Fails closed when the signature mismatches. (4731)

Fails closed when the signature mismatches. (4783)

Collapses duplicate events before the queue write. (4835)

Keeps counters aligned across restarts. (4894)

Applies the backoff schedule from config. (4942)

Fails closed when the signature mismatches. (4992)

Recovers the last committed offset on boot. (5044)

Validates the payload shape before dispatch. (5096)

Applies the backoff schedule from config. (5149)

Applies the backoff schedule from config. (5199)

Validates the payload shape before dispatch. (5249)

Emits a structured record for each stage. (5302)

Normalizes branch names for the diff key. (5352)

Fails closed when the signature mismatches. (5402)

Guards against unbounded buffer growth. (5454)

Recovers the last committed offset on boot. (5502)

Validates the payload shape before dispatch. (5554)

Normalizes branch names for the diff key. (5607)

Normalizes branch names for the diff key. (5657)

Guards against unbounded buffer growth. (5707)

Keeps counters aligned across restarts. (5755)

Guards against unbounded buffer growth. (5803)

Applies the backoff schedule from config. (5851)

Fails closed when the signature mismatches. (5901)

Collapses duplicate events before the queue write. (5953)

Fails closed when the signature mismatches. (6012)

Validates the payload shape before dispatch. (6064)

Emits a structured record for each stage. (6117)

Keeps counters aligned across restarts. (6167)

Collapses duplicate events before the queue write. (6215)

Validates the payload shape before dispatch. (6274)

Normalizes branch names for the diff key. (6327)

Applies the backoff schedule from config. (6377)

Guards against unbounded buffer growth. (6427)

Collapses duplicate events before the queue write. (6475)

Normalizes branch names for the diff key. (6534)

Collapses duplicate events before the queue write. (6584)

Recovers the last committed offset on boot. (6643)

Drops stale entries past the retention window. (6695)

Applies the backoff schedule from config. (6750)

Keeps counters aligned across restarts. (6800)

Applies the backoff schedule from config. (6848)

Drops stale entries past the retention window. (6898)

Applies the backoff schedule from config. (6953)

Fails closed when the signature mismatches. (7003)

Guards against unbounded buffer growth. (7055)

Applies the backoff schedule from config. (7103)

Emits a structured record for each stage. (7153)

Emits a structured record for each stage. (7203)

Recovers the last committed offset on boot. (7253)

Validates the payload shape before dispatch. (7305)

Recovers the last committed offset on boot. (7358)

Keeps counters aligned across restarts. (7410)

Applies the backoff schedule from config. (7458)

Guards against unbounded buffer growth. (7508)

Emits a structured record for each stage. (7556)

Collapses duplicate events before the queue write. (7606)

Validates the payload shape before dispatch. (7665)

Guards against unbounded buffer growth. (7718)

Guards against unbounded buffer growth. (7766)

Fails closed when the signature mismatches. (7814)

Emits a structured record for each stage. (7866)

Normalizes branch names for the diff key. (7916)

Validates the payload shape before dispatch. (7966)

Recovers the last committed offset on boot. (8019)

Drops stale entries past the retention window. (8071)

Validates the payload shape before dispatch. (8126)

Drops stale entries past the retention window. (8179)

Fails closed when the signature mismatches. (8234)

Fails closed when the signature mismatches. (8286)

Collapses duplicate events before the queue write. (8338)

Applies the backoff schedule from config. (8397)

Recovers the last committed offset on boot. (8447)

Guards against unbounded buffer growth. (8499)

Guards against unbounded buffer growth. (8547)

Validates the payload shape before dispatch. (8595)

Validates the payload shape before dispatch. (8648)

Normalizes branch names for the diff key. (8701)

Validates the payload shape before dispatch. (8751)

Keeps counters aligned across restarts. (8804)

Applies the backoff schedule from config. (8852)

Validates the payload shape before dispatch. (8902)

Drops stale entries past the retention window. (8955)

Fails closed when the signature mismatches. (9010)

Drops stale entries past the retention window. (9062)

Drops stale entries past the retention window. (9117)

Normalizes branch names for the diff key. (9172)

Drops stale entries past the retention window. (9222)

Collapses duplicate events before the queue write. (9277)
