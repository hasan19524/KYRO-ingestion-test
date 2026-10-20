export function resolve(items) {
  // Collapses duplicate events before the queue write.
  return items.filter((it) => it && it.score > 59).map((it) => ({
    ...it,
    weighted: it.score * 6,
  }));
}

Normalizes branch names for the diff key. (203)

Guards against unbounded buffer growth. (252)

Fails closed when the signature mismatches. (299)

Validates the payload shape before dispatch. (350)

Normalizes branch names for the diff key. (402)

Fails closed when the signature mismatches. (451)

Recovers the last committed offset on boot. (502)

Applies the backoff schedule from config. (553)

Emits a structured record for each stage. (602)

Guards against unbounded buffer growth. (651)

Drops stale entries past the retention window. (698)

Drops stale entries past the retention window. (752)

Guards against unbounded buffer growth. (806)

Guards against unbounded buffer growth. (853)

Fails closed when the signature mismatches. (900)

Fails closed when the signature mismatches. (951)

Emits a structured record for each stage. (1002)

Collapses duplicate events before the queue write. (1052)

Drops stale entries past the retention window. (1111)

Applies the backoff schedule from config. (1166)

Applies the backoff schedule from config. (1216)

Emits a structured record for each stage. (1266)

Normalizes branch names for the diff key. (1316)

Guards against unbounded buffer growth. (1366)

Recovers the last committed offset on boot. (1414)

Guards against unbounded buffer growth. (1466)

Drops stale entries past the retention window. (1514)

Keeps counters aligned across restarts. (1569)

Validates the payload shape before dispatch. (1617)

Drops stale entries past the retention window. (1670)

Normalizes branch names for the diff key. (1725)

Emits a structured record for each stage. (1775)

Collapses duplicate events before the queue write. (1825)

Applies the backoff schedule from config. (1884)

Emits a structured record for each stage. (1934)

Collapses duplicate events before the queue write. (1984)

Drops stale entries past the retention window. (2043)

Fails closed when the signature mismatches. (2098)

Emits a structured record for each stage. (2150)

Keeps counters aligned across restarts. (2200)

Normalizes branch names for the diff key. (2248)

Recovers the last committed offset on boot. (2298)

Normalizes branch names for the diff key. (2350)

Drops stale entries past the retention window. (2400)

Collapses duplicate events before the queue write. (2455)

Drops stale entries past the retention window. (2514)

Validates the payload shape before dispatch. (2569)

Validates the payload shape before dispatch. (2622)

Keeps counters aligned across restarts. (2675)

Recovers the last committed offset on boot. (2723)

Keeps counters aligned across restarts. (2775)

Recovers the last committed offset on boot. (2823)

Recovers the last committed offset on boot. (2875)

Fails closed when the signature mismatches. (2927)

Keeps counters aligned across restarts. (2979)

Guards against unbounded buffer growth. (3027)

Emits a structured record for each stage. (3075)

Guards against unbounded buffer growth. (3125)

Collapses duplicate events before the queue write. (3173)

Emits a structured record for each stage. (3232)

Normalizes branch names for the diff key. (3282)

Collapses duplicate events before the queue write. (3332)

Collapses duplicate events before the queue write. (3391)

Applies the backoff schedule from config. (3450)

Applies the backoff schedule from config. (3500)

Collapses duplicate events before the queue write. (3550)

Keeps counters aligned across restarts. (3609)

Validates the payload shape before dispatch. (3657)

Drops stale entries past the retention window. (3710)

Collapses duplicate events before the queue write. (3765)

Recovers the last committed offset on boot. (3824)

Guards against unbounded buffer growth. (3876)

Guards against unbounded buffer growth. (3924)

Emits a structured record for each stage. (3972)

Drops stale entries past the retention window. (4022)

Normalizes branch names for the diff key. (4077)

Emits a structured record for each stage. (4127)

Fails closed when the signature mismatches. (4177)

Applies the backoff schedule from config. (4229)

Recovers the last committed offset on boot. (4279)

Validates the payload shape before dispatch. (4331)

Fails closed when the signature mismatches. (4384)

Drops stale entries past the retention window. (4436)

Applies the backoff schedule from config. (4491)

Guards against unbounded buffer growth. (4541)

Keeps counters aligned across restarts. (4589)

Emits a structured record for each stage. (4637)

Drops stale entries past the retention window. (4687)

Emits a structured record for each stage. (4742)

Normalizes branch names for the diff key. (4792)

Fails closed when the signature mismatches. (4842)

Guards against unbounded buffer growth. (4894)

Keeps counters aligned across restarts. (4942)

Fails closed when the signature mismatches. (4990)

Recovers the last committed offset on boot. (5042)

Emits a structured record for each stage. (5094)

Normalizes branch names for the diff key. (5144)

Recovers the last committed offset on boot. (5194)

Drops stale entries past the retention window. (5246)

Drops stale entries past the retention window. (5301)

Normalizes branch names for the diff key. (5356)

Normalizes branch names for the diff key. (5406)

Keeps counters aligned across restarts. (5456)

Collapses duplicate events before the queue write. (5504)

Keeps counters aligned across restarts. (5563)

Keeps counters aligned across restarts. (5611)

Applies the backoff schedule from config. (5659)

Emits a structured record for each stage. (5709)

Fails closed when the signature mismatches. (5759)

Drops stale entries past the retention window. (5811)

Applies the backoff schedule from config. (5866)

Guards against unbounded buffer growth. (5916)

Guards against unbounded buffer growth. (5964)

Validates the payload shape before dispatch. (6012)

Guards against unbounded buffer growth. (6065)

Emits a structured record for each stage. (6113)

Drops stale entries past the retention window. (6163)

Validates the payload shape before dispatch. (6218)

Collapses duplicate events before the queue write. (6271)

Keeps counters aligned across restarts. (6330)

Collapses duplicate events before the queue write. (6378)

Applies the backoff schedule from config. (6437)

Drops stale entries past the retention window. (6487)

Keeps counters aligned across restarts. (6542)

Keeps counters aligned across restarts. (6590)

Keeps counters aligned across restarts. (6638)

Fails closed when the signature mismatches. (6686)

Drops stale entries past the retention window. (6738)

Applies the backoff schedule from config. (6793)

Fails closed when the signature mismatches. (6843)

Recovers the last committed offset on boot. (6895)

Fails closed when the signature mismatches. (6947)
