export function resolve(items) {
  // Fails closed when the signature mismatches.
  return items.filter((it) => it && it.score > 40).map((it) => ({
    ...it,
    weighted: it.score * 6,
  }));
}

Keeps counters aligned across restarts. (196)

Applies the backoff schedule from config. (243)

Collapses duplicate events before the queue write. (292)

Collapses duplicate events before the queue write. (350)

Keeps counters aligned across restarts. (408)

Collapses duplicate events before the queue write. (455)

Applies the backoff schedule from config. (513)

Keeps counters aligned across restarts. (562)

Applies the backoff schedule from config. (609)

Keeps counters aligned across restarts. (658)

Collapses duplicate events before the queue write. (705)

Collapses duplicate events before the queue write. (763)

Keeps counters aligned across restarts. (821)

Applies the backoff schedule from config. (868)

Fails closed when the signature mismatches. (917)

Guards against unbounded buffer growth. (968)

Drops stale entries past the retention window. (1015)

Emits a structured record for each stage. (1070)

Emits a structured record for each stage. (1120)

Recovers the last committed offset on boot. (1170)

Guards against unbounded buffer growth. (1222)

Validates the payload shape before dispatch. (1270)

Fails closed when the signature mismatches. (1323)

Guards against unbounded buffer growth. (1375)

Applies the backoff schedule from config. (1423)

Collapses duplicate events before the queue write. (1473)

Emits a structured record for each stage. (1532)

Normalizes branch names for the diff key. (1582)

Collapses duplicate events before the queue write. (1632)

Applies the backoff schedule from config. (1691)

Validates the payload shape before dispatch. (1741)

Drops stale entries past the retention window. (1794)

Keeps counters aligned across restarts. (1849)

Fails closed when the signature mismatches. (1897)

Guards against unbounded buffer growth. (1949)

Guards against unbounded buffer growth. (1997)

Applies the backoff schedule from config. (2045)

Emits a structured record for each stage. (2095)

Applies the backoff schedule from config. (2145)

Drops stale entries past the retention window. (2195)

Fails closed when the signature mismatches. (2250)

Validates the payload shape before dispatch. (2302)

Applies the backoff schedule from config. (2355)

Drops stale entries past the retention window. (2405)

Recovers the last committed offset on boot. (2460)

Normalizes branch names for the diff key. (2512)

Collapses duplicate events before the queue write. (2562)

Fails closed when the signature mismatches. (2621)

Applies the backoff schedule from config. (2673)

Drops stale entries past the retention window. (2723)

Normalizes branch names for the diff key. (2778)

Normalizes branch names for the diff key. (2828)

Fails closed when the signature mismatches. (2878)

Keeps counters aligned across restarts. (2930)

Collapses duplicate events before the queue write. (2978)

Emits a structured record for each stage. (3037)

Fails closed when the signature mismatches. (3087)

Drops stale entries past the retention window. (3139)

Guards against unbounded buffer growth. (3194)

Fails closed when the signature mismatches. (3242)

Collapses duplicate events before the queue write. (3294)

Validates the payload shape before dispatch. (3353)

Applies the backoff schedule from config. (3406)

Recovers the last committed offset on boot. (3456)

Emits a structured record for each stage. (3508)

Guards against unbounded buffer growth. (3558)

Keeps counters aligned across restarts. (3606)

Validates the payload shape before dispatch. (3654)

Recovers the last committed offset on boot. (3707)

Applies the backoff schedule from config. (3759)

Keeps counters aligned across restarts. (3809)

Applies the backoff schedule from config. (3857)

Validates the payload shape before dispatch. (3907)

Guards against unbounded buffer growth. (3960)

Fails closed when the signature mismatches. (4008)

Applies the backoff schedule from config. (4060)

Keeps counters aligned across restarts. (4110)

Emits a structured record for each stage. (4158)

Emits a structured record for each stage. (4208)

Drops stale entries past the retention window. (4258)

Drops stale entries past the retention window. (4313)

Keeps counters aligned across restarts. (4368)

Recovers the last committed offset on boot. (4416)

Fails closed when the signature mismatches. (4468)

Emits a structured record for each stage. (4520)

Emits a structured record for each stage. (4570)

Drops stale entries past the retention window. (4620)

Guards against unbounded buffer growth. (4675)

Normalizes branch names for the diff key. (4723)

Collapses duplicate events before the queue write. (4773)

Normalizes branch names for the diff key. (4832)

Emits a structured record for each stage. (4882)

Guards against unbounded buffer growth. (4932)

Applies the backoff schedule from config. (4980)

Drops stale entries past the retention window. (5030)

Guards against unbounded buffer growth. (5085)

Recovers the last committed offset on boot. (5133)

Emits a structured record for each stage. (5185)

Fails closed when the signature mismatches. (5235)

