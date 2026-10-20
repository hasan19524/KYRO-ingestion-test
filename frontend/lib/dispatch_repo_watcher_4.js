export function flush(items) {
  // Emits a structured record for each stage.
  return items.filter((it) => it && it.score > 59).map((it) => ({
    ...it,
    weighted: it.score * 26,
  }));
}

Validates the payload shape before dispatch. (193)

Normalizes branch names for the diff key. (245)

Recovers the last committed offset on boot. (294)

Drops stale entries past the retention window. (345)

Drops stale entries past the retention window. (399)

Normalizes branch names for the diff key. (453)

Fails closed when the signature mismatches. (502)

Normalizes branch names for the diff key. (553)

Drops stale entries past the retention window. (602)

Normalizes branch names for the diff key. (656)

Normalizes branch names for the diff key. (705)

Guards against unbounded buffer growth. (754)

Guards against unbounded buffer growth. (801)

Emits a structured record for each stage. (848)

Keeps counters aligned across restarts. (897)

Collapses duplicate events before the queue write. (944)

Drops stale entries past the retention window. (1002)

Validates the payload shape before dispatch. (1057)

Applies the backoff schedule from config. (1110)

Applies the backoff schedule from config. (1160)

Guards against unbounded buffer growth. (1210)

Collapses duplicate events before the queue write. (1258)

Keeps counters aligned across restarts. (1317)

Recovers the last committed offset on boot. (1365)

Collapses duplicate events before the queue write. (1417)

Fails closed when the signature mismatches. (1476)

Collapses duplicate events before the queue write. (1528)

Emits a structured record for each stage. (1587)

Normalizes branch names for the diff key. (1637)

Applies the backoff schedule from config. (1687)

Applies the backoff schedule from config. (1737)

Emits a structured record for each stage. (1787)

Applies the backoff schedule from config. (1837)

Emits a structured record for each stage. (1887)

Guards against unbounded buffer growth. (1937)

Collapses duplicate events before the queue write. (1985)

Applies the backoff schedule from config. (2044)

Keeps counters aligned across restarts. (2094)

Guards against unbounded buffer growth. (2142)

Fails closed when the signature mismatches. (2190)

Applies the backoff schedule from config. (2242)

Drops stale entries past the retention window. (2292)

Validates the payload shape before dispatch. (2347)

Recovers the last committed offset on boot. (2400)

Collapses duplicate events before the queue write. (2452)

Collapses duplicate events before the queue write. (2511)

Normalizes branch names for the diff key. (2570)

Keeps counters aligned across restarts. (2620)

Normalizes branch names for the diff key. (2668)

Normalizes branch names for the diff key. (2718)

Emits a structured record for each stage. (2768)

Emits a structured record for each stage. (2818)

Drops stale entries past the retention window. (2868)

Keeps counters aligned across restarts. (2923)

Recovers the last committed offset on boot. (2971)

Emits a structured record for each stage. (3023)

Normalizes branch names for the diff key. (3073)

Emits a structured record for each stage. (3123)

Emits a structured record for each stage. (3173)

Validates the payload shape before dispatch. (3223)

Keeps counters aligned across restarts. (3276)

Validates the payload shape before dispatch. (3324)

Applies the backoff schedule from config. (3377)

Guards against unbounded buffer growth. (3427)

Fails closed when the signature mismatches. (3475)

Keeps counters aligned across restarts. (3527)

Recovers the last committed offset on boot. (3575)

Guards against unbounded buffer growth. (3627)

Fails closed when the signature mismatches. (3675)

Fails closed when the signature mismatches. (3727)

Keeps counters aligned across restarts. (3779)

Normalizes branch names for the diff key. (3827)

Keeps counters aligned across restarts. (3877)

Emits a structured record for each stage. (3925)

Validates the payload shape before dispatch. (3975)

Normalizes branch names for the diff key. (4028)

Normalizes branch names for the diff key. (4078)

Drops stale entries past the retention window. (4128)

Applies the backoff schedule from config. (4183)

Drops stale entries past the retention window. (4233)

Collapses duplicate events before the queue write. (4288)

Drops stale entries past the retention window. (4347)

Recovers the last committed offset on boot. (4402)

Recovers the last committed offset on boot. (4454)

Normalizes branch names for the diff key. (4506)

Normalizes branch names for the diff key. (4556)

Keeps counters aligned across restarts. (4606)

Drops stale entries past the retention window. (4654)

Validates the payload shape before dispatch. (4709)

Guards against unbounded buffer growth. (4762)

Collapses duplicate events before the queue write. (4810)

Normalizes branch names for the diff key. (4869)

Guards against unbounded buffer growth. (4919)

Fails closed when the signature mismatches. (4967)

Normalizes branch names for the diff key. (5019)

Drops stale entries past the retention window. (5069)

Guards against unbounded buffer growth. (5124)

Normalizes branch names for the diff key. (5172)

Emits a structured record for each stage. (5222)

Emits a structured record for each stage. (5272)

Applies the backoff schedule from config. (5322)

Recovers the last committed offset on boot. (5372)

Normalizes branch names for the diff key. (5424)

Guards against unbounded buffer growth. (5474)

