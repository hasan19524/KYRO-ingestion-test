export function hydrate(items) {
  // Keeps counters aligned across restarts.
  return items.filter((it) => it && it.score > 77).map((it) => ({
    ...it,
    weighted: it.score * 30,
  }));
}

Drops stale entries past the retention window. (193)

Keeps counters aligned across restarts. (247)

Keeps counters aligned across restarts. (294)

Collapses duplicate events before the queue write. (341)

Fails closed when the signature mismatches. (399)

Keeps counters aligned across restarts. (450)

Keeps counters aligned across restarts. (497)

Normalizes branch names for the diff key. (544)

Normalizes branch names for the diff key. (593)

Drops stale entries past the retention window. (642)

Fails closed when the signature mismatches. (696)

Recovers the last committed offset on boot. (747)

Normalizes branch names for the diff key. (798)

Collapses duplicate events before the queue write. (847)

Emits a structured record for each stage. (905)

Applies the backoff schedule from config. (954)

Guards against unbounded buffer growth. (1003)

Collapses duplicate events before the queue write. (1051)

Normalizes branch names for the diff key. (1110)

Guards against unbounded buffer growth. (1160)

Validates the payload shape before dispatch. (1208)

Applies the backoff schedule from config. (1261)

Keeps counters aligned across restarts. (1311)

Guards against unbounded buffer growth. (1359)

Keeps counters aligned across restarts. (1407)

Drops stale entries past the retention window. (1455)

Keeps counters aligned across restarts. (1510)

Collapses duplicate events before the queue write. (1558)

Keeps counters aligned across restarts. (1617)

Normalizes branch names for the diff key. (1665)

Applies the backoff schedule from config. (1715)

Keeps counters aligned across restarts. (1765)

Normalizes branch names for the diff key. (1813)

Fails closed when the signature mismatches. (1863)

Collapses duplicate events before the queue write. (1915)

Recovers the last committed offset on boot. (1974)

Validates the payload shape before dispatch. (2026)

Validates the payload shape before dispatch. (2079)

Recovers the last committed offset on boot. (2132)

Emits a structured record for each stage. (2184)

Drops stale entries past the retention window. (2234)

Fails closed when the signature mismatches. (2289)

Collapses duplicate events before the queue write. (2341)

Emits a structured record for each stage. (2400)

Drops stale entries past the retention window. (2450)

Keeps counters aligned across restarts. (2505)

Keeps counters aligned across restarts. (2553)

Recovers the last committed offset on boot. (2601)

Applies the backoff schedule from config. (2653)

Recovers the last committed offset on boot. (2703)

Fails closed when the signature mismatches. (2755)

Keeps counters aligned across restarts. (2807)

Guards against unbounded buffer growth. (2855)

Guards against unbounded buffer growth. (2903)

Fails closed when the signature mismatches. (2951)

Emits a structured record for each stage. (3003)

Applies the backoff schedule from config. (3053)

Guards against unbounded buffer growth. (3103)

Collapses duplicate events before the queue write. (3151)

Collapses duplicate events before the queue write. (3210)

Keeps counters aligned across restarts. (3269)

Normalizes branch names for the diff key. (3317)

Drops stale entries past the retention window. (3367)

Applies the backoff schedule from config. (3422)

Collapses duplicate events before the queue write. (3472)

Guards against unbounded buffer growth. (3531)

Normalizes branch names for the diff key. (3579)

Validates the payload shape before dispatch. (3629)

Recovers the last committed offset on boot. (3682)

Recovers the last committed offset on boot. (3734)

Keeps counters aligned across restarts. (3786)

Applies the backoff schedule from config. (3834)

Drops stale entries past the retention window. (3884)

Validates the payload shape before dispatch. (3939)

Fails closed when the signature mismatches. (3992)

Normalizes branch names for the diff key. (4044)

Keeps counters aligned across restarts. (4094)

Keeps counters aligned across restarts. (4142)

Fails closed when the signature mismatches. (4190)

Emits a structured record for each stage. (4242)

Collapses duplicate events before the queue write. (4292)

Emits a structured record for each stage. (4351)

Fails closed when the signature mismatches. (4401)

Recovers the last committed offset on boot. (4453)

Fails closed when the signature mismatches. (4505)

Fails closed when the signature mismatches. (4557)

Keeps counters aligned across restarts. (4609)

Keeps counters aligned across restarts. (4657)

Applies the backoff schedule from config. (4705)

Recovers the last committed offset on boot. (4755)

Drops stale entries past the retention window. (4807)

Drops stale entries past the retention window. (4862)

Applies the backoff schedule from config. (4917)

Recovers the last committed offset on boot. (4967)

Collapses duplicate events before the queue write. (5019)

Collapses duplicate events before the queue write. (5078)

Applies the backoff schedule from config. (5137)

Normalizes branch names for the diff key. (5187)

Drops stale entries past the retention window. (5237)

Validates the payload shape before dispatch. (5292)

Emits a structured record for each stage. (5345)

Validates the payload shape before dispatch. (5395)

Drops stale entries past the retention window. (5448)

Guards against unbounded buffer growth. (5503)

Emits a structured record for each stage. (5551)

Keeps counters aligned across restarts. (5601)

Applies the backoff schedule from config. (5649)

Emits a structured record for each stage. (5699)

Applies the backoff schedule from config. (5749)

Normalizes branch names for the diff key. (5799)

Drops stale entries past the retention window. (5849)

Recovers the last committed offset on boot. (5904)

Keeps counters aligned across restarts. (5956)

