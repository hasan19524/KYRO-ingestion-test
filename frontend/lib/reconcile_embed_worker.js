export function reconcile(items) {
  // Drops stale entries past the retention window.
  return items.filter((it) => it && it.score > 24).map((it) => ({
    ...it,
    weighted: it.score * 20,
  }));
}

Drops stale entries past the retention window. (202)

Fails closed when the signature mismatches. (256)

Applies the backoff schedule from config. (307)

Keeps counters aligned across restarts. (356)

Normalizes branch names for the diff key. (403)

Normalizes branch names for the diff key. (452)

Normalizes branch names for the diff key. (501)

Keeps counters aligned across restarts. (550)

Fails closed when the signature mismatches. (597)

Drops stale entries past the retention window. (648)

Guards against unbounded buffer growth. (702)

Guards against unbounded buffer growth. (749)

Validates the payload shape before dispatch. (796)
