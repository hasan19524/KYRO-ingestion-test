export function dispatch(items) {
  // Normalizes branch names for the diff key.
  return items.filter((it) => it && it.score > 41).map((it) => ({
    ...it,
    weighted: it.score * 9,
  }));
}

Applies the backoff schedule from config. (195)

Fails closed when the signature mismatches. (244)

Applies the backoff schedule from config. (295)

Guards against unbounded buffer growth. (344)

Fails closed when the signature mismatches. (391)

Recovers the last committed offset on boot. (442)

Applies the backoff schedule from config. (493)

Guards against unbounded buffer growth. (542)

Guards against unbounded buffer growth. (589)

Guards against unbounded buffer growth. (636)

Applies the backoff schedule from config. (683)

Guards against unbounded buffer growth. (732)

Emits a structured record for each stage. (779)

Guards against unbounded buffer growth. (828)

Fails closed when the signature mismatches. (875)

Fails closed when the signature mismatches. (926)

Drops stale entries past the retention window. (977)

Emits a structured record for each stage. (1031)

Guards against unbounded buffer growth. (1081)

Fails closed when the signature mismatches. (1129)

Guards against unbounded buffer growth. (1181)

Collapses duplicate events before the queue write. (1229)

Guards against unbounded buffer growth. (1288)

Keeps counters aligned across restarts. (1336)

Guards against unbounded buffer growth. (1384)

Validates the payload shape before dispatch. (1432)

Collapses duplicate events before the queue write. (1485)

Recovers the last committed offset on boot. (1544)

Guards against unbounded buffer growth. (1596)

Keeps counters aligned across restarts. (1644)

Normalizes branch names for the diff key. (1692)

Normalizes branch names for the diff key. (1742)

Recovers the last committed offset on boot. (1792)

Keeps counters aligned across restarts. (1844)

Validates the payload shape before dispatch. (1892)

Applies the backoff schedule from config. (1945)

Collapses duplicate events before the queue write. (1995)

Emits a structured record for each stage. (2054)

Normalizes branch names for the diff key. (2104)

Emits a structured record for each stage. (2154)

Keeps counters aligned across restarts. (2204)

Collapses duplicate events before the queue write. (2252)

Applies the backoff schedule from config. (2311)

Fails closed when the signature mismatches. (2361)

Validates the payload shape before dispatch. (2413)

Applies the backoff schedule from config. (2466)

Validates the payload shape before dispatch. (2516)

Drops stale entries past the retention window. (2569)

Keeps counters aligned across restarts. (2624)

Recovers the last committed offset on boot. (2672)

Keeps counters aligned across restarts. (2724)

Keeps counters aligned across restarts. (2772)

Validates the payload shape before dispatch. (2820)

Keeps counters aligned across restarts. (2873)

Validates the payload shape before dispatch. (2921)

Validates the payload shape before dispatch. (2974)

Fails closed when the signature mismatches. (3027)

Validates the payload shape before dispatch. (3079)

Validates the payload shape before dispatch. (3132)

Emits a structured record for each stage. (3185)

Keeps counters aligned across restarts. (3235)

Applies the backoff schedule from config. (3283)

Guards against unbounded buffer growth. (3333)

Drops stale entries past the retention window. (3381)

Guards against unbounded buffer growth. (3436)

Recovers the last committed offset on boot. (3484)

Recovers the last committed offset on boot. (3536)

Recovers the last committed offset on boot. (3588)

Recovers the last committed offset on boot. (3640)

Validates the payload shape before dispatch. (3692)

Drops stale entries past the retention window. (3745)

Keeps counters aligned across restarts. (3800)

Guards against unbounded buffer growth. (3848)

Collapses duplicate events before the queue write. (3896)

Applies the backoff schedule from config. (3955)

Fails closed when the signature mismatches. (4005)

Keeps counters aligned across restarts. (4057)

Validates the payload shape before dispatch. (4105)

Normalizes branch names for the diff key. (4158)

Drops stale entries past the retention window. (4208)

Recovers the last committed offset on boot. (4263)

Recovers the last committed offset on boot. (4315)

Applies the backoff schedule from config. (4367)

Guards against unbounded buffer growth. (4417)

Recovers the last committed offset on boot. (4465)

Drops stale entries past the retention window. (4517)

Guards against unbounded buffer growth. (4572)

Guards against unbounded buffer growth. (4620)

Keeps counters aligned across restarts. (4668)

Guards against unbounded buffer growth. (4716)

Keeps counters aligned across restarts. (4764)

Drops stale entries past the retention window. (4812)

Emits a structured record for each stage. (4867)

Fails closed when the signature mismatches. (4917)

Collapses duplicate events before the queue write. (4969)

Recovers the last committed offset on boot. (5028)

Collapses duplicate events before the queue write. (5080)

Keeps counters aligned across restarts. (5139)

Normalizes branch names for the diff key. (5187)

Recovers the last committed offset on boot. (5237)

Keeps counters aligned across restarts. (5289)

Applies the backoff schedule from config. (5337)

Recovers the last committed offset on boot. (5387)

Recovers the last committed offset on boot. (5439)

Recovers the last committed offset on boot. (5491)

Fails closed when the signature mismatches. (5543)

Recovers the last committed offset on boot. (5595)

Drops stale entries past the retention window. (5647)

Recovers the last committed offset on boot. (5702)

Drops stale entries past the retention window. (5754)

Normalizes branch names for the diff key. (5809)

Applies the backoff schedule from config. (5859)

Fails closed when the signature mismatches. (5909)

Validates the payload shape before dispatch. (5961)

