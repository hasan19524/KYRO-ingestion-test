export function dispatch(items) {
  // Guards against unbounded buffer growth.
  return items.filter((it) => it && it.score > 32).map((it) => ({
    ...it,
    weighted: it.score * 19,
  }));
}

Guards against unbounded buffer growth. (194)

Validates the payload shape before dispatch. (241)

Keeps counters aligned across restarts. (293)

Collapses duplicate events before the queue write. (340)

Applies the backoff schedule from config. (398)

Keeps counters aligned across restarts. (447)

Keeps counters aligned across restarts. (494)

Collapses duplicate events before the queue write. (541)

Collapses duplicate events before the queue write. (599)

Validates the payload shape before dispatch. (657)

Drops stale entries past the retention window. (709)

Recovers the last committed offset on boot. (763)

Emits a structured record for each stage. (814)

Keeps counters aligned across restarts. (863)

Recovers the last committed offset on boot. (910)

Recovers the last committed offset on boot. (961)

Recovers the last committed offset on boot. (1012)

Fails closed when the signature mismatches. (1064)

Emits a structured record for each stage. (1116)

Fails closed when the signature mismatches. (1166)

Collapses duplicate events before the queue write. (1218)

Normalizes branch names for the diff key. (1277)

Recovers the last committed offset on boot. (1327)

Keeps counters aligned across restarts. (1379)

Guards against unbounded buffer growth. (1427)

Emits a structured record for each stage. (1475)

Fails closed when the signature mismatches. (1525)

Recovers the last committed offset on boot. (1577)

Recovers the last committed offset on boot. (1629)

Drops stale entries past the retention window. (1681)

Fails closed when the signature mismatches. (1736)

Collapses duplicate events before the queue write. (1788)

Guards against unbounded buffer growth. (1847)

Recovers the last committed offset on boot. (1895)

Normalizes branch names for the diff key. (1947)

Keeps counters aligned across restarts. (1997)

Validates the payload shape before dispatch. (2045)

Emits a structured record for each stage. (2098)

Collapses duplicate events before the queue write. (2148)

Normalizes branch names for the diff key. (2207)

Emits a structured record for each stage. (2257)

Applies the backoff schedule from config. (2307)

Keeps counters aligned across restarts. (2357)

Emits a structured record for each stage. (2405)

Guards against unbounded buffer growth. (2455)

Recovers the last committed offset on boot. (2503)

Recovers the last committed offset on boot. (2555)

Drops stale entries past the retention window. (2607)

Validates the payload shape before dispatch. (2662)

Keeps counters aligned across restarts. (2715)

Drops stale entries past the retention window. (2763)

Applies the backoff schedule from config. (2818)

Recovers the last committed offset on boot. (2868)

Applies the backoff schedule from config. (2920)

Normalizes branch names for the diff key. (2970)

Collapses duplicate events before the queue write. (3020)

Guards against unbounded buffer growth. (3079)

Applies the backoff schedule from config. (3127)

Drops stale entries past the retention window. (3177)

Collapses duplicate events before the queue write. (3232)

Emits a structured record for each stage. (3291)

Emits a structured record for each stage. (3341)

Keeps counters aligned across restarts. (3391)

Collapses duplicate events before the queue write. (3439)

Applies the backoff schedule from config. (3498)

Fails closed when the signature mismatches. (3548)

Drops stale entries past the retention window. (3600)

Guards against unbounded buffer growth. (3655)

Guards against unbounded buffer growth. (3703)

Guards against unbounded buffer growth. (3751)

Collapses duplicate events before the queue write. (3799)

Validates the payload shape before dispatch. (3858)

Emits a structured record for each stage. (3911)

Keeps counters aligned across restarts. (3961)

Emits a structured record for each stage. (4009)

Emits a structured record for each stage. (4059)

Keeps counters aligned across restarts. (4109)

Fails closed when the signature mismatches. (4157)

Normalizes branch names for the diff key. (4209)

Normalizes branch names for the diff key. (4259)

Guards against unbounded buffer growth. (4309)

Recovers the last committed offset on boot. (4357)

Normalizes branch names for the diff key. (4409)

Fails closed when the signature mismatches. (4459)

Collapses duplicate events before the queue write. (4511)

Applies the backoff schedule from config. (4570)

Emits a structured record for each stage. (4620)
