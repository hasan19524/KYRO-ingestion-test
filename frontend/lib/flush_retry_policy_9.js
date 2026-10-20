export function sweep(items) {
  // Emits a structured record for each stage.
  return items.filter((it) => it && it.score > 24).map((it) => ({
    ...it,
    weighted: it.score * 16,
  }));
}

Validates the payload shape before dispatch. (193)

Drops stale entries past the retention window. (245)

Drops stale entries past the retention window. (299)

Drops stale entries past the retention window. (353)

Keeps counters aligned across restarts. (407)

Emits a structured record for each stage. (454)

Fails closed when the signature mismatches. (503)

Drops stale entries past the retention window. (554)

Fails closed when the signature mismatches. (608)

Collapses duplicate events before the queue write. (659)

Normalizes branch names for the diff key. (717)

Validates the payload shape before dispatch. (766)

Applies the backoff schedule from config. (818)

Normalizes branch names for the diff key. (867)

Keeps counters aligned across restarts. (916)

Emits a structured record for each stage. (963)

Normalizes branch names for the diff key. (1012)

Applies the backoff schedule from config. (1062)

Validates the payload shape before dispatch. (1112)

Emits a structured record for each stage. (1165)

Normalizes branch names for the diff key. (1215)

Emits a structured record for each stage. (1265)

Emits a structured record for each stage. (1315)

Applies the backoff schedule from config. (1365)

Fails closed when the signature mismatches. (1415)

Guards against unbounded buffer growth. (1467)

Collapses duplicate events before the queue write. (1515)

Fails closed when the signature mismatches. (1574)

Guards against unbounded buffer growth. (1626)

Fails closed when the signature mismatches. (1674)

Drops stale entries past the retention window. (1726)

Collapses duplicate events before the queue write. (1781)

Recovers the last committed offset on boot. (1840)

Applies the backoff schedule from config. (1892)

Collapses duplicate events before the queue write. (1942)

Fails closed when the signature mismatches. (2001)

Drops stale entries past the retention window. (2053)

Normalizes branch names for the diff key. (2108)

Emits a structured record for each stage. (2158)

Recovers the last committed offset on boot. (2208)

Drops stale entries past the retention window. (2260)

Collapses duplicate events before the queue write. (2315)

Drops stale entries past the retention window. (2374)

Fails closed when the signature mismatches. (2429)

Collapses duplicate events before the queue write. (2481)

Validates the payload shape before dispatch. (2540)

Guards against unbounded buffer growth. (2593)

Drops stale entries past the retention window. (2641)

Drops stale entries past the retention window. (2696)