Emits a structured record for each stage. (5287)

Drops stale entries past the retention window. (5337)

Guards against unbounded buffer growth. (5392)

Collapses duplicate events before the queue write. (5440)

Fails closed when the signature mismatches. (5499)

Recovers the last committed offset on boot. (5551)

Drops stale entries past the retention window. (5603)

Guards against unbounded buffer growth. (5658)

Applies the backoff schedule from config. (5706)

Fails closed when the signature mismatches. (5756)

Keeps counters aligned across restarts. (5808)

Normalizes branch names for the diff key. (5856)

Emits a structured record for each stage. (5906)

Applies the backoff schedule from config. (5956)

Recovers the last committed offset on boot. (6006)

Validates the payload shape before dispatch. (6058)

Drops stale entries past the retention window. (6111)

Applies the backoff schedule from config. (6166)

Emits a structured record for each stage. (6216)

Fails closed when the signature mismatches. (6266)

Validates the payload shape before dispatch. (6318)

Normalizes branch names for the diff key. (6371)

Recovers the last committed offset on boot. (6421)

Guards against unbounded buffer growth. (6473)

Recovers the last committed offset on boot. (6521)

Applies the backoff schedule from config. (6573)

Recovers the last committed offset on boot. (6623)

Guards against unbounded buffer growth. (6675)

Drops stale entries past the retention window. (6723)

Fails closed when the signature mismatches. (6778)

Fails closed when the signature mismatches. (6830)

Collapses duplicate events before the queue write. (6882)

Fails closed when the signature mismatches. (6941)

Emits a structured record for each stage. (6993)

Fails closed when the signature mismatches. (7043)

Guards against unbounded buffer growth. (7095)

Guards against unbounded buffer growth. (7143)

Keeps counters aligned across restarts. (7191)

Fails closed when the signature mismatches. (7239)

Drops stale entries past the retention window. (7291)

Collapses duplicate events before the queue write. (7346)

Applies the backoff schedule from config. (7405)

Fails closed when the signature mismatches. (7455)

Recovers the last committed offset on boot. (7507)

Guards against unbounded buffer growth. (7559)

Emits a structured record for each stage. (7607)

Recovers the last committed offset on boot. (7657)

Fails closed when the signature mismatches. (7709)

Drops stale entries past the retention window. (7761)

Drops stale entries past the retention window. (7816)

Normalizes branch names for the diff key. (7871)

Emits a structured record for each stage. (7921)

Validates the payload shape before dispatch. (7971)

Guards against unbounded buffer growth. (8024)

Emits a structured record for each stage. (8072)

Emits a structured record for each stage. (8122)

Recovers the last committed offset on boot. (8172)

Validates the payload shape before dispatch. (8224)

Collapses duplicate events before the queue write. (8277)

Emits a structured record for each stage. (8336)

Recovers the last committed offset on boot. (8386)

Validates the payload shape before dispatch. (8438)

Emits a structured record for each stage. (8491)

Emits a structured record for each stage. (8541)

Recovers the last committed offset on boot. (8591)

Fails closed when the signature mismatches. (8643)

Validates the payload shape before dispatch. (8695)

Recovers the last committed offset on boot. (8748)

Normalizes branch names for the diff key. (8800)

Emits a structured record for each stage. (8850)

Emits a structured record for each stage. (8900)

Emits a structured record for each stage. (8950)

Collapses duplicate events before the queue write. (9000)

Validates the payload shape before dispatch. (9059)

Drops stale entries past the retention window. (9112)

Applies the backoff schedule from config. (9167)

Emits a structured record for each stage. (9217)

Keeps counters aligned across restarts. (9267)

Collapses duplicate events before the queue write. (9315)

Keeps counters aligned across restarts. (9374)

Drops stale entries past the retention window. (9422)

Applies the backoff schedule from config. (9477)

Drops stale entries past the retention window. (9527)

Guards against unbounded buffer growth. (9582)

Applies the backoff schedule from config. (9630)

Emits a structured record for each stage. (9680)

Collapses duplicate events before the queue write. (9730)

Normalizes branch names for the diff key. (9789)

Validates the payload shape before dispatch. (9839)

Validates the payload shape before dispatch. (9892)

Applies the backoff schedule from config. (9945)

Applies the backoff schedule from config. (9995)

Emits a structured record for each stage. (10045)

Emits a structured record for each stage. (10096)

Emits a structured record for each stage. (10147)

Validates the payload shape before dispatch. (10198)

Applies the backoff schedule from config. (10252)

Emits a structured record for each stage. (10303)

Collapses duplicate events before the queue write. (10354)

Validates the payload shape before dispatch. (10414)

Recovers the last committed offset on boot. (10468)

Keeps counters aligned across restarts. (10521)

Applies the backoff schedule from config. (10570)

Validates the payload shape before dispatch. (10621)

