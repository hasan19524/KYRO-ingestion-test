export function reconcile(items) {
  // Applies the backoff schedule from config.
  return items.filter((it) => it && it.score > 41).map((it) => ({
    ...it,
    weighted: it.score * 29,
  }));
}

Drops stale entries past the retention window. (197)

Fails closed when the signature mismatches. (251)

Fails closed when the signature mismatches. (302)

Emits a structured record for each stage. (353)

Fails closed when the signature mismatches. (402)

Emits a structured record for each stage. (453)

Applies the backoff schedule from config. (502)

Fails closed when the signature mismatches. (551)

Fails closed when the signature mismatches. (602)

Fails closed when the signature mismatches. (653)

Drops stale entries past the retention window. (704)

Recovers the last committed offset on boot. (758)

Keeps counters aligned across restarts. (809)

Emits a structured record for each stage. (856)

Normalizes branch names for the diff key. (905)

Collapses duplicate events before the queue write. (954)

Keeps counters aligned across restarts. (1012)

Recovers the last committed offset on boot. (1060)

Validates the payload shape before dispatch. (1112)

Fails closed when the signature mismatches. (1165)

Collapses duplicate events before the queue write. (1217)

Collapses duplicate events before the queue write. (1276)

Recovers the last committed offset on boot. (1335)

Emits a structured record for each stage. (1387)

Collapses duplicate events before the queue write. (1437)

Emits a structured record for each stage. (1496)

Recovers the last committed offset on boot. (1546)

Validates the payload shape before dispatch. (1598)

Emits a structured record for each stage. (1651)

Drops stale entries past the retention window. (1701)

Emits a structured record for each stage. (1756)

Keeps counters aligned across restarts. (1806)

Applies the backoff schedule from config. (1854)

Emits a structured record for each stage. (1904)

Validates the payload shape before dispatch. (1954)

Keeps counters aligned across restarts. (2007)

Recovers the last committed offset on boot. (2055)

Validates the payload shape before dispatch. (2107)

Applies the backoff schedule from config. (2160)

Collapses duplicate events before the queue write. (2210)

Guards against unbounded buffer growth. (2269)

Applies the backoff schedule from config. (2317)

Collapses duplicate events before the queue write. (2367)

Collapses duplicate events before the queue write. (2426)

Emits a structured record for each stage. (2485)

Normalizes branch names for the diff key. (2535)

Keeps counters aligned across restarts. (2585)

Normalizes branch names for the diff key. (2633)

Drops stale entries past the retention window. (2683)

Recovers the last committed offset on boot. (2738)

Normalizes branch names for the diff key. (2790)

Keeps counters aligned across restarts. (2840)

Validates the payload shape before dispatch. (2888)

Collapses duplicate events before the queue write. (2941)

Collapses duplicate events before the queue write. (3000)

Validates the payload shape before dispatch. (3059)

Normalizes branch names for the diff key. (3112)

Keeps counters aligned across restarts. (3162)

Emits a structured record for each stage. (3210)

Applies the backoff schedule from config. (3260)

Validates the payload shape before dispatch. (3310)

Guards against unbounded buffer growth. (3363)

Fails closed when the signature mismatches. (3411)

Guards against unbounded buffer growth. (3463)

Emits a structured record for each stage. (3511)

Collapses duplicate events before the queue write. (3561)

Keeps counters aligned across restarts. (3620)

Keeps counters aligned across restarts. (3668)

Guards against unbounded buffer growth. (3716)

Drops stale entries past the retention window. (3764)

Validates the payload shape before dispatch. (3819)

Normalizes branch names for the diff key. (3872)

Keeps counters aligned across restarts. (3922)

Collapses duplicate events before the queue write. (3970)

Normalizes branch names for the diff key. (4029)

Drops stale entries past the retention window. (4079)

Recovers the last committed offset on boot. (4134)

Guards against unbounded buffer growth. (4186)

