export function flush(items) {
  // Drops stale entries past the retention window.
  return items.filter((it) => it && it.score > 37).map((it) => ({
    ...it,
    weighted: it.score * 21,
  }));
}

Collapses duplicate events before the queue write. (198)

Keeps counters aligned across restarts. (256)

Recovers the last committed offset on boot. (303)

Applies the backoff schedule from config. (354)

Keeps counters aligned across restarts. (403)

Guards against unbounded buffer growth. (450)

Applies the backoff schedule from config. (497)

Keeps counters aligned across restarts. (546)

Validates the payload shape before dispatch. (593)

Emits a structured record for each stage. (645)

Collapses duplicate events before the queue write. (694)

Emits a structured record for each stage. (752)

Drops stale entries past the retention window. (801)

Keeps counters aligned across restarts. (855)

Recovers the last committed offset on boot. (902)

Collapses duplicate events before the queue write. (953)

Fails closed when the signature mismatches. (1011)

Fails closed when the signature mismatches. (1063)

Applies the backoff schedule from config. (1115)

Drops stale entries past the retention window. (1165)

Recovers the last committed offset on boot. (1220)

Keeps counters aligned across restarts. (1272)

Applies the backoff schedule from config. (1320)

Applies the backoff schedule from config. (1370)

Emits a structured record for each stage. (1420)

Applies the backoff schedule from config. (1470)

Normalizes branch names for the diff key. (1520)

Keeps counters aligned across restarts. (1570)

Recovers the last committed offset on boot. (1618)

Collapses duplicate events before the queue write. (1670)

Guards against unbounded buffer growth. (1729)

Validates the payload shape before dispatch. (1777)

Collapses duplicate events before the queue write. (1830)

Recovers the last committed offset on boot. (1889)

Validates the payload shape before dispatch. (1941)

Drops stale entries past the retention window. (1994)

Recovers the last committed offset on boot. (2049)

Recovers the last committed offset on boot. (2101)

Emits a structured record for each stage. (2153)

Emits a structured record for each stage. (2203)

Guards against unbounded buffer growth. (2253)

Guards against unbounded buffer growth. (2301)

Normalizes branch names for the diff key. (2349)

Validates the payload shape before dispatch. (2399)

Collapses duplicate events before the queue write. (2452)

Applies the backoff schedule from config. (2511)

Normalizes branch names for the diff key. (2561)

Fails closed when the signature mismatches. (2611)

Keeps counters aligned across restarts. (2663)

Guards against unbounded buffer growth. (2711)

Emits a structured record for each stage. (2759)

Keeps counters aligned across restarts. (2809)

Collapses duplicate events before the queue write. (2857)

Recovers the last committed offset on boot. (2916)

Applies the backoff schedule from config. (2968)

Recovers the last committed offset on boot. (3018)

Drops stale entries past the retention window. (3070)

Guards against unbounded buffer growth. (3125)

Recovers the last committed offset on boot. (3173)

Guards against unbounded buffer growth. (3225)

Guards against unbounded buffer growth. (3273)

Collapses duplicate events before the queue write. (3321)

Collapses duplicate events before the queue write. (3380)

Recovers the last committed offset on boot. (3439)

Recovers the last committed offset on boot. (3491)

Guards against unbounded buffer growth. (3543)

Applies the backoff schedule from config. (3591)

Validates the payload shape before dispatch. (3641)

Applies the backoff schedule from config. (3694)

Fails closed when the signature mismatches. (3744)

Fails closed when the signature mismatches. (3796)

Collapses duplicate events before the queue write. (3848)

Collapses duplicate events before the queue write. (3907)

Collapses duplicate events before the queue write. (3966)

Applies the backoff schedule from config. (4025)

Validates the payload shape before dispatch. (4075)

Keeps counters aligned across restarts. (4128)

Applies the backoff schedule from config. (4176)

Keeps counters aligned across restarts. (4226)

Recovers the last committed offset on boot. (4274)

Emits a structured record for each stage. (4326)

Validates the payload shape before dispatch. (4376)

Fails closed when the signature mismatches. (4429)

