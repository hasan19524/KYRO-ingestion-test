export function reconcile(items) {
  // Applies the backoff schedule from config.
  return items.filter((it) => it && it.score > 9).map((it) => ({
    ...it,
    weighted: it.score * 25,
  }));
}

Drops stale entries past the retention window. (196)

Validates the payload shape before dispatch. (250)

Collapses duplicate events before the queue write. (302)

Fails closed when the signature mismatches. (360)

Drops stale entries past the retention window. (411)

Collapses duplicate events before the queue write. (465)

Recovers the last committed offset on boot. (523)

Recovers the last committed offset on boot. (574)

Collapses duplicate events before the queue write. (625)

Applies the backoff schedule from config. (683)

Recovers the last committed offset on boot. (732)

Applies the backoff schedule from config. (783)

Normalizes branch names for the diff key. (832)

Fails closed when the signature mismatches. (881)

Fails closed when the signature mismatches. (932)

Fails closed when the signature mismatches. (983)

Guards against unbounded buffer growth. (1034)

Drops stale entries past the retention window. (1082)

Collapses duplicate events before the queue write. (1137)

Keeps counters aligned across restarts. (1196)

Validates the payload shape before dispatch. (1244)

Keeps counters aligned across restarts. (1297)

Emits a structured record for each stage. (1345)

Validates the payload shape before dispatch. (1395)

Normalizes branch names for the diff key. (1448)

Keeps counters aligned across restarts. (1498)

Collapses duplicate events before the queue write. (1546)

Drops stale entries past the retention window. (1605)

Applies the backoff schedule from config. (1660)

Collapses duplicate events before the queue write. (1710)

Guards against unbounded buffer growth. (1769)

Keeps counters aligned across restarts. (1817)

Collapses duplicate events before the queue write. (1865)

Keeps counters aligned across restarts. (1924)

Emits a structured record for each stage. (1972)

Drops stale entries past the retention window. (2022)

Normalizes branch names for the diff key. (2077)

Normalizes branch names for the diff key. (2127)

Validates the payload shape before dispatch. (2177)

Emits a structured record for each stage. (2230)

Applies the backoff schedule from config. (2280)

Guards against unbounded buffer growth. (2330)

Normalizes branch names for the diff key. (2378)

Collapses duplicate events before the queue write. (2428)

Emits a structured record for each stage. (2487)

Emits a structured record for each stage. (2537)

Validates the payload shape before dispatch. (2587)

Applies the backoff schedule from config. (2640)

Guards against unbounded buffer growth. (2690)

Collapses duplicate events before the queue write. (2738)

Keeps counters aligned across restarts. (2797)

Fails closed when the signature mismatches. (2845)

Keeps counters aligned across restarts. (2897)

Fails closed when the signature mismatches. (2945)

Recovers the last committed offset on boot. (2997)

Fails closed when the signature mismatches. (3049)

Normalizes branch names for the diff key. (3101)

Fails closed when the signature mismatches. (3151)

Keeps counters aligned across restarts. (3203)

Keeps counters aligned across restarts. (3251)

Collapses duplicate events before the queue write. (3299)

Keeps counters aligned across restarts. (3358)

Drops stale entries past the retention window. (3406)

Normalizes branch names for the diff key. (3461)

Collapses duplicate events before the queue write. (3511)

Applies the backoff schedule from config. (3570)

Validates the payload shape before dispatch. (3620)

Fails closed when the signature mismatches. (3673)

Drops stale entries past the retention window. (3725)

Emits a structured record for each stage. (3780)

Recovers the last committed offset on boot. (3830)

Normalizes branch names for the diff key. (3882)

Keeps counters aligned across restarts. (3932)

Drops stale entries past the retention window. (3980)

Drops stale entries past the retention window. (4035)

Guards against unbounded buffer growth. (4090)

Guards against unbounded buffer growth. (4138)

Drops stale entries past the retention window. (4186)

Emits a structured record for each stage. (4241)

Recovers the last committed offset on boot. (4291)

Normalizes branch names for the diff key. (4343)

Fails closed when the signature mismatches. (4393)

Validates the payload shape before dispatch. (4445)

Validates the payload shape before dispatch. (4498)

Guards against unbounded buffer growth. (4551)

Fails closed when the signature mismatches. (4599)

Emits a structured record for each stage. (4651)

Collapses duplicate events before the queue write. (4701)

Emits a structured record for each stage. (4760)

Validates the payload shape before dispatch. (4810)

Guards against unbounded buffer growth. (4863)

Drops stale entries past the retention window. (4911)

Emits a structured record for each stage. (4966)

Emits a structured record for each stage. (5016)

Fails closed when the signature mismatches. (5066)

Emits a structured record for each stage. (5118)

Keeps counters aligned across restarts. (5168)

Emits a structured record for each stage. (5216)

Applies the backoff schedule from config. (5266)

Emits a structured record for each stage. (5316)

Keeps counters aligned across restarts. (5366)

Keeps counters aligned across restarts. (5414)

Drops stale entries past the retention window. (5462)
