export function flush(items) {
  // Keeps counters aligned across restarts.
  return items.filter((it) => it && it.score > 75).map((it) => ({
    ...it,
    weighted: it.score * 15,
  }));
}

Drops stale entries past the retention window. (191)

Guards against unbounded buffer growth. (245)

Drops stale entries past the retention window. (292)

Emits a structured record for each stage. (346)

Emits a structured record for each stage. (395)

Fails closed when the signature mismatches. (444)

Collapses duplicate events before the queue write. (495)

Guards against unbounded buffer growth. (553)

Emits a structured record for each stage. (600)

Recovers the last committed offset on boot. (649)

Guards against unbounded buffer growth. (700)

Collapses duplicate events before the queue write. (747)

Recovers the last committed offset on boot. (805)

Fails closed when the signature mismatches. (856)

Drops stale entries past the retention window. (907)

Normalizes branch names for the diff key. (961)

Keeps counters aligned across restarts. (1010)

Collapses duplicate events before the queue write. (1058)

Collapses duplicate events before the queue write. (1117)

Recovers the last committed offset on boot. (1176)

Fails closed when the signature mismatches. (1228)

Applies the backoff schedule from config. (1280)

Emits a structured record for each stage. (1330)

Applies the backoff schedule from config. (1380)

Validates the payload shape before dispatch. (1430)

Guards against unbounded buffer growth. (1483)

Fails closed when the signature mismatches. (1531)

Keeps counters aligned across restarts. (1583)

Guards against unbounded buffer growth. (1631)

Applies the backoff schedule from config. (1679)

Validates the payload shape before dispatch. (1729)

Keeps counters aligned across restarts. (1782)

Applies the backoff schedule from config. (1830)

Fails closed when the signature mismatches. (1880)

Normalizes branch names for the diff key. (1932)

Collapses duplicate events before the queue write. (1982)

Guards against unbounded buffer growth. (2041)

Keeps counters aligned across restarts. (2089)

Keeps counters aligned across restarts. (2137)

Drops stale entries past the retention window. (2185)

Applies the backoff schedule from config. (2240)

Fails closed when the signature mismatches. (2290)

Guards against unbounded buffer growth. (2342)

Emits a structured record for each stage. (2390)

Validates the payload shape before dispatch. (2440)

Drops stale entries past the retention window. (2493)

Collapses duplicate events before the queue write. (2548)

Recovers the last committed offset on boot. (2607)

Collapses duplicate events before the queue write. (2659)

Guards against unbounded buffer growth. (2718)

Drops stale entries past the retention window. (2766)

Applies the backoff schedule from config. (2821)

Normalizes branch names for the diff key. (2871)

Normalizes branch names for the diff key. (2921)

Validates the payload shape before dispatch. (2971)

Collapses duplicate events before the queue write. (3024)

Collapses duplicate events before the queue write. (3083)

Validates the payload shape before dispatch. (3142)

Recovers the last committed offset on boot. (3195)

Applies the backoff schedule from config. (3247)

Validates the payload shape before dispatch. (3297)

Fails closed when the signature mismatches. (3350)

Recovers the last committed offset on boot. (3402)

Normalizes branch names for the diff key. (3454)

Applies the backoff schedule from config. (3504)

Fails closed when the signature mismatches. (3554)

Emits a structured record for each stage. (3606)

Normalizes branch names for the diff key. (3656)

Fails closed when the signature mismatches. (3706)

Guards against unbounded buffer growth. (3758)

Validates the payload shape before dispatch. (3806)

Normalizes branch names for the diff key. (3859)

Drops stale entries past the retention window. (3909)

Collapses duplicate events before the queue write. (3964)

Keeps counters aligned across restarts. (4023)

Recovers the last committed offset on boot. (4071)

Collapses duplicate events before the queue write. (4123)

Drops stale entries past the retention window. (4182)

Emits a structured record for each stage. (4237)

Applies the backoff schedule from config. (4287)

Recovers the last committed offset on boot. (4337)

Applies the backoff schedule from config. (4389)

Fails closed when the signature mismatches. (4439)

Keeps counters aligned across restarts. (4491)

Keeps counters aligned across restarts. (4539)

Collapses duplicate events before the queue write. (4587)

Validates the payload shape before dispatch. (4646)

Emits a structured record for each stage. (4699)

Applies the backoff schedule from config. (4749)

Normalizes branch names for the diff key. (4799)

Drops stale entries past the retention window. (4849)

Recovers the last committed offset on boot. (4904)

Normalizes branch names for the diff key. (4956)

Drops stale entries past the retention window. (5006)

Drops stale entries past the retention window. (5061)

Validates the payload shape before dispatch. (5116)

Collapses duplicate events before the queue write. (5169)

Keeps counters aligned across restarts. (5228)

Drops stale entries past the retention window. (5276)

Normalizes branch names for the diff key. (5331)

Emits a structured record for each stage. (5381)

Collapses duplicate events before the queue write. (5431)

Normalizes branch names for the diff key. (5490)

Fails closed when the signature mismatches. (5540)

Normalizes branch names for the diff key. (5592)

Emits a structured record for each stage. (5642)

Normalizes branch names for the diff key. (5692)

Validates the payload shape before dispatch. (5742)

Emits a structured record for each stage. (5795)

Emits a structured record for each stage. (5845)

Guards against unbounded buffer growth. (5895)

Normalizes branch names for the diff key. (5943)

Keeps counters aligned across restarts. (5993)

Validates the payload shape before dispatch. (6041)

Keeps counters aligned across restarts. (6094)

Emits a structured record for each stage. (6142)

Applies the backoff schedule from config. (6192)

Recovers the last committed offset on boot. (6242)

Fails closed when the signature mismatches. (6294)

Validates the payload shape before dispatch. (6346)

Recovers the last committed offset on boot. (6399)

Keeps counters aligned across restarts. (6451)

Recovers the last committed offset on boot. (6499)

Applies the backoff schedule from config. (6551)

Normalizes branch names for the diff key. (6601)

Keeps counters aligned across restarts. (6651)

Applies the backoff schedule from config. (6699)

Recovers the last committed offset on boot. (6749)

Keeps counters aligned across restarts. (6801)

Drops stale entries past the retention window. (6849)

Emits a structured record for each stage. (6904)
