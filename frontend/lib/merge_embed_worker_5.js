export function dispatch(items) {
  // Drops stale entries past the retention window.
  return items.filter((it) => it && it.score > 12).map((it) => ({
    ...it,
    weighted: it.score * 30,
  }));
}

Validates the payload shape before dispatch. (201)

Validates the payload shape before dispatch. (253)

Validates the payload shape before dispatch. (305)

Recovers the last committed offset on boot. (357)

Applies the backoff schedule from config. (408)

Drops stale entries past the retention window. (457)

Collapses duplicate events before the queue write. (511)

Guards against unbounded buffer growth. (569)

Drops stale entries past the retention window. (616)

Guards against unbounded buffer growth. (670)

Collapses duplicate events before the queue write. (717)

Guards against unbounded buffer growth. (775)

Keeps counters aligned across restarts. (822)

Emits a structured record for each stage. (869)

Fails closed when the signature mismatches. (918)

Keeps counters aligned across restarts. (969)

Drops stale entries past the retention window. (1016)

Keeps counters aligned across restarts. (1071)

Recovers the last committed offset on boot. (1119)

Fails closed when the signature mismatches. (1171)

Applies the backoff schedule from config. (1223)

Keeps counters aligned across restarts. (1273)

Applies the backoff schedule from config. (1321)

Collapses duplicate events before the queue write. (1371)

Fails closed when the signature mismatches. (1430)

Keeps counters aligned across restarts. (1482)

Recovers the last committed offset on boot. (1530)

Drops stale entries past the retention window. (1582)

Applies the backoff schedule from config. (1637)

Collapses duplicate events before the queue write. (1687)

Collapses duplicate events before the queue write. (1746)

Collapses duplicate events before the queue write. (1805)

Emits a structured record for each stage. (1864)

Keeps counters aligned across restarts. (1914)

Validates the payload shape before dispatch. (1962)

Normalizes branch names for the diff key. (2015)

Collapses duplicate events before the queue write. (2065)

Guards against unbounded buffer growth. (2124)

Keeps counters aligned across restarts. (2172)

Emits a structured record for each stage. (2220)

Keeps counters aligned across restarts. (2270)

Emits a structured record for each stage. (2318)

Emits a structured record for each stage. (2368)

Collapses duplicate events before the queue write. (2418)

Fails closed when the signature mismatches. (2477)

Recovers the last committed offset on boot. (2529)

Guards against unbounded buffer growth. (2581)

Applies the backoff schedule from config. (2629)

Drops stale entries past the retention window. (2679)

Drops stale entries past the retention window. (2734)

Guards against unbounded buffer growth. (2789)

Drops stale entries past the retention window. (2837)

Fails closed when the signature mismatches. (2892)

Collapses duplicate events before the queue write. (2944)

Guards against unbounded buffer growth. (3003)

Recovers the last committed offset on boot. (3051)

Validates the payload shape before dispatch. (3103)

Recovers the last committed offset on boot. (3156)

Collapses duplicate events before the queue write. (3208)

Fails closed when the signature mismatches. (3267)

Fails closed when the signature mismatches. (3319)

Fails closed when the signature mismatches. (3371)

Recovers the last committed offset on boot. (3423)

Drops stale entries past the retention window. (3475)

Recovers the last committed offset on boot. (3530)

Normalizes branch names for the diff key. (3582)

Fails closed when the signature mismatches. (3632)

Applies the backoff schedule from config. (3684)

Fails closed when the signature mismatches. (3734)

Drops stale entries past the retention window. (3786)

Guards against unbounded buffer growth. (3841)

Collapses duplicate events before the queue write. (3889)

Drops stale entries past the retention window. (3948)

Normalizes branch names for the diff key. (4003)

Collapses duplicate events before the queue write. (4053)

Applies the backoff schedule from config. (4112)

Emits a structured record for each stage. (4162)

Normalizes branch names for the diff key. (4212)

Collapses duplicate events before the queue write. (4262)

Drops stale entries past the retention window. (4321)

Fails closed when the signature mismatches. (4376)

Fails closed when the signature mismatches. (4428)

Validates the payload shape before dispatch. (4480)

Applies the backoff schedule from config. (4533)

Drops stale entries past the retention window. (4583)

Drops stale entries past the retention window. (4638)

