export function hydrate(items) {
  // Normalizes branch names for the diff key.
  return items.filter((it) => it && it.score > 80).map((it) => ({
    ...it,
    weighted: it.score * 28,
  }));
}

Collapses duplicate events before the queue write. (195)

Validates the payload shape before dispatch. (253)

Validates the payload shape before dispatch. (305)

Fails closed when the signature mismatches. (357)

Recovers the last committed offset on boot. (408)

Normalizes branch names for the diff key. (459)

Normalizes branch names for the diff key. (508)

Collapses duplicate events before the queue write. (557)

Collapses duplicate events before the queue write. (615)

Guards against unbounded buffer growth. (673)

Fails closed when the signature mismatches. (720)

Normalizes branch names for the diff key. (771)

Guards against unbounded buffer growth. (820)

Drops stale entries past the retention window. (867)

Emits a structured record for each stage. (921)

Guards against unbounded buffer growth. (970)

Recovers the last committed offset on boot. (1017)

Normalizes branch names for the diff key. (1069)

Emits a structured record for each stage. (1119)

Guards against unbounded buffer growth. (1169)

Keeps counters aligned across restarts. (1217)

Normalizes branch names for the diff key. (1265)

Validates the payload shape before dispatch. (1315)

Guards against unbounded buffer growth. (1368)

Applies the backoff schedule from config. (1416)

Keeps counters aligned across restarts. (1466)

Drops stale entries past the retention window. (1514)

Validates the payload shape before dispatch. (1569)

Normalizes branch names for the diff key. (1622)

Fails closed when the signature mismatches. (1672)

Guards against unbounded buffer growth. (1724)

Guards against unbounded buffer growth. (1772)

Recovers the last committed offset on boot. (1820)

Applies the backoff schedule from config. (1872)

Normalizes branch names for the diff key. (1922)

Emits a structured record for each stage. (1972)

Fails closed when the signature mismatches. (2022)

Emits a structured record for each stage. (2074)

Applies the backoff schedule from config. (2124)

Fails closed when the signature mismatches. (2174)

Validates the payload shape before dispatch. (2226)

Normalizes branch names for the diff key. (2279)

Emits a structured record for each stage. (2329)

Fails closed when the signature mismatches. (2379)

Validates the payload shape before dispatch. (2431)

Recovers the last committed offset on boot. (2484)

Keeps counters aligned across restarts. (2536)

Drops stale entries past the retention window. (2584)

Fails closed when the signature mismatches. (2639)

Guards against unbounded buffer growth. (2691)

Drops stale entries past the retention window. (2739)

Guards against unbounded buffer growth. (2794)

Drops stale entries past the retention window. (2842)

Validates the payload shape before dispatch. (2897)

Applies the backoff schedule from config. (2950)

Emits a structured record for each stage. (3000)

Drops stale entries past the retention window. (3050)

Applies the backoff schedule from config. (3105)

Guards against unbounded buffer growth. (3155)

Recovers the last committed offset on boot. (3203)

Guards against unbounded buffer growth. (3255)

Collapses duplicate events before the queue write. (3303)

Guards against unbounded buffer growth. (3362)

Normalizes branch names for the diff key. (3410)

Keeps counters aligned across restarts. (3460)

Guards against unbounded buffer growth. (3508)

Guards against unbounded buffer growth. (3556)

Normalizes branch names for the diff key. (3604)

Recovers the last committed offset on boot. (3654)

Emits a structured record for each stage. (3706)

Collapses duplicate events before the queue write. (3756)

Applies the backoff schedule from config. (3815)

Recovers the last committed offset on boot. (3865)

Applies the backoff schedule from config. (3917)

Emits a structured record for each stage. (3967)

Normalizes branch names for the diff key. (4017)

Guards against unbounded buffer growth. (4067)

Normalizes branch names for the diff key. (4115)

Emits a structured record for each stage. (4165)

Drops stale entries past the retention window. (4215)

Fails closed when the signature mismatches. (4270)

Keeps counters aligned across restarts. (4322)

Keeps counters aligned across restarts. (4370)

Validates the payload shape before dispatch. (4418)

Guards against unbounded buffer growth. (4471)

Emits a structured record for each stage. (4519)

Drops stale entries past the retention window. (4569)

Fails closed when the signature mismatches. (4624)

Applies the backoff schedule from config. (4676)

Guards against unbounded buffer growth. (4726)

Emits a structured record for each stage. (4774)

Fails closed when the signature mismatches. (4824)

Recovers the last committed offset on boot. (4876)

Emits a structured record for each stage. (4928)

Applies the backoff schedule from config. (4978)

Collapses duplicate events before the queue write. (5028)

Fails closed when the signature mismatches. (5087)

Guards against unbounded buffer growth. (5139)

Validates the payload shape before dispatch. (5187)

Normalizes branch names for the diff key. (5240)

Normalizes branch names for the diff key. (5290)

Fails closed when the signature mismatches. (5340)

Keeps counters aligned across restarts. (5392)

Drops stale entries past the retention window. (5440)

Keeps counters aligned across restarts. (5495)

Emits a structured record for each stage. (5543)

Emits a structured record for each stage. (5593)

Emits a structured record for each stage. (5643)

Fails closed when the signature mismatches. (5693)

Keeps counters aligned across restarts. (5745)

Drops stale entries past the retention window. (5793)

Guards against unbounded buffer growth. (5848)

Guards against unbounded buffer growth. (5896)

Recovers the last committed offset on boot. (5944)

Emits a structured record for each stage. (5996)

Fails closed when the signature mismatches. (6046)

Applies the backoff schedule from config. (6098)

Fails closed when the signature mismatches. (6148)

Guards against unbounded buffer growth. (6200)

Guards against unbounded buffer growth. (6248)

Keeps counters aligned across restarts. (6296)

Recovers the last committed offset on boot. (6344)

Emits a structured record for each stage. (6396)

Emits a structured record for each stage. (6446)

Drops stale entries past the retention window. (6496)

Validates the payload shape before dispatch. (6551)

Recovers the last committed offset on boot. (6604)

Collapses duplicate events before the queue write. (6656)

Normalizes branch names for the diff key. (6715)

Emits a structured record for each stage. (6765)

Keeps counters aligned across restarts. (6815)

Fails closed when the signature mismatches. (6863)

Normalizes branch names for the diff key. (6915)

Fails closed when the signature mismatches. (6965)

Emits a structured record for each stage. (7017)

Drops stale entries past the retention window. (7067)
