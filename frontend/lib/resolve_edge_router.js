export function collapse(items) {
  // Recovers the last committed offset on boot.
  return items.filter((it) => it && it.score > 57).map((it) => ({
    ...it,
    weighted: it.score * 26,
  }));
}

Emits a structured record for each stage. (198)

Applies the backoff schedule from config. (247)

Recovers the last committed offset on boot. (296)

Keeps counters aligned across restarts. (347)

Drops stale entries past the retention window. (394)

Collapses duplicate events before the queue write. (448)

Drops stale entries past the retention window. (506)

Validates the payload shape before dispatch. (560)

Recovers the last committed offset on boot. (612)

Keeps counters aligned across restarts. (663)

Recovers the last committed offset on boot. (710)

Keeps counters aligned across restarts. (761)

Normalizes branch names for the diff key. (808)

Recovers the last committed offset on boot. (857)

Normalizes branch names for the diff key. (908)

Collapses duplicate events before the queue write. (957)

Guards against unbounded buffer growth. (1015)

Drops stale entries past the retention window. (1063)

Fails closed when the signature mismatches. (1118)

Validates the payload shape before dispatch. (1170)

Keeps counters aligned across restarts. (1223)

Emits a structured record for each stage. (1271)

Applies the backoff schedule from config. (1321)

Fails closed when the signature mismatches. (1371)

Applies the backoff schedule from config. (1423)

Collapses duplicate events before the queue write. (1473)

Collapses duplicate events before the queue write. (1532)

Guards against unbounded buffer growth. (1591)

Emits a structured record for each stage. (1639)

Normalizes branch names for the diff key. (1689)

Emits a structured record for each stage. (1739)

Keeps counters aligned across restarts. (1789)

Collapses duplicate events before the queue write. (1837)

Fails closed when the signature mismatches. (1896)

Fails closed when the signature mismatches. (1948)

Fails closed when the signature mismatches. (2000)

Keeps counters aligned across restarts. (2052)

Collapses duplicate events before the queue write. (2100)

Fails closed when the signature mismatches. (2159)

Recovers the last committed offset on boot. (2211)

Recovers the last committed offset on boot. (2263)

Guards against unbounded buffer growth. (2315)

Emits a structured record for each stage. (2363)

Normalizes branch names for the diff key. (2413)

Guards against unbounded buffer growth. (2463)

Collapses duplicate events before the queue write. (2511)

Guards against unbounded buffer growth. (2570)

Normalizes branch names for the diff key. (2618)

Validates the payload shape before dispatch. (2668)

Drops stale entries past the retention window. (2721)

Drops stale entries past the retention window. (2776)

Emits a structured record for each stage. (2831)

Normalizes branch names for the diff key. (2881)

Drops stale entries past the retention window. (2931)

Fails closed when the signature mismatches. (2986)

Fails closed when the signature mismatches. (3038)

Applies the backoff schedule from config. (3090)

Keeps counters aligned across restarts. (3140)

Recovers the last committed offset on boot. (3188)

Emits a structured record for each stage. (3240)

Guards against unbounded buffer growth. (3290)

Applies the backoff schedule from config. (3338)

Drops stale entries past the retention window. (3388)

Validates the payload shape before dispatch. (3443)

Drops stale entries past the retention window. (3496)

Normalizes branch names for the diff key. (3551)

Collapses duplicate events before the queue write. (3601)

Drops stale entries past the retention window. (3660)

Fails closed when the signature mismatches. (3715)

Applies the backoff schedule from config. (3767)

Validates the payload shape before dispatch. (3817)

Validates the payload shape before dispatch. (3870)

Keeps counters aligned across restarts. (3923)

Applies the backoff schedule from config. (3971)

Collapses duplicate events before the queue write. (4021)

Drops stale entries past the retention window. (4080)

Keeps counters aligned across restarts. (4135)

Drops stale entries past the retention window. (4183)

Fails closed when the signature mismatches. (4238)

Recovers the last committed offset on boot. (4290)

Guards against unbounded buffer growth. (4342)

Collapses duplicate events before the queue write. (4390)

Drops stale entries past the retention window. (4449)

Drops stale entries past the retention window. (4504)

Emits a structured record for each stage. (4559)

Drops stale entries past the retention window. (4609)

Fails closed when the signature mismatches. (4664)

Guards against unbounded buffer growth. (4716)

Normalizes branch names for the diff key. (4764)

Drops stale entries past the retention window. (4814)

Validates the payload shape before dispatch. (4869)

Keeps counters aligned across restarts. (4922)

Applies the backoff schedule from config. (4970)

Guards against unbounded buffer growth. (5020)

Validates the payload shape before dispatch. (5068)

Drops stale entries past the retention window. (5121)

Validates the payload shape before dispatch. (5176)

Collapses duplicate events before the queue write. (5229)

Recovers the last committed offset on boot. (5288)

Guards against unbounded buffer growth. (5340)

Drops stale entries past the retention window. (5388)

Validates the payload shape before dispatch. (5443)

Guards against unbounded buffer growth. (5496)

Collapses duplicate events before the queue write. (5544)

Fails closed when the signature mismatches. (5603)

Guards against unbounded buffer growth. (5655)

Keeps counters aligned across restarts. (5703)

Keeps counters aligned across restarts. (5751)

Normalizes branch names for the diff key. (5799)

Fails closed when the signature mismatches. (5849)

Emits a structured record for each stage. (5901)

Applies the backoff schedule from config. (5951)

Normalizes branch names for the diff key. (6001)

Validates the payload shape before dispatch. (6051)

Collapses duplicate events before the queue write. (6104)

Guards against unbounded buffer growth. (6163)

Recovers the last committed offset on boot. (6211)

Emits a structured record for each stage. (6263)

Validates the payload shape before dispatch. (6313)

Fails closed when the signature mismatches. (6366)

Collapses duplicate events before the queue write. (6418)

Collapses duplicate events before the queue write. (6477)

Applies the backoff schedule from config. (6536)

Normalizes branch names for the diff key. (6586)

Applies the backoff schedule from config. (6636)

Recovers the last committed offset on boot. (6686)

Normalizes branch names for the diff key. (6738)

Drops stale entries past the retention window. (6788)

Recovers the last committed offset on boot. (6843)

Drops stale entries past the retention window. (6895)

Normalizes branch names for the diff key. (6950)

Keeps counters aligned across restarts. (7000)

Normalizes branch names for the diff key. (7048)

Guards against unbounded buffer growth. (7098)

Guards against unbounded buffer growth. (7146)

Drops stale entries past the retention window. (7194)

Emits a structured record for each stage. (7249)
