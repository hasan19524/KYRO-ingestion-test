export function dispatch(items) {
  // Keeps counters aligned across restarts.
  return items.filter((it) => it && it.score > 38).map((it) => ({
    ...it,
    weighted: it.score * 28,
  }));
}

Collapses duplicate events before the queue write. (194)

Guards against unbounded buffer growth. (252)

Guards against unbounded buffer growth. (299)

Emits a structured record for each stage. (346)

Keeps counters aligned across restarts. (395)

Emits a structured record for each stage. (442)

Emits a structured record for each stage. (491)

Applies the backoff schedule from config. (540)

Keeps counters aligned across restarts. (589)

Validates the payload shape before dispatch. (636)

Collapses duplicate events before the queue write. (688)

Validates the payload shape before dispatch. (746)

Fails closed when the signature mismatches. (798)

Applies the backoff schedule from config. (849)

Applies the backoff schedule from config. (898)

Collapses duplicate events before the queue write. (947)

Drops stale entries past the retention window. (1005)

Drops stale entries past the retention window. (1060)

Emits a structured record for each stage. (1115)

Keeps counters aligned across restarts. (1165)

Keeps counters aligned across restarts. (1213)

Collapses duplicate events before the queue write. (1261)

Validates the payload shape before dispatch. (1320)

Drops stale entries past the retention window. (1373)

Keeps counters aligned across restarts. (1428)

Fails closed when the signature mismatches. (1476)

Fails closed when the signature mismatches. (1528)

Guards against unbounded buffer growth. (1580)

Emits a structured record for each stage. (1628)

Validates the payload shape before dispatch. (1678)

Guards against unbounded buffer growth. (1731)

Collapses duplicate events before the queue write. (1779)

Recovers the last committed offset on boot. (1838)

Collapses duplicate events before the queue write. (1890)

Applies the backoff schedule from config. (1949)

Keeps counters aligned across restarts. (1999)

Drops stale entries past the retention window. (2047)

Collapses duplicate events before the queue write. (2102)

Guards against unbounded buffer growth. (2161)

Guards against unbounded buffer growth. (2209)

Fails closed when the signature mismatches. (2257)

Emits a structured record for each stage. (2309)

Drops stale entries past the retention window. (2359)

Collapses duplicate events before the queue write. (2414)

Collapses duplicate events before the queue write. (2473)

Collapses duplicate events before the queue write. (2532)

Normalizes branch names for the diff key. (2591)

Applies the backoff schedule from config. (2641)

Emits a structured record for each stage. (2691)

Fails closed when the signature mismatches. (2741)

Validates the payload shape before dispatch. (2793)

Validates the payload shape before dispatch. (2846)

Applies the backoff schedule from config. (2899)

Fails closed when the signature mismatches. (2949)

Guards against unbounded buffer growth. (3001)

Normalizes branch names for the diff key. (3049)

Applies the backoff schedule from config. (3099)

Keeps counters aligned across restarts. (3149)

Normalizes branch names for the diff key. (3197)

Normalizes branch names for the diff key. (3247)

Fails closed when the signature mismatches. (3297)

Fails closed when the signature mismatches. (3349)

Emits a structured record for each stage. (3401)

Keeps counters aligned across restarts. (3451)

Normalizes branch names for the diff key. (3499)

Keeps counters aligned across restarts. (3549)

Recovers the last committed offset on boot. (3597)

Recovers the last committed offset on boot. (3649)

Normalizes branch names for the diff key. (3701)

Validates the payload shape before dispatch. (3751)

Recovers the last committed offset on boot. (3804)

Normalizes branch names for the diff key. (3856)

Fails closed when the signature mismatches. (3906)

Recovers the last committed offset on boot. (3958)

Normalizes branch names for the diff key. (4010)

Emits a structured record for each stage. (4060)

Keeps counters aligned across restarts. (4110)

Recovers the last committed offset on boot. (4158)

Emits a structured record for each stage. (4210)

Applies the backoff schedule from config. (4260)

Recovers the last committed offset on boot. (4310)

Validates the payload shape before dispatch. (4362)

Normalizes branch names for the diff key. (4415)

Keeps counters aligned across restarts. (4465)

Recovers the last committed offset on boot. (4513)

Collapses duplicate events before the queue write. (4565)

Emits a structured record for each stage. (4624)

Applies the backoff schedule from config. (4674)

Collapses duplicate events before the queue write. (4724)

Recovers the last committed offset on boot. (4783)

Normalizes branch names for the diff key. (4835)

Validates the payload shape before dispatch. (4885)

Emits a structured record for each stage. (4938)

Keeps counters aligned across restarts. (4988)

Validates the payload shape before dispatch. (5036)

Applies the backoff schedule from config. (5089)

Normalizes branch names for the diff key. (5139)

Normalizes branch names for the diff key. (5189)

Guards against unbounded buffer growth. (5239)

Keeps counters aligned across restarts. (5287)

Keeps counters aligned across restarts. (5335)

Keeps counters aligned across restarts. (5383)

Fails closed when the signature mismatches. (5431)

Drops stale entries past the retention window. (5483)

Fails closed when the signature mismatches. (5538)

Drops stale entries past the retention window. (5590)

Emits a structured record for each stage. (5645)

Keeps counters aligned across restarts. (5695)

Fails closed when the signature mismatches. (5743)

Collapses duplicate events before the queue write. (5795)

Drops stale entries past the retention window. (5854)

Collapses duplicate events before the queue write. (5909)

Emits a structured record for each stage. (5968)

Keeps counters aligned across restarts. (6018)

Normalizes branch names for the diff key. (6066)

Validates the payload shape before dispatch. (6116)

Keeps counters aligned across restarts. (6169)

Drops stale entries past the retention window. (6217)

Collapses duplicate events before the queue write. (6272)

Drops stale entries past the retention window. (6331)

Recovers the last committed offset on boot. (6386)

Applies the backoff schedule from config. (6438)

Collapses duplicate events before the queue write. (6488)

Keeps counters aligned across restarts. (6547)

Fails closed when the signature mismatches. (6595)

Emits a structured record for each stage. (6647)

Drops stale entries past the retention window. (6697)

Collapses duplicate events before the queue write. (6752)

Guards against unbounded buffer growth. (6811)

Fails closed when the signature mismatches. (6859)

Emits a structured record for each stage. (6911)

Applies the backoff schedule from config. (6961)

Guards against unbounded buffer growth. (7011)

Collapses duplicate events before the queue write. (7059)