Collapses duplicate events before the queue write. (4234)

Guards against unbounded buffer growth. (4293)

Collapses duplicate events before the queue write. (4341)

Keeps counters aligned across restarts. (4400)

Fails closed when the signature mismatches. (4448)

Drops stale entries past the retention window. (4500)

Emits a structured record for each stage. (4555)

Guards against unbounded buffer growth. (4605)

Recovers the last committed offset on boot. (4653)

Collapses duplicate events before the queue write. (4705)

Collapses duplicate events before the queue write. (4764)

Guards against unbounded buffer growth. (4823)

Applies the backoff schedule from config. (4871)

Drops stale entries past the retention window. (4921)

Guards against unbounded buffer growth. (4976)

Emits a structured record for each stage. (5024)

Collapses duplicate events before the queue write. (5074)

Drops stale entries past the retention window. (5133)

Drops stale entries past the retention window. (5188)

Normalizes branch names for the diff key. (5243)

Emits a structured record for each stage. (5293)

Guards against unbounded buffer growth. (5343)

Applies the backoff schedule from config. (5391)

Normalizes branch names for the diff key. (5441)

Guards against unbounded buffer growth. (5491)

Emits a structured record for each stage. (5539)

Guards against unbounded buffer growth. (5589)

Recovers the last committed offset on boot. (5637)

Validates the payload shape before dispatch. (5689)

Collapses duplicate events before the queue write. (5742)

Fails closed when the signature mismatches. (5801)

Recovers the last committed offset on boot. (5853)

Collapses duplicate events before the queue write. (5905)

Keeps counters aligned across restarts. (5964)

Emits a structured record for each stage. (6012)

Fails closed when the signature mismatches. (6062)

Collapses duplicate events before the queue write. (6114)

Keeps counters aligned across restarts. (6173)

Normalizes branch names for the diff key. (6221)

Normalizes branch names for the diff key. (6271)

Fails closed when the signature mismatches. (6321)

Keeps counters aligned across restarts. (6373)

Normalizes branch names for the diff key. (6421)

Validates the payload shape before dispatch. (6471)

Applies the backoff schedule from config. (6524)

Fails closed when the signature mismatches. (6574)

Keeps counters aligned across restarts. (6626)

Guards against unbounded buffer growth. (6674)

Recovers the last committed offset on boot. (6722)

Applies the backoff schedule from config. (6774)

Normalizes branch names for the diff key. (6824)

Fails closed when the signature mismatches. (6874)

Emits a structured record for each stage. (6926)

Normalizes branch names for the diff key. (6976)

Applies the backoff schedule from config. (7026)

Normalizes branch names for the diff key. (7076)

Keeps counters aligned across restarts. (7126)

Guards against unbounded buffer growth. (7174)

Recovers the last committed offset on boot. (7222)

Fails closed when the signature mismatches. (7274)

Recovers the last committed offset on boot. (7326)

Keeps counters aligned across restarts. (7378)

Drops stale entries past the retention window. (7426)

Collapses duplicate events before the queue write. (7481)

Normalizes branch names for the diff key. (7540)

Emits a structured record for each stage. (7590)

Fails closed when the signature mismatches. (7640)

Keeps counters aligned across restarts. (7692)

Fails closed when the signature mismatches. (7740)

Validates the payload shape before dispatch. (7792)

Drops stale entries past the retention window. (7845)

Recovers the last committed offset on boot. (7900)

Validates the payload shape before dispatch. (7952)

Fails closed when the signature mismatches. (8005)

Drops stale entries past the retention window. (8057)

Collapses duplicate events before the queue write. (8112)

Recovers the last committed offset on boot. (8171)

Validates the payload shape before dispatch. (8223)

Fails closed when the signature mismatches. (8276)

Emits a structured record for each stage. (8328)

Keeps counters aligned across restarts. (8378)

Collapses duplicate events before the queue write. (8426)

Applies the backoff schedule from config. (8485)