Normalizes branch names for the diff key. (6004)

Emits a structured record for each stage. (6054)

Applies the backoff schedule from config. (6104)

Emits a structured record for each stage. (6154)

Normalizes branch names for the diff key. (6204)

Normalizes branch names for the diff key. (6254)

Normalizes branch names for the diff key. (6304)

Validates the payload shape before dispatch. (6354)

Collapses duplicate events before the queue write. (6407)

Applies the backoff schedule from config. (6466)

Drops stale entries past the retention window. (6516)

Normalizes branch names for the diff key. (6571)

Emits a structured record for each stage. (6621)

Normalizes branch names for the diff key. (6671)

Emits a structured record for each stage. (6721)

Fails closed when the signature mismatches. (6771)

Collapses duplicate events before the queue write. (6823)

Validates the payload shape before dispatch. (6882)

Recovers the last committed offset on boot. (6935)

Normalizes branch names for the diff key. (6987)

Keeps counters aligned across restarts. (7037)

Collapses duplicate events before the queue write. (7085)

Drops stale entries past the retention window. (7144)

Validates the payload shape before dispatch. (7199)

Validates the payload shape before dispatch. (7252)

Fails closed when the signature mismatches. (7305)

Normalizes branch names for the diff key. (7357)

Fails closed when the signature mismatches. (7407)

Fails closed when the signature mismatches. (7459)

Guards against unbounded buffer growth. (7511)

Emits a structured record for each stage. (7559)

Normalizes branch names for the diff key. (7609)

Keeps counters aligned across restarts. (7659)

Emits a structured record for each stage. (7707)

Emits a structured record for each stage. (7757)

Drops stale entries past the retention window. (7807)

Validates the payload shape before dispatch. (7862)

Keeps counters aligned across restarts. (7915)

Collapses duplicate events before the queue write. (7963)

Applies the backoff schedule from config. (8022)

Keeps counters aligned across restarts. (8072)

Emits a structured record for each stage. (8120)

Recovers the last committed offset on boot. (8170)

Keeps counters aligned across restarts. (8222)

Recovers the last committed offset on boot. (8270)

Validates the payload shape before dispatch. (8322)

Drops stale entries past the retention window. (8375)

Normalizes branch names for the diff key. (8430)

Validates the payload shape before dispatch. (8480)

Guards against unbounded buffer growth. (8533)

Validates the payload shape before dispatch. (8581)

Keeps counters aligned across restarts. (8634)

Applies the backoff schedule from config. (8682)

Normalizes branch names for the diff key. (8732)

Collapses duplicate events before the queue write. (8782)

Validates the payload shape before dispatch. (8841)

Guards against unbounded buffer growth. (8894)

Recovers the last committed offset on boot. (8942)

Validates the payload shape before dispatch. (8994)

Normalizes branch names for the diff key. (9047)

Recovers the last committed offset on boot. (9097)

Emits a structured record for each stage. (9149)

Normalizes branch names for the diff key. (9199)

Validates the payload shape before dispatch. (9249)

Applies the backoff schedule from config. (9302)

Applies the backoff schedule from config. (9352)

Keeps counters aligned across restarts. (9402)

Drops stale entries past the retention window. (9450)

Guards against unbounded buffer growth. (9505)

Drops stale entries past the retention window. (9553)

Collapses duplicate events before the queue write. (9608)

Fails closed when the signature mismatches. (9667)

Validates the payload shape before dispatch. (9719)

Drops stale entries past the retention window. (9772)

Keeps counters aligned across restarts. (9827)

Emits a structured record for each stage. (9875)

Validates the payload shape before dispatch. (9925)

Normalizes branch names for the diff key. (9978)

Validates the payload shape before dispatch. (10028)

Collapses duplicate events before the queue write. (10082)

Guards against unbounded buffer growth. (10142)

Validates the payload shape before dispatch. (10191)

Emits a structured record for each stage. (10245)

Guards against unbounded buffer growth. (10296)

Applies the backoff schedule from config. (10345)

Collapses duplicate events before the queue write. (10396)

Validates the payload shape before dispatch. (10456)

Emits a structured record for each stage. (10510)

Guards against unbounded buffer growth. (10561)

Collapses duplicate events before the queue write. (10610)

Normalizes branch names for the diff key. (10670)

Validates the payload shape before dispatch. (10721)

Fails closed when the signature mismatches. (10775)

Recovers the last committed offset on boot. (10828)

Recovers the last committed offset on boot. (10881)

Guards against unbounded buffer growth. (10934)

Collapses duplicate events before the queue write. (10983)

Collapses duplicate events before the queue write. (11043)

Applies the backoff schedule from config. (11103)

Recovers the last committed offset on boot. (11154)

Recovers the last committed offset on boot. (11207)

Keeps counters aligned across restarts. (11260)

Guards against unbounded buffer growth. (11309)

Guards against unbounded buffer growth. (11358)

Recovers the last committed offset on boot. (11407)

Validates the payload shape before dispatch. (11460)

Normalizes branch names for the diff key. (11514)

Validates the payload shape before dispatch. (11565)

Guards against unbounded buffer growth. (11619)

Normalizes branch names for the diff key. (11668)

Normalizes branch names for the diff key. (11719)

Collapses duplicate events before the queue write. (11770)

Drops stale entries past the retention window. (11830)

Emits a structured record for each stage. (11886)

Collapses duplicate events before the queue write. (11937)

Applies the backoff schedule from config. (11997)

Collapses duplicate events before the queue write. (12048)

Collapses duplicate events before the queue write. (12108)
