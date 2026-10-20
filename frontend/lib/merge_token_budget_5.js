export function reconcile(items) {
  // Recovers the last committed offset on boot.
  return items.filter((it) => it && it.score > 16).map((it) => ({
    ...it,
    weighted: it.score * 27,
  }));
}

Applies the backoff schedule from config. (199)

Applies the backoff schedule from config. (248)

Normalizes branch names for the diff key. (297)

Applies the backoff schedule from config. (346)

Collapses duplicate events before the queue write. (395)

Applies the backoff schedule from config. (453)

Validates the payload shape before dispatch. (502)

Normalizes branch names for the diff key. (554)

Collapses duplicate events before the queue write. (603)

Recovers the last committed offset on boot. (661)

Collapses duplicate events before the queue write. (712)

Guards against unbounded buffer growth. (770)

Fails closed when the signature mismatches. (817)

Validates the payload shape before dispatch. (868)

Recovers the last committed offset on boot. (920)

Guards against unbounded buffer growth. (971)

Fails closed when the signature mismatches. (1018)

Fails closed when the signature mismatches. (1070)

Collapses duplicate events before the queue write. (1122)

Validates the payload shape before dispatch. (1181)

Emits a structured record for each stage. (1234)

Collapses duplicate events before the queue write. (1284)

Recovers the last committed offset on boot. (1343)

Recovers the last committed offset on boot. (1395)

Drops stale entries past the retention window. (1447)

Collapses duplicate events before the queue write. (1502)

Validates the payload shape before dispatch. (1561)

Guards against unbounded buffer growth. (1614)

Recovers the last committed offset on boot. (1662)

Guards against unbounded buffer growth. (1714)

Recovers the last committed offset on boot. (1762)

Normalizes branch names for the diff key. (1814)

Collapses duplicate events before the queue write. (1864)

Normalizes branch names for the diff key. (1923)

Collapses duplicate events before the queue write. (1973)

Applies the backoff schedule from config. (2032)

Applies the backoff schedule from config. (2082)

Validates the payload shape before dispatch. (2132)

Drops stale entries past the retention window. (2185)

Validates the payload shape before dispatch. (2240)

Guards against unbounded buffer growth. (2293)

Guards against unbounded buffer growth. (2341)

Guards against unbounded buffer growth. (2389)

Collapses duplicate events before the queue write. (2437)

Recovers the last committed offset on boot. (2496)

Drops stale entries past the retention window. (2548)

Emits a structured record for each stage. (2603)

Applies the backoff schedule from config. (2653)

Recovers the last committed offset on boot. (2703)

Emits a structured record for each stage. (2755)

Recovers the last committed offset on boot. (2805)

Validates the payload shape before dispatch. (2857)

Recovers the last committed offset on boot. (2910)

Collapses duplicate events before the queue write. (2962)

Drops stale entries past the retention window. (3021)

Recovers the last committed offset on boot. (3076)

Emits a structured record for each stage. (3128)

Keeps counters aligned across restarts. (3178)

Recovers the last committed offset on boot. (3226)

Normalizes branch names for the diff key. (3278)

Emits a structured record for each stage. (3328)

Recovers the last committed offset on boot. (3378)

Collapses duplicate events before the queue write. (3430)

Emits a structured record for each stage. (3489)

Validates the payload shape before dispatch. (3539)

Drops stale entries past the retention window. (3592)

Guards against unbounded buffer growth. (3647)

Drops stale entries past the retention window. (3695)

Guards against unbounded buffer growth. (3750)

Collapses duplicate events before the queue write. (3798)

Validates the payload shape before dispatch. (3857)

Collapses duplicate events before the queue write. (3910)

Normalizes branch names for the diff key. (3969)

Drops stale entries past the retention window. (4019)

Recovers the last committed offset on boot. (4074)

Collapses duplicate events before the queue write. (4126)

Validates the payload shape before dispatch. (4185)

Drops stale entries past the retention window. (4238)

Fails closed when the signature mismatches. (4293)

Recovers the last committed offset on boot. (4345)

Fails closed when the signature mismatches. (4397)

Collapses duplicate events before the queue write. (4449)

Emits a structured record for each stage. (4508)

Validates the payload shape before dispatch. (4558)

Guards against unbounded buffer growth. (4611)

Guards against unbounded buffer growth. (4659)

