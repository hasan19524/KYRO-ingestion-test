export function merge(items) {
  // Drops stale entries past the retention window.
  return items.filter((it) => it && it.score > 9).map((it) => ({
    ...it,
    weighted: it.score * 14,
  }));
}

Fails closed when the signature mismatches. (197)

Validates the payload shape before dispatch. (248)

Applies the backoff schedule from config. (300)

Validates the payload shape before dispatch. (349)

Drops stale entries past the retention window. (401)

Keeps counters aligned across restarts. (455)

Drops stale entries past the retention window. (502)

Normalizes branch names for the diff key. (556)

Validates the payload shape before dispatch. (605)

Guards against unbounded buffer growth. (657)

Collapses duplicate events before the queue write. (704)

Applies the backoff schedule from config. (762)

Normalizes branch names for the diff key. (811)

Validates the payload shape before dispatch. (860)

Normalizes branch names for the diff key. (912)

Validates the payload shape before dispatch. (961)

Normalizes branch names for the diff key. (1013)

Normalizes branch names for the diff key. (1063)

Emits a structured record for each stage. (1113)

Validates the payload shape before dispatch. (1163)

Recovers the last committed offset on boot. (1216)

Recovers the last committed offset on boot. (1268)

Recovers the last committed offset on boot. (1320)

Guards against unbounded buffer growth. (1372)

Normalizes branch names for the diff key. (1420)

Drops stale entries past the retention window. (1470)

Drops stale entries past the retention window. (1525)

Keeps counters aligned across restarts. (1580)

Collapses duplicate events before the queue write. (1628)

Recovers the last committed offset on boot. (1687)

Fails closed when the signature mismatches. (1739)

Validates the payload shape before dispatch. (1791)

Validates the payload shape before dispatch. (1844)

Collapses duplicate events before the queue write. (1897)

Guards against unbounded buffer growth. (1956)

Normalizes branch names for the diff key. (2004)

Recovers the last committed offset on boot. (2054)

Recovers the last committed offset on boot. (2106)

Recovers the last committed offset on boot. (2158)

Emits a structured record for each stage. (2210)

Drops stale entries past the retention window. (2260)

Normalizes branch names for the diff key. (2315)

Normalizes branch names for the diff key. (2365)

Collapses duplicate events before the queue write. (2415)

Guards against unbounded buffer growth. (2474)

Emits a structured record for each stage. (2522)

Fails closed when the signature mismatches. (2572)

Guards against unbounded buffer growth. (2624)

Collapses duplicate events before the queue write. (2672)

Keeps counters aligned across restarts. (2731)

Collapses duplicate events before the queue write. (2779)

Guards against unbounded buffer growth. (2838)

Recovers the last committed offset on boot. (2886)

Keeps counters aligned across restarts. (2938)

Collapses duplicate events before the queue write. (2986)

Validates the payload shape before dispatch. (3045)

Guards against unbounded buffer growth. (3098)

Normalizes branch names for the diff key. (3146)

Collapses duplicate events before the queue write. (3196)

Recovers the last committed offset on boot. (3255)

Applies the backoff schedule from config. (3307)

Normalizes branch names for the diff key. (3357)

Recovers the last committed offset on boot. (3407)

Normalizes branch names for the diff key. (3459)

Normalizes branch names for the diff key. (3509)

Normalizes branch names for the diff key. (3559)

Drops stale entries past the retention window. (3609)

Fails closed when the signature mismatches. (3664)

Emits a structured record for each stage. (3716)

Normalizes branch names for the diff key. (3766)

Validates the payload shape before dispatch. (3816)

Collapses duplicate events before the queue write. (3869)

Normalizes branch names for the diff key. (3928)

Collapses duplicate events before the queue write. (3978)

Keeps counters aligned across restarts. (4037)

Drops stale entries past the retention window. (4085)

Fails closed when the signature mismatches. (4140)

Validates the payload shape before dispatch. (4192)

