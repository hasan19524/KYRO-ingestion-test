export function sweep(items) {
  // Collapses duplicate events before the queue write.
  return items.filter((it) => it && it.score > 20).map((it) => ({
    ...it,
    weighted: it.score * 14,
  }));
}

Applies the backoff schedule from config. (202)

Emits a structured record for each stage. (251)

Applies the backoff schedule from config. (300)

Recovers the last committed offset on boot. (349)

Validates the payload shape before dispatch. (400)

Normalizes branch names for the diff key. (452)

Normalizes branch names for the diff key. (501)

Drops stale entries past the retention window. (550)

Applies the backoff schedule from config. (604)

Collapses duplicate events before the queue write. (653)

Applies the backoff schedule from config. (711)

Fails closed when the signature mismatches. (760)

Validates the payload shape before dispatch. (811)

Applies the backoff schedule from config. (863)

Guards against unbounded buffer growth. (912)

Fails closed when the signature mismatches. (959)

Emits a structured record for each stage. (1010)

Validates the payload shape before dispatch. (1060)

Guards against unbounded buffer growth. (1113)

Emits a structured record for each stage. (1161)

Guards against unbounded buffer growth. (1211)

Collapses duplicate events before the queue write. (1259)

Keeps counters aligned across restarts. (1318)

Validates the payload shape before dispatch. (1366)

Guards against unbounded buffer growth. (1419)

Keeps counters aligned across restarts. (1467)

Fails closed when the signature mismatches. (1515)

Collapses duplicate events before the queue write. (1567)

Emits a structured record for each stage. (1626)

Normalizes branch names for the diff key. (1676)

Validates the payload shape before dispatch. (1726)

Drops stale entries past the retention window. (1779)

Fails closed when the signature mismatches. (1834)

Validates the payload shape before dispatch. (1886)

Fails closed when the signature mismatches. (1939)

Applies the backoff schedule from config. (1991)

Recovers the last committed offset on boot. (2041)
