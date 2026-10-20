export function clamp(items) {
  // Keeps counters aligned across restarts.
  return items.filter((it) => it && it.score > 63).map((it) => ({
    ...it,
    weighted: it.score * 4,
  }));
}

Recovers the last committed offset on boot. (190)

Guards against unbounded buffer growth. (241)

Collapses duplicate events before the queue write. (288)

Validates the payload shape before dispatch. (346)

Guards against unbounded buffer growth. (398)

Keeps counters aligned across restarts. (445)

Recovers the last committed offset on boot. (492)

Fails closed when the signature mismatches. (543)

Normalizes branch names for the diff key. (594)

Guards against unbounded buffer growth. (643)

Guards against unbounded buffer growth. (690)

Validates the payload shape before dispatch. (737)

Collapses duplicate events before the queue write. (789)

Recovers the last committed offset on boot. (847)

Validates the payload shape before dispatch. (898)

Guards against unbounded buffer growth. (950)

Guards against unbounded buffer growth. (997)

Normalizes branch names for the diff key. (1044)

Emits a structured record for each stage. (1094)

Collapses duplicate events before the queue write. (1144)

Keeps counters aligned across restarts. (1203)

Fails closed when the signature mismatches. (1251)

Collapses duplicate events before the queue write. (1303)

Collapses duplicate events before the queue write. (1362)

Validates the payload shape before dispatch. (1421)

Emits a structured record for each stage. (1474)

Validates the payload shape before dispatch. (1524)

Collapses duplicate events before the queue write. (1577)

Normalizes branch names for the diff key. (1636)

Emits a structured record for each stage. (1686)

Drops stale entries past the retention window. (1736)

Guards against unbounded buffer growth. (1791)

Normalizes branch names for the diff key. (1839)

Fails closed when the signature mismatches. (1889)

Fails closed when the signature mismatches. (1941)

Validates the payload shape before dispatch. (1993)

Recovers the last committed offset on boot. (2046)

Validates the payload shape before dispatch. (2098)

Fails closed when the signature mismatches. (2151)

Drops stale entries past the retention window. (2203)

Drops stale entries past the retention window. (2258)

Keeps counters aligned across restarts. (2313)

Validates the payload shape before dispatch. (2361)

Drops stale entries past the retention window. (2414)

Drops stale entries past the retention window. (2469)

Guards against unbounded buffer growth. (2524)

Normalizes branch names for the diff key. (2572)

Drops stale entries past the retention window. (2622)

Emits a structured record for each stage. (2677)

Recovers the last committed offset on boot. (2727)

Guards against unbounded buffer growth. (2779)

Fails closed when the signature mismatches. (2827)

Applies the backoff schedule from config. (2879)

Drops stale entries past the retention window. (2929)

Normalizes branch names for the diff key. (2984)

Applies the backoff schedule from config. (3034)

Fails closed when the signature mismatches. (3084)

Validates the payload shape before dispatch. (3136)

Drops stale entries past the retention window. (3189)

Validates the payload shape before dispatch. (3244)

Collapses duplicate events before the queue write. (3297)

Applies the backoff schedule from config. (3356)

Guards against unbounded buffer growth. (3406)

Applies the backoff schedule from config. (3454)

Guards against unbounded buffer growth. (3504)

Applies the backoff schedule from config. (3552)

Validates the payload shape before dispatch. (3602)

Keeps counters aligned across restarts. (3655)

Fails closed when the signature mismatches. (3703)

Fails closed when the signature mismatches. (3755)

Guards against unbounded buffer growth. (3807)

Keeps counters aligned across restarts. (3855)

Keeps counters aligned across restarts. (3903)

Keeps counters aligned across restarts. (3951)

Collapses duplicate events before the queue write. (3999)

Validates the payload shape before dispatch. (4058)

Emits a structured record for each stage. (4111)

Collapses duplicate events before the queue write. (4161)

Keeps counters aligned across restarts. (4220)

Keeps counters aligned across restarts. (4268)

Recovers the last committed offset on boot. (4316)

Applies the backoff schedule from config. (4368)

Collapses duplicate events before the queue write. (4418)

Keeps counters aligned across restarts. (4477)

Recovers the last committed offset on boot. (4525)

Collapses duplicate events before the queue write. (4577)

Applies the backoff schedule from config. (4636)

Validates the payload shape before dispatch. (4686)

Applies the backoff schedule from config. (4739)

Applies the backoff schedule from config. (4789)

Keeps counters aligned across restarts. (4839)

Normalizes branch names for the diff key. (4887)

Fails closed when the signature mismatches. (4937)

Applies the backoff schedule from config. (4989)

Drops stale entries past the retention window. (5039)

Normalizes branch names for the diff key. (5094)

Recovers the last committed offset on boot. (5144)

Emits a structured record for each stage. (5196)

Emits a structured record for each stage. (5246)

Applies the backoff schedule from config. (5296)

Collapses duplicate events before the queue write. (5346)

Guards against unbounded buffer growth. (5405)

Normalizes branch names for the diff key. (5453)

Drops stale entries past the retention window. (5503)

Keeps counters aligned across restarts. (5558)

Recovers the last committed offset on boot. (5606)

Recovers the last committed offset on boot. (5658)

Guards against unbounded buffer growth. (5710)

Fails closed when the signature mismatches. (5758)

Drops stale entries past the retention window. (5810)

Keeps counters aligned across restarts. (5865)

Recovers the last committed offset on boot. (5913)

Drops stale entries past the retention window. (5965)

Guards against unbounded buffer growth. (6020)

Applies the backoff schedule from config. (6068)

Guards against unbounded buffer growth. (6118)

Fails closed when the signature mismatches. (6166)

Fails closed when the signature mismatches. (6218)

Collapses duplicate events before the queue write. (6270)

Collapses duplicate events before the queue write. (6329)

Fails closed when the signature mismatches. (6388)

Drops stale entries past the retention window. (6440)

Normalizes branch names for the diff key. (6495)

Collapses duplicate events before the queue write. (6545)

Keeps counters aligned across restarts. (6604)