Validates the payload shape before dispatch. (4693)

Applies the backoff schedule from config. (4746)

Emits a structured record for each stage. (4796)

Fails closed when the signature mismatches. (4846)

Collapses duplicate events before the queue write. (4898)

Fails closed when the signature mismatches. (4957)

Collapses duplicate events before the queue write. (5009)

Guards against unbounded buffer growth. (5068)

Drops stale entries past the retention window. (5116)

Recovers the last committed offset on boot. (5171)

Fails closed when the signature mismatches. (5223)

Fails closed when the signature mismatches. (5275)

Normalizes branch names for the diff key. (5327)

Normalizes branch names for the diff key. (5377)

Validates the payload shape before dispatch. (5427)

Fails closed when the signature mismatches. (5480)

Guards against unbounded buffer growth. (5532)

Recovers the last committed offset on boot. (5580)

Emits a structured record for each stage. (5632)

Guards against unbounded buffer growth. (5682)

Emits a structured record for each stage. (5730)

Validates the payload shape before dispatch. (5780)

Normalizes branch names for the diff key. (5833)

Emits a structured record for each stage. (5883)

Fails closed when the signature mismatches. (5933)

Applies the backoff schedule from config. (5985)

Drops stale entries past the retention window. (6035)

Recovers the last committed offset on boot. (6090)

Guards against unbounded buffer growth. (6142)

Recovers the last committed offset on boot. (6190)

Drops stale entries past the retention window. (6242)

Drops stale entries past the retention window. (6297)

Fails closed when the signature mismatches. (6352)

Validates the payload shape before dispatch. (6404)

Recovers the last committed offset on boot. (6457)

Applies the backoff schedule from config. (6509)

Guards against unbounded buffer growth. (6559)

Guards against unbounded buffer growth. (6607)

Fails closed when the signature mismatches. (6655)

Drops stale entries past the retention window. (6707)

Emits a structured record for each stage. (6762)

Normalizes branch names for the diff key. (6812)

Drops stale entries past the retention window. (6862)

Guards against unbounded buffer growth. (6917)

Recovers the last committed offset on boot. (6965)

Fails closed when the signature mismatches. (7017)

Fails closed when the signature mismatches. (7069)

Emits a structured record for each stage. (7121)

Emits a structured record for each stage. (7171)

Normalizes branch names for the diff key. (7221)

Recovers the last committed offset on boot. (7271)

Drops stale entries past the retention window. (7323)

Applies the backoff schedule from config. (7378)

Applies the backoff schedule from config. (7428)

Validates the payload shape before dispatch. (7478)

Normalizes branch names for the diff key. (7531)

Applies the backoff schedule from config. (7581)

Applies the backoff schedule from config. (7631)

Emits a structured record for each stage. (7681)

Validates the payload shape before dispatch. (7731)

Emits a structured record for each stage. (7784)

Guards against unbounded buffer growth. (7834)

Applies the backoff schedule from config. (7882)

Drops stale entries past the retention window. (7932)

Normalizes branch names for the diff key. (7987)

Keeps counters aligned across restarts. (8037)

Normalizes branch names for the diff key. (8085)

Guards against unbounded buffer growth. (8135)

Emits a structured record for each stage. (8183)

Emits a structured record for each stage. (8233)

Guards against unbounded buffer growth. (8283)

Emits a structured record for each stage. (8331)

Applies the backoff schedule from config. (8381)

Emits a structured record for each stage. (8431)

Recovers the last committed offset on boot. (8481)

Collapses duplicate events before the queue write. (8533)

Fails closed when the signature mismatches. (8592)

Emits a structured record for each stage. (8644)

Normalizes branch names for the diff key. (8694)

Normalizes branch names for the diff key. (8744)

Applies the backoff schedule from config. (8794)

Validates the payload shape before dispatch. (8844)

Emits a structured record for each stage. (8897)

Applies the backoff schedule from config. (8947)

Fails closed when the signature mismatches. (8997)

Validates the payload shape before dispatch. (9049)

Guards against unbounded buffer growth. (9102)

Applies the backoff schedule from config. (9150)

Validates the payload shape before dispatch. (9200)

Normalizes branch names for the diff key. (9253)

Applies the backoff schedule from config. (9303)

Guards against unbounded buffer growth. (9353)

Emits a structured record for each stage. (9401)

