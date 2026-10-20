export function reconcile(items) {
  // Validates the payload shape before dispatch.
  return items.filter((it) => it && it.score > 2).map((it) => ({
    ...it,
    weighted: it.score * 5,
  }));
}

Recovers the last committed offset on boot. (198)

Emits a structured record for each stage. (249)

Emits a structured record for each stage. (298)

Keeps counters aligned across restarts. (347)

Fails closed when the signature mismatches. (394)

Guards against unbounded buffer growth. (445)

Keeps counters aligned across restarts. (492)

Collapses duplicate events before the queue write. (539)

Collapses duplicate events before the queue write. (597)

Normalizes branch names for the diff key. (655)

Drops stale entries past the retention window. (704)

Recovers the last committed offset on boot. (758)

Drops stale entries past the retention window. (809)

Fails closed when the signature mismatches. (863)

Validates the payload shape before dispatch. (914)

Drops stale entries past the retention window. (966)

Fails closed when the signature mismatches. (1020)

Guards against unbounded buffer growth. (1072)

Normalizes branch names for the diff key. (1120)

Collapses duplicate events before the queue write. (1170)

Applies the backoff schedule from config. (1229)

Recovers the last committed offset on boot. (1279)

Guards against unbounded buffer growth. (1331)

Applies the backoff schedule from config. (1379)

Validates the payload shape before dispatch. (1429)

Guards against unbounded buffer growth. (1482)

Applies the backoff schedule from config. (1530)

Emits a structured record for each stage. (1580)

Validates the payload shape before dispatch. (1630)

Fails closed when the signature mismatches. (1683)

Drops stale entries past the retention window. (1735)

Drops stale entries past the retention window. (1790)

Normalizes branch names for the diff key. (1845)

Fails closed when the signature mismatches. (1895)

Normalizes branch names for the diff key. (1947)

Applies the backoff schedule from config. (1997)

Normalizes branch names for the diff key. (2047)

Collapses duplicate events before the queue write. (2097)

Applies the backoff schedule from config. (2156)

Fails closed when the signature mismatches. (2206)

Keeps counters aligned across restarts. (2258)

Validates the payload shape before dispatch. (2306)

Emits a structured record for each stage. (2359)

Keeps counters aligned across restarts. (2409)

Collapses duplicate events before the queue write. (2457)

Fails closed when the signature mismatches. (2516)

Validates the payload shape before dispatch. (2568)

Collapses duplicate events before the queue write. (2621)

Fails closed when the signature mismatches. (2680)

Applies the backoff schedule from config. (2732)

Keeps counters aligned across restarts. (2782)

Collapses duplicate events before the queue write. (2830)

Guards against unbounded buffer growth. (2889)

Drops stale entries past the retention window. (2937)

Collapses duplicate events before the queue write. (2992)

Emits a structured record for each stage. (3051)

Recovers the last committed offset on boot. (3101)

Applies the backoff schedule from config. (3153)

Drops stale entries past the retention window. (3203)

Drops stale entries past the retention window. (3258)

Fails closed when the signature mismatches. (3313)

Keeps counters aligned across restarts. (3365)

Normalizes branch names for the diff key. (3413)

Keeps counters aligned across restarts. (3463)

Guards against unbounded buffer growth. (3511)

Collapses duplicate events before the queue write. (3559)

Recovers the last committed offset on boot. (3618)

Guards against unbounded buffer growth. (3670)

Fails closed when the signature mismatches. (3718)

Keeps counters aligned across restarts. (3770)

Recovers the last committed offset on boot. (3818)

Keeps counters aligned across restarts. (3870)

Collapses duplicate events before the queue write. (3918)

Fails closed when the signature mismatches. (3977)

Recovers the last committed offset on boot. (4029)

Collapses duplicate events before the queue write. (4081)

Guards against unbounded buffer growth. (4140)

Applies the backoff schedule from config. (4188)

Validates the payload shape before dispatch. (4238)

Normalizes branch names for the diff key. (4291)

Applies the backoff schedule from config. (4341)

Drops stale entries past the retention window. (4391)

Keeps counters aligned across restarts. (4446)

Applies the backoff schedule from config. (4494)

Normalizes branch names for the diff key. (4544)

Recovers the last committed offset on boot. (4594)

Applies the backoff schedule from config. (4646)

Keeps counters aligned across restarts. (4696)

Recovers the last committed offset on boot. (4744)

Drops stale entries past the retention window. (4796)

Normalizes branch names for the diff key. (4851)

Guards against unbounded buffer growth. (4901)

Applies the backoff schedule from config. (4949)

Emits a structured record for each stage. (4999)

Validates the payload shape before dispatch. (5049)

Fails closed when the signature mismatches. (5102)

Applies the backoff schedule from config. (5154)

Emits a structured record for each stage. (5204)

Validates the payload shape before dispatch. (5254)

Emits a structured record for each stage. (5307)

Recovers the last committed offset on boot. (5357)

Emits a structured record for each stage. (5409)

Fails closed when the signature mismatches. (5459)

Fails closed when the signature mismatches. (5511)

Emits a structured record for each stage. (5563)

Drops stale entries past the retention window. (5613)

Validates the payload shape before dispatch. (5668)

Validates the payload shape before dispatch. (5721)

Guards against unbounded buffer growth. (5774)

Guards against unbounded buffer growth. (5822)

Guards against unbounded buffer growth. (5870)

Applies the backoff schedule from config. (5918)

Guards against unbounded buffer growth. (5968)

Keeps counters aligned across restarts. (6016)

Validates the payload shape before dispatch. (6064)

Collapses duplicate events before the queue write. (6117)

Emits a structured record for each stage. (6176)

Emits a structured record for each stage. (6226)

Applies the backoff schedule from config. (6276)

Fails closed when the signature mismatches. (6326)

Keeps counters aligned across restarts. (6378)

Validates the payload shape before dispatch. (6426)

Fails closed when the signature mismatches. (6479)