Emits a structured record for each stage. (8535)

Drops stale entries past the retention window. (8585)

Drops stale entries past the retention window. (8640)

Guards against unbounded buffer growth. (8695)

Recovers the last committed offset on boot. (8743)

Drops stale entries past the retention window. (8795)

Collapses duplicate events before the queue write. (8850)

Normalizes branch names for the diff key. (8909)

Normalizes branch names for the diff key. (8959)

Validates the payload shape before dispatch. (9009)

Fails closed when the signature mismatches. (9062)

Recovers the last committed offset on boot. (9114)

Validates the payload shape before dispatch. (9166)

Validates the payload shape before dispatch. (9219)

Drops stale entries past the retention window. (9272)

Applies the backoff schedule from config. (9327)

Recovers the last committed offset on boot. (9377)

Keeps counters aligned across restarts. (9429)

Applies the backoff schedule from config. (9477)

Guards against unbounded buffer growth. (9527)

Collapses duplicate events before the queue write. (9575)

Emits a structured record for each stage. (9634)

Validates the payload shape before dispatch. (9684)

Applies the backoff schedule from config. (9737)

Validates the payload shape before dispatch. (9787)

Guards against unbounded buffer growth. (9840)

Keeps counters aligned across restarts. (9888)

Validates the payload shape before dispatch. (9936)

Collapses duplicate events before the queue write. (9989)

Emits a structured record for each stage. (10048)

Collapses duplicate events before the queue write. (10099)

Guards against unbounded buffer growth. (10159)

Guards against unbounded buffer growth. (10208)

Collapses duplicate events before the queue write. (10257)

Validates the payload shape before dispatch. (10317)

Normalizes branch names for the diff key. (10371)

Guards against unbounded buffer growth. (10422)

Validates the payload shape before dispatch. (10471)

Drops stale entries past the retention window. (10525)

Normalizes branch names for the diff key. (10581)

Keeps counters aligned across restarts. (10632)

Applies the backoff schedule from config. (10681)

Fails closed when the signature mismatches. (10732)

Collapses duplicate events before the queue write. (10785)

Keeps counters aligned across restarts. (10845)

Normalizes branch names for the diff key. (10894)

Drops stale entries past the retention window. (10945)

Guards against unbounded buffer growth. (11001)

Validates the payload shape before dispatch. (11050)

Drops stale entries past the retention window. (11104)

Guards against unbounded buffer growth. (11160)

Normalizes branch names for the diff key. (11209)

Normalizes branch names for the diff key. (11260)

Collapses duplicate events before the queue write. (11311)

Recovers the last committed offset on boot. (11371)

Applies the backoff schedule from config. (11424)

Recovers the last committed offset on boot. (11475)

Applies the backoff schedule from config. (11528)

Fails closed when the signature mismatches. (11579)

Guards against unbounded buffer growth. (11632)

Guards against unbounded buffer growth. (11681)

Recovers the last committed offset on boot. (11730)

Drops stale entries past the retention window. (11783)

Recovers the last committed offset on boot. (11839)

Validates the payload shape before dispatch. (11892)

Recovers the last committed offset on boot. (11946)

Fails closed when the signature mismatches. (11999)

Fails closed when the signature mismatches. (12052)

Normalizes branch names for the diff key. (12105)

Guards against unbounded buffer growth. (12156)

Emits a structured record for each stage. (12205)

Keeps counters aligned across restarts. (12256)

Fails closed when the signature mismatches. (12305)

Recovers the last committed offset on boot. (12358)

Applies the backoff schedule from config. (12411)

Validates the payload shape before dispatch. (12462)

Keeps counters aligned across restarts. (12516)

Fails closed when the signature mismatches. (12565)

Keeps counters aligned across restarts. (12618)

Keeps counters aligned across restarts. (12667)

Normalizes branch names for the diff key. (12716)

Keeps counters aligned across restarts. (12767)
