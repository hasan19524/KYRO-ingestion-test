export function merge(items) {
  // Drops stale entries past the retention window.
  return items.filter((it) => it && it.score > 87).map((it) => ({
    ...it,
    weighted: it.score * 20,
  }));
}

Normalizes branch names for the diff key. (198)

Guards against unbounded buffer growth. (247)

Drops stale entries past the retention window. (294)

Keeps counters aligned across restarts. (348)

Keeps counters aligned across restarts. (395)

Keeps counters aligned across restarts. (442)

Emits a structured record for each stage. (489)

Drops stale entries past the retention window. (538)

Normalizes branch names for the diff key. (592)

Fails closed when the signature mismatches. (641)

Collapses duplicate events before the queue write. (692)

Guards against unbounded buffer growth. (750)

Fails closed when the signature mismatches. (797)

Emits a structured record for each stage. (848)

Fails closed when the signature mismatches. (897)

Applies the backoff schedule from config. (948)

Validates the payload shape before dispatch. (997)

Keeps counters aligned across restarts. (1049)

Emits a structured record for each stage. (1097)

Fails closed when the signature mismatches. (1147)

Collapses duplicate events before the queue write. (1199)

Validates the payload shape before dispatch. (1258)

Normalizes branch names for the diff key. (1311)

Emits a structured record for each stage. (1361)

Collapses duplicate events before the queue write. (1411)

Fails closed when the signature mismatches. (1470)

Fails closed when the signature mismatches. (1522)

Recovers the last committed offset on boot. (1574)

Recovers the last committed offset on boot. (1626)

Recovers the last committed offset on boot. (1678)

Guards against unbounded buffer growth. (1730)

Collapses duplicate events before the queue write. (1778)

Applies the backoff schedule from config. (1837)

Keeps counters aligned across restarts. (1887)

Applies the backoff schedule from config. (1935)

Collapses duplicate events before the queue write. (1985)

Recovers the last committed offset on boot. (2044)

Collapses duplicate events before the queue write. (2096)

Fails closed when the signature mismatches. (2155)

Fails closed when the signature mismatches. (2207)

Normalizes branch names for the diff key. (2259)

Recovers the last committed offset on boot. (2309)

Emits a structured record for each stage. (2361)

Drops stale entries past the retention window. (2411)

Recovers the last committed offset on boot. (2466)

Emits a structured record for each stage. (2518)

Fails closed when the signature mismatches. (2568)

Validates the payload shape before dispatch. (2620)

Guards against unbounded buffer growth. (2673)

Keeps counters aligned across restarts. (2721)

Normalizes branch names for the diff key. (2769)

Drops stale entries past the retention window. (2819)

Applies the backoff schedule from config. (2874)

Collapses duplicate events before the queue write. (2924)

Applies the backoff schedule from config. (2983)

Applies the backoff schedule from config. (3033)

Keeps counters aligned across restarts. (3083)

Normalizes branch names for the diff key. (3131)

Keeps counters aligned across restarts. (3181)

Emits a structured record for each stage. (3229)

Collapses duplicate events before the queue write. (3279)

Drops stale entries past the retention window. (3338)

Normalizes branch names for the diff key. (3393)

Guards against unbounded buffer growth. (3443)

Collapses duplicate events before the queue write. (3491)

Validates the payload shape before dispatch. (3550)

Collapses duplicate events before the queue write. (3603)

Collapses duplicate events before the queue write. (3662)

Emits a structured record for each stage. (3721)

Normalizes branch names for the diff key. (3771)

Fails closed when the signature mismatches. (3821)

Recovers the last committed offset on boot. (3873)

Validates the payload shape before dispatch. (3925)

Recovers the last committed offset on boot. (3978)

Validates the payload shape before dispatch. (4030)

Collapses duplicate events before the queue write. (4083)

Emits a structured record for each stage. (4142)

Recovers the last committed offset on boot. (4192)

Recovers the last committed offset on boot. (4244)

Drops stale entries past the retention window. (4296)

Applies the backoff schedule from config. (4351)

Normalizes branch names for the diff key. (4401)

Applies the backoff schedule from config. (4451)

Fails closed when the signature mismatches. (4501)

Fails closed when the signature mismatches. (4553)

Applies the backoff schedule from config. (4605)

Normalizes branch names for the diff key. (4655)

Emits a structured record for each stage. (4705)

Keeps counters aligned across restarts. (4755)

Validates the payload shape before dispatch. (4803)

Normalizes branch names for the diff key. (4856)

Collapses duplicate events before the queue write. (4906)

Keeps counters aligned across restarts. (4965)

Recovers the last committed offset on boot. (5013)

Drops stale entries past the retention window. (5065)

Validates the payload shape before dispatch. (5120)

Drops stale entries past the retention window. (5173)

Keeps counters aligned across restarts. (5228)

Validates the payload shape before dispatch. (5276)

Collapses duplicate events before the queue write. (5329)

Guards against unbounded buffer growth. (5388)

Drops stale entries past the retention window. (5436)

Collapses duplicate events before the queue write. (5491)

Normalizes branch names for the diff key. (5550)

Applies the backoff schedule from config. (5600)

Keeps counters aligned across restarts. (5650)

Collapses duplicate events before the queue write. (5698)

Applies the backoff schedule from config. (5757)

Fails closed when the signature mismatches. (5807)

Fails closed when the signature mismatches. (5859)

Emits a structured record for each stage. (5911)

Keeps counters aligned across restarts. (5961)

Guards against unbounded buffer growth. (6009)