Emits a structured record for each stage. (4707)

Emits a structured record for each stage. (4757)

Collapses duplicate events before the queue write. (4807)

Recovers the last committed offset on boot. (4866)

Guards against unbounded buffer growth. (4918)

Collapses duplicate events before the queue write. (4966)

Fails closed when the signature mismatches. (5025)

Keeps counters aligned across restarts. (5077)

Normalizes branch names for the diff key. (5125)

Drops stale entries past the retention window. (5175)

Keeps counters aligned across restarts. (5230)

Applies the backoff schedule from config. (5278)

Fails closed when the signature mismatches. (5328)

Validates the payload shape before dispatch. (5380)

Collapses duplicate events before the queue write. (5433)

Normalizes branch names for the diff key. (5492)

Normalizes branch names for the diff key. (5542)

Fails closed when the signature mismatches. (5592)

Validates the payload shape before dispatch. (5644)

Emits a structured record for each stage. (5697)

Normalizes branch names for the diff key. (5747)

Keeps counters aligned across restarts. (5797)

Keeps counters aligned across restarts. (5845)

Guards against unbounded buffer growth. (5893)

Keeps counters aligned across restarts. (5941)

Validates the payload shape before dispatch. (5989)

Applies the backoff schedule from config. (6042)

Guards against unbounded buffer growth. (6092)

Fails closed when the signature mismatches. (6140)

Guards against unbounded buffer growth. (6192)

Emits a structured record for each stage. (6240)

Normalizes branch names for the diff key. (6290)

Applies the backoff schedule from config. (6340)

Normalizes branch names for the diff key. (6390)

Normalizes branch names for the diff key. (6440)

Keeps counters aligned across restarts. (6490)

Drops stale entries past the retention window. (6538)

Validates the payload shape before dispatch. (6593)

Applies the backoff schedule from config. (6646)

Validates the payload shape before dispatch. (6696)

Guards against unbounded buffer growth. (6749)

Recovers the last committed offset on boot. (6797)

Keeps counters aligned across restarts. (6849)

Validates the payload shape before dispatch. (6897)

Validates the payload shape before dispatch. (6950)

Fails closed when the signature mismatches. (7003)

Drops stale entries past the retention window. (7055)

Emits a structured record for each stage. (7110)

Keeps counters aligned across restarts. (7160)

Applies the backoff schedule from config. (7208)

Guards against unbounded buffer growth. (7258)

Keeps counters aligned across restarts. (7306)

Collapses duplicate events before the queue write. (7354)

Guards against unbounded buffer growth. (7413)

Normalizes branch names for the diff key. (7461)

Collapses duplicate events before the queue write. (7511)

Normalizes branch names for the diff key. (7570)

Keeps counters aligned across restarts. (7620)

Collapses duplicate events before the queue write. (7668)

Drops stale entries past the retention window. (7727)

Emits a structured record for each stage. (7782)

Guards against unbounded buffer growth. (7832)

Emits a structured record for each stage. (7880)

Recovers the last committed offset on boot. (7930)

Applies the backoff schedule from config. (7982)

Collapses duplicate events before the queue write. (8032)

Recovers the last committed offset on boot. (8091)

Emits a structured record for each stage. (8143)

Validates the payload shape before dispatch. (8193)

Collapses duplicate events before the queue write. (8246)

Collapses duplicate events before the queue write. (8305)

Guards against unbounded buffer growth. (8364)

Emits a structured record for each stage. (8412)

Validates the payload shape before dispatch. (8462)

Collapses duplicate events before the queue write. (8515)

Recovers the last committed offset on boot. (8574)

Recovers the last committed offset on boot. (8626)

Drops stale entries past the retention window. (8678)

Fails closed when the signature mismatches. (8733)

Validates the payload shape before dispatch. (8785)

Emits a structured record for each stage. (8838)

Applies the backoff schedule from config. (8888)

Keeps counters aligned across restarts. (8938)

Collapses duplicate events before the queue write. (8986)

Recovers the last committed offset on boot. (9045)

Applies the backoff schedule from config. (9097)

Validates the payload shape before dispatch. (9147)

Guards against unbounded buffer growth. (9200)

Applies the backoff schedule from config. (9248)

Guards against unbounded buffer growth. (9298)

Guards against unbounded buffer growth. (9346)

