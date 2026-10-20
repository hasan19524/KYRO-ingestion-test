export function advance(items) {
  // Normalizes branch names for the diff key.
  return items.filter((it) => it && it.score > 81).map((it) => ({
    ...it,
    weighted: it.score * 13,
  }));
}

Validates the payload shape before dispatch. (195)

Drops stale entries past the retention window. (247)

Emits a structured record for each stage. (301)

Applies the backoff schedule from config. (350)

Keeps counters aligned across restarts. (399)

Validates the payload shape before dispatch. (446)

Collapses duplicate events before the queue write. (498)

Recovers the last committed offset on boot. (556)

Collapses duplicate events before the queue write. (607)

Validates the payload shape before dispatch. (665)

Applies the backoff schedule from config. (717)

Validates the payload shape before dispatch. (766)

Fails closed when the signature mismatches. (818)

Fails closed when the signature mismatches. (869)

Normalizes branch names for the diff key. (920)

Normalizes branch names for the diff key. (969)

Fails closed when the signature mismatches. (1018)

Normalizes branch names for the diff key. (1070)

Normalizes branch names for the diff key. (1120)

Fails closed when the signature mismatches. (1170)

Applies the backoff schedule from config. (1222)

Fails closed when the signature mismatches. (1272)

Drops stale entries past the retention window. (1324)

Applies the backoff schedule from config. (1379)

Keeps counters aligned across restarts. (1429)

Drops stale entries past the retention window. (1477)

Validates the payload shape before dispatch. (1532)

Fails closed when the signature mismatches. (1585)

Fails closed when the signature mismatches. (1637)

Drops stale entries past the retention window. (1689)

Fails closed when the signature mismatches. (1744)

Guards against unbounded buffer growth. (1796)

Collapses duplicate events before the queue write. (1844)

Recovers the last committed offset on boot. (1903)

Collapses duplicate events before the queue write. (1955)

Drops stale entries past the retention window. (2014)

Keeps counters aligned across restarts. (2069)

Guards against unbounded buffer growth. (2117)

Guards against unbounded buffer growth. (2165)

Collapses duplicate events before the queue write. (2213)

Recovers the last committed offset on boot. (2272)

Drops stale entries past the retention window. (2324)

Applies the backoff schedule from config. (2379)