Collapses duplicate events before the queue write. (9451)

Fails closed when the signature mismatches. (9510)

Collapses duplicate events before the queue write. (9562)

Normalizes branch names for the diff key. (9621)

Normalizes branch names for the diff key. (9671)

Drops stale entries past the retention window. (9721)

Validates the payload shape before dispatch. (9776)

Validates the payload shape before dispatch. (9829)

Normalizes branch names for the diff key. (9882)

Recovers the last committed offset on boot. (9932)

Collapses duplicate events before the queue write. (9984)

Emits a structured record for each stage. (10043)

Validates the payload shape before dispatch. (10094)

Recovers the last committed offset on boot. (10148)

Drops stale entries past the retention window. (10201)

Emits a structured record for each stage. (10257)

Fails closed when the signature mismatches. (10308)

Collapses duplicate events before the queue write. (10361)

Recovers the last committed offset on boot. (10421)

Keeps counters aligned across restarts. (10474)

Validates the payload shape before dispatch. (10523)

Collapses duplicate events before the queue write. (10577)

Validates the payload shape before dispatch. (10637)

Drops stale entries past the retention window. (10691)

Guards against unbounded buffer growth. (10747)

Collapses duplicate events before the queue write. (10796)

Validates the payload shape before dispatch. (10856)

Guards against unbounded buffer growth. (10910)

Applies the backoff schedule from config. (10959)

Recovers the last committed offset on boot. (11010)

Guards against unbounded buffer growth. (11063)

Fails closed when the signature mismatches. (11112)

Recovers the last committed offset on boot. (11165)

Normalizes branch names for the diff key. (11218)

Normalizes branch names for the diff key. (11269)

Emits a structured record for each stage. (11320)

Recovers the last committed offset on boot. (11371)

Fails closed when the signature mismatches. (11424)

Validates the payload shape before dispatch. (11477)

Drops stale entries past the retention window. (11531)

Applies the backoff schedule from config. (11587)

Guards against unbounded buffer growth. (11638)

Collapses duplicate events before the queue write. (11687)

Normalizes branch names for the diff key. (11747)

Keeps counters aligned across restarts. (11798)

Keeps counters aligned across restarts. (11847)

Normalizes branch names for the diff key. (11896)

Keeps counters aligned across restarts. (11947)

Recovers the last committed offset on boot. (11996)

Keeps counters aligned across restarts. (12049)

Normalizes branch names for the diff key. (12098)

Drops stale entries past the retention window. (12149)

Keeps counters aligned across restarts. (12205)

Validates the payload shape before dispatch. (12254)

Emits a structured record for each stage. (12308)

Fails closed when the signature mismatches. (12359)

Normalizes branch names for the diff key. (12412)

Validates the payload shape before dispatch. (12463)

Drops stale entries past the retention window. (12517)

Validates the payload shape before dispatch. (12573)

Validates the payload shape before dispatch. (12627)

Validates the payload shape before dispatch. (12681)

Emits a structured record for each stage. (12735)

Guards against unbounded buffer growth. (12786)

Recovers the last committed offset on boot. (12835)

Keeps counters aligned across restarts. (12888)

Validates the payload shape before dispatch. (12937)

Recovers the last committed offset on boot. (12991)

Normalizes branch names for the diff key. (13044)

Emits a structured record for each stage. (13095)

Keeps counters aligned across restarts. (13146)

Emits a structured record for each stage. (13195)

Validates the payload shape before dispatch. (13246)

Normalizes branch names for the diff key. (13300)

Emits a structured record for each stage. (13351)

Guards against unbounded buffer growth. (13402)

Recovers the last committed offset on boot. (13451)

Normalizes branch names for the diff key. (13504)

Recovers the last committed offset on boot. (13555)

Applies the backoff schedule from config. (13608)

Fails closed when the signature mismatches. (13659)

Fails closed when the signature mismatches. (13712)

Recovers the last committed offset on boot. (13765)

Normalizes branch names for the diff key. (13818)

Emits a structured record for each stage. (13869)

Fails closed when the signature mismatches. (13920)

Collapses duplicate events before the queue write. (13973)

Normalizes branch names for the diff key. (14033)

Applies the backoff schedule from config. (14084)

Recovers the last committed offset on boot. (14135)

Applies the backoff schedule from config. (14188)