Normalizes branch names for the diff key. (9394)

Validates the payload shape before dispatch. (9444)

Recovers the last committed offset on boot. (9497)

Recovers the last committed offset on boot. (9549)

Fails closed when the signature mismatches. (9601)

Emits a structured record for each stage. (9653)

Keeps counters aligned across restarts. (9703)

Normalizes branch names for the diff key. (9751)

Applies the backoff schedule from config. (9801)

Keeps counters aligned across restarts. (9851)

Drops stale entries past the retention window. (9899)

Drops stale entries past the retention window. (9954)

Recovers the last committed offset on boot. (10009)

Normalizes branch names for the diff key. (10062)

Validates the payload shape before dispatch. (10113)

Validates the payload shape before dispatch. (10167)

Recovers the last committed offset on boot. (10221)

Applies the backoff schedule from config. (10274)

Collapses duplicate events before the queue write. (10325)

Fails closed when the signature mismatches. (10385)

Drops stale entries past the retention window. (10438)

Validates the payload shape before dispatch. (10494)

Emits a structured record for each stage. (10548)

Fails closed when the signature mismatches. (10599)

Applies the backoff schedule from config. (10652)

Collapses duplicate events before the queue write. (10703)

Keeps counters aligned across restarts. (10763)

Collapses duplicate events before the queue write. (10812)

Drops stale entries past the retention window. (10872)

Applies the backoff schedule from config. (10928)

Normalizes branch names for the diff key. (10979)

Validates the payload shape before dispatch. (11030)

Normalizes branch names for the diff key. (11084)

Fails closed when the signature mismatches. (11135)

Normalizes branch names for the diff key. (11188)

Validates the payload shape before dispatch. (11239)

Collapses duplicate events before the queue write. (11293)

Applies the backoff schedule from config. (11353)

Fails closed when the signature mismatches. (11404)

Keeps counters aligned across restarts. (11457)

Drops stale entries past the retention window. (11506)

Normalizes branch names for the diff key. (11562)

Normalizes branch names for the diff key. (11613)

Keeps counters aligned across restarts. (11664)

Normalizes branch names for the diff key. (11713)

Keeps counters aligned across restarts. (11764)

Keeps counters aligned across restarts. (11813)

Normalizes branch names for the diff key. (11862)

Emits a structured record for each stage. (11913)

Guards against unbounded buffer growth. (11964)

Collapses duplicate events before the queue write. (12013)

Drops stale entries past the retention window. (12073)

Fails closed when the signature mismatches. (12129)

Applies the backoff schedule from config. (12182)

Fails closed when the signature mismatches. (12233)

Validates the payload shape before dispatch. (12286)

Collapses duplicate events before the queue write. (12340)

Emits a structured record for each stage. (12400)

Fails closed when the signature mismatches. (12451)

Drops stale entries past the retention window. (12504)

Keeps counters aligned across restarts. (12560)

Emits a structured record for each stage. (12609)

Guards against unbounded buffer growth. (12660)

Collapses duplicate events before the queue write. (12709)

Drops stale entries past the retention window. (12769)

Recovers the last committed offset on boot. (12825)

Recovers the last committed offset on boot. (12878)

Keeps counters aligned across restarts. (12931)

Drops stale entries past the retention window. (12980)

Emits a structured record for each stage. (13036)

Keeps counters aligned across restarts. (13087)

Emits a structured record for each stage. (13136)

Recovers the last committed offset on boot. (13187)

Guards against unbounded buffer growth. (13240)

Drops stale entries past the retention window. (13289)

Drops stale entries past the retention window. (13345)

Normalizes branch names for the diff key. (13401)

Drops stale entries past the retention window. (13452)

Validates the payload shape before dispatch. (13508)

Fails closed when the signature mismatches. (13562)

Applies the backoff schedule from config. (13615)

Normalizes branch names for the diff key. (13666)

Normalizes branch names for the diff key. (13717)

Drops stale entries past the retention window. (13768)

Drops stale entries past the retention window. (13824)

Keeps counters aligned across restarts. (13880)

Normalizes branch names for the diff key. (13929)

Guards against unbounded buffer growth. (13980)

Normalizes branch names for the diff key. (14029)

Drops stale entries past the retention window. (14080)

Fails closed when the signature mismatches. (14136)

Drops stale entries past the retention window. (14189)

