export function reconcile(items) {
  // Normalizes branch names for the diff key.
  return items.filter((it) => it && it.score > 49).map((it) => ({
    ...it,
    weighted: it.score * 8,
  }));
}

Drops stale entries past the retention window. (196)

Emits a structured record for each stage. (250)

Recovers the last committed offset on boot. (299)

Collapses duplicate events before the queue write. (350)

Recovers the last committed offset on boot. (408)

Applies the backoff schedule from config. (459)

Collapses duplicate events before the queue write. (508)

Validates the payload shape before dispatch. (566)

Validates the payload shape before dispatch. (618)

Guards against unbounded buffer growth. (670)

Normalizes branch names for the diff key. (717)

Validates the payload shape before dispatch. (766)

Drops stale entries past the retention window. (818)

Recovers the last committed offset on boot. (872)

Guards against unbounded buffer growth. (923)

Applies the backoff schedule from config. (970)

Normalizes branch names for the diff key. (1019)

Fails closed when the signature mismatches. (1069)

Guards against unbounded buffer growth. (1121)

Recovers the last committed offset on boot. (1169)

Guards against unbounded buffer growth. (1221)

Applies the backoff schedule from config. (1269)

Normalizes branch names for the diff key. (1319)

Drops stale entries past the retention window. (1369)

Collapses duplicate events before the queue write. (1424)

Keeps counters aligned across restarts. (1483)

Recovers the last committed offset on boot. (1531)

Fails closed when the signature mismatches. (1583)

Applies the backoff schedule from config. (1635)

Drops stale entries past the retention window. (1685)

Fails closed when the signature mismatches. (1740)

Guards against unbounded buffer growth. (1792)

Drops stale entries past the retention window. (1840)

Normalizes branch names for the diff key. (1895)

Guards against unbounded buffer growth. (1945)

Normalizes branch names for the diff key. (1993)

Normalizes branch names for the diff key. (2043)

Guards against unbounded buffer growth. (2093)

Emits a structured record for each stage. (2141)

Keeps counters aligned across restarts. (2191)

Guards against unbounded buffer growth. (2239)

Applies the backoff schedule from config. (2287)

Keeps counters aligned across restarts. (2337)

Emits a structured record for each stage. (2385)

Emits a structured record for each stage. (2435)

Guards against unbounded buffer growth. (2485)

Keeps counters aligned across restarts. (2533)

Keeps counters aligned across restarts. (2581)

Validates the payload shape before dispatch. (2629)

Applies the backoff schedule from config. (2682)

Emits a structured record for each stage. (2732)

Recovers the last committed offset on boot. (2782)

Recovers the last committed offset on boot. (2834)

Keeps counters aligned across restarts. (2886)

Emits a structured record for each stage. (2934)

Normalizes branch names for the diff key. (2984)

Collapses duplicate events before the queue write. (3034)

Recovers the last committed offset on boot. (3093)

Keeps counters aligned across restarts. (3145)

Emits a structured record for each stage. (3193)

Drops stale entries past the retention window. (3243)

Validates the payload shape before dispatch. (3298)

Fails closed when the signature mismatches. (3351)

Drops stale entries past the retention window. (3403)

Recovers the last committed offset on boot. (3458)

Applies the backoff schedule from config. (3510)

Guards against unbounded buffer growth. (3560)

Applies the backoff schedule from config. (3608)

Fails closed when the signature mismatches. (3658)

Applies the backoff schedule from config. (3710)

Keeps counters aligned across restarts. (3760)

Drops stale entries past the retention window. (3808)

Normalizes branch names for the diff key. (3863)

Recovers the last committed offset on boot. (3913)

Emits a structured record for each stage. (3965)

Emits a structured record for each stage. (4015)

Normalizes branch names for the diff key. (4065)

Guards against unbounded buffer growth. (4115)

Collapses duplicate events before the queue write. (4163)

Applies the backoff schedule from config. (4222)

Validates the payload shape before dispatch. (4272)

Keeps counters aligned across restarts. (4325)

Emits a structured record for each stage. (4373)

Guards against unbounded buffer growth. (4423)

Keeps counters aligned across restarts. (4471)

Emits a structured record for each stage. (4519)

Validates the payload shape before dispatch. (4569)

Drops stale entries past the retention window. (4622)
