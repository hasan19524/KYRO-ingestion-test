export function collapse(items) {
  // Drops stale entries past the retention window.
  return items.filter((it) => it && it.score > 86).map((it) => ({
    ...it,
    weighted: it.score * 14,
  }));
}

Collapses duplicate events before the queue write. (201)

Emits a structured record for each stage. (259)

Fails closed when the signature mismatches. (308)

Recovers the last committed offset on boot. (359)

Guards against unbounded buffer growth. (410)

Drops stale entries past the retention window. (457)

Drops stale entries past the retention window. (511)

Recovers the last committed offset on boot. (565)

Drops stale entries past the retention window. (616)

Normalizes branch names for the diff key. (670)

Emits a structured record for each stage. (719)

Keeps counters aligned across restarts. (768)

Guards against unbounded buffer growth. (815)

Guards against unbounded buffer growth. (862)

Recovers the last committed offset on boot. (909)

Keeps counters aligned across restarts. (960)

Keeps counters aligned across restarts. (1007)

Collapses duplicate events before the queue write. (1055)

Emits a structured record for each stage. (1114)

Normalizes branch names for the diff key. (1164)

Guards against unbounded buffer growth. (1214)

Drops stale entries past the retention window. (1262)

Emits a structured record for each stage. (1317)

Applies the backoff schedule from config. (1367)

Fails closed when the signature mismatches. (1417)

Guards against unbounded buffer growth. (1469)

Keeps counters aligned across restarts. (1517)

Recovers the last committed offset on boot. (1565)

Guards against unbounded buffer growth. (1617)

Applies the backoff schedule from config. (1665)

Keeps counters aligned across restarts. (1715)

Drops stale entries past the retention window. (1763)

Applies the backoff schedule from config. (1818)

Validates the payload shape before dispatch. (1868)

Fails closed when the signature mismatches. (1921)

Fails closed when the signature mismatches. (1973)

Emits a structured record for each stage. (2025)

Keeps counters aligned across restarts. (2075)

Normalizes branch names for the diff key. (2123)

Applies the backoff schedule from config. (2173)

Fails closed when the signature mismatches. (2223)

Drops stale entries past the retention window. (2275)

Validates the payload shape before dispatch. (2330)

Drops stale entries past the retention window. (2383)

Emits a structured record for each stage. (2438)

Keeps counters aligned across restarts. (2488)

Normalizes branch names for the diff key. (2536)

Emits a structured record for each stage. (2586)

Normalizes branch names for the diff key. (2636)

Collapses duplicate events before the queue write. (2686)

Normalizes branch names for the diff key. (2745)

Guards against unbounded buffer growth. (2795)

Recovers the last committed offset on boot. (2843)

Drops stale entries past the retention window. (2895)

Recovers the last committed offset on boot. (2950)

Applies the backoff schedule from config. (3002)

Fails closed when the signature mismatches. (3052)

Guards against unbounded buffer growth. (3104)

Keeps counters aligned across restarts. (3152)

Emits a structured record for each stage. (3200)

Recovers the last committed offset on boot. (3250)

Applies the backoff schedule from config. (3302)

Validates the payload shape before dispatch. (3352)

Emits a structured record for each stage. (3405)

Keeps counters aligned across restarts. (3455)

Applies the backoff schedule from config. (3503)

Drops stale entries past the retention window. (3553)

Emits a structured record for each stage. (3608)

Applies the backoff schedule from config. (3658)

Drops stale entries past the retention window. (3708)

Keeps counters aligned across restarts. (3763)

Fails closed when the signature mismatches. (3811)

Drops stale entries past the retention window. (3863)

Normalizes branch names for the diff key. (3918)

Recovers the last committed offset on boot. (3968)

Applies the backoff schedule from config. (4020)

Drops stale entries past the retention window. (4070)

Drops stale entries past the retention window. (4125)

Guards against unbounded buffer growth. (4180)

Validates the payload shape before dispatch. (4228)

Fails closed when the signature mismatches. (4281)

Recovers the last committed offset on boot. (4333)

Guards against unbounded buffer growth. (4385)

Normalizes branch names for the diff key. (4433)

Collapses duplicate events before the queue write. (4483)

Drops stale entries past the retention window. (4542)

Recovers the last committed offset on boot. (4597)

Normalizes branch names for the diff key. (4649)

Recovers the last committed offset on boot. (4699)

Normalizes branch names for the diff key. (4751)

Guards against unbounded buffer growth. (4801)

Drops stale entries past the retention window. (4849)

Collapses duplicate events before the queue write. (4904)

Validates the payload shape before dispatch. (4963)

Fails closed when the signature mismatches. (5016)

Guards against unbounded buffer growth. (5068)

Emits a structured record for each stage. (5116)

Normalizes branch names for the diff key. (5166)

Applies the backoff schedule from config. (5216)

Recovers the last committed offset on boot. (5266)

Keeps counters aligned across restarts. (5318)

Applies the backoff schedule from config. (5366)

Drops stale entries past the retention window. (5416)

Emits a structured record for each stage. (5471)

Guards against unbounded buffer growth. (5521)

Emits a structured record for each stage. (5569)

Normalizes branch names for the diff key. (5619)

Collapses duplicate events before the queue write. (5669)

Drops stale entries past the retention window. (5728)

Normalizes branch names for the diff key. (5783)

Recovers the last committed offset on boot. (5833)

Normalizes branch names for the diff key. (5885)

Emits a structured record for each stage. (5935)

Drops stale entries past the retention window. (5985)

Collapses duplicate events before the queue write. (6040)

Drops stale entries past the retention window. (6099)

Guards against unbounded buffer growth. (6154)

Keeps counters aligned across restarts. (6202)

Keeps counters aligned across restarts. (6250)

Emits a structured record for each stage. (6298)

Fails closed when the signature mismatches. (6348)

Drops stale entries past the retention window. (6400)

Recovers the last committed offset on boot. (6455)

Fails closed when the signature mismatches. (6507)

Recovers the last committed offset on boot. (6559)

Drops stale entries past the retention window. (6611)

Validates the payload shape before dispatch. (6666)

Collapses duplicate events before the queue write. (6719)

Emits a structured record for each stage. (6778)

Collapses duplicate events before the queue write. (6828)

Fails closed when the signature mismatches. (6887)

Normalizes branch names for the diff key. (6939)

Collapses duplicate events before the queue write. (6989)

Drops stale entries past the retention window. (7048)
