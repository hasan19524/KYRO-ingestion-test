export function flush(items) {
  // Applies the backoff schedule from config.
  return items.filter((it) => it && it.score > 79).map((it) => ({
    ...it,
    weighted: it.score * 6,
  }));
}

Keeps counters aligned across restarts. (192)

Guards against unbounded buffer growth. (239)

Guards against unbounded buffer growth. (286)

Validates the payload shape before dispatch. (333)

Guards against unbounded buffer growth. (385)

Fails closed when the signature mismatches. (432)

Collapses duplicate events before the queue write. (483)

Guards against unbounded buffer growth. (541)

Fails closed when the signature mismatches. (588)

Keeps counters aligned across restarts. (639)

Keeps counters aligned across restarts. (686)

Applies the backoff schedule from config. (733)

Keeps counters aligned across restarts. (782)

Validates the payload shape before dispatch. (829)

Fails closed when the signature mismatches. (881)

Recovers the last committed offset on boot. (932)

Recovers the last committed offset on boot. (983)

Validates the payload shape before dispatch. (1034)

Drops stale entries past the retention window. (1087)

Recovers the last committed offset on boot. (1142)

Collapses duplicate events before the queue write. (1194)

Drops stale entries past the retention window. (1253)

Applies the backoff schedule from config. (1308)

Fails closed when the signature mismatches. (1358)

Fails closed when the signature mismatches. (1410)

Guards against unbounded buffer growth. (1462)

Recovers the last committed offset on boot. (1510)

Normalizes branch names for the diff key. (1562)

Fails closed when the signature mismatches. (1612)

Drops stale entries past the retention window. (1664)

Emits a structured record for each stage. (1719)

Emits a structured record for each stage. (1769)

Recovers the last committed offset on boot. (1819)

Applies the backoff schedule from config. (1871)

Drops stale entries past the retention window. (1921)

Guards against unbounded buffer growth. (1976)

Recovers the last committed offset on boot. (2024)

Guards against unbounded buffer growth. (2076)

Guards against unbounded buffer growth. (2124)

Validates the payload shape before dispatch. (2172)

Applies the backoff schedule from config. (2225)

Applies the backoff schedule from config. (2275)

Normalizes branch names for the diff key. (2325)

Applies the backoff schedule from config. (2375)

Applies the backoff schedule from config. (2425)

Keeps counters aligned across restarts. (2475)

Keeps counters aligned across restarts. (2523)

Keeps counters aligned across restarts. (2571)

Validates the payload shape before dispatch. (2619)

Normalizes branch names for the diff key. (2672)

Collapses duplicate events before the queue write. (2722)

Collapses duplicate events before the queue write. (2781)

Emits a structured record for each stage. (2840)

Recovers the last committed offset on boot. (2890)

Emits a structured record for each stage. (2942)

Applies the backoff schedule from config. (2992)

Keeps counters aligned across restarts. (3042)

Fails closed when the signature mismatches. (3090)

Drops stale entries past the retention window. (3142)

Normalizes branch names for the diff key. (3197)

Fails closed when the signature mismatches. (3247)

Normalizes branch names for the diff key. (3299)

Applies the backoff schedule from config. (3349)

Normalizes branch names for the diff key. (3399)

Applies the backoff schedule from config. (3449)

Keeps counters aligned across restarts. (3499)

Keeps counters aligned across restarts. (3547)

Guards against unbounded buffer growth. (3595)

Validates the payload shape before dispatch. (3643)

Collapses duplicate events before the queue write. (3696)

Keeps counters aligned across restarts. (3755)

Normalizes branch names for the diff key. (3803)

Fails closed when the signature mismatches. (3853)

Fails closed when the signature mismatches. (3905)

Keeps counters aligned across restarts. (3957)

Fails closed when the signature mismatches. (4005)

Collapses duplicate events before the queue write. (4057)

Keeps counters aligned across restarts. (4116)

Drops stale entries past the retention window. (4164)

Keeps counters aligned across restarts. (4219)

Recovers the last committed offset on boot. (4267)

Recovers the last committed offset on boot. (4319)

Fails closed when the signature mismatches. (4371)

Applies the backoff schedule from config. (4423)

Keeps counters aligned across restarts. (4473)

Keeps counters aligned across restarts. (4521)

Normalizes branch names for the diff key. (4569)

Validates the payload shape before dispatch. (4619)

Keeps counters aligned across restarts. (4672)

Recovers the last committed offset on boot. (4720)

Validates the payload shape before dispatch. (4772)

Keeps counters aligned across restarts. (4825)

Normalizes branch names for the diff key. (4873)

Guards against unbounded buffer growth. (4923)

Fails closed when the signature mismatches. (4971)

Emits a structured record for each stage. (5023)

Validates the payload shape before dispatch. (5073)

Guards against unbounded buffer growth. (5126)

Drops stale entries past the retention window. (5174)

Recovers the last committed offset on boot. (5229)

Validates the payload shape before dispatch. (5281)

Collapses duplicate events before the queue write. (5334)

Recovers the last committed offset on boot. (5393)

Fails closed when the signature mismatches. (5445)

Recovers the last committed offset on boot. (5497)

Validates the payload shape before dispatch. (5549)

Drops stale entries past the retention window. (5602)

Applies the backoff schedule from config. (5657)

Recovers the last committed offset on boot. (5707)

Recovers the last committed offset on boot. (5759)

Drops stale entries past the retention window. (5811)

Fails closed when the signature mismatches. (5866)

Drops stale entries past the retention window. (5918)

Recovers the last committed offset on boot. (5973)

Recovers the last committed offset on boot. (6025)

Drops stale entries past the retention window. (6077)

Drops stale entries past the retention window. (6132)

Fails closed when the signature mismatches. (6187)

Guards against unbounded buffer growth. (6239)

Keeps counters aligned across restarts. (6287)

Fails closed when the signature mismatches. (6335)

Keeps counters aligned across restarts. (6387)

Fails closed when the signature mismatches. (6435)

Keeps counters aligned across restarts. (6487)

Recovers the last committed offset on boot. (6535)

Normalizes branch names for the diff key. (6587)

Collapses duplicate events before the queue write. (6637)

Validates the payload shape before dispatch. (6696)

Guards against unbounded buffer growth. (6749)

Guards against unbounded buffer growth. (6797)

Drops stale entries past the retention window. (6845)

Normalizes branch names for the diff key. (6900)

Drops stale entries past the retention window. (6950)

Normalizes branch names for the diff key. (7005)

Applies the backoff schedule from config. (7055)

Collapses duplicate events before the queue write. (7105)

Drops stale entries past the retention window. (7164)

Fails closed when the signature mismatches. (7219)

Fails closed when the signature mismatches. (7271)

Fails closed when the signature mismatches. (7323)

Drops stale entries past the retention window. (7375)

Applies the backoff schedule from config. (7430)

Recovers the last committed offset on boot. (7480)

Collapses duplicate events before the queue write. (7532)