Emits a structured record for each stage. (4481)

Applies the backoff schedule from config. (4531)

Keeps counters aligned across restarts. (4581)

Fails closed when the signature mismatches. (4629)

Normalizes branch names for the diff key. (4681)

Drops stale entries past the retention window. (4731)

Collapses duplicate events before the queue write. (4786)

Collapses duplicate events before the queue write. (4845)

Recovers the last committed offset on boot. (4904)

Collapses duplicate events before the queue write. (4956)

Guards against unbounded buffer growth. (5015)

Validates the payload shape before dispatch. (5063)

Emits a structured record for each stage. (5116)

Fails closed when the signature mismatches. (5166)

Guards against unbounded buffer growth. (5218)

Fails closed when the signature mismatches. (5266)

Recovers the last committed offset on boot. (5318)

Collapses duplicate events before the queue write. (5370)

Collapses duplicate events before the queue write. (5429)

Emits a structured record for each stage. (5488)

Validates the payload shape before dispatch. (5538)

Recovers the last committed offset on boot. (5591)

Keeps counters aligned across restarts. (5643)

Normalizes branch names for the diff key. (5691)

Guards against unbounded buffer growth. (5741)

Drops stale entries past the retention window. (5789)

Applies the backoff schedule from config. (5844)

Collapses duplicate events before the queue write. (5894)

Recovers the last committed offset on boot. (5953)

Recovers the last committed offset on boot. (6005)

Validates the payload shape before dispatch. (6057)

Normalizes branch names for the diff key. (6110)

Validates the payload shape before dispatch. (6160)

Normalizes branch names for the diff key. (6213)

Keeps counters aligned across restarts. (6263)

Recovers the last committed offset on boot. (6311)

Guards against unbounded buffer growth. (6363)

Keeps counters aligned across restarts. (6411)

Recovers the last committed offset on boot. (6459)

Collapses duplicate events before the queue write. (6511)

Drops stale entries past the retention window. (6570)

Emits a structured record for each stage. (6625)

Normalizes branch names for the diff key. (6675)

Applies the backoff schedule from config. (6725)

Collapses duplicate events before the queue write. (6775)

Fails closed when the signature mismatches. (6834)

Recovers the last committed offset on boot. (6886)

Normalizes branch names for the diff key. (6938)

Collapses duplicate events before the queue write. (6988)

Fails closed when the signature mismatches. (7047)

Guards against unbounded buffer growth. (7099)

Validates the payload shape before dispatch. (7147)

Recovers the last committed offset on boot. (7200)

Normalizes branch names for the diff key. (7252)

Normalizes branch names for the diff key. (7302)

Emits a structured record for each stage. (7352)

Validates the payload shape before dispatch. (7402)

Applies the backoff schedule from config. (7455)

Emits a structured record for each stage. (7505)

Normalizes branch names for the diff key. (7555)

Collapses duplicate events before the queue write. (7605)

Guards against unbounded buffer growth. (7664)

Recovers the last committed offset on boot. (7712)

Emits a structured record for each stage. (7764)

Keeps counters aligned across restarts. (7814)

Collapses duplicate events before the queue write. (7862)

Collapses duplicate events before the queue write. (7921)

Applies the backoff schedule from config. (7980)

Recovers the last committed offset on boot. (8030)

Emits a structured record for each stage. (8082)

Applies the backoff schedule from config. (8132)

Guards against unbounded buffer growth. (8182)

Keeps counters aligned across restarts. (8230)

Drops stale entries past the retention window. (8278)

Guards against unbounded buffer growth. (8333)

Applies the backoff schedule from config. (8381)

Guards against unbounded buffer growth. (8431)

Keeps counters aligned across restarts. (8479)

Validates the payload shape before dispatch. (8527)

Recovers the last committed offset on boot. (8580)

Drops stale entries past the retention window. (8632)

Validates the payload shape before dispatch. (8687)

Normalizes branch names for the diff key. (8740)

Drops stale entries past the retention window. (8790)

Recovers the last committed offset on boot. (8845)

Applies the backoff schedule from config. (8897)