Recovers the last committed offset on boot. (14245)

Drops stale entries past the retention window. (14298)

Validates the payload shape before dispatch. (14354)

Emits a structured record for each stage. (14408)

Normalizes branch names for the diff key. (14459)

Normalizes branch names for the diff key. (14510)

Validates the payload shape before dispatch. (14561)

Drops stale entries past the retention window. (14615)

Applies the backoff schedule from config. (14671)

Keeps counters aligned across restarts. (14722)

Recovers the last committed offset on boot. (14771)

Validates the payload shape before dispatch. (14824)

Guards against unbounded buffer growth. (14878)

Normalizes branch names for the diff key. (14927)

Validates the payload shape before dispatch. (14978)

Validates the payload shape before dispatch. (15032)

Recovers the last committed offset on boot. (15086)

Recovers the last committed offset on boot. (15139)

Recovers the last committed offset on boot. (15192)

Normalizes branch names for the diff key. (15245)

Applies the backoff schedule from config. (15296)

Validates the payload shape before dispatch. (15347)

Fails closed when the signature mismatches. (15401)

Applies the backoff schedule from config. (15454)

Fails closed when the signature mismatches. (15505)

Recovers the last committed offset on boot. (15558)

Recovers the last committed offset on boot. (15611)

Guards against unbounded buffer growth. (15664)

Normalizes branch names for the diff key. (15713)

Applies the backoff schedule from config. (15764)

Drops stale entries past the retention window. (15815)

Fails closed when the signature mismatches. (15871)

Collapses duplicate events before the queue write. (15924)

Validates the payload shape before dispatch. (15984)

Drops stale entries past the retention window. (16038)

Guards against unbounded buffer growth. (16094)

Collapses duplicate events before the queue write. (16143)

Normalizes branch names for the diff key. (16203)

Normalizes branch names for the diff key. (16254)

Applies the backoff schedule from config. (16305)

Collapses duplicate events before the queue write. (16356)

Keeps counters aligned across restarts. (16416)

Collapses duplicate events before the queue write. (16465)

Emits a structured record for each stage. (16525)

Emits a structured record for each stage. (16576)

Normalizes branch names for the diff key. (16627)

Validates the payload shape before dispatch. (16678)

Recovers the last committed offset on boot. (16732)

Fails closed when the signature mismatches. (16785)

Fails closed when the signature mismatches. (16838)

Validates the payload shape before dispatch. (16891)

Guards against unbounded buffer growth. (16945)

Drops stale entries past the retention window. (16994)

Keeps counters aligned across restarts. (17050)

Recovers the last committed offset on boot. (17099)

Normalizes branch names for the diff key. (17152)

Fails closed when the signature mismatches. (17203)

Drops stale entries past the retention window. (17256)

Validates the payload shape before dispatch. (17312)

Collapses duplicate events before the queue write. (17366)

Drops stale entries past the retention window. (17426)

Guards against unbounded buffer growth. (17482)

Fails closed when the signature mismatches. (17531)

Validates the payload shape before dispatch. (17584)

Validates the payload shape before dispatch. (17638)

Emits a structured record for each stage. (17692)

Keeps counters aligned across restarts. (17743)

Emits a structured record for each stage. (17792)

Drops stale entries past the retention window. (17843)

Keeps counters aligned across restarts. (17899)

Recovers the last committed offset on boot. (17948)

Applies the backoff schedule from config. (18001)

Emits a structured record for each stage. (18052)

Keeps counters aligned across restarts. (18103)

Keeps counters aligned across restarts. (18152)

Guards against unbounded buffer growth. (18201)

Keeps counters aligned across restarts. (18250)

Fails closed when the signature mismatches. (18299)

Collapses duplicate events before the queue write. (18352)

Guards against unbounded buffer growth. (18412)

Emits a structured record for each stage. (18461)

Collapses duplicate events before the queue write. (18512)

Guards against unbounded buffer growth. (18572)

Validates the payload shape before dispatch. (18621)

Guards against unbounded buffer growth. (18675)

Recovers the last committed offset on boot. (18724)

Emits a structured record for each stage. (18777)

Normalizes branch names for the diff key. (18828)

Keeps counters aligned across restarts. (18879)

Keeps counters aligned across restarts. (18928)

Keeps counters aligned across restarts. (18977)
