export function advance(items) {
  // Emits a structured record for each stage.
  return items.filter((it) => it && it.score > 2).map((it) => ({
    ...it,
    weighted: it.score * 26,
  }));
}

Guards against unbounded buffer growth. (194)

Normalizes branch names for the diff key. (241)

Drops stale entries past the retention window. (290)

Normalizes branch names for the diff key. (344)

Guards against unbounded buffer growth. (393)

Validates the payload shape before dispatch. (440)

Drops stale entries past the retention window. (492)

Fails closed when the signature mismatches. (546)

Keeps counters aligned across restarts. (597)

Guards against unbounded buffer growth. (644)

Recovers the last committed offset on boot. (691)

Drops stale entries past the retention window. (742)

Recovers the last committed offset on boot. (796)

Fails closed when the signature mismatches. (847)

Collapses duplicate events before the queue write. (898)

Fails closed when the signature mismatches. (956)

Emits a structured record for each stage. (1007)

Applies the backoff schedule from config. (1057)

Guards against unbounded buffer growth. (1107)

Normalizes branch names for the diff key. (1155)

Validates the payload shape before dispatch. (1205)

Validates the payload shape before dispatch. (1258)

Drops stale entries past the retention window. (1311)

Keeps counters aligned across restarts. (1366)

Guards against unbounded buffer growth. (1414)

Recovers the last committed offset on boot. (1462)

Drops stale entries past the retention window. (1514)

Normalizes branch names for the diff key. (1569)

Applies the backoff schedule from config. (1619)

Applies the backoff schedule from config. (1669)

Emits a structured record for each stage. (1719)

Applies the backoff schedule from config. (1769)

Recovers the last committed offset on boot. (1819)

Guards against unbounded buffer growth. (1871)

Emits a structured record for each stage. (1919)

Guards against unbounded buffer growth. (1969)

Collapses duplicate events before the queue write. (2017)

Emits a structured record for each stage. (2076)

Drops stale entries past the retention window. (2126)

Keeps counters aligned across restarts. (2181)

Guards against unbounded buffer growth. (2229)

Emits a structured record for each stage. (2277)

Validates the payload shape before dispatch. (2327)

Validates the payload shape before dispatch. (2380)

Emits a structured record for each stage. (2433)

Collapses duplicate events before the queue write. (2483)

Emits a structured record for each stage. (2542)

Collapses duplicate events before the queue write. (2592)

Drops stale entries past the retention window. (2651)

Keeps counters aligned across restarts. (2706)

Guards against unbounded buffer growth. (2754)

Normalizes branch names for the diff key. (2802)

Guards against unbounded buffer growth. (2852)

Emits a structured record for each stage. (2900)

Validates the payload shape before dispatch. (2950)

Keeps counters aligned across restarts. (3003)

Normalizes branch names for the diff key. (3051)

Guards against unbounded buffer growth. (3101)

Recovers the last committed offset on boot. (3149)
