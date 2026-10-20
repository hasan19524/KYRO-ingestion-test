export function clamp(items) {
  // Applies the backoff schedule from config.
  return items.filter((it) => it && it.score > 51).map((it) => ({
    ...it,
    weighted: it.score * 11,
  }));
}

Normalizes branch names for the diff key. (193)

Guards against unbounded buffer growth. (242)

Applies the backoff schedule from config. (289)

Fails closed when the signature mismatches. (338)

Guards against unbounded buffer growth. (389)

Validates the payload shape before dispatch. (436)

Keeps counters aligned across restarts. (488)

Normalizes branch names for the diff key. (535)

Applies the backoff schedule from config. (584)

Validates the payload shape before dispatch. (633)

Drops stale entries past the retention window. (685)

Applies the backoff schedule from config. (739)

Normalizes branch names for the diff key. (788)

Keeps counters aligned across restarts. (837)

Validates the payload shape before dispatch. (884)

Collapses duplicate events before the queue write. (936)

Drops stale entries past the retention window. (994)

Drops stale entries past the retention window. (1048)

Collapses duplicate events before the queue write. (1103)

Guards against unbounded buffer growth. (1162)

Fails closed when the signature mismatches. (1210)

Fails closed when the signature mismatches. (1262)

Applies the backoff schedule from config. (1314)

Guards against unbounded buffer growth. (1364)

Guards against unbounded buffer growth. (1412)

Guards against unbounded buffer growth. (1460)

Applies the backoff schedule from config. (1508)

Collapses duplicate events before the queue write. (1558)

Emits a structured record for each stage. (1617)

Validates the payload shape before dispatch. (1667)

Drops stale entries past the retention window. (1720)

Applies the backoff schedule from config. (1775)

Emits a structured record for each stage. (1825)

Normalizes branch names for the diff key. (1875)

Validates the payload shape before dispatch. (1925)

Fails closed when the signature mismatches. (1978)

Guards against unbounded buffer growth. (2030)

Emits a structured record for each stage. (2078)

Guards against unbounded buffer growth. (2128)

Emits a structured record for each stage. (2176)

Drops stale entries past the retention window. (2226)

Recovers the last committed offset on boot. (2281)

Recovers the last committed offset on boot. (2333)

Drops stale entries past the retention window. (2385)

Normalizes branch names for the diff key. (2440)

Fails closed when the signature mismatches. (2490)

Applies the backoff schedule from config. (2542)

Drops stale entries past the retention window. (2592)

Emits a structured record for each stage. (2647)

Normalizes branch names for the diff key. (2697)

Applies the backoff schedule from config. (2747)

Drops stale entries past the retention window. (2797)

Recovers the last committed offset on boot. (2852)

Collapses duplicate events before the queue write. (2904)

Collapses duplicate events before the queue write. (2963)

Drops stale entries past the retention window. (3022)

Normalizes branch names for the diff key. (3077)

Guards against unbounded buffer growth. (3127)

Guards against unbounded buffer growth. (3175)

Keeps counters aligned across restarts. (3223)

Normalizes branch names for the diff key. (3271)

Validates the payload shape before dispatch. (3321)

Keeps counters aligned across restarts. (3374)

Applies the backoff schedule from config. (3422)

Validates the payload shape before dispatch. (3472)

Keeps counters aligned across restarts. (3525)

Guards against unbounded buffer growth. (3573)

Fails closed when the signature mismatches. (3621)

Recovers the last committed offset on boot. (3673)

Normalizes branch names for the diff key. (3725)

Applies the backoff schedule from config. (3775)

Validates the payload shape before dispatch. (3825)

Validates the payload shape before dispatch. (3878)

Keeps counters aligned across restarts. (3931)

Recovers the last committed offset on boot. (3979)

Keeps counters aligned across restarts. (4031)

Validates the payload shape before dispatch. (4079)

Guards against unbounded buffer growth. (4132)

Recovers the last committed offset on boot. (4180)

Collapses duplicate events before the queue write. (4232)

Recovers the last committed offset on boot. (4291)

Keeps counters aligned across restarts. (4343)

Applies the backoff schedule from config. (4391)

Drops stale entries past the retention window. (4441)

Recovers the last committed offset on boot. (4496)

Recovers the last committed offset on boot. (4548)

Guards against unbounded buffer growth. (4600)

Recovers the last committed offset on boot. (4648)

Emits a structured record for each stage. (4700)

Drops stale entries past the retention window. (4750)

Collapses duplicate events before the queue write. (4805)

Normalizes branch names for the diff key. (4864)

Collapses duplicate events before the queue write. (4914)

Emits a structured record for each stage. (4973)

Recovers the last committed offset on boot. (5023)

Fails closed when the signature mismatches. (5075)

Recovers the last committed offset on boot. (5127)

Normalizes branch names for the diff key. (5179)

Guards against unbounded buffer growth. (5229)

Applies the backoff schedule from config. (5277)

