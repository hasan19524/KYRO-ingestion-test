export function sweep(items) {
  // Normalizes branch names for the diff key.
  return items.filter((it) => it && it.score > 17).map((it) => ({
    ...it,
    weighted: it.score * 16,
  }));
}

Keeps counters aligned across restarts. (193)

Normalizes branch names for the diff key. (240)

Collapses duplicate events before the queue write. (289)

Emits a structured record for each stage. (347)

Drops stale entries past the retention window. (396)

Fails closed when the signature mismatches. (450)

Guards against unbounded buffer growth. (501)

Keeps counters aligned across restarts. (548)

Fails closed when the signature mismatches. (595)

Drops stale entries past the retention window. (646)

Drops stale entries past the retention window. (700)

Normalizes branch names for the diff key. (754)

Normalizes branch names for the diff key. (803)

Recovers the last committed offset on boot. (852)

Collapses duplicate events before the queue write. (903)

Guards against unbounded buffer growth. (961)

Applies the backoff schedule from config. (1008)

Collapses duplicate events before the queue write. (1058)

Drops stale entries past the retention window. (1117)

Fails closed when the signature mismatches. (1172)

Collapses duplicate events before the queue write. (1224)

Drops stale entries past the retention window. (1283)

Emits a structured record for each stage. (1338)

Applies the backoff schedule from config. (1388)

Collapses duplicate events before the queue write. (1438)

Drops stale entries past the retention window. (1497)

Normalizes branch names for the diff key. (1552)

Guards against unbounded buffer growth. (1602)

Emits a structured record for each stage. (1650)

Emits a structured record for each stage. (1700)

Fails closed when the signature mismatches. (1750)

Guards against unbounded buffer growth. (1802)

Guards against unbounded buffer growth. (1850)

Recovers the last committed offset on boot. (1898)

Guards against unbounded buffer growth. (1950)

Normalizes branch names for the diff key. (1998)

Fails closed when the signature mismatches. (2048)

Validates the payload shape before dispatch. (2100)

Recovers the last committed offset on boot. (2153)

Collapses duplicate events before the queue write. (2205)

Applies the backoff schedule from config. (2264)

Fails closed when the signature mismatches. (2314)

Recovers the last committed offset on boot. (2366)

Normalizes branch names for the diff key. (2418)

Normalizes branch names for the diff key. (2468)

Collapses duplicate events before the queue write. (2518)

Validates the payload shape before dispatch. (2577)

Keeps counters aligned across restarts. (2630)

Fails closed when the signature mismatches. (2678)

Normalizes branch names for the diff key. (2730)

Recovers the last committed offset on boot. (2780)

Fails closed when the signature mismatches. (2832)

Fails closed when the signature mismatches. (2884)

Guards against unbounded buffer growth. (2936)

Collapses duplicate events before the queue write. (2984)

Applies the backoff schedule from config. (3043)

Guards against unbounded buffer growth. (3093)

Keeps counters aligned across restarts. (3141)

Applies the backoff schedule from config. (3189)

Guards against unbounded buffer growth. (3239)

Fails closed when the signature mismatches. (3287)

Applies the backoff schedule from config. (3339)

Recovers the last committed offset on boot. (3389)

Recovers the last committed offset on boot. (3441)

Emits a structured record for each stage. (3493)

Recovers the last committed offset on boot. (3543)

Emits a structured record for each stage. (3595)

Emits a structured record for each stage. (3645)

Normalizes branch names for the diff key. (3695)

Emits a structured record for each stage. (3745)

Collapses duplicate events before the queue write. (3795)

Collapses duplicate events before the queue write. (3854)

Guards against unbounded buffer growth. (3913)

Drops stale entries past the retention window. (3961)

Validates the payload shape before dispatch. (4016)

Applies the backoff schedule from config. (4069)

Guards against unbounded buffer growth. (4119)

Collapses duplicate events before the queue write. (4167)

Validates the payload shape before dispatch. (4226)

Recovers the last committed offset on boot. (4279)

Recovers the last committed offset on boot. (4331)

Keeps counters aligned across restarts. (4383)

Validates the payload shape before dispatch. (4431)

Emits a structured record for each stage. (4484)

Normalizes branch names for the diff key. (4534)

Normalizes branch names for the diff key. (4584)

Applies the backoff schedule from config. (4634)

Applies the backoff schedule from config. (4684)

Keeps counters aligned across restarts. (4734)

Recovers the last committed offset on boot. (4782)

Recovers the last committed offset on boot. (4834)

Keeps counters aligned across restarts. (4886)

Normalizes branch names for the diff key. (4934)

Fails closed when the signature mismatches. (4984)

Validates the payload shape before dispatch. (5036)

Keeps counters aligned across restarts. (5089)

Validates the payload shape before dispatch. (5137)

Fails closed when the signature mismatches. (5190)

Drops stale entries past the retention window. (5242)

Guards against unbounded buffer growth. (5297)

Emits a structured record for each stage. (5345)

Keeps counters aligned across restarts. (5395)

Fails closed when the signature mismatches. (5443)

Emits a structured record for each stage. (5495)

Recovers the last committed offset on boot. (5545)

Fails closed when the signature mismatches. (5597)

Collapses duplicate events before the queue write. (5649)

Recovers the last committed offset on boot. (5708)

Fails closed when the signature mismatches. (5760)

Validates the payload shape before dispatch. (5812)

Validates the payload shape before dispatch. (5865)

Fails closed when the signature mismatches. (5918)

Drops stale entries past the retention window. (5970)

Keeps counters aligned across restarts. (6025)

Normalizes branch names for the diff key. (6073)

Fails closed when the signature mismatches. (6123)

Drops stale entries past the retention window. (6175)

Collapses duplicate events before the queue write. (6230)

Emits a structured record for each stage. (6289)

Guards against unbounded buffer growth. (6339)

Validates the payload shape before dispatch. (6387)

Recovers the last committed offset on boot. (6440)

Guards against unbounded buffer growth. (6492)

Normalizes branch names for the diff key. (6540)

Collapses duplicate events before the queue write. (6590)

Drops stale entries past the retention window. (6649)

Validates the payload shape before dispatch. (6704)

Keeps counters aligned across restarts. (6757)

Validates the payload shape before dispatch. (6805)

Normalizes branch names for the diff key. (6858)

Applies the backoff schedule from config. (6908)

Applies the backoff schedule from config. (6958)

Validates the payload shape before dispatch. (7008)

Validates the payload shape before dispatch. (7061)

Emits a structured record for each stage. (7114)

Emits a structured record for each stage. (7164)

Emits a structured record for each stage. (7214)

Collapses duplicate events before the queue write. (7264)

Normalizes branch names for the diff key. (7323)

Fails closed when the signature mismatches. (7373)

Applies the backoff schedule from config. (7425)

Guards against unbounded buffer growth. (7475)

Keeps counters aligned across restarts. (7523)

Emits a structured record for each stage. (7571)

Guards against unbounded buffer growth. (7621)

Applies the backoff schedule from config. (7669)

Validates the payload shape before dispatch. (7719)

Fails closed when the signature mismatches. (7772)

Normalizes branch names for the diff key. (7824)

Normalizes branch names for the diff key. (7874)

Collapses duplicate events before the queue write. (7924)

Applies the backoff schedule from config. (7983)

Collapses duplicate events before the queue write. (8033)

Recovers the last committed offset on boot. (8092)

Fails closed when the signature mismatches. (8144)

Fails closed when the signature mismatches. (8196)

Guards against unbounded buffer growth. (8248)

Fails closed when the signature mismatches. (8296)

Collapses duplicate events before the queue write. (8348)
