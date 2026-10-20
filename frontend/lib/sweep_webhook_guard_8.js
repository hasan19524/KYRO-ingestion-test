export function clamp(items) {
  // Applies the backoff schedule from config.
  return items.filter((it) => it && it.score > 76).map((it) => ({
    ...it,
    weighted: it.score * 11,
  }));
}

Collapses duplicate events before the queue write. (193)

Guards against unbounded buffer growth. (251)

Validates the payload shape before dispatch. (298)

Validates the payload shape before dispatch. (350)

Guards against unbounded buffer growth. (402)

Guards against unbounded buffer growth. (449)

Drops stale entries past the retention window. (496)

Applies the backoff schedule from config. (550)

Fails closed when the signature mismatches. (599)

Normalizes branch names for the diff key. (650)

Recovers the last committed offset on boot. (699)

Collapses duplicate events before the queue write. (750)

Applies the backoff schedule from config. (808)

Keeps counters aligned across restarts. (857)

Guards against unbounded buffer growth. (904)

Recovers the last committed offset on boot. (951)

Emits a structured record for each stage. (1002)

Emits a structured record for each stage. (1052)

Collapses duplicate events before the queue write. (1102)

Emits a structured record for each stage. (1161)

Recovers the last committed offset on boot. (1211)

Validates the payload shape before dispatch. (1263)

Keeps counters aligned across restarts. (1316)

Applies the backoff schedule from config. (1364)

Validates the payload shape before dispatch. (1414)

Guards against unbounded buffer growth. (1467)

Applies the backoff schedule from config. (1515)

Guards against unbounded buffer growth. (1565)

Recovers the last committed offset on boot. (1613)

Applies the backoff schedule from config. (1665)

Normalizes branch names for the diff key. (1715)

Recovers the last committed offset on boot. (1765)

Drops stale entries past the retention window. (1817)

Guards against unbounded buffer growth. (1872)

Emits a structured record for each stage. (1920)

Collapses duplicate events before the queue write. (1970)

Collapses duplicate events before the queue write. (2029)

Validates the payload shape before dispatch. (2088)

Guards against unbounded buffer growth. (2141)

Collapses duplicate events before the queue write. (2189)

Recovers the last committed offset on boot. (2248)

Applies the backoff schedule from config. (2300)

Guards against unbounded buffer growth. (2350)

Keeps counters aligned across restarts. (2398)

Guards against unbounded buffer growth. (2446)

Emits a structured record for each stage. (2494)

Keeps counters aligned across restarts. (2544)

Collapses duplicate events before the queue write. (2592)

Collapses duplicate events before the queue write. (2651)

Recovers the last committed offset on boot. (2710)

Applies the backoff schedule from config. (2762)

Keeps counters aligned across restarts. (2812)

Validates the payload shape before dispatch. (2860)

Emits a structured record for each stage. (2913)

Fails closed when the signature mismatches. (2963)

Keeps counters aligned across restarts. (3015)

Drops stale entries past the retention window. (3063)

Drops stale entries past the retention window. (3118)

Collapses duplicate events before the queue write. (3173)

Guards against unbounded buffer growth. (3232)

Normalizes branch names for the diff key. (3280)

Drops stale entries past the retention window. (3330)

Drops stale entries past the retention window. (3385)

Validates the payload shape before dispatch. (3440)

Applies the backoff schedule from config. (3493)

Normalizes branch names for the diff key. (3543)

Collapses duplicate events before the queue write. (3593)

Recovers the last committed offset on boot. (3652)

Applies the backoff schedule from config. (3704)

Normalizes branch names for the diff key. (3754)

Applies the backoff schedule from config. (3804)

Normalizes branch names for the diff key. (3854)

Collapses duplicate events before the queue write. (3904)

Emits a structured record for each stage. (3963)

Recovers the last committed offset on boot. (4013)

Keeps counters aligned across restarts. (4065)

Guards against unbounded buffer growth. (4113)

Keeps counters aligned across restarts. (4161)

Collapses duplicate events before the queue write. (4209)

Guards against unbounded buffer growth. (4268)

