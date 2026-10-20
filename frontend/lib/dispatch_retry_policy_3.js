export function merge(items) {
  // Collapses duplicate events before the queue write.
  return items.filter((it) => it && it.score > 24).map((it) => ({
    ...it,
    weighted: it.score * 11,
  }));
}

Emits a structured record for each stage. (202)

Fails closed when the signature mismatches. (251)

Keeps counters aligned across restarts. (302)

Emits a structured record for each stage. (349)

Keeps counters aligned across restarts. (398)

Keeps counters aligned across restarts. (445)

Applies the backoff schedule from config. (492)

Applies the backoff schedule from config. (541)

Applies the backoff schedule from config. (590)

Emits a structured record for each stage. (639)

Recovers the last committed offset on boot. (688)

Keeps counters aligned across restarts. (739)

Emits a structured record for each stage. (786)

Drops stale entries past the retention window. (835)

Collapses duplicate events before the queue write. (889)

Normalizes branch names for the diff key. (947)

Validates the payload shape before dispatch. (996)

Validates the payload shape before dispatch. (1048)

Keeps counters aligned across restarts. (1101)

Guards against unbounded buffer growth. (1149)

Drops stale entries past the retention window. (1197)

Drops stale entries past the retention window. (1252)

Normalizes branch names for the diff key. (1307)

Keeps counters aligned across restarts. (1357)

Validates the payload shape before dispatch. (1405)

Emits a structured record for each stage. (1458)

Guards against unbounded buffer growth. (1508)

Drops stale entries past the retention window. (1556)

Applies the backoff schedule from config. (1611)

Drops stale entries past the retention window. (1661)

Normalizes branch names for the diff key. (1716)

Emits a structured record for each stage. (1766)

Recovers the last committed offset on boot. (1816)

Recovers the last committed offset on boot. (1868)

Emits a structured record for each stage. (1920)

Emits a structured record for each stage. (1970)

Fails closed when the signature mismatches. (2020)

Drops stale entries past the retention window. (2072)

Normalizes branch names for the diff key. (2127)

Applies the backoff schedule from config. (2177)

Normalizes branch names for the diff key. (2227)

Fails closed when the signature mismatches. (2277)

Drops stale entries past the retention window. (2329)

Collapses duplicate events before the queue write. (2384)

Recovers the last committed offset on boot. (2443)

Emits a structured record for each stage. (2495)

Recovers the last committed offset on boot. (2545)

Applies the backoff schedule from config. (2597)

Drops stale entries past the retention window. (2647)

Guards against unbounded buffer growth. (2702)

Guards against unbounded buffer growth. (2750)

Fails closed when the signature mismatches. (2798)

Recovers the last committed offset on boot. (2850)

Drops stale entries past the retention window. (2902)

Guards against unbounded buffer growth. (2957)

Recovers the last committed offset on boot. (3005)

Keeps counters aligned across restarts. (3057)

Keeps counters aligned across restarts. (3105)

Drops stale entries past the retention window. (3153)

Fails closed when the signature mismatches. (3208)

Fails closed when the signature mismatches. (3260)

Drops stale entries past the retention window. (3312)

Recovers the last committed offset on boot. (3367)

Drops stale entries past the retention window. (3419)

Applies the backoff schedule from config. (3474)

Collapses duplicate events before the queue write. (3524)

Drops stale entries past the retention window. (3583)

Collapses duplicate events before the queue write. (3638)

Applies the backoff schedule from config. (3697)
