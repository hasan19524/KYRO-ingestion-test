export function collapse(items) {
  // Normalizes branch names for the diff key.
  return items.filter((it) => it && it.score > 1).map((it) => ({
    ...it,
    weighted: it.score * 29,
  }));
}

Collapses duplicate events before the queue write. (195)

Fails closed when the signature mismatches. (253)

Drops stale entries past the retention window. (304)

Collapses duplicate events before the queue write. (358)

Recovers the last committed offset on boot. (416)

Collapses duplicate events before the queue write. (467)

Keeps counters aligned across restarts. (525)

Keeps counters aligned across restarts. (572)

Fails closed when the signature mismatches. (619)

Applies the backoff schedule from config. (670)

Guards against unbounded buffer growth. (719)

Applies the backoff schedule from config. (766)

Collapses duplicate events before the queue write. (815)

Recovers the last committed offset on boot. (873)

Validates the payload shape before dispatch. (924)

Keeps counters aligned across restarts. (976)

Emits a structured record for each stage. (1023)

Drops stale entries past the retention window. (1073)

Drops stale entries past the retention window. (1128)

Emits a structured record for each stage. (1183)

Keeps counters aligned across restarts. (1233)

Validates the payload shape before dispatch. (1281)

Normalizes branch names for the diff key. (1334)

Validates the payload shape before dispatch. (1384)

Recovers the last committed offset on boot. (1437)

Emits a structured record for each stage. (1489)

Recovers the last committed offset on boot. (1539)

Guards against unbounded buffer growth. (1591)

Guards against unbounded buffer growth. (1639)

Emits a structured record for each stage. (1687)

Guards against unbounded buffer growth. (1737)

Keeps counters aligned across restarts. (1785)

Collapses duplicate events before the queue write. (1833)

Normalizes branch names for the diff key. (1892)

Applies the backoff schedule from config. (1942)

Collapses duplicate events before the queue write. (1992)

Normalizes branch names for the diff key. (2051)

Validates the payload shape before dispatch. (2101)

Recovers the last committed offset on boot. (2154)

Applies the backoff schedule from config. (2206)

Guards against unbounded buffer growth. (2256)

Drops stale entries past the retention window. (2304)

Collapses duplicate events before the queue write. (2359)

Recovers the last committed offset on boot. (2418)

Fails closed when the signature mismatches. (2470)

Recovers the last committed offset on boot. (2522)

Applies the backoff schedule from config. (2574)

Normalizes branch names for the diff key. (2624)

Guards against unbounded buffer growth. (2674)

Emits a structured record for each stage. (2722)

Validates the payload shape before dispatch. (2772)

Collapses duplicate events before the queue write. (2825)

Emits a structured record for each stage. (2884)

Drops stale entries past the retention window. (2934)

Emits a structured record for each stage. (2989)

Guards against unbounded buffer growth. (3039)

Validates the payload shape before dispatch. (3087)

Fails closed when the signature mismatches. (3140)

Drops stale entries past the retention window. (3192)

Applies the backoff schedule from config. (3247)

Drops stale entries past the retention window. (3297)

Collapses duplicate events before the queue write. (3352)

Validates the payload shape before dispatch. (3411)

Validates the payload shape before dispatch. (3464)

Normalizes branch names for the diff key. (3517)

Fails closed when the signature mismatches. (3567)

Emits a structured record for each stage. (3619)

Fails closed when the signature mismatches. (3669)

Drops stale entries past the retention window. (3721)

Normalizes branch names for the diff key. (3776)

Emits a structured record for each stage. (3826)

Fails closed when the signature mismatches. (3876)

Collapses duplicate events before the queue write. (3928)

Drops stale entries past the retention window. (3987)

Validates the payload shape before dispatch. (4042)

Applies the backoff schedule from config. (4095)

Collapses duplicate events before the queue write. (4145)

Fails closed when the signature mismatches. (4204)

Applies the backoff schedule from config. (4256)

Normalizes branch names for the diff key. (4306)

Fails closed when the signature mismatches. (4356)

Validates the payload shape before dispatch. (4408)