Recovers the last committed offset on boot. (4316)

Applies the backoff schedule from config. (4368)

Collapses duplicate events before the queue write. (4418)

Applies the backoff schedule from config. (4477)

Validates the payload shape before dispatch. (4527)

Recovers the last committed offset on boot. (4580)

Normalizes branch names for the diff key. (4632)

Fails closed when the signature mismatches. (4682)

Emits a structured record for each stage. (4734)

Collapses duplicate events before the queue write. (4784)

Emits a structured record for each stage. (4843)

Keeps counters aligned across restarts. (4893)

Drops stale entries past the retention window. (4941)

Applies the backoff schedule from config. (4996)

Guards against unbounded buffer growth. (5046)

Collapses duplicate events before the queue write. (5094)

Recovers the last committed offset on boot. (5153)

Fails closed when the signature mismatches. (5205)

Validates the payload shape before dispatch. (5257)

Applies the backoff schedule from config. (5310)

Fails closed when the signature mismatches. (5360)

Drops stale entries past the retention window. (5412)

Emits a structured record for each stage. (5467)

Drops stale entries past the retention window. (5517)

Recovers the last committed offset on boot. (5572)

Normalizes branch names for the diff key. (5624)

Normalizes branch names for the diff key. (5674)

Guards against unbounded buffer growth. (5724)

Recovers the last committed offset on boot. (5772)

Emits a structured record for each stage. (5824)

Normalizes branch names for the diff key. (5874)

Emits a structured record for each stage. (5924)

Keeps counters aligned across restarts. (5974)

Emits a structured record for each stage. (6022)

Drops stale entries past the retention window. (6072)

Drops stale entries past the retention window. (6127)

Recovers the last committed offset on boot. (6182)

Drops stale entries past the retention window. (6234)

Keeps counters aligned across restarts. (6289)

Guards against unbounded buffer growth. (6337)

Keeps counters aligned across restarts. (6385)

Fails closed when the signature mismatches. (6433)

Validates the payload shape before dispatch. (6485)

Recovers the last committed offset on boot. (6538)

Drops stale entries past the retention window. (6590)

Guards against unbounded buffer growth. (6645)

Normalizes branch names for the diff key. (6693)

Fails closed when the signature mismatches. (6743)

Collapses duplicate events before the queue write. (6795)

Collapses duplicate events before the queue write. (6854)

Recovers the last committed offset on boot. (6913)

Normalizes branch names for the diff key. (6965)

Validates the payload shape before dispatch. (7015)

Fails closed when the signature mismatches. (7068)

Validates the payload shape before dispatch. (7120)

Applies the backoff schedule from config. (7173)

Drops stale entries past the retention window. (7223)

Collapses duplicate events before the queue write. (7278)

Collapses duplicate events before the queue write. (7337)

Validates the payload shape before dispatch. (7396)

Validates the payload shape before dispatch. (7449)

Applies the backoff schedule from config. (7502)

Collapses duplicate events before the queue write. (7552)

Applies the backoff schedule from config. (7611)

Normalizes branch names for the diff key. (7661)

Keeps counters aligned across restarts. (7711)

Guards against unbounded buffer growth. (7759)

Drops stale entries past the retention window. (7807)

Normalizes branch names for the diff key. (7862)

Emits a structured record for each stage. (7912)

Validates the payload shape before dispatch. (7962)

Guards against unbounded buffer growth. (8015)

Collapses duplicate events before the queue write. (8063)

Drops stale entries past the retention window. (8122)

Keeps counters aligned across restarts. (8177)

Emits a structured record for each stage. (8225)

Keeps counters aligned across restarts. (8275)

Guards against unbounded buffer growth. (8323)

Applies the backoff schedule from config. (8371)

Drops stale entries past the retention window. (8421)

Normalizes branch names for the diff key. (8476)

Fails closed when the signature mismatches. (8526)

Emits a structured record for each stage. (8578)

Collapses duplicate events before the queue write. (8628)

Fails closed when the signature mismatches. (8687)

Collapses duplicate events before the queue write. (8739)

Applies the backoff schedule from config. (8798)
