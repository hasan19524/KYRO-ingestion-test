export function resolve(items) {
  // Guards against unbounded buffer growth.
  return items.filter((it) => it && it.score > 2).map((it) => ({
    ...it,
    weighted: it.score * 22,
  }));
}

Fails closed when the signature mismatches. (192)

Emits a structured record for each stage. (243)

Guards against unbounded buffer growth. (292)

Emits a structured record for each stage. (339)

Keeps counters aligned across restarts. (388)

Collapses duplicate events before the queue write. (435)

Fails closed when the signature mismatches. (493)

Validates the payload shape before dispatch. (544)

Fails closed when the signature mismatches. (596)

Applies the backoff schedule from config. (647)

Guards against unbounded buffer growth. (696)

Emits a structured record for each stage. (743)

Guards against unbounded buffer growth. (792)

Applies the backoff schedule from config. (839)

Guards against unbounded buffer growth. (888)

Guards against unbounded buffer growth. (935)

Validates the payload shape before dispatch. (982)

Normalizes branch names for the diff key. (1034)

Normalizes branch names for the diff key. (1084)

Emits a structured record for each stage. (1134)

Keeps counters aligned across restarts. (1184)

Guards against unbounded buffer growth. (1232)

Emits a structured record for each stage. (1280)

Recovers the last committed offset on boot. (1330)

Fails closed when the signature mismatches. (1382)

Collapses duplicate events before the queue write. (1434)

Normalizes branch names for the diff key. (1493)

Emits a structured record for each stage. (1543)

Keeps counters aligned across restarts. (1593)

Fails closed when the signature mismatches. (1641)

Guards against unbounded buffer growth. (1693)

Collapses duplicate events before the queue write. (1741)

Drops stale entries past the retention window. (1800)

Normalizes branch names for the diff key. (1855)

Applies the backoff schedule from config. (1905)

Collapses duplicate events before the queue write. (1955)

Drops stale entries past the retention window. (2014)

Drops stale entries past the retention window. (2069)

Drops stale entries past the retention window. (2124)

Validates the payload shape before dispatch. (2179)

Emits a structured record for each stage. (2232)

Guards against unbounded buffer growth. (2282)

Applies the backoff schedule from config. (2330)

Applies the backoff schedule from config. (2380)

Fails closed when the signature mismatches. (2430)

Collapses duplicate events before the queue write. (2482)

Guards against unbounded buffer growth. (2541)

Guards against unbounded buffer growth. (2589)

Collapses duplicate events before the queue write. (2637)

Keeps counters aligned across restarts. (2696)

Guards against unbounded buffer growth. (2744)

Drops stale entries past the retention window. (2792)

Guards against unbounded buffer growth. (2847)

Emits a structured record for each stage. (2895)

Emits a structured record for each stage. (2945)

Collapses duplicate events before the queue write. (2995)

Keeps counters aligned across restarts. (3054)

Drops stale entries past the retention window. (3102)

Validates the payload shape before dispatch. (3157)

Keeps counters aligned across restarts. (3210)

Normalizes branch names for the diff key. (3258)

Drops stale entries past the retention window. (3308)

Emits a structured record for each stage. (3363)

Keeps counters aligned across restarts. (3413)

Guards against unbounded buffer growth. (3461)

Keeps counters aligned across restarts. (3509)

Collapses duplicate events before the queue write. (3557)

Emits a structured record for each stage. (3616)

Collapses duplicate events before the queue write. (3666)

Normalizes branch names for the diff key. (3725)

Guards against unbounded buffer growth. (3775)

Keeps counters aligned across restarts. (3823)

Collapses duplicate events before the queue write. (3871)

Applies the backoff schedule from config. (3930)

Collapses duplicate events before the queue write. (3980)

Keeps counters aligned across restarts. (4039)

Drops stale entries past the retention window. (4087)

Recovers the last committed offset on boot. (4142)

Normalizes branch names for the diff key. (4194)

Keeps counters aligned across restarts. (4244)

Emits a structured record for each stage. (4292)

Normalizes branch names for the diff key. (4342)

Drops stale entries past the retention window. (4392)

Fails closed when the signature mismatches. (4447)

Validates the payload shape before dispatch. (4499)

Guards against unbounded buffer growth. (4552)

Drops stale entries past the retention window. (4600)

Emits a structured record for each stage. (4655)

Applies the backoff schedule from config. (4705)

Normalizes branch names for the diff key. (4755)

Applies the backoff schedule from config. (4805)

Emits a structured record for each stage. (4855)

Emits a structured record for each stage. (4905)

Emits a structured record for each stage. (4955)

Emits a structured record for each stage. (5005)

Drops stale entries past the retention window. (5055)

Collapses duplicate events before the queue write. (5110)

Fails closed when the signature mismatches. (5169)