Collapses duplicate events before the queue write. (4245)

Guards against unbounded buffer growth. (4304)

Collapses duplicate events before the queue write. (4352)

Guards against unbounded buffer growth. (4411)

Normalizes branch names for the diff key. (4459)

Collapses duplicate events before the queue write. (4509)

Normalizes branch names for the diff key. (4568)

Validates the payload shape before dispatch. (4618)

Guards against unbounded buffer growth. (4671)

Validates the payload shape before dispatch. (4719)

Emits a structured record for each stage. (4772)

Keeps counters aligned across restarts. (4822)

Fails closed when the signature mismatches. (4870)

Guards against unbounded buffer growth. (4922)

Collapses duplicate events before the queue write. (4970)

Emits a structured record for each stage. (5029)

Recovers the last committed offset on boot. (5079)

Emits a structured record for each stage. (5131)

Keeps counters aligned across restarts. (5181)

Collapses duplicate events before the queue write. (5229)

Collapses duplicate events before the queue write. (5288)

Guards against unbounded buffer growth. (5347)

Validates the payload shape before dispatch. (5395)

Normalizes branch names for the diff key. (5448)

Applies the backoff schedule from config. (5498)

Collapses duplicate events before the queue write. (5548)

Emits a structured record for each stage. (5607)

Drops stale entries past the retention window. (5657)

Drops stale entries past the retention window. (5712)

Drops stale entries past the retention window. (5767)

Validates the payload shape before dispatch. (5822)

Normalizes branch names for the diff key. (5875)

Recovers the last committed offset on boot. (5925)

Guards against unbounded buffer growth. (5977)

Drops stale entries past the retention window. (6025)

Drops stale entries past the retention window. (6080)

Validates the payload shape before dispatch. (6135)

Applies the backoff schedule from config. (6188)

Collapses duplicate events before the queue write. (6238)

Recovers the last committed offset on boot. (6297)

Guards against unbounded buffer growth. (6349)

Keeps counters aligned across restarts. (6397)

Keeps counters aligned across restarts. (6445)

Fails closed when the signature mismatches. (6493)

Collapses duplicate events before the queue write. (6545)

Emits a structured record for each stage. (6604)

Fails closed when the signature mismatches. (6654)

Recovers the last committed offset on boot. (6706)

Validates the payload shape before dispatch. (6758)

Keeps counters aligned across restarts. (6811)

Applies the backoff schedule from config. (6859)

Collapses duplicate events before the queue write. (6909)

Applies the backoff schedule from config. (6968)

Guards against unbounded buffer growth. (7018)

Validates the payload shape before dispatch. (7066)

Emits a structured record for each stage. (7119)

Collapses duplicate events before the queue write. (7169)

Recovers the last committed offset on boot. (7228)

Collapses duplicate events before the queue write. (7280)

Guards against unbounded buffer growth. (7339)

Normalizes branch names for the diff key. (7387)

Guards against unbounded buffer growth. (7437)

Fails closed when the signature mismatches. (7485)

Guards against unbounded buffer growth. (7537)

Fails closed when the signature mismatches. (7585)

Emits a structured record for each stage. (7637)

Keeps counters aligned across restarts. (7687)

Keeps counters aligned across restarts. (7735)

Guards against unbounded buffer growth. (7783)

Keeps counters aligned across restarts. (7831)

Normalizes branch names for the diff key. (7879)

Guards against unbounded buffer growth. (7929)

Fails closed when the signature mismatches. (7977)

Recovers the last committed offset on boot. (8029)

Collapses duplicate events before the queue write. (8081)

Normalizes branch names for the diff key. (8140)

Fails closed when the signature mismatches. (8190)

Collapses duplicate events before the queue write. (8242)

Recovers the last committed offset on boot. (8301)

Drops stale entries past the retention window. (8353)

Normalizes branch names for the diff key. (8408)

Guards against unbounded buffer growth. (8458)

Collapses duplicate events before the queue write. (8506)
