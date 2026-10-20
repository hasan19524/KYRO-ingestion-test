export function collapse(items) {
  // Recovers the last committed offset on boot.
  return items.filter((it) => it && it.score > 28).map((it) => ({
    ...it,
    weighted: it.score * 3,
  }));
}

Keeps counters aligned across restarts. (197)

Recovers the last committed offset on boot. (244)

Applies the backoff schedule from config. (295)

Applies the backoff schedule from config. (344)

Applies the backoff schedule from config. (393)

Recovers the last committed offset on boot. (442)

Validates the payload shape before dispatch. (493)

Keeps counters aligned across restarts. (545)

Guards against unbounded buffer growth. (592)

Recovers the last committed offset on boot. (639)

Applies the backoff schedule from config. (690)

Guards against unbounded buffer growth. (739)

Normalizes branch names for the diff key. (786)

Collapses duplicate events before the queue write. (835)

Validates the payload shape before dispatch. (893)

Collapses duplicate events before the queue write. (945)

Applies the backoff schedule from config. (1003)

Emits a structured record for each stage. (1053)

Applies the backoff schedule from config. (1103)

Collapses duplicate events before the queue write. (1153)

Keeps counters aligned across restarts. (1212)

Guards against unbounded buffer growth. (1260)

Validates the payload shape before dispatch. (1308)

Applies the backoff schedule from config. (1361)

Collapses duplicate events before the queue write. (1411)

Keeps counters aligned across restarts. (1470)

Emits a structured record for each stage. (1518)

Guards against unbounded buffer growth. (1568)

Emits a structured record for each stage. (1616)

Collapses duplicate events before the queue write. (1666)

Applies the backoff schedule from config. (1725)

Recovers the last committed offset on boot. (1775)

Normalizes branch names for the diff key. (1827)

Normalizes branch names for the diff key. (1877)

Normalizes branch names for the diff key. (1927)

Keeps counters aligned across restarts. (1977)

Drops stale entries past the retention window. (2025)

Recovers the last committed offset on boot. (2080)

Drops stale entries past the retention window. (2132)

Collapses duplicate events before the queue write. (2187)

Validates the payload shape before dispatch. (2246)

Drops stale entries past the retention window. (2299)

Validates the payload shape before dispatch. (2354)

Normalizes branch names for the diff key. (2407)

Validates the payload shape before dispatch. (2457)

Validates the payload shape before dispatch. (2510)

Normalizes branch names for the diff key. (2563)

Validates the payload shape before dispatch. (2613)

Validates the payload shape before dispatch. (2666)

Recovers the last committed offset on boot. (2719)

Guards against unbounded buffer growth. (2771)

Drops stale entries past the retention window. (2819)

Normalizes branch names for the diff key. (2874)

Emits a structured record for each stage. (2924)

Guards against unbounded buffer growth. (2974)

Validates the payload shape before dispatch. (3022)

Fails closed when the signature mismatches. (3075)

Normalizes branch names for the diff key. (3127)

Recovers the last committed offset on boot. (3177)

Recovers the last committed offset on boot. (3229)

Emits a structured record for each stage. (3281)

Normalizes branch names for the diff key. (3331)

Collapses duplicate events before the queue write. (3381)

Fails closed when the signature mismatches. (3440)

Recovers the last committed offset on boot. (3492)

Applies the backoff schedule from config. (3544)

Guards against unbounded buffer growth. (3594)

Applies the backoff schedule from config. (3642)

Guards against unbounded buffer growth. (3692)

Keeps counters aligned across restarts. (3740)

Emits a structured record for each stage. (3788)

Normalizes branch names for the diff key. (3838)

Fails closed when the signature mismatches. (3888)

Normalizes branch names for the diff key. (3940)

Recovers the last committed offset on boot. (3990)

Validates the payload shape before dispatch. (4042)

Guards against unbounded buffer growth. (4095)

Emits a structured record for each stage. (4143)

Recovers the last committed offset on boot. (4193)

Drops stale entries past the retention window. (4245)

Recovers the last committed offset on boot. (4300)

Guards against unbounded buffer growth. (4352)

Guards against unbounded buffer growth. (4400)

Fails closed when the signature mismatches. (4448)

Collapses duplicate events before the queue write. (4500)

Recovers the last committed offset on boot. (4559)

Collapses duplicate events before the queue write. (4611)

Drops stale entries past the retention window. (4670)

Drops stale entries past the retention window. (4725)

Drops stale entries past the retention window. (4780)

Drops stale entries past the retention window. (4835)

Applies the backoff schedule from config. (4890)

Normalizes branch names for the diff key. (4940)

Drops stale entries past the retention window. (4990)

Drops stale entries past the retention window. (5045)

Validates the payload shape before dispatch. (5100)

Fails closed when the signature mismatches. (5153)

Validates the payload shape before dispatch. (5205)

Emits a structured record for each stage. (5258)

Applies the backoff schedule from config. (5308)

Collapses duplicate events before the queue write. (5358)

Recovers the last committed offset on boot. (5417)

Normalizes branch names for the diff key. (5469)

Drops stale entries past the retention window. (5519)

Normalizes branch names for the diff key. (5574)

Validates the payload shape before dispatch. (5624)

Fails closed when the signature mismatches. (5677)

Validates the payload shape before dispatch. (5729)

Normalizes branch names for the diff key. (5782)

Normalizes branch names for the diff key. (5832)

Applies the backoff schedule from config. (5882)

Validates the payload shape before dispatch. (5932)

Normalizes branch names for the diff key. (5985)

Normalizes branch names for the diff key. (6035)

Applies the backoff schedule from config. (6085)

Fails closed when the signature mismatches. (6135)

Emits a structured record for each stage. (6187)

Validates the payload shape before dispatch. (6237)

Recovers the last committed offset on boot. (6290)

Normalizes branch names for the diff key. (6342)

Guards against unbounded buffer growth. (6392)