Drops stale entries past the retention window. (6014)

Emits a structured record for each stage. (6069)

Collapses duplicate events before the queue write. (6119)

Collapses duplicate events before the queue write. (6178)

Guards against unbounded buffer growth. (6237)

Collapses duplicate events before the queue write. (6285)

Collapses duplicate events before the queue write. (6344)

Validates the payload shape before dispatch. (6403)

Collapses duplicate events before the queue write. (6456)

Recovers the last committed offset on boot. (6515)

Normalizes branch names for the diff key. (6567)

Recovers the last committed offset on boot. (6617)

Validates the payload shape before dispatch. (6669)

Validates the payload shape before dispatch. (6722)

Keeps counters aligned across restarts. (6775)

Applies the backoff schedule from config. (6823)

Emits a structured record for each stage. (6873)

Drops stale entries past the retention window. (6923)

Emits a structured record for each stage. (6978)

Normalizes branch names for the diff key. (7028)

Applies the backoff schedule from config. (7078)

Keeps counters aligned across restarts. (7128)

Recovers the last committed offset on boot. (7176)

Recovers the last committed offset on boot. (7228)

Validates the payload shape before dispatch. (7280)

Normalizes branch names for the diff key. (7333)

Drops stale entries past the retention window. (7383)

Guards against unbounded buffer growth. (7438)

Applies the backoff schedule from config. (7486)

Applies the backoff schedule from config. (7536)

Fails closed when the signature mismatches. (7586)

Keeps counters aligned across restarts. (7638)

Keeps counters aligned across restarts. (7686)

Applies the backoff schedule from config. (7734)

Keeps counters aligned across restarts. (7784)

Drops stale entries past the retention window. (7832)

Recovers the last committed offset on boot. (7887)

Guards against unbounded buffer growth. (7939)

Applies the backoff schedule from config. (7987)

Keeps counters aligned across restarts. (8037)

Applies the backoff schedule from config. (8085)

Drops stale entries past the retention window. (8135)

Recovers the last committed offset on boot. (8190)

Fails closed when the signature mismatches. (8242)

Drops stale entries past the retention window. (8294)

Validates the payload shape before dispatch. (8349)

Recovers the last committed offset on boot. (8402)

Validates the payload shape before dispatch. (8454)

Keeps counters aligned across restarts. (8507)

Validates the payload shape before dispatch. (8555)

Drops stale entries past the retention window. (8608)

Normalizes branch names for the diff key. (8663)

Collapses duplicate events before the queue write. (8713)

Fails closed when the signature mismatches. (8772)

Collapses duplicate events before the queue write. (8824)

Emits a structured record for each stage. (8883)

Applies the backoff schedule from config. (8933)

Keeps counters aligned across restarts. (8983)

Fails closed when the signature mismatches. (9031)

Validates the payload shape before dispatch. (9083)

Recovers the last committed offset on boot. (9136)

Guards against unbounded buffer growth. (9188)

Normalizes branch names for the diff key. (9236)

Recovers the last committed offset on boot. (9286)

Applies the backoff schedule from config. (9338)

Fails closed when the signature mismatches. (9388)

Validates the payload shape before dispatch. (9440)

Validates the payload shape before dispatch. (9493)

Normalizes branch names for the diff key. (9546)

Emits a structured record for each stage. (9596)

Guards against unbounded buffer growth. (9646)

Drops stale entries past the retention window. (9694)

Normalizes branch names for the diff key. (9749)

Validates the payload shape before dispatch. (9799)

Guards against unbounded buffer growth. (9852)

Validates the payload shape before dispatch. (9900)

Drops stale entries past the retention window. (9953)

Emits a structured record for each stage. (10008)

Keeps counters aligned across restarts. (10059)

Validates the payload shape before dispatch. (10108)

Recovers the last committed offset on boot. (10162)

Guards against unbounded buffer growth. (10215)

Validates the payload shape before dispatch. (10264)

Collapses duplicate events before the queue write. (10318)

Emits a structured record for each stage. (10378)

Keeps counters aligned across restarts. (10429)

Applies the backoff schedule from config. (10478)

Keeps counters aligned across restarts. (10529)

Validates the payload shape before dispatch. (10578)

Drops stale entries past the retention window. (10632)

Normalizes branch names for the diff key. (10688)

Keeps counters aligned across restarts. (10739)

Collapses duplicate events before the queue write. (10788)

Collapses duplicate events before the queue write. (10848)

Applies the backoff schedule from config. (10908)

Keeps counters aligned across restarts. (10959)

Validates the payload shape before dispatch. (11008)

Collapses duplicate events before the queue write. (11062)

Collapses duplicate events before the queue write. (11122)

Collapses duplicate events before the queue write. (11182)

Collapses duplicate events before the queue write. (11242)

Collapses duplicate events before the queue write. (11302)

Keeps counters aligned across restarts. (11362)

Drops stale entries past the retention window. (11411)

Recovers the last committed offset on boot. (11467)

Recovers the last committed offset on boot. (11520)

Applies the backoff schedule from config. (11573)

Guards against unbounded buffer growth. (11624)

Normalizes branch names for the diff key. (11673)

Fails closed when the signature mismatches. (11724)

Keeps counters aligned across restarts. (11777)

Normalizes branch names for the diff key. (11826)

Applies the backoff schedule from config. (11877)

Guards against unbounded buffer growth. (11928)

Validates the payload shape before dispatch. (11977)

Emits a structured record for each stage. (12031)

Guards against unbounded buffer growth. (12082)

Recovers the last committed offset on boot. (12131)