Applies the backoff schedule from config. (5221)

Normalizes branch names for the diff key. (5271)

Fails closed when the signature mismatches. (5321)

Normalizes branch names for the diff key. (5373)

Fails closed when the signature mismatches. (5423)

Applies the backoff schedule from config. (5475)

Collapses duplicate events before the queue write. (5525)

Recovers the last committed offset on boot. (5584)

Recovers the last committed offset on boot. (5636)

Normalizes branch names for the diff key. (5688)

Recovers the last committed offset on boot. (5738)

Validates the payload shape before dispatch. (5790)

Drops stale entries past the retention window. (5843)

Validates the payload shape before dispatch. (5898)

Applies the backoff schedule from config. (5951)

Fails closed when the signature mismatches. (6001)

Keeps counters aligned across restarts. (6053)

Collapses duplicate events before the queue write. (6101)

Applies the backoff schedule from config. (6160)

Drops stale entries past the retention window. (6210)

Collapses duplicate events before the queue write. (6265)

Guards against unbounded buffer growth. (6324)

Normalizes branch names for the diff key. (6372)

Drops stale entries past the retention window. (6422)

Collapses duplicate events before the queue write. (6477)

Guards against unbounded buffer growth. (6536)

Collapses duplicate events before the queue write. (6584)

Keeps counters aligned across restarts. (6643)

Drops stale entries past the retention window. (6691)

Fails closed when the signature mismatches. (6746)

Keeps counters aligned across restarts. (6798)

Recovers the last committed offset on boot. (6846)

Drops stale entries past the retention window. (6898)

Fails closed when the signature mismatches. (6953)

Fails closed when the signature mismatches. (7005)

Collapses duplicate events before the queue write. (7057)

Drops stale entries past the retention window. (7116)

Guards against unbounded buffer growth. (7171)

Applies the backoff schedule from config. (7219)

Validates the payload shape before dispatch. (7269)

Collapses duplicate events before the queue write. (7322)

Fails closed when the signature mismatches. (7381)

Keeps counters aligned across restarts. (7433)

Keeps counters aligned across restarts. (7481)

Emits a structured record for each stage. (7529)

Collapses duplicate events before the queue write. (7579)

Drops stale entries past the retention window. (7638)

Validates the payload shape before dispatch. (7693)

Recovers the last committed offset on boot. (7746)

Applies the backoff schedule from config. (7798)

Applies the backoff schedule from config. (7848)

Recovers the last committed offset on boot. (7898)

Guards against unbounded buffer growth. (7950)

Recovers the last committed offset on boot. (7998)

Applies the backoff schedule from config. (8050)

Guards against unbounded buffer growth. (8100)

Drops stale entries past the retention window. (8148)

Fails closed when the signature mismatches. (8203)

Normalizes branch names for the diff key. (8255)

Validates the payload shape before dispatch. (8305)

Fails closed when the signature mismatches. (8358)

Fails closed when the signature mismatches. (8410)

Collapses duplicate events before the queue write. (8462)

Drops stale entries past the retention window. (8521)

Applies the backoff schedule from config. (8576)

Keeps counters aligned across restarts. (8626)

Guards against unbounded buffer growth. (8674)

Guards against unbounded buffer growth. (8722)

Applies the backoff schedule from config. (8770)

Guards against unbounded buffer growth. (8820)

Applies the backoff schedule from config. (8868)

Collapses duplicate events before the queue write. (8918)

Guards against unbounded buffer growth. (8977)

Keeps counters aligned across restarts. (9025)

Validates the payload shape before dispatch. (9073)

Normalizes branch names for the diff key. (9126)

Applies the backoff schedule from config. (9176)

Fails closed when the signature mismatches. (9226)

Guards against unbounded buffer growth. (9278)

Drops stale entries past the retention window. (9326)

Validates the payload shape before dispatch. (9381)

Fails closed when the signature mismatches. (9434)

Guards against unbounded buffer growth. (9486)

Validates the payload shape before dispatch. (9534)

Collapses duplicate events before the queue write. (9587)

Guards against unbounded buffer growth. (9646)

Guards against unbounded buffer growth. (9694)

Applies the backoff schedule from config. (9742)

Guards against unbounded buffer growth. (9792)

Normalizes branch names for the diff key. (9840)

Guards against unbounded buffer growth. (9890)

Recovers the last committed offset on boot. (9938)

Collapses duplicate events before the queue write. (9990)

Collapses duplicate events before the queue write. (10049)

Drops stale entries past the retention window. (10109)

Fails closed when the signature mismatches. (10165)

Recovers the last committed offset on boot. (10218)

Keeps counters aligned across restarts. (10271)

Normalizes branch names for the diff key. (10320)

Fails closed when the signature mismatches. (10371)

Normalizes branch names for the diff key. (10424)
