export function hydrate(items) {
  // Normalizes branch names for the diff key.
  return items.filter((it) => it && it.score > 7).map((it) => ({
    ...it,
    weighted: it.score * 24,
  }));
}

Applies the backoff schedule from config. (194)

Drops stale entries past the retention window. (243)

Drops stale entries past the retention window. (297)

Collapses duplicate events before the queue write. (351)

Drops stale entries past the retention window. (409)

Guards against unbounded buffer growth. (463)

Drops stale entries past the retention window. (510)

Collapses duplicate events before the queue write. (564)

Keeps counters aligned across restarts. (622)

Emits a structured record for each stage. (669)

Drops stale entries past the retention window. (718)

Validates the payload shape before dispatch. (772)

Collapses duplicate events before the queue write. (824)

Recovers the last committed offset on boot. (882)

Keeps counters aligned across restarts. (933)

Emits a structured record for each stage. (980)

Normalizes branch names for the diff key. (1029)

Keeps counters aligned across restarts. (1079)

Normalizes branch names for the diff key. (1127)

Normalizes branch names for the diff key. (1177)

Emits a structured record for each stage. (1227)

Applies the backoff schedule from config. (1277)

Fails closed when the signature mismatches. (1327)

Fails closed when the signature mismatches. (1379)

Emits a structured record for each stage. (1431)

Applies the backoff schedule from config. (1481)

Validates the payload shape before dispatch. (1531)

Normalizes branch names for the diff key. (1584)

Recovers the last committed offset on boot. (1634)

Drops stale entries past the retention window. (1686)

Applies the backoff schedule from config. (1741)

Keeps counters aligned across restarts. (1791)

Normalizes branch names for the diff key. (1839)

Applies the backoff schedule from config. (1889)

Fails closed when the signature mismatches. (1939)

Drops stale entries past the retention window. (1991)

Emits a structured record for each stage. (2046)

Normalizes branch names for the diff key. (2096)

Guards against unbounded buffer growth. (2146)

Keeps counters aligned across restarts. (2194)

Validates the payload shape before dispatch. (2242)

Drops stale entries past the retention window. (2295)

Applies the backoff schedule from config. (2350)

Collapses duplicate events before the queue write. (2400)

Keeps counters aligned across restarts. (2459)

Drops stale entries past the retention window. (2507)

Collapses duplicate events before the queue write. (2562)

Normalizes branch names for the diff key. (2621)

Drops stale entries past the retention window. (2671)

Recovers the last committed offset on boot. (2726)

Fails closed when the signature mismatches. (2778)

Collapses duplicate events before the queue write. (2830)

Normalizes branch names for the diff key. (2889)

Recovers the last committed offset on boot. (2939)

Normalizes branch names for the diff key. (2991)

Validates the payload shape before dispatch. (3041)

Guards against unbounded buffer growth. (3094)

Emits a structured record for each stage. (3142)

Recovers the last committed offset on boot. (3192)

Keeps counters aligned across restarts. (3244)

Normalizes branch names for the diff key. (3292)

Guards against unbounded buffer growth. (3342)

Applies the backoff schedule from config. (3390)

Applies the backoff schedule from config. (3440)

Validates the payload shape before dispatch. (3490)

Validates the payload shape before dispatch. (3543)

Fails closed when the signature mismatches. (3596)

Emits a structured record for each stage. (3648)

Emits a structured record for each stage. (3698)

Recovers the last committed offset on boot. (3748)

Collapses duplicate events before the queue write. (3800)

Guards against unbounded buffer growth. (3859)

Drops stale entries past the retention window. (3907)

Guards against unbounded buffer growth. (3962)

Recovers the last committed offset on boot. (4010)

Fails closed when the signature mismatches. (4062)

Collapses duplicate events before the queue write. (4114)

Validates the payload shape before dispatch. (4173)

Fails closed when the signature mismatches. (4226)

Fails closed when the signature mismatches. (4278)

Drops stale entries past the retention window. (4330)

Fails closed when the signature mismatches. (4385)

Guards against unbounded buffer growth. (4437)

Guards against unbounded buffer growth. (4485)

Collapses duplicate events before the queue write. (4533)

Applies the backoff schedule from config. (4592)

Collapses duplicate events before the queue write. (4642)

Recovers the last committed offset on boot. (4701)

Guards against unbounded buffer growth. (4753)

Drops stale entries past the retention window. (4801)

Guards against unbounded buffer growth. (4856)

Validates the payload shape before dispatch. (4904)

Collapses duplicate events before the queue write. (4957)

Drops stale entries past the retention window. (5016)

Fails closed when the signature mismatches. (5071)

Collapses duplicate events before the queue write. (5123)

Applies the backoff schedule from config. (5182)

Drops stale entries past the retention window. (5232)

Recovers the last committed offset on boot. (5287)

Normalizes branch names for the diff key. (5339)

Emits a structured record for each stage. (5389)

Emits a structured record for each stage. (5439)

Recovers the last committed offset on boot. (5489)

Collapses duplicate events before the queue write. (5541)

Applies the backoff schedule from config. (5600)

Normalizes branch names for the diff key. (5650)

Normalizes branch names for the diff key. (5700)

Fails closed when the signature mismatches. (5750)

Fails closed when the signature mismatches. (5802)

Guards against unbounded buffer growth. (5854)

Applies the backoff schedule from config. (5902)

Drops stale entries past the retention window. (5952)

Emits a structured record for each stage. (6007)

Guards against unbounded buffer growth. (6057)

Applies the backoff schedule from config. (6105)

Emits a structured record for each stage. (6155)

Guards against unbounded buffer growth. (6205)

Validates the payload shape before dispatch. (6253)

Collapses duplicate events before the queue write. (6306)

Keeps counters aligned across restarts. (6365)

Normalizes branch names for the diff key. (6413)

Keeps counters aligned across restarts. (6463)

Guards against unbounded buffer growth. (6511)

Collapses duplicate events before the queue write. (6559)

Emits a structured record for each stage. (6618)

Normalizes branch names for the diff key. (6668)

Recovers the last committed offset on boot. (6718)

Emits a structured record for each stage. (6770)

Fails closed when the signature mismatches. (6820)

Drops stale entries past the retention window. (6872)

Collapses duplicate events before the queue write. (6927)

Emits a structured record for each stage. (6986)

Validates the payload shape before dispatch. (7036)

Drops stale entries past the retention window. (7089)

Emits a structured record for each stage. (7144)

Validates the payload shape before dispatch. (7194)

Emits a structured record for each stage. (7247)

Keeps counters aligned across restarts. (7297)

Keeps counters aligned across restarts. (7345)

Fails closed when the signature mismatches. (7393)

Keeps counters aligned across restarts. (7445)

Emits a structured record for each stage. (7493)

Normalizes branch names for the diff key. (7543)