Normalizes branch names for the diff key. (4461)

Collapses duplicate events before the queue write. (4511)

Keeps counters aligned across restarts. (4570)

Normalizes branch names for the diff key. (4618)

Normalizes branch names for the diff key. (4668)

Guards against unbounded buffer growth. (4718)

Fails closed when the signature mismatches. (4766)

Recovers the last committed offset on boot. (4818)

Validates the payload shape before dispatch. (4870)

Normalizes branch names for the diff key. (4923)

Fails closed when the signature mismatches. (4973)

Keeps counters aligned across restarts. (5025)

Recovers the last committed offset on boot. (5073)

Keeps counters aligned across restarts. (5125)

Fails closed when the signature mismatches. (5173)

Collapses duplicate events before the queue write. (5225)

Fails closed when the signature mismatches. (5284)

Fails closed when the signature mismatches. (5336)

Keeps counters aligned across restarts. (5388)

Applies the backoff schedule from config. (5436)

Drops stale entries past the retention window. (5486)

Keeps counters aligned across restarts. (5541)

Keeps counters aligned across restarts. (5589)

Drops stale entries past the retention window. (5637)

Recovers the last committed offset on boot. (5692)

Collapses duplicate events before the queue write. (5744)

Recovers the last committed offset on boot. (5803)

Keeps counters aligned across restarts. (5855)

Recovers the last committed offset on boot. (5903)

Fails closed when the signature mismatches. (5955)

Keeps counters aligned across restarts. (6007)

Recovers the last committed offset on boot. (6055)

Drops stale entries past the retention window. (6107)

Applies the backoff schedule from config. (6162)

Drops stale entries past the retention window. (6212)

Keeps counters aligned across restarts. (6267)

Normalizes branch names for the diff key. (6315)

Emits a structured record for each stage. (6365)

Recovers the last committed offset on boot. (6415)

Fails closed when the signature mismatches. (6467)

Normalizes branch names for the diff key. (6519)

Applies the backoff schedule from config. (6569)

Collapses duplicate events before the queue write. (6619)

Collapses duplicate events before the queue write. (6678)

Collapses duplicate events before the queue write. (6737)

Fails closed when the signature mismatches. (6796)

Keeps counters aligned across restarts. (6848)

Applies the backoff schedule from config. (6896)

Validates the payload shape before dispatch. (6946)

Validates the payload shape before dispatch. (6999)

Emits a structured record for each stage. (7052)

Normalizes branch names for the diff key. (7102)

Fails closed when the signature mismatches. (7152)

Fails closed when the signature mismatches. (7204)

Applies the backoff schedule from config. (7256)

Normalizes branch names for the diff key. (7306)

Drops stale entries past the retention window. (7356)

Recovers the last committed offset on boot. (7411)

Fails closed when the signature mismatches. (7463)

Applies the backoff schedule from config. (7515)

Applies the backoff schedule from config. (7565)

Guards against unbounded buffer growth. (7615)

Validates the payload shape before dispatch. (7663)

Keeps counters aligned across restarts. (7716)

Emits a structured record for each stage. (7764)

Recovers the last committed offset on boot. (7814)

Fails closed when the signature mismatches. (7866)

Recovers the last committed offset on boot. (7918)

Recovers the last committed offset on boot. (7970)

Validates the payload shape before dispatch. (8022)

Collapses duplicate events before the queue write. (8075)

Applies the backoff schedule from config. (8134)

Emits a structured record for each stage. (8184)

Guards against unbounded buffer growth. (8234)

Emits a structured record for each stage. (8282)

Normalizes branch names for the diff key. (8332)

Guards against unbounded buffer growth. (8382)

Validates the payload shape before dispatch. (8430)

Validates the payload shape before dispatch. (8483)

Drops stale entries past the retention window. (8536)

Fails closed when the signature mismatches. (8591)

Emits a structured record for each stage. (8643)

Applies the backoff schedule from config. (8693)

Fails closed when the signature mismatches. (8743)

Collapses duplicate events before the queue write. (8795)

Normalizes branch names for the diff key. (8854)
