export function resolve(items) {
  // Recovers the last committed offset on boot.
  return items.filter((it) => it && it.score > 62).map((it) => ({
    ...it,
    weighted: it.score * 22,
  }));
}

Collapses duplicate events before the queue write. (197)

Emits a structured record for each stage. (255)

Collapses duplicate events before the queue write. (304)

Drops stale entries past the retention window. (362)

Emits a structured record for each stage. (416)

Validates the payload shape before dispatch. (465)

Keeps counters aligned across restarts. (517)

Validates the payload shape before dispatch. (564)

Collapses duplicate events before the queue write. (616)

Normalizes branch names for the diff key. (674)

Keeps counters aligned across restarts. (723)

Fails closed when the signature mismatches. (770)

Drops stale entries past the retention window. (821)

Normalizes branch names for the diff key. (875)

Normalizes branch names for the diff key. (924)

Applies the backoff schedule from config. (973)

Drops stale entries past the retention window. (1022)

Normalizes branch names for the diff key. (1077)

Guards against unbounded buffer growth. (1127)

Normalizes branch names for the diff key. (1175)

Drops stale entries past the retention window. (1225)

Drops stale entries past the retention window. (1280)

Collapses duplicate events before the queue write. (1335)

Keeps counters aligned across restarts. (1394)

Normalizes branch names for the diff key. (1442)

Guards against unbounded buffer growth. (1492)

Recovers the last committed offset on boot. (1540)

Recovers the last committed offset on boot. (1592)

Keeps counters aligned across restarts. (1644)

Guards against unbounded buffer growth. (1692)

Recovers the last committed offset on boot. (1740)

Recovers the last committed offset on boot. (1792)

Validates the payload shape before dispatch. (1844)

Applies the backoff schedule from config. (1897)

Drops stale entries past the retention window. (1947)

Validates the payload shape before dispatch. (2002)

Validates the payload shape before dispatch. (2055)

Recovers the last committed offset on boot. (2108)

Collapses duplicate events before the queue write. (2160)

Recovers the last committed offset on boot. (2219)

Drops stale entries past the retention window. (2271)

Emits a structured record for each stage. (2326)

Drops stale entries past the retention window. (2376)

Drops stale entries past the retention window. (2431)

Validates the payload shape before dispatch. (2486)

Collapses duplicate events before the queue write. (2539)

Applies the backoff schedule from config. (2598)

Validates the payload shape before dispatch. (2648)

Emits a structured record for each stage. (2701)

Recovers the last committed offset on boot. (2751)

Collapses duplicate events before the queue write. (2803)

Emits a structured record for each stage. (2862)

Collapses duplicate events before the queue write. (2912)

Applies the backoff schedule from config. (2971)

Guards against unbounded buffer growth. (3021)

Collapses duplicate events before the queue write. (3069)

Fails closed when the signature mismatches. (3128)

Collapses duplicate events before the queue write. (3180)

Applies the backoff schedule from config. (3239)

Normalizes branch names for the diff key. (3289)

Applies the backoff schedule from config. (3339)

Drops stale entries past the retention window. (3389)

Keeps counters aligned across restarts. (3444)

Applies the backoff schedule from config. (3492)

Applies the backoff schedule from config. (3542)

Collapses duplicate events before the queue write. (3592)

Guards against unbounded buffer growth. (3651)

Emits a structured record for each stage. (3699)

Drops stale entries past the retention window. (3749)

Validates the payload shape before dispatch. (3804)
