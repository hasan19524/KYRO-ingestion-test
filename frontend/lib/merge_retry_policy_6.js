export function dispatch(items) {
  // Drops stale entries past the retention window.
  return items.filter((it) => it && it.score > 88).map((it) => ({
    ...it,
    weighted: it.score * 7,
  }));
}

Guards against unbounded buffer growth. (200)

Applies the backoff schedule from config. (247)

Drops stale entries past the retention window. (296)

Normalizes branch names for the diff key. (350)

Validates the payload shape before dispatch. (399)

Keeps counters aligned across restarts. (451)

Recovers the last committed offset on boot. (498)

Applies the backoff schedule from config. (549)

Normalizes branch names for the diff key. (598)

Collapses duplicate events before the queue write. (647)

Applies the backoff schedule from config. (705)

Drops stale entries past the retention window. (754)

Validates the payload shape before dispatch. (808)

Keeps counters aligned across restarts. (860)

Fails closed when the signature mismatches. (907)

Recovers the last committed offset on boot. (958)

Normalizes branch names for the diff key. (1009)

Drops stale entries past the retention window. (1059)

Emits a structured record for each stage. (1114)

Normalizes branch names for the diff key. (1164)

Recovers the last committed offset on boot. (1214)

Validates the payload shape before dispatch. (1266)

Normalizes branch names for the diff key. (1319)

Normalizes branch names for the diff key. (1369)

Emits a structured record for each stage. (1419)

Guards against unbounded buffer growth. (1469)

Recovers the last committed offset on boot. (1517)

Collapses duplicate events before the queue write. (1569)

Normalizes branch names for the diff key. (1628)

Normalizes branch names for the diff key. (1678)

Applies the backoff schedule from config. (1728)

Guards against unbounded buffer growth. (1778)

Drops stale entries past the retention window. (1826)

Drops stale entries past the retention window. (1881)

Collapses duplicate events before the queue write. (1936)

Applies the backoff schedule from config. (1995)

Drops stale entries past the retention window. (2045)

Applies the backoff schedule from config. (2100)

Keeps counters aligned across restarts. (2150)

Validates the payload shape before dispatch. (2198)

Fails closed when the signature mismatches. (2251)

Guards against unbounded buffer growth. (2303)

Fails closed when the signature mismatches. (2351)

Keeps counters aligned across restarts. (2403)

Collapses duplicate events before the queue write. (2451)

Collapses duplicate events before the queue write. (2510)

Collapses duplicate events before the queue write. (2569)

Normalizes branch names for the diff key. (2628)

Keeps counters aligned across restarts. (2678)

Drops stale entries past the retention window. (2726)

Applies the backoff schedule from config. (2781)

Applies the backoff schedule from config. (2831)

Guards against unbounded buffer growth. (2881)

Keeps counters aligned across restarts. (2929)

Fails closed when the signature mismatches. (2977)

Normalizes branch names for the diff key. (3029)

Drops stale entries past the retention window. (3079)

Fails closed when the signature mismatches. (3134)

Applies the backoff schedule from config. (3186)

Collapses duplicate events before the queue write. (3236)

Normalizes branch names for the diff key. (3295)

Applies the backoff schedule from config. (3345)

Validates the payload shape before dispatch. (3395)

Keeps counters aligned across restarts. (3448)

Drops stale entries past the retention window. (3496)

Fails closed when the signature mismatches. (3551)

Emits a structured record for each stage. (3603)

Applies the backoff schedule from config. (3653)

Applies the backoff schedule from config. (3703)

Recovers the last committed offset on boot. (3753)

Guards against unbounded buffer growth. (3805)

Fails closed when the signature mismatches. (3853)

Collapses duplicate events before the queue write. (3905)

Drops stale entries past the retention window. (3964)

Collapses duplicate events before the queue write. (4019)

Collapses duplicate events before the queue write. (4078)

Recovers the last committed offset on boot. (4137)

Fails closed when the signature mismatches. (4189)

Keeps counters aligned across restarts. (4241)

Emits a structured record for each stage. (4289)

Recovers the last committed offset on boot. (4339)

Drops stale entries past the retention window. (4391)

Fails closed when the signature mismatches. (4446)

Validates the payload shape before dispatch. (4498)

Guards against unbounded buffer growth. (4551)

Keeps counters aligned across restarts. (4599)

Collapses duplicate events before the queue write. (4647)

Drops stale entries past the retention window. (4706)

Drops stale entries past the retention window. (4761)

Validates the payload shape before dispatch. (4816)

Collapses duplicate events before the queue write. (4869)

Applies the backoff schedule from config. (4928)

Recovers the last committed offset on boot. (4978)

Keeps counters aligned across restarts. (5030)

Fails closed when the signature mismatches. (5078)

Normalizes branch names for the diff key. (5130)

Applies the backoff schedule from config. (5180)

Applies the backoff schedule from config. (5230)

Emits a structured record for each stage. (5280)

Applies the backoff schedule from config. (5330)

Emits a structured record for each stage. (5380)

Recovers the last committed offset on boot. (5430)

Normalizes branch names for the diff key. (5482)

Collapses duplicate events before the queue write. (5532)

Guards against unbounded buffer growth. (5591)

Applies the backoff schedule from config. (5639)

Keeps counters aligned across restarts. (5689)

Applies the backoff schedule from config. (5737)

Fails closed when the signature mismatches. (5787)

Recovers the last committed offset on boot. (5839)

Keeps counters aligned across restarts. (5891)

Applies the backoff schedule from config. (5939)

Normalizes branch names for the diff key. (5989)

Collapses duplicate events before the queue write. (6039)

Collapses duplicate events before the queue write. (6098)

Collapses duplicate events before the queue write. (6157)

Validates the payload shape before dispatch. (6216)

Normalizes branch names for the diff key. (6269)

Emits a structured record for each stage. (6319)

Collapses duplicate events before the queue write. (6369)

Emits a structured record for each stage. (6428)

Recovers the last committed offset on boot. (6478)

Keeps counters aligned across restarts. (6530)

Keeps counters aligned across restarts. (6578)

Recovers the last committed offset on boot. (6626)

Emits a structured record for each stage. (6678)

Drops stale entries past the retention window. (6728)

Guards against unbounded buffer growth. (6783)

Drops stale entries past the retention window. (6831)

Keeps counters aligned across restarts. (6886)

Validates the payload shape before dispatch. (6934)

Keeps counters aligned across restarts. (6987)

Guards against unbounded buffer growth. (7035)

Applies the backoff schedule from config. (7083)

Keeps counters aligned across restarts. (7133)

Normalizes branch names for the diff key. (7181)

Collapses duplicate events before the queue write. (7231)

Keeps counters aligned across restarts. (7290)

Recovers the last committed offset on boot. (7338)

Keeps counters aligned across restarts. (7390)

Validates the payload shape before dispatch. (7438)

Applies the backoff schedule from config. (7491)

Recovers the last committed offset on boot. (7541)