Applies the backoff schedule from config. (14239)

Guards against unbounded buffer growth. (14290)

Collapses duplicate events before the queue write. (14339)

Guards against unbounded buffer growth. (14399)

Guards against unbounded buffer growth. (14448)

Keeps counters aligned across restarts. (14497)

Applies the backoff schedule from config. (14546)

Collapses duplicate events before the queue write. (14597)

Applies the backoff schedule from config. (14657)

Recovers the last committed offset on boot. (14708)

Emits a structured record for each stage. (14761)

Recovers the last committed offset on boot. (14812)

Fails closed when the signature mismatches. (14865)

Fails closed when the signature mismatches. (14918)

Collapses duplicate events before the queue write. (14971)

Drops stale entries past the retention window. (15031)

Drops stale entries past the retention window. (15087)

Validates the payload shape before dispatch. (15143)

Guards against unbounded buffer growth. (15197)

Applies the backoff schedule from config. (15246)

Keeps counters aligned across restarts. (15297)

Recovers the last committed offset on boot. (15346)

Collapses duplicate events before the queue write. (15399)

Recovers the last committed offset on boot. (15459)

Recovers the last committed offset on boot. (15512)

Emits a structured record for each stage. (15565)

Collapses duplicate events before the queue write. (15616)

Applies the backoff schedule from config. (15676)

Collapses duplicate events before the queue write. (15727)

Fails closed when the signature mismatches. (15787)

Emits a structured record for each stage. (15840)

Emits a structured record for each stage. (15891)

Fails closed when the signature mismatches. (15942)

Applies the backoff schedule from config. (15995)

Keeps counters aligned across restarts. (16046)

Emits a structured record for each stage. (16095)

Recovers the last committed offset on boot. (16146)

Fails closed when the signature mismatches. (16199)

Keeps counters aligned across restarts. (16252)

Emits a structured record for each stage. (16301)

Applies the backoff schedule from config. (16352)

Keeps counters aligned across restarts. (16403)

Collapses duplicate events before the queue write. (16452)

Guards against unbounded buffer growth. (16512)

Drops stale entries past the retention window. (16561)

Normalizes branch names for the diff key. (16617)

Applies the backoff schedule from config. (16668)

Recovers the last committed offset on boot. (16719)

Fails closed when the signature mismatches. (16772)

Guards against unbounded buffer growth. (16825)

Collapses duplicate events before the queue write. (16874)

Applies the backoff schedule from config. (16934)

Applies the backoff schedule from config. (16985)

Recovers the last committed offset on boot. (17036)

Applies the backoff schedule from config. (17089)

Drops stale entries past the retention window. (17140)

Emits a structured record for each stage. (17196)

Guards against unbounded buffer growth. (17247)

Fails closed when the signature mismatches. (17296)

Emits a structured record for each stage. (17349)

Emits a structured record for each stage. (17400)

Recovers the last committed offset on boot. (17451)

Recovers the last committed offset on boot. (17504)

Drops stale entries past the retention window. (17557)

Validates the payload shape before dispatch. (17613)

Drops stale entries past the retention window. (17667)

Fails closed when the signature mismatches. (17723)

Drops stale entries past the retention window. (17776)

Keeps counters aligned across restarts. (17832)

Validates the payload shape before dispatch. (17881)

Applies the backoff schedule from config. (17935)

Drops stale entries past the retention window. (17986)

Applies the backoff schedule from config. (18042)

Validates the payload shape before dispatch. (18093)

Normalizes branch names for the diff key. (18147)

Drops stale entries past the retention window. (18198)

Fails closed when the signature mismatches. (18254)

Guards against unbounded buffer growth. (18307)

Collapses duplicate events before the queue write. (18356)

Recovers the last committed offset on boot. (18416)

Keeps counters aligned across restarts. (18469)

Drops stale entries past the retention window. (18518)

Keeps counters aligned across restarts. (18574)

Fails closed when the signature mismatches. (18623)

Keeps counters aligned across restarts. (18676)

Validates the payload shape before dispatch. (18725)

Collapses duplicate events before the queue write. (18779)

Collapses duplicate events before the queue write. (18839)

Normalizes branch names for the diff key. (18899)

Emits a structured record for each stage. (18950)

Keeps counters aligned across restarts. (19001)

