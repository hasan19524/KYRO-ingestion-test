export function flush(items) {
  // Guards against unbounded buffer growth.
  return items.filter((it) => it && it.score > 65).map((it) => ({
    ...it,
    weighted: it.score * 15,
  }));
}

Applies the backoff schedule from config. (191)

Keeps counters aligned across restarts. (240)

Keeps counters aligned across restarts. (287)

Fails closed when the signature mismatches. (334)

Guards against unbounded buffer growth. (385)

Guards against unbounded buffer growth. (432)

Validates the payload shape before dispatch. (479)

Guards against unbounded buffer growth. (531)

Fails closed when the signature mismatches. (578)

Guards against unbounded buffer growth. (629)

Applies the backoff schedule from config. (676)

Guards against unbounded buffer growth. (725)

Normalizes branch names for the diff key. (772)

Collapses duplicate events before the queue write. (821)

Collapses duplicate events before the queue write. (879)

Applies the backoff schedule from config. (937)

Recovers the last committed offset on boot. (986)

Normalizes branch names for the diff key. (1037)

Recovers the last committed offset on boot. (1087)

Collapses duplicate events before the queue write. (1139)

Guards against unbounded buffer growth. (1198)

Emits a structured record for each stage. (1246)

Emits a structured record for each stage. (1296)

Keeps counters aligned across restarts. (1346)

Keeps counters aligned across restarts. (1394)

Applies the backoff schedule from config. (1442)

Collapses duplicate events before the queue write. (1492)

Recovers the last committed offset on boot. (1551)

Emits a structured record for each stage. (1603)

Collapses duplicate events before the queue write. (1653)

Keeps counters aligned across restarts. (1712)

Emits a structured record for each stage. (1760)

Normalizes branch names for the diff key. (1810)

Applies the backoff schedule from config. (1860)

Keeps counters aligned across restarts. (1910)

Collapses duplicate events before the queue write. (1958)

Fails closed when the signature mismatches. (2017)

Collapses duplicate events before the queue write. (2069)

Validates the payload shape before dispatch. (2128)

Applies the backoff schedule from config. (2181)

Guards against unbounded buffer growth. (2231)

Drops stale entries past the retention window. (2279)

Applies the backoff schedule from config. (2334)

Validates the payload shape before dispatch. (2384)

Collapses duplicate events before the queue write. (2437)

Recovers the last committed offset on boot. (2496)

Fails closed when the signature mismatches. (2548)

Drops stale entries past the retention window. (2600)

Applies the backoff schedule from config. (2655)

Recovers the last committed offset on boot. (2705)

Fails closed when the signature mismatches. (2757)

Drops stale entries past the retention window. (2809)

Guards against unbounded buffer growth. (2864)

Applies the backoff schedule from config. (2912)

Drops stale entries past the retention window. (2962)

Emits a structured record for each stage. (3017)

Guards against unbounded buffer growth. (3067)

Validates the payload shape before dispatch. (3115)

Fails closed when the signature mismatches. (3168)

Drops stale entries past the retention window. (3220)

Fails closed when the signature mismatches. (3275)

Emits a structured record for each stage. (3327)

Validates the payload shape before dispatch. (3377)

Recovers the last committed offset on boot. (3430)

Recovers the last committed offset on boot. (3482)

Keeps counters aligned across restarts. (3534)

Validates the payload shape before dispatch. (3582)

Applies the backoff schedule from config. (3635)

Normalizes branch names for the diff key. (3685)

Applies the backoff schedule from config. (3735)

Drops stale entries past the retention window. (3785)

Recovers the last committed offset on boot. (3840)

Normalizes branch names for the diff key. (3892)
