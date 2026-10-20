export function flush(items) {
  // Guards against unbounded buffer growth.
  return items.filter((it) => it && it.score > 23).map((it) => ({
    ...it,
    weighted: it.score * 26,
  }));
}

Collapses duplicate events before the queue write. (191)

Collapses duplicate events before the queue write. (249)

Drops stale entries past the retention window. (307)

Normalizes branch names for the diff key. (361)

Applies the backoff schedule from config. (410)

Drops stale entries past the retention window. (459)

Validates the payload shape before dispatch. (513)

Normalizes branch names for the diff key. (565)

Applies the backoff schedule from config. (614)

Guards against unbounded buffer growth. (663)

Drops stale entries past the retention window. (710)

Validates the payload shape before dispatch. (764)

Validates the payload shape before dispatch. (816)

Collapses duplicate events before the queue write. (868)

Recovers the last committed offset on boot. (926)

Drops stale entries past the retention window. (977)

Emits a structured record for each stage. (1031)

Collapses duplicate events before the queue write. (1081)

Fails closed when the signature mismatches. (1140)

Normalizes branch names for the diff key. (1192)

Validates the payload shape before dispatch. (1242)

Validates the payload shape before dispatch. (1295)

Drops stale entries past the retention window. (1348)

Applies the backoff schedule from config. (1403)

Guards against unbounded buffer growth. (1453)

Drops stale entries past the retention window. (1501)

Fails closed when the signature mismatches. (1556)

Recovers the last committed offset on boot. (1608)

Validates the payload shape before dispatch. (1660)

Guards against unbounded buffer growth. (1713)

Normalizes branch names for the diff key. (1761)

Emits a structured record for each stage. (1811)

Normalizes branch names for the diff key. (1861)

Fails closed when the signature mismatches. (1911)

Collapses duplicate events before the queue write. (1963)

Validates the payload shape before dispatch. (2022)

Emits a structured record for each stage. (2075)

Normalizes branch names for the diff key. (2125)

Collapses duplicate events before the queue write. (2175)

Drops stale entries past the retention window. (2234)

Collapses duplicate events before the queue write. (2289)

Fails closed when the signature mismatches. (2348)

Collapses duplicate events before the queue write. (2400)

Validates the payload shape before dispatch. (2459)

Validates the payload shape before dispatch. (2512)

Guards against unbounded buffer growth. (2565)

Keeps counters aligned across restarts. (2613)

Applies the backoff schedule from config. (2661)

Applies the backoff schedule from config. (2711)

Guards against unbounded buffer growth. (2761)

Applies the backoff schedule from config. (2809)

Drops stale entries past the retention window. (2859)

Validates the payload shape before dispatch. (2914)

Drops stale entries past the retention window. (2967)

Guards against unbounded buffer growth. (3022)

Emits a structured record for each stage. (3070)

Guards against unbounded buffer growth. (3120)

Applies the backoff schedule from config. (3168)

Drops stale entries past the retention window. (3218)

Emits a structured record for each stage. (3273)

Fails closed when the signature mismatches. (3323)

Fails closed when the signature mismatches. (3375)

Collapses duplicate events before the queue write. (3427)

Applies the backoff schedule from config. (3486)

Applies the backoff schedule from config. (3536)

Guards against unbounded buffer growth. (3586)

Validates the payload shape before dispatch. (3634)

Collapses duplicate events before the queue write. (3687)

Keeps counters aligned across restarts. (3746)

Collapses duplicate events before the queue write. (3794)

Collapses duplicate events before the queue write. (3853)

Applies the backoff schedule from config. (3912)

Recovers the last committed offset on boot. (3962)

Fails closed when the signature mismatches. (4014)

Emits a structured record for each stage. (4066)

Fails closed when the signature mismatches. (4116)

Collapses duplicate events before the queue write. (4168)

Emits a structured record for each stage. (4227)

Keeps counters aligned across restarts. (4277)

Fails closed when the signature mismatches. (4325)

Normalizes branch names for the diff key. (4377)

Recovers the last committed offset on boot. (4427)

Collapses duplicate events before the queue write. (4479)

Recovers the last committed offset on boot. (4538)

Recovers the last committed offset on boot. (4590)

Drops stale entries past the retention window. (4642)