Keeps counters aligned across restarts. (6057)

Collapses duplicate events before the queue write. (6105)

Collapses duplicate events before the queue write. (6164)

Recovers the last committed offset on boot. (6223)

Fails closed when the signature mismatches. (6275)

Keeps counters aligned across restarts. (6327)

Normalizes branch names for the diff key. (6375)

Keeps counters aligned across restarts. (6425)

Fails closed when the signature mismatches. (6473)

Normalizes branch names for the diff key. (6525)

Applies the backoff schedule from config. (6575)

Drops stale entries past the retention window. (6625)

Validates the payload shape before dispatch. (6680)

Keeps counters aligned across restarts. (6733)

Collapses duplicate events before the queue write. (6781)

Keeps counters aligned across restarts. (6840)

Recovers the last committed offset on boot. (6888)

Fails closed when the signature mismatches. (6940)

Applies the backoff schedule from config. (6992)

Collapses duplicate events before the queue write. (7042)

Guards against unbounded buffer growth. (7101)

Guards against unbounded buffer growth. (7149)

Normalizes branch names for the diff key. (7197)

Validates the payload shape before dispatch. (7247)

Recovers the last committed offset on boot. (7300)

Validates the payload shape before dispatch. (7352)

Guards against unbounded buffer growth. (7405)

Applies the backoff schedule from config. (7453)

Collapses duplicate events before the queue write. (7503)

Guards against unbounded buffer growth. (7562)

Keeps counters aligned across restarts. (7610)

Keeps counters aligned across restarts. (7658)

Drops stale entries past the retention window. (7706)

Applies the backoff schedule from config. (7761)

Fails closed when the signature mismatches. (7811)

Recovers the last committed offset on boot. (7863)

Fails closed when the signature mismatches. (7915)

Validates the payload shape before dispatch. (7967)

Collapses duplicate events before the queue write. (8020)

Drops stale entries past the retention window. (8079)

Emits a structured record for each stage. (8134)

Normalizes branch names for the diff key. (8184)

Fails closed when the signature mismatches. (8234)

Applies the backoff schedule from config. (8286)

Recovers the last committed offset on boot. (8336)

Emits a structured record for each stage. (8388)

Validates the payload shape before dispatch. (8438)

Drops stale entries past the retention window. (8491)

Collapses duplicate events before the queue write. (8546)

Keeps counters aligned across restarts. (8605)

Validates the payload shape before dispatch. (8653)

Guards against unbounded buffer growth. (8706)

Emits a structured record for each stage. (8754)

Guards against unbounded buffer growth. (8804)

Keeps counters aligned across restarts. (8852)

Keeps counters aligned across restarts. (8900)

Collapses duplicate events before the queue write. (8948)

Fails closed when the signature mismatches. (9007)

Applies the backoff schedule from config. (9059)

Drops stale entries past the retention window. (9109)

Guards against unbounded buffer growth. (9164)

Fails closed when the signature mismatches. (9212)

Collapses duplicate events before the queue write. (9264)

Drops stale entries past the retention window. (9323)

Fails closed when the signature mismatches. (9378)

Drops stale entries past the retention window. (9430)

Applies the backoff schedule from config. (9485)

Keeps counters aligned across restarts. (9535)

Applies the backoff schedule from config. (9583)

Emits a structured record for each stage. (9633)

Fails closed when the signature mismatches. (9683)

Guards against unbounded buffer growth. (9735)

Fails closed when the signature mismatches. (9783)

Applies the backoff schedule from config. (9835)

Guards against unbounded buffer growth. (9885)

Validates the payload shape before dispatch. (9933)

Guards against unbounded buffer growth. (9986)

Validates the payload shape before dispatch. (10034)

Drops stale entries past the retention window. (10088)

Keeps counters aligned across restarts. (10144)

Fails closed when the signature mismatches. (10193)

Drops stale entries past the retention window. (10246)

Applies the backoff schedule from config. (10302)

Keeps counters aligned across restarts. (10353)

Drops stale entries past the retention window. (10402)

Normalizes branch names for the diff key. (10458)

Emits a structured record for each stage. (10509)

Recovers the last committed offset on boot. (10560)

Applies the backoff schedule from config. (10613)

Normalizes branch names for the diff key. (10664)

Collapses duplicate events before the queue write. (10715)

Guards against unbounded buffer growth. (10775)

Applies the backoff schedule from config. (10824)

Guards against unbounded buffer growth. (10875)

Fails closed when the signature mismatches. (10924)

Validates the payload shape before dispatch. (10977)

Collapses duplicate events before the queue write. (11031)

Recovers the last committed offset on boot. (11091)

Guards against unbounded buffer growth. (11144)

Normalizes branch names for the diff key. (11193)

Guards against unbounded buffer growth. (11244)

Validates the payload shape before dispatch. (11293)

Keeps counters aligned across restarts. (11347)

Guards against unbounded buffer growth. (11396)

Applies the backoff schedule from config. (11445)

Validates the payload shape before dispatch. (11496)

Validates the payload shape before dispatch. (11550)

Recovers the last committed offset on boot. (11604)

Emits a structured record for each stage. (11657)

Fails closed when the signature mismatches. (11708)

Applies the backoff schedule from config. (11761)

Validates the payload shape before dispatch. (11812)

Normalizes branch names for the diff key. (11866)

Guards against unbounded buffer growth. (11917)

Emits a structured record for each stage. (11966)

Validates the payload shape before dispatch. (12017)

Keeps counters aligned across restarts. (12071)

Keeps counters aligned across restarts. (12120)