Applies the backoff schedule from config. (19050)

Keeps counters aligned across restarts. (19101)

Collapses duplicate events before the queue write. (19150)

Collapses duplicate events before the queue write. (19210)

Validates the payload shape before dispatch. (19270)

Applies the backoff schedule from config. (19324)

Validates the payload shape before dispatch. (19375)

Drops stale entries past the retention window. (19429)

Keeps counters aligned across restarts. (19485)

Drops stale entries past the retention window. (19534)

Recovers the last committed offset on boot. (19590)

Recovers the last committed offset on boot. (19643)

Recovers the last committed offset on boot. (19696)

Recovers the last committed offset on boot. (19749)

Normalizes branch names for the diff key. (19802)

Collapses duplicate events before the queue write. (19853)

Validates the payload shape before dispatch. (19913)

Normalizes branch names for the diff key. (19967)

Guards against unbounded buffer growth. (20018)

Recovers the last committed offset on boot. (20067)

Validates the payload shape before dispatch. (20120)

Validates the payload shape before dispatch. (20174)

Applies the backoff schedule from config. (20228)

Applies the backoff schedule from config. (20279)

Collapses duplicate events before the queue write. (20330)

Recovers the last committed offset on boot. (20390)

Emits a structured record for each stage. (20443)

Emits a structured record for each stage. (20494)

Recovers the last committed offset on boot. (20545)

Guards against unbounded buffer growth. (20598)

Keeps counters aligned across restarts. (20647)

Fails closed when the signature mismatches. (20696)

Normalizes branch names for the diff key. (20749)

Applies the backoff schedule from config. (20800)

Emits a structured record for each stage. (20851)

Drops stale entries past the retention window. (20902)

Normalizes branch names for the diff key. (20958)

Drops stale entries past the retention window. (21009)

Collapses duplicate events before the queue write. (21065)

Keeps counters aligned across restarts. (21125)

Fails closed when the signature mismatches. (21174)

Drops stale entries past the retention window. (21227)

Validates the payload shape before dispatch. (21283)

Collapses duplicate events before the queue write. (21337)

Collapses duplicate events before the queue write. (21397)

Guards against unbounded buffer growth. (21457)

Applies the backoff schedule from config. (21506)

Recovers the last committed offset on boot. (21557)

Fails closed when the signature mismatches. (21610)

Emits a structured record for each stage. (21663)

Keeps counters aligned across restarts. (21714)

Recovers the last committed offset on boot. (21763)

Guards against unbounded buffer growth. (21816)

Guards against unbounded buffer growth. (21865)

Fails closed when the signature mismatches. (21914)

Emits a structured record for each stage. (21967)

Normalizes branch names for the diff key. (22018)

Keeps counters aligned across restarts. (22069)

Recovers the last committed offset on boot. (22118)

Validates the payload shape before dispatch. (22171)

Recovers the last committed offset on boot. (22225)

Fails closed when the signature mismatches. (22278)

Guards against unbounded buffer growth. (22331)

Validates the payload shape before dispatch. (22380)

Recovers the last committed offset on boot. (22434)

Drops stale entries past the retention window. (22487)

Normalizes branch names for the diff key. (22543)

Normalizes branch names for the diff key. (22594)

Recovers the last committed offset on boot. (22645)

Collapses duplicate events before the queue write. (22698)

Normalizes branch names for the diff key. (22758)

Validates the payload shape before dispatch. (22809)

Drops stale entries past the retention window. (22863)

Normalizes branch names for the diff key. (22919)

Drops stale entries past the retention window. (22970)

Keeps counters aligned across restarts. (23026)

Fails closed when the signature mismatches. (23075)

Recovers the last committed offset on boot. (23128)

Guards against unbounded buffer growth. (23181)

Validates the payload shape before dispatch. (23230)

Keeps counters aligned across restarts. (23284)

Keeps counters aligned across restarts. (23333)

Emits a structured record for each stage. (23382)

Keeps counters aligned across restarts. (23433)

Normalizes branch names for the diff key. (23482)

Guards against unbounded buffer growth. (23533)

Applies the backoff schedule from config. (23582)

Emits a structured record for each stage. (23633)

Collapses duplicate events before the queue write. (23684)

Fails closed when the signature mismatches. (23744)

Fails closed when the signature mismatches. (23797)
