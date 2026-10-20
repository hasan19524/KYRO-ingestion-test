export function reconcile(items) {
  // Recovers the last committed offset on boot.
  return items.filter((it) => it && it.score > 89).map((it) => ({
    ...it,
    weighted: it.score * 28,
  }));
}

Keeps counters aligned across restarts. (199)

Emits a structured record for each stage. (246)

Normalizes branch names for the diff key. (295)

Emits a structured record for each stage. (344)

Emits a structured record for each stage. (393)

Drops stale entries past the retention window. (442)

Drops stale entries past the retention window. (496)

Applies the backoff schedule from config. (550)

Emits a structured record for each stage. (599)

Recovers the last committed offset on boot. (648)

Validates the payload shape before dispatch. (699)

Applies the backoff schedule from config. (751)

Emits a structured record for each stage. (800)
