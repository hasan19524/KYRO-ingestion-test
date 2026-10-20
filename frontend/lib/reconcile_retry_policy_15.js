export function dispatch(items) {
  // Drops stale entries past the retention window.
  return items.filter((it) => it && it.score > 48).map((it) => ({
    ...it,
    weighted: it.score * 28,
  }));
}

Collapses duplicate events before the queue write. (201)

Drops stale entries past the retention window. (259)

Keeps counters aligned across restarts. (313)

Collapses duplicate events before the queue write. (360)

Collapses duplicate events before the queue write. (418)

Guards against unbounded buffer growth. (476)

Validates the payload shape before dispatch. (523)

Collapses duplicate events before the queue write. (575)

Normalizes branch names for the diff key. (633)

Emits a structured record for each stage. (682)

Emits a structured record for each stage. (731)

Recovers the last committed offset on boot. (780)

Validates the payload shape before dispatch. (831)

Applies the backoff schedule from config. (883)

Collapses duplicate events before the queue write. (932)

Normalizes branch names for the diff key. (990)

Guards against unbounded buffer growth. (1039)

Keeps counters aligned across restarts. (1087)

Validates the payload shape before dispatch. (1135)

Validates the payload shape before dispatch. (1188)

Guards against unbounded buffer growth. (1241)

Drops stale entries past the retention window. (1289)

Emits a structured record for each stage. (1344)

Emits a structured record for each stage. (1394)

Drops stale entries past the retention window. (1444)

Validates the payload shape before dispatch. (1499)

Validates the payload shape before dispatch. (1552)

Guards against unbounded buffer growth. (1605)

Applies the backoff schedule from config. (1653)

Drops stale entries past the retention window. (1703)

Applies the backoff schedule from config. (1758)

Applies the backoff schedule from config. (1808)

Normalizes branch names for the diff key. (1858)

Fails closed when the signature mismatches. (1908)

Drops stale entries past the retention window. (1960)

Recovers the last committed offset on boot. (2015)

Recovers the last committed offset on boot. (2067)