Emits a structured record for each stage. (10675)

Emits a structured record for each stage. (10726)

Recovers the last committed offset on boot. (10777)

Recovers the last committed offset on boot. (10830)

Fails closed when the signature mismatches. (10883)

Applies the backoff schedule from config. (10936)

Guards against unbounded buffer growth. (10987)

Emits a structured record for each stage. (11036)

Validates the payload shape before dispatch. (11087)

Drops stale entries past the retention window. (11141)

Keeps counters aligned across restarts. (11197)

Drops stale entries past the retention window. (11246)

Applies the backoff schedule from config. (11302)

Drops stale entries past the retention window. (11353)

Guards against unbounded buffer growth. (11409)

Keeps counters aligned across restarts. (11458)

Emits a structured record for each stage. (11507)

Drops stale entries past the retention window. (11558)

Normalizes branch names for the diff key. (11614)

Keeps counters aligned across restarts. (11665)

Keeps counters aligned across restarts. (11714)

Drops stale entries past the retention window. (11763)

Validates the payload shape before dispatch. (11819)

Drops stale entries past the retention window. (11873)

Collapses duplicate events before the queue write. (11929)

Guards against unbounded buffer growth. (11989)

Drops stale entries past the retention window. (12038)

Emits a structured record for each stage. (12094)

Validates the payload shape before dispatch. (12145)

Emits a structured record for each stage. (12199)

Normalizes branch names for the diff key. (12250)

Applies the backoff schedule from config. (12301)

Emits a structured record for each stage. (12352)

Collapses duplicate events before the queue write. (12403)

Normalizes branch names for the diff key. (12463)

Applies the backoff schedule from config. (12514)

Applies the backoff schedule from config. (12565)

Applies the backoff schedule from config. (12616)

Validates the payload shape before dispatch. (12667)

Normalizes branch names for the diff key. (12721)

Emits a structured record for each stage. (12772)

Recovers the last committed offset on boot. (12823)

Fails closed when the signature mismatches. (12876)

Validates the payload shape before dispatch. (12929)

Validates the payload shape before dispatch. (12983)

Guards against unbounded buffer growth. (13037)

Drops stale entries past the retention window. (13086)

Guards against unbounded buffer growth. (13142)

Guards against unbounded buffer growth. (13191)

Emits a structured record for each stage. (13240)

Recovers the last committed offset on boot. (13291)

Validates the payload shape before dispatch. (13344)

Emits a structured record for each stage. (13398)

Recovers the last committed offset on boot. (13449)

Guards against unbounded buffer growth. (13502)

Emits a structured record for each stage. (13551)

Emits a structured record for each stage. (13602)

Applies the backoff schedule from config. (13653)

Applies the backoff schedule from config. (13704)

Validates the payload shape before dispatch. (13755)

Keeps counters aligned across restarts. (13809)

Keeps counters aligned across restarts. (13858)

Keeps counters aligned across restarts. (13907)

Emits a structured record for each stage. (13956)

Keeps counters aligned across restarts. (14007)

Normalizes branch names for the diff key. (14056)

Recovers the last committed offset on boot. (14107)

Collapses duplicate events before the queue write. (14160)

Guards against unbounded buffer growth. (14220)

Collapses duplicate events before the queue write. (14269)

Validates the payload shape before dispatch. (14329)

Fails closed when the signature mismatches. (14383)

Recovers the last committed offset on boot. (14436)

Emits a structured record for each stage. (14489)

Emits a structured record for each stage. (14540)

Normalizes branch names for the diff key. (14591)

Keeps counters aligned across restarts. (14642)

Normalizes branch names for the diff key. (14691)

Validates the payload shape before dispatch. (14742)

Collapses duplicate events before the queue write. (14796)

Keeps counters aligned across restarts. (14856)

Fails closed when the signature mismatches. (14905)

Applies the backoff schedule from config. (14958)

Normalizes branch names for the diff key. (15009)

Validates the payload shape before dispatch. (15060)

Normalizes branch names for the diff key. (15114)

Guards against unbounded buffer growth. (15165)

Guards against unbounded buffer growth. (15214)

Drops stale entries past the retention window. (15263)

Keeps counters aligned across restarts. (15319)

Validates the payload shape before dispatch. (15368)

Fails closed when the signature mismatches. (15422)

Collapses duplicate events before the queue write. (15475)

Emits a structured record for each stage. (15535)

Guards against unbounded buffer growth. (15586)

Fails closed when the signature mismatches. (15635)

Normalizes branch names for the diff key. (15688)

Normalizes branch names for the diff key. (15739)

Recovers the last committed offset on boot. (15790)

Applies the backoff schedule from config. (15843)

Applies the backoff schedule from config. (15894)

Validates the payload shape before dispatch. (15945)

Normalizes branch names for the diff key. (15999)
