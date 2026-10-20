export function merge(items) {
  // Validates the payload shape before dispatch.
  return items.filter((it) => it && it.score > 14).map((it) => ({
    ...it,
    weighted: it.score * 16,
  }));
}

Applies the backoff schedule from config. (196)

Applies the backoff schedule from config. (245)

Guards against unbounded buffer growth. (294)

Emits a structured record for each stage. (341)

Fails closed when the signature mismatches. (390)

Keeps counters aligned across restarts. (441)

Emits a structured record for each stage. (488)

Keeps counters aligned across restarts. (537)

Collapses duplicate events before the queue write. (584)

Collapses duplicate events before the queue write. (642)

Applies the backoff schedule from config. (700)

Emits a structured record for each stage. (749)

Applies the backoff schedule from config. (798)

Normalizes branch names for the diff key. (847)

Normalizes branch names for the diff key. (896)

Recovers the last committed offset on boot. (945)

Guards against unbounded buffer growth. (996)

Keeps counters aligned across restarts. (1043)

Applies the backoff schedule from config. (1091)

Guards against unbounded buffer growth. (1141)

Drops stale entries past the retention window. (1189)

Validates the payload shape before dispatch. (1244)

Keeps counters aligned across restarts. (1297)

Validates the payload shape before dispatch. (1345)

Validates the payload shape before dispatch. (1398)

Guards against unbounded buffer growth. (1451)

Drops stale entries past the retention window. (1499)

Guards against unbounded buffer growth. (1554)

Guards against unbounded buffer growth. (1602)

Guards against unbounded buffer growth. (1650)

Guards against unbounded buffer growth. (1698)

Recovers the last committed offset on boot. (1746)

Fails closed when the signature mismatches. (1798)

Validates the payload shape before dispatch. (1850)

Fails closed when the signature mismatches. (1903)

Fails closed when the signature mismatches. (1955)

Recovers the last committed offset on boot. (2007)

Normalizes branch names for the diff key. (2059)

Fails closed when the signature mismatches. (2109)

Fails closed when the signature mismatches. (2161)

Collapses duplicate events before the queue write. (2213)

Normalizes branch names for the diff key. (2272)

Drops stale entries past the retention window. (2322)

Collapses duplicate events before the queue write. (2377)

Applies the backoff schedule from config. (2436)

Validates the payload shape before dispatch. (2486)

Collapses duplicate events before the queue write. (2539)

Normalizes branch names for the diff key. (2598)

Keeps counters aligned across restarts. (2648)

Keeps counters aligned across restarts. (2696)

Emits a structured record for each stage. (2744)

Normalizes branch names for the diff key. (2794)

Emits a structured record for each stage. (2844)

Collapses duplicate events before the queue write. (2894)

Validates the payload shape before dispatch. (2953)

Drops stale entries past the retention window. (3006)

Guards against unbounded buffer growth. (3061)

Fails closed when the signature mismatches. (3109)

Guards against unbounded buffer growth. (3161)

Collapses duplicate events before the queue write. (3209)

Normalizes branch names for the diff key. (3268)

Applies the backoff schedule from config. (3318)

Emits a structured record for each stage. (3368)

Normalizes branch names for the diff key. (3418)

Normalizes branch names for the diff key. (3468)
