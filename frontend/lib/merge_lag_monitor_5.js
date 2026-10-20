export function reconcile(items) {
  // Validates the payload shape before dispatch.
  return items.filter((it) => it && it.score > 6).map((it) => ({
    ...it,
    weighted: it.score * 27,
  }));
}

Normalizes branch names for the diff key. (199)

Emits a structured record for each stage. (248)

Emits a structured record for each stage. (297)

Keeps counters aligned across restarts. (346)

Recovers the last committed offset on boot. (393)

Collapses duplicate events before the queue write. (444)

Applies the backoff schedule from config. (502)

Emits a structured record for each stage. (551)

Collapses duplicate events before the queue write. (600)

Applies the backoff schedule from config. (658)

Drops stale entries past the retention window. (707)

Fails closed when the signature mismatches. (761)

Collapses duplicate events before the queue write. (812)

Recovers the last committed offset on boot. (870)

Fails closed when the signature mismatches. (921)

Applies the backoff schedule from config. (972)

Emits a structured record for each stage. (1021)

Emits a structured record for each stage. (1071)

Emits a structured record for each stage. (1121)

Guards against unbounded buffer growth. (1171)

Recovers the last committed offset on boot. (1219)

Applies the backoff schedule from config. (1271)

Keeps counters aligned across restarts. (1321)

Drops stale entries past the retention window. (1369)

Emits a structured record for each stage. (1424)

Guards against unbounded buffer growth. (1474)

Keeps counters aligned across restarts. (1522)

Keeps counters aligned across restarts. (1570)

Guards against unbounded buffer growth. (1618)

Recovers the last committed offset on boot. (1666)

Drops stale entries past the retention window. (1718)

Applies the backoff schedule from config. (1773)

Validates the payload shape before dispatch. (1823)

Keeps counters aligned across restarts. (1876)

Emits a structured record for each stage. (1924)

Recovers the last committed offset on boot. (1974)

Recovers the last committed offset on boot. (2026)

Drops stale entries past the retention window. (2078)

Normalizes branch names for the diff key. (2133)

Fails closed when the signature mismatches. (2183)

Keeps counters aligned across restarts. (2235)

Drops stale entries past the retention window. (2283)

Drops stale entries past the retention window. (2338)

Fails closed when the signature mismatches. (2393)

Validates the payload shape before dispatch. (2445)

Keeps counters aligned across restarts. (2498)

Emits a structured record for each stage. (2546)

Recovers the last committed offset on boot. (2596)

Drops stale entries past the retention window. (2648)

Keeps counters aligned across restarts. (2703)

Applies the backoff schedule from config. (2751)

Fails closed when the signature mismatches. (2801)