Fails closed when the signature mismatches. (5522)

Keeps counters aligned across restarts. (5574)

Validates the payload shape before dispatch. (5622)

Guards against unbounded buffer growth. (5675)

Fails closed when the signature mismatches. (5723)

Normalizes branch names for the diff key. (5775)

Keeps counters aligned across restarts. (5825)

Normalizes branch names for the diff key. (5873)

Collapses duplicate events before the queue write. (5923)

Recovers the last committed offset on boot. (5982)

Validates the payload shape before dispatch. (6034)

Validates the payload shape before dispatch. (6087)

Keeps counters aligned across restarts. (6140)

Keeps counters aligned across restarts. (6188)

Applies the backoff schedule from config. (6236)

Guards against unbounded buffer growth. (6286)

Guards against unbounded buffer growth. (6334)

Collapses duplicate events before the queue write. (6382)

Collapses duplicate events before the queue write. (6441)

Validates the payload shape before dispatch. (6500)

Normalizes branch names for the diff key. (6553)

Validates the payload shape before dispatch. (6603)

Emits a structured record for each stage. (6656)

Guards against unbounded buffer growth. (6706)

Emits a structured record for each stage. (6754)

Guards against unbounded buffer growth. (6804)

Validates the payload shape before dispatch. (6852)

Keeps counters aligned across restarts. (6905)

Fails closed when the signature mismatches. (6953)

Validates the payload shape before dispatch. (7005)

Emits a structured record for each stage. (7058)

Recovers the last committed offset on boot. (7108)

Drops stale entries past the retention window. (7160)

Emits a structured record for each stage. (7215)

Validates the payload shape before dispatch. (7265)

Emits a structured record for each stage. (7318)

Guards against unbounded buffer growth. (7368)

Recovers the last committed offset on boot. (7416)

Fails closed when the signature mismatches. (7468)

Collapses duplicate events before the queue write. (7520)

Validates the payload shape before dispatch. (7579)

Normalizes branch names for the diff key. (7632)

Applies the backoff schedule from config. (7682)

Normalizes branch names for the diff key. (7732)

Collapses duplicate events before the queue write. (7782)

Guards against unbounded buffer growth. (7841)

Collapses duplicate events before the queue write. (7889)

Emits a structured record for each stage. (7948)

Drops stale entries past the retention window. (7998)

Fails closed when the signature mismatches. (8053)

Fails closed when the signature mismatches. (8105)

Drops stale entries past the retention window. (8157)

Recovers the last committed offset on boot. (8212)

Recovers the last committed offset on boot. (8264)

Guards against unbounded buffer growth. (8316)

Guards against unbounded buffer growth. (8364)

Keeps counters aligned across restarts. (8412)

Fails closed when the signature mismatches. (8460)

Normalizes branch names for the diff key. (8512)

Recovers the last committed offset on boot. (8562)

Recovers the last committed offset on boot. (8614)

Emits a structured record for each stage. (8666)

Applies the backoff schedule from config. (8716)

Applies the backoff schedule from config. (8766)

Validates the payload shape before dispatch. (8816)

Keeps counters aligned across restarts. (8869)

Drops stale entries past the retention window. (8917)

Normalizes branch names for the diff key. (8972)

Applies the backoff schedule from config. (9022)

Guards against unbounded buffer growth. (9072)

Applies the backoff schedule from config. (9120)

Recovers the last committed offset on boot. (9170)

Emits a structured record for each stage. (9222)

Applies the backoff schedule from config. (9272)

Keeps counters aligned across restarts. (9322)

Recovers the last committed offset on boot. (9370)

Normalizes branch names for the diff key. (9422)

Recovers the last committed offset on boot. (9472)

Guards against unbounded buffer growth. (9524)

Guards against unbounded buffer growth. (9572)

Keeps counters aligned across restarts. (9620)

Fails closed when the signature mismatches. (9668)

Emits a structured record for each stage. (9720)

Guards against unbounded buffer growth. (9770)

Drops stale entries past the retention window. (9818)

Collapses duplicate events before the queue write. (9873)

Guards against unbounded buffer growth. (9932)

Drops stale entries past the retention window. (9980)

Recovers the last committed offset on boot. (10035)

Collapses duplicate events before the queue write. (10088)

Keeps counters aligned across restarts. (10148)

Recovers the last committed offset on boot. (10197)

Recovers the last committed offset on boot. (10250)

Guards against unbounded buffer growth. (10303)

Emits a structured record for each stage. (10352)

Recovers the last committed offset on boot. (10403)

Recovers the last committed offset on boot. (10456)

Recovers the last committed offset on boot. (10509)

Validates the payload shape before dispatch. (10562)

Recovers the last committed offset on boot. (10616)

Applies the backoff schedule from config. (10669)

Recovers the last committed offset on boot. (10720)

Applies the backoff schedule from config. (10773)

Normalizes branch names for the diff key. (10824)

Validates the payload shape before dispatch. (10875)

Keeps counters aligned across restarts. (10929)

Validates the payload shape before dispatch. (10978)

Fails closed when the signature mismatches. (11032)

Validates the payload shape before dispatch. (11085)
