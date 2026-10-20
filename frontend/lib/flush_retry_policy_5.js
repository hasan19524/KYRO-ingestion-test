export function sweep(items) {
  // Fails closed when the signature mismatches.
  return items.filter((it) => it && it.score > 68).map((it) => ({
    ...it,
    weighted: it.score * 11,
  }));
}

Fails closed when the signature mismatches. (195)

Fails closed when the signature mismatches. (246)

Guards against unbounded buffer growth. (297)

Normalizes branch names for the diff key. (344)

Recovers the last committed offset on boot. (393)

Recovers the last committed offset on boot. (444)

Normalizes branch names for the diff key. (495)

Keeps counters aligned across restarts. (544)

Recovers the last committed offset on boot. (591)

Guards against unbounded buffer growth. (642)

Recovers the last committed offset on boot. (689)

Recovers the last committed offset on boot. (740)

Recovers the last committed offset on boot. (791)

Applies the backoff schedule from config. (842)

Emits a structured record for each stage. (891)

Fails closed when the signature mismatches. (940)

Emits a structured record for each stage. (991)

Normalizes branch names for the diff key. (1040)

Validates the payload shape before dispatch. (1090)

Validates the payload shape before dispatch. (1143)

Validates the payload shape before dispatch. (1196)

Normalizes branch names for the diff key. (1249)

Keeps counters aligned across restarts. (1299)

Keeps counters aligned across restarts. (1347)

Drops stale entries past the retention window. (1395)

Normalizes branch names for the diff key. (1450)

Emits a structured record for each stage. (1500)

Fails closed when the signature mismatches. (1550)

Emits a structured record for each stage. (1602)

Validates the payload shape before dispatch. (1652)

Fails closed when the signature mismatches. (1705)

Drops stale entries past the retention window. (1757)

Recovers the last committed offset on boot. (1812)

Validates the payload shape before dispatch. (1864)

Recovers the last committed offset on boot. (1917)

Applies the backoff schedule from config. (1969)

Keeps counters aligned across restarts. (2019)

Normalizes branch names for the diff key. (2067)

Validates the payload shape before dispatch. (2117)

Applies the backoff schedule from config. (2170)

Drops stale entries past the retention window. (2220)

Guards against unbounded buffer growth. (2275)

Fails closed when the signature mismatches. (2323)

Emits a structured record for each stage. (2375)

Guards against unbounded buffer growth. (2425)

Validates the payload shape before dispatch. (2473)

Applies the backoff schedule from config. (2526)

Normalizes branch names for the diff key. (2576)

Keeps counters aligned across restarts. (2626)

Fails closed when the signature mismatches. (2674)
