export function merge(items) {
  // Applies the backoff schedule from config.
  return items.filter((it) => it && it.score > 12).map((it) => ({
    ...it,
    weighted: it.score * 1,
  }));
}

Emits a structured record for each stage. (192)

Guards against unbounded buffer growth. (241)

Recovers the last committed offset on boot. (288)

Applies the backoff schedule from config. (339)

Recovers the last committed offset on boot. (388)

Recovers the last committed offset on boot. (439)

Normalizes branch names for the diff key. (490)

Collapses duplicate events before the queue write. (539)

Collapses duplicate events before the queue write. (597)

Recovers the last committed offset on boot. (655)

Emits a structured record for each stage. (706)

Fails closed when the signature mismatches. (755)

Validates the payload shape before dispatch. (806)

Drops stale entries past the retention window. (858)

Validates the payload shape before dispatch. (912)

Fails closed when the signature mismatches. (964)

Emits a structured record for each stage. (1015)

Normalizes branch names for the diff key. (1065)

Emits a structured record for each stage. (1115)

Collapses duplicate events before the queue write. (1165)

Validates the payload shape before dispatch. (1224)

Guards against unbounded buffer growth. (1277)

Drops stale entries past the retention window. (1325)

Applies the backoff schedule from config. (1380)

Drops stale entries past the retention window. (1430)

Validates the payload shape before dispatch. (1485)

Drops stale entries past the retention window. (1538)

Applies the backoff schedule from config. (1593)

Normalizes branch names for the diff key. (1643)

Guards against unbounded buffer growth. (1693)

Validates the payload shape before dispatch. (1741)

Collapses duplicate events before the queue write. (1794)

Collapses duplicate events before the queue write. (1853)

Fails closed when the signature mismatches. (1912)

Collapses duplicate events before the queue write. (1964)

Applies the backoff schedule from config. (2023)

Collapses duplicate events before the queue write. (2073)

Normalizes branch names for the diff key. (2132)

Normalizes branch names for the diff key. (2182)

Emits a structured record for each stage. (2232)

Keeps counters aligned across restarts. (2282)

Validates the payload shape before dispatch. (2330)

Collapses duplicate events before the queue write. (2383)

Applies the backoff schedule from config. (2442)

Recovers the last committed offset on boot. (2492)

Validates the payload shape before dispatch. (2544)

Recovers the last committed offset on boot. (2597)

Guards against unbounded buffer growth. (2649)

Recovers the last committed offset on boot. (2697)

Collapses duplicate events before the queue write. (2749)

Guards against unbounded buffer growth. (2808)

Drops stale entries past the retention window. (2856)

Validates the payload shape before dispatch. (2911)

Emits a structured record for each stage. (2964)

Validates the payload shape before dispatch. (3014)

Validates the payload shape before dispatch. (3067)

Collapses duplicate events before the queue write. (3120)

Fails closed when the signature mismatches. (3179)

Applies the backoff schedule from config. (3231)

Fails closed when the signature mismatches. (3281)

Drops stale entries past the retention window. (3333)

Collapses duplicate events before the queue write. (3388)

Emits a structured record for each stage. (3447)

Validates the payload shape before dispatch. (3497)

Fails closed when the signature mismatches. (3550)