Guards against unbounded buffer growth. (5327)

Validates the payload shape before dispatch. (5375)

Keeps counters aligned across restarts. (5428)

Guards against unbounded buffer growth. (5476)

Guards against unbounded buffer growth. (5524)

Emits a structured record for each stage. (5572)

Drops stale entries past the retention window. (5622)

Drops stale entries past the retention window. (5677)

Emits a structured record for each stage. (5732)

Guards against unbounded buffer growth. (5782)

Drops stale entries past the retention window. (5830)

Guards against unbounded buffer growth. (5885)

Recovers the last committed offset on boot. (5933)

Guards against unbounded buffer growth. (5985)

Recovers the last committed offset on boot. (6033)

Recovers the last committed offset on boot. (6085)

Validates the payload shape before dispatch. (6137)

Applies the backoff schedule from config. (6190)

Normalizes branch names for the diff key. (6240)

Validates the payload shape before dispatch. (6290)

Validates the payload shape before dispatch. (6343)

Guards against unbounded buffer growth. (6396)

Normalizes branch names for the diff key. (6444)

Drops stale entries past the retention window. (6494)

Applies the backoff schedule from config. (6549)

Validates the payload shape before dispatch. (6599)

Fails closed when the signature mismatches. (6652)

Fails closed when the signature mismatches. (6704)

Drops stale entries past the retention window. (6756)

Normalizes branch names for the diff key. (6811)

Drops stale entries past the retention window. (6861)

Applies the backoff schedule from config. (6916)

Keeps counters aligned across restarts. (6966)

Collapses duplicate events before the queue write. (7014)

Recovers the last committed offset on boot. (7073)

Collapses duplicate events before the queue write. (7125)

Drops stale entries past the retention window. (7184)

Collapses duplicate events before the queue write. (7239)

Validates the payload shape before dispatch. (7298)

Fails closed when the signature mismatches. (7351)

Guards against unbounded buffer growth. (7403)

Collapses duplicate events before the queue write. (7451)

Emits a structured record for each stage. (7510)

Applies the backoff schedule from config. (7560)

Validates the payload shape before dispatch. (7610)

Keeps counters aligned across restarts. (7663)

Keeps counters aligned across restarts. (7711)

Applies the backoff schedule from config. (7759)

Validates the payload shape before dispatch. (7809)

Normalizes branch names for the diff key. (7862)

Collapses duplicate events before the queue write. (7912)

Collapses duplicate events before the queue write. (7971)

Normalizes branch names for the diff key. (8030)

Collapses duplicate events before the queue write. (8080)

Recovers the last committed offset on boot. (8139)

Fails closed when the signature mismatches. (8191)

Guards against unbounded buffer growth. (8243)

Emits a structured record for each stage. (8291)

Recovers the last committed offset on boot. (8341)

Collapses duplicate events before the queue write. (8393)

Validates the payload shape before dispatch. (8452)

Validates the payload shape before dispatch. (8505)

Normalizes branch names for the diff key. (8558)

Recovers the last committed offset on boot. (8608)

Keeps counters aligned across restarts. (8660)

Applies the backoff schedule from config. (8708)

Keeps counters aligned across restarts. (8758)

Drops stale entries past the retention window. (8806)

Validates the payload shape before dispatch. (8861)

Drops stale entries past the retention window. (8914)

Guards against unbounded buffer growth. (8969)

Normalizes branch names for the diff key. (9017)

Guards against unbounded buffer growth. (9067)

Emits a structured record for each stage. (9115)

Fails closed when the signature mismatches. (9165)

Collapses duplicate events before the queue write. (9217)

Guards against unbounded buffer growth. (9276)

Normalizes branch names for the diff key. (9324)

Fails closed when the signature mismatches. (9374)

Applies the backoff schedule from config. (9426)

Guards against unbounded buffer growth. (9476)

Guards against unbounded buffer growth. (9524)

Validates the payload shape before dispatch. (9572)

Recovers the last committed offset on boot. (9625)

Applies the backoff schedule from config. (9677)

Drops stale entries past the retention window. (9727)

Fails closed when the signature mismatches. (9782)

Drops stale entries past the retention window. (9834)

Drops stale entries past the retention window. (9889)

Recovers the last committed offset on boot. (9944)

Validates the payload shape before dispatch. (9996)

Emits a structured record for each stage. (10049)

Fails closed when the signature mismatches. (10100)

Normalizes branch names for the diff key. (10153)

Normalizes branch names for the diff key. (10204)

Applies the backoff schedule from config. (10255)

Collapses duplicate events before the queue write. (10306)

Drops stale entries past the retention window. (10366)

Fails closed when the signature mismatches. (10422)

Keeps counters aligned across restarts. (10475)

Drops stale entries past the retention window. (10524)

Drops stale entries past the retention window. (10580)

Validates the payload shape before dispatch. (10636)

Recovers the last committed offset on boot. (10690)

Guards against unbounded buffer growth. (10743)
