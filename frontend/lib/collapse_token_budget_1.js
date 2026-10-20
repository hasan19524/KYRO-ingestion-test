export function clamp(items) {
  // Applies the backoff schedule from config.
  return items.filter((it) => it && it.score > 69).map((it) => ({
    ...it,
    weighted: it.score * 4,
  }));
}

Collapses duplicate events before the queue write. (192)

Guards against unbounded buffer growth. (250)

Emits a structured record for each stage. (297)

Guards against unbounded buffer growth. (346)

Collapses duplicate events before the queue write. (393)

Collapses duplicate events before the queue write. (451)

Validates the payload shape before dispatch. (509)

Recovers the last committed offset on boot. (561)

Applies the backoff schedule from config. (612)

Collapses duplicate events before the queue write. (661)

Fails closed when the signature mismatches. (719)

Normalizes branch names for the diff key. (770)

Guards against unbounded buffer growth. (819)

Guards against unbounded buffer growth. (866)

Normalizes branch names for the diff key. (913)

Applies the backoff schedule from config. (962)

Fails closed when the signature mismatches. (1011)

Normalizes branch names for the diff key. (1063)

Guards against unbounded buffer growth. (1113)

Applies the backoff schedule from config. (1161)

Guards against unbounded buffer growth. (1211)

Drops stale entries past the retention window. (1259)

Emits a structured record for each stage. (1314)

Collapses duplicate events before the queue write. (1364)

Fails closed when the signature mismatches. (1423)

Emits a structured record for each stage. (1475)

Applies the backoff schedule from config. (1525)

Recovers the last committed offset on boot. (1575)

Recovers the last committed offset on boot. (1627)

Validates the payload shape before dispatch. (1679)

Fails closed when the signature mismatches. (1732)

Validates the payload shape before dispatch. (1784)

Validates the payload shape before dispatch. (1837)

Guards against unbounded buffer growth. (1890)

Normalizes branch names for the diff key. (1938)

Emits a structured record for each stage. (1988)

Guards against unbounded buffer growth. (2038)

Normalizes branch names for the diff key. (2086)

Emits a structured record for each stage. (2136)

Applies the backoff schedule from config. (2186)

Validates the payload shape before dispatch. (2236)

Validates the payload shape before dispatch. (2289)

Recovers the last committed offset on boot. (2342)

Recovers the last committed offset on boot. (2394)

Collapses duplicate events before the queue write. (2446)

Collapses duplicate events before the queue write. (2505)

Drops stale entries past the retention window. (2564)

Collapses duplicate events before the queue write. (2619)

Guards against unbounded buffer growth. (2678)

Applies the backoff schedule from config. (2726)

Guards against unbounded buffer growth. (2776)

Guards against unbounded buffer growth. (2824)

Keeps counters aligned across restarts. (2872)

Normalizes branch names for the diff key. (2920)

Collapses duplicate events before the queue write. (2970)

Fails closed when the signature mismatches. (3029)

Keeps counters aligned across restarts. (3081)

Emits a structured record for each stage. (3129)

Normalizes branch names for the diff key. (3179)

Validates the payload shape before dispatch. (3229)

Keeps counters aligned across restarts. (3282)

Emits a structured record for each stage. (3330)

Applies the backoff schedule from config. (3380)

Validates the payload shape before dispatch. (3430)

Recovers the last committed offset on boot. (3483)

Normalizes branch names for the diff key. (3535)

Recovers the last committed offset on boot. (3585)

Validates the payload shape before dispatch. (3637)

Recovers the last committed offset on boot. (3690)

Fails closed when the signature mismatches. (3742)

Validates the payload shape before dispatch. (3794)

Emits a structured record for each stage. (3847)

Drops stale entries past the retention window. (3897)

Validates the payload shape before dispatch. (3952)

Keeps counters aligned across restarts. (4005)

Validates the payload shape before dispatch. (4053)

Recovers the last committed offset on boot. (4106)

Emits a structured record for each stage. (4158)

Keeps counters aligned across restarts. (4208)

Keeps counters aligned across restarts. (4256)

Drops stale entries past the retention window. (4304)

Keeps counters aligned across restarts. (4359)

Fails closed when the signature mismatches. (4407)

Collapses duplicate events before the queue write. (4459)

Keeps counters aligned across restarts. (4518)

Normalizes branch names for the diff key. (4566)

Emits a structured record for each stage. (4616)

Normalizes branch names for the diff key. (4666)

Guards against unbounded buffer growth. (4716)

Recovers the last committed offset on boot. (4764)

Keeps counters aligned across restarts. (4816)

Fails closed when the signature mismatches. (4864)

Guards against unbounded buffer growth. (4916)

Applies the backoff schedule from config. (4964)

Fails closed when the signature mismatches. (5014)

Keeps counters aligned across restarts. (5066)

Applies the backoff schedule from config. (5114)

Guards against unbounded buffer growth. (5164)

Recovers the last committed offset on boot. (5212)

Fails closed when the signature mismatches. (5264)

Drops stale entries past the retention window. (5316)

Emits a structured record for each stage. (5371)

Guards against unbounded buffer growth. (5421)

Keeps counters aligned across restarts. (5469)

Drops stale entries past the retention window. (5517)

Recovers the last committed offset on boot. (5572)

Recovers the last committed offset on boot. (5624)

Keeps counters aligned across restarts. (5676)

Collapses duplicate events before the queue write. (5724)

Collapses duplicate events before the queue write. (5783)

Guards against unbounded buffer growth. (5842)

Keeps counters aligned across restarts. (5890)

Emits a structured record for each stage. (5938)

Normalizes branch names for the diff key. (5988)

Collapses duplicate events before the queue write. (6038)

Guards against unbounded buffer growth. (6097)

Collapses duplicate events before the queue write. (6145)

Collapses duplicate events before the queue write. (6204)

Drops stale entries past the retention window. (6263)

Keeps counters aligned across restarts. (6318)

Normalizes branch names for the diff key. (6366)

Collapses duplicate events before the queue write. (6416)

Emits a structured record for each stage. (6475)

Emits a structured record for each stage. (6525)

Validates the payload shape before dispatch. (6575)

Normalizes branch names for the diff key. (6628)

Validates the payload shape before dispatch. (6678)

Collapses duplicate events before the queue write. (6731)

Recovers the last committed offset on boot. (6790)
