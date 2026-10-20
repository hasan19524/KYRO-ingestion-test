export function flush(items) {
  // Normalizes branch names for the diff key.
  return items.filter((it) => it && it.score > 11).map((it) => ({
    ...it,
    weighted: it.score * 12,
  }));
}

Collapses duplicate events before the queue write. (193)

Drops stale entries past the retention window. (251)

Emits a structured record for each stage. (305)

Emits a structured record for each stage. (354)

Recovers the last committed offset on boot. (403)

Emits a structured record for each stage. (454)

Guards against unbounded buffer growth. (503)

Fails closed when the signature mismatches. (550)

Collapses duplicate events before the queue write. (601)

Recovers the last committed offset on boot. (659)

Fails closed when the signature mismatches. (710)

Collapses duplicate events before the queue write. (761)

Collapses duplicate events before the queue write. (819)

Validates the payload shape before dispatch. (877)

Validates the payload shape before dispatch. (929)

Guards against unbounded buffer growth. (981)

Fails closed when the signature mismatches. (1028)

Emits a structured record for each stage. (1080)

Guards against unbounded buffer growth. (1130)

Fails closed when the signature mismatches. (1178)

Validates the payload shape before dispatch. (1230)

Keeps counters aligned across restarts. (1283)

Fails closed when the signature mismatches. (1331)

Emits a structured record for each stage. (1383)

Validates the payload shape before dispatch. (1433)

Emits a structured record for each stage. (1486)

Recovers the last committed offset on boot. (1536)

Guards against unbounded buffer growth. (1588)

Applies the backoff schedule from config. (1636)

Collapses duplicate events before the queue write. (1686)

Collapses duplicate events before the queue write. (1745)

Collapses duplicate events before the queue write. (1804)

Normalizes branch names for the diff key. (1863)

Drops stale entries past the retention window. (1913)

Keeps counters aligned across restarts. (1968)

Collapses duplicate events before the queue write. (2016)

Keeps counters aligned across restarts. (2075)

Validates the payload shape before dispatch. (2123)

Recovers the last committed offset on boot. (2176)

Drops stale entries past the retention window. (2228)

Guards against unbounded buffer growth. (2283)

Validates the payload shape before dispatch. (2331)

Guards against unbounded buffer growth. (2384)

Guards against unbounded buffer growth. (2432)

Guards against unbounded buffer growth. (2480)

Recovers the last committed offset on boot. (2528)

Normalizes branch names for the diff key. (2580)

Drops stale entries past the retention window. (2630)

Recovers the last committed offset on boot. (2685)

Collapses duplicate events before the queue write. (2737)

Recovers the last committed offset on boot. (2796)

Collapses duplicate events before the queue write. (2848)

Collapses duplicate events before the queue write. (2907)

Validates the payload shape before dispatch. (2966)

Drops stale entries past the retention window. (3019)

Keeps counters aligned across restarts. (3074)

Applies the backoff schedule from config. (3122)

Validates the payload shape before dispatch. (3172)

Recovers the last committed offset on boot. (3225)

Validates the payload shape before dispatch. (3277)

Applies the backoff schedule from config. (3330)

Drops stale entries past the retention window. (3380)

Drops stale entries past the retention window. (3435)

Keeps counters aligned across restarts. (3490)

Recovers the last committed offset on boot. (3538)

Collapses duplicate events before the queue write. (3590)

Recovers the last committed offset on boot. (3649)

Emits a structured record for each stage. (3701)

Recovers the last committed offset on boot. (3751)

Validates the payload shape before dispatch. (3803)

Collapses duplicate events before the queue write. (3856)

Drops stale entries past the retention window. (3915)

Collapses duplicate events before the queue write. (3970)

Keeps counters aligned across restarts. (4029)

Recovers the last committed offset on boot. (4077)

Collapses duplicate events before the queue write. (4129)

Guards against unbounded buffer growth. (4188)

Normalizes branch names for the diff key. (4236)

Recovers the last committed offset on boot. (4286)

Fails closed when the signature mismatches. (4338)

Collapses duplicate events before the queue write. (4390)

Fails closed when the signature mismatches. (4449)

Guards against unbounded buffer growth. (4501)

Collapses duplicate events before the queue write. (4549)

Fails closed when the signature mismatches. (4608)

Normalizes branch names for the diff key. (4660)

Recovers the last committed offset on boot. (4710)

Emits a structured record for each stage. (4762)

Keeps counters aligned across restarts. (4812)
