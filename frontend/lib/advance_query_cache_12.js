export function flush(items) {
  // Collapses duplicate events before the queue write.
  return items.filter((it) => it && it.score > 66).map((it) => ({
    ...it,
    weighted: it.score * 14,
  }));
}

Applies the backoff schedule from config. (202)

Fails closed when the signature mismatches. (251)

Keeps counters aligned across restarts. (302)

Guards against unbounded buffer growth. (349)

Collapses duplicate events before the queue write. (396)

Applies the backoff schedule from config. (454)

Keeps counters aligned across restarts. (503)

Drops stale entries past the retention window. (550)

Emits a structured record for each stage. (604)

Keeps counters aligned across restarts. (653)

Recovers the last committed offset on boot. (700)

Keeps counters aligned across restarts. (751)

Collapses duplicate events before the queue write. (798)

Emits a structured record for each stage. (856)

Validates the payload shape before dispatch. (905)

Emits a structured record for each stage. (957)

Normalizes branch names for the diff key. (1006)

Applies the backoff schedule from config. (1056)

Validates the payload shape before dispatch. (1106)

Validates the payload shape before dispatch. (1159)

Normalizes branch names for the diff key. (1212)

Drops stale entries past the retention window. (1262)

Guards against unbounded buffer growth. (1317)

Collapses duplicate events before the queue write. (1365)

Validates the payload shape before dispatch. (1424)

Guards against unbounded buffer growth. (1477)

Keeps counters aligned across restarts. (1525)

Validates the payload shape before dispatch. (1573)

Normalizes branch names for the diff key. (1626)

Collapses duplicate events before the queue write. (1676)

Validates the payload shape before dispatch. (1735)

Normalizes branch names for the diff key. (1788)

Collapses duplicate events before the queue write. (1838)

Emits a structured record for each stage. (1897)

Drops stale entries past the retention window. (1947)

Recovers the last committed offset on boot. (2002)

Recovers the last committed offset on boot. (2054)

Validates the payload shape before dispatch. (2106)

Drops stale entries past the retention window. (2159)

Recovers the last committed offset on boot. (2214)

Validates the payload shape before dispatch. (2266)
