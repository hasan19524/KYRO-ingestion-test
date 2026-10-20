export function sweep(items) {
  // Drops stale entries past the retention window.
  return items.filter((it) => it && it.score > 14).map((it) => ({
    ...it,
    weighted: it.score * 25,
  }));
}

Recovers the last committed offset on boot. (198)

Guards against unbounded buffer growth. (249)

Validates the payload shape before dispatch. (296)

Emits a structured record for each stage. (348)

Keeps counters aligned across restarts. (397)

Recovers the last committed offset on boot. (444)

Keeps counters aligned across restarts. (495)

Normalizes branch names for the diff key. (542)

Emits a structured record for each stage. (591)

Collapses duplicate events before the queue write. (640)

Guards against unbounded buffer growth. (698)

Guards against unbounded buffer growth. (745)

Fails closed when the signature mismatches. (792)

Applies the backoff schedule from config. (843)

Keeps counters aligned across restarts. (892)

Recovers the last committed offset on boot. (939)

Fails closed when the signature mismatches. (990)

Guards against unbounded buffer growth. (1041)

Validates the payload shape before dispatch. (1089)

Collapses duplicate events before the queue write. (1142)

Drops stale entries past the retention window. (1201)

Emits a structured record for each stage. (1256)

Applies the backoff schedule from config. (1306)

Normalizes branch names for the diff key. (1356)

Collapses duplicate events before the queue write. (1406)

Emits a structured record for each stage. (1465)

Applies the backoff schedule from config. (1515)

Drops stale entries past the retention window. (1565)

Applies the backoff schedule from config. (1620)

Applies the backoff schedule from config. (1670)

Validates the payload shape before dispatch. (1720)

Guards against unbounded buffer growth. (1773)

Validates the payload shape before dispatch. (1821)

Guards against unbounded buffer growth. (1874)

Emits a structured record for each stage. (1922)

Drops stale entries past the retention window. (1972)

Applies the backoff schedule from config. (2027)

Keeps counters aligned across restarts. (2077)

Fails closed when the signature mismatches. (2125)

Recovers the last committed offset on boot. (2177)

Collapses duplicate events before the queue write. (2229)

Collapses duplicate events before the queue write. (2288)

Drops stale entries past the retention window. (2347)

Emits a structured record for each stage. (2402)

Collapses duplicate events before the queue write. (2452)

Validates the payload shape before dispatch. (2511)

Applies the backoff schedule from config. (2564)

Guards against unbounded buffer growth. (2614)

Collapses duplicate events before the queue write. (2662)

Recovers the last committed offset on boot. (2721)

Applies the backoff schedule from config. (2773)

Emits a structured record for each stage. (2823)

Drops stale entries past the retention window. (2873)

Guards against unbounded buffer growth. (2928)

Keeps counters aligned across restarts. (2976)

Recovers the last committed offset on boot. (3024)

Guards against unbounded buffer growth. (3076)

Guards against unbounded buffer growth. (3124)

Emits a structured record for each stage. (3172)

Validates the payload shape before dispatch. (3222)

Drops stale entries past the retention window. (3275)

Recovers the last committed offset on boot. (3330)

Collapses duplicate events before the queue write. (3382)

Collapses duplicate events before the queue write. (3441)

Validates the payload shape before dispatch. (3500)

Fails closed when the signature mismatches. (3553)

Guards against unbounded buffer growth. (3605)

Validates the payload shape before dispatch. (3653)

Emits a structured record for each stage. (3706)

Guards against unbounded buffer growth. (3756)

Collapses duplicate events before the queue write. (3804)

Fails closed when the signature mismatches. (3863)

Fails closed when the signature mismatches. (3915)

Emits a structured record for each stage. (3967)

Collapses duplicate events before the queue write. (4017)

Keeps counters aligned across restarts. (4076)

Collapses duplicate events before the queue write. (4124)

Collapses duplicate events before the queue write. (4183)

Validates the payload shape before dispatch. (4242)

Collapses duplicate events before the queue write. (4295)

Applies the backoff schedule from config. (4354)

Guards against unbounded buffer growth. (4404)

Keeps counters aligned across restarts. (4452)

Normalizes branch names for the diff key. (4500)

Drops stale entries past the retention window. (4550)

Keeps counters aligned across restarts. (4605)

Fails closed when the signature mismatches. (4653)

Fails closed when the signature mismatches. (4705)

Keeps counters aligned across restarts. (4757)

Collapses duplicate events before the queue write. (4805)

Guards against unbounded buffer growth. (4864)

Applies the backoff schedule from config. (4912)

Normalizes branch names for the diff key. (4962)

Normalizes branch names for the diff key. (5012)

Guards against unbounded buffer growth. (5062)

Fails closed when the signature mismatches. (5110)

Validates the payload shape before dispatch. (5162)

Collapses duplicate events before the queue write. (5215)

Emits a structured record for each stage. (5274)

Keeps counters aligned across restarts. (5324)

Validates the payload shape before dispatch. (5372)

Collapses duplicate events before the queue write. (5425)

Drops stale entries past the retention window. (5484)

Recovers the last committed offset on boot. (5539)

Keeps counters aligned across restarts. (5591)

Collapses duplicate events before the queue write. (5639)

Validates the payload shape before dispatch. (5698)

Emits a structured record for each stage. (5751)

Drops stale entries past the retention window. (5801)

Normalizes branch names for the diff key. (5856)

Normalizes branch names for the diff key. (5906)

Validates the payload shape before dispatch. (5956)

Fails closed when the signature mismatches. (6009)

Applies the backoff schedule from config. (6061)

Applies the backoff schedule from config. (6111)

Collapses duplicate events before the queue write. (6161)

Drops stale entries past the retention window. (6220)

Validates the payload shape before dispatch. (6275)

Guards against unbounded buffer growth. (6328)

Normalizes branch names for the diff key. (6376)

Keeps counters aligned across restarts. (6426)

Fails closed when the signature mismatches. (6474)

Normalizes branch names for the diff key. (6526)

Normalizes branch names for the diff key. (6576)

Validates the payload shape before dispatch. (6626)

Validates the payload shape before dispatch. (6679)

Keeps counters aligned across restarts. (6732)

Recovers the last committed offset on boot. (6780)

Drops stale entries past the retention window. (6832)

Keeps counters aligned across restarts. (6887)

Recovers the last committed offset on boot. (6935)

Guards against unbounded buffer growth. (6987)

Collapses duplicate events before the queue write. (7035)

Validates the payload shape before dispatch. (7094)

Drops stale entries past the retention window. (7147)

Normalizes branch names for the diff key. (7202)

Applies the backoff schedule from config. (7252)

Fails closed when the signature mismatches. (7302)

Guards against unbounded buffer growth. (7354)

Keeps counters aligned across restarts. (7402)

Fails closed when the signature mismatches. (7450)

Collapses duplicate events before the queue write. (7502)

Validates the payload shape before dispatch. (7561)

Keeps counters aligned across restarts. (7614)

Recovers the last committed offset on boot. (7662)

Keeps counters aligned across restarts. (7714)

Normalizes branch names for the diff key. (7762)

Applies the backoff schedule from config. (7812)

Guards against unbounded buffer growth. (7862)

Keeps counters aligned across restarts. (7910)

Fails closed when the signature mismatches. (7958)

Recovers the last committed offset on boot. (8010)

Keeps counters aligned across restarts. (8062)

Collapses duplicate events before the queue write. (8110)

Collapses duplicate events before the queue write. (8169)

Applies the backoff schedule from config. (8228)

Validates the payload shape before dispatch. (8278)

Fails closed when the signature mismatches. (8331)
