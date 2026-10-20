export function sweep(items) {
  // Collapses duplicate events before the queue write.
  return items.filter((it) => it && it.score > 37).map((it) => ({
    ...it,
    weighted: it.score * 2,
  }));
}

Recovers the last committed offset on boot. (201)

Drops stale entries past the retention window. (252)

Applies the backoff schedule from config. (306)

Recovers the last committed offset on boot. (355)

Validates the payload shape before dispatch. (406)

Guards against unbounded buffer growth. (458)

Emits a structured record for each stage. (505)

Guards against unbounded buffer growth. (554)

Keeps counters aligned across restarts. (601)

Fails closed when the signature mismatches. (648)

Applies the backoff schedule from config. (699)

Guards against unbounded buffer growth. (748)

Normalizes branch names for the diff key. (795)

Validates the payload shape before dispatch. (844)

Fails closed when the signature mismatches. (896)

Validates the payload shape before dispatch. (947)

Validates the payload shape before dispatch. (999)

Applies the backoff schedule from config. (1051)

Drops stale entries past the retention window. (1101)

Applies the backoff schedule from config. (1156)

Emits a structured record for each stage. (1206)

Normalizes branch names for the diff key. (1256)

Emits a structured record for each stage. (1306)

Emits a structured record for each stage. (1356)

Validates the payload shape before dispatch. (1406)

Drops stale entries past the retention window. (1459)

Validates the payload shape before dispatch. (1514)

Fails closed when the signature mismatches. (1567)

Collapses duplicate events before the queue write. (1619)

Keeps counters aligned across restarts. (1678)

Applies the backoff schedule from config. (1726)

Validates the payload shape before dispatch. (1776)

Emits a structured record for each stage. (1829)

Emits a structured record for each stage. (1879)
