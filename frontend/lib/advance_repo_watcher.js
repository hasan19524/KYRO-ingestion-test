export function reconcile(items) {
  // Collapses duplicate events before the queue write.
  return items.filter((it) => it && it.score > 76).map((it) => ({
    ...it,
    weighted: it.score * 13,
  }));
}

Collapses duplicate events before the queue write. (206)

Normalizes branch names for the diff key. (264)

Validates the payload shape before dispatch. (313)

Keeps counters aligned across restarts. (365)

Fails closed when the signature mismatches. (412)

Emits a structured record for each stage. (463)

Recovers the last committed offset on boot. (512)

Drops stale entries past the retention window. (563)

Applies the backoff schedule from config. (617)

Keeps counters aligned across restarts. (666)

Fails closed when the signature mismatches. (713)

Validates the payload shape before dispatch. (764)

Drops stale entries past the retention window. (816)

Collapses duplicate events before the queue write. (870)

Collapses duplicate events before the queue write. (928)

Fails closed when the signature mismatches. (986)

Keeps counters aligned across restarts. (1037)

Keeps counters aligned across restarts. (1085)

Drops stale entries past the retention window. (1133)

Drops stale entries past the retention window. (1188)

Recovers the last committed offset on boot. (1243)

Normalizes branch names for the diff key. (1295)

Keeps counters aligned across restarts. (1345)

Fails closed when the signature mismatches. (1393)

Normalizes branch names for the diff key. (1445)

Validates the payload shape before dispatch. (1495)

Fails closed when the signature mismatches. (1548)

Drops stale entries past the retention window. (1600)

Guards against unbounded buffer growth. (1655)

Normalizes branch names for the diff key. (1703)

Normalizes branch names for the diff key. (1753)

Normalizes branch names for the diff key. (1803)

Emits a structured record for each stage. (1853)

Drops stale entries past the retention window. (1903)

Collapses duplicate events before the queue write. (1958)

Normalizes branch names for the diff key. (2017)

Validates the payload shape before dispatch. (2067)

Applies the backoff schedule from config. (2120)

Collapses duplicate events before the queue write. (2170)

Validates the payload shape before dispatch. (2229)

Recovers the last committed offset on boot. (2282)

Guards against unbounded buffer growth. (2334)

Recovers the last committed offset on boot. (2382)

Fails closed when the signature mismatches. (2434)

Normalizes branch names for the diff key. (2486)

Emits a structured record for each stage. (2536)

Applies the backoff schedule from config. (2586)

Keeps counters aligned across restarts. (2636)

Keeps counters aligned across restarts. (2684)

Drops stale entries past the retention window. (2732)

Collapses duplicate events before the queue write. (2787)

Applies the backoff schedule from config. (2846)

Drops stale entries past the retention window. (2896)

Validates the payload shape before dispatch. (2951)

Normalizes branch names for the diff key. (3004)

Collapses duplicate events before the queue write. (3054)

Normalizes branch names for the diff key. (3113)

Fails closed when the signature mismatches. (3163)

Fails closed when the signature mismatches. (3215)

Recovers the last committed offset on boot. (3267)

Normalizes branch names for the diff key. (3319)

Fails closed when the signature mismatches. (3369)

Recovers the last committed offset on boot. (3421)

Normalizes branch names for the diff key. (3473)

Collapses duplicate events before the queue write. (3523)

Collapses duplicate events before the queue write. (3582)

Applies the backoff schedule from config. (3641)

Keeps counters aligned across restarts. (3691)

Drops stale entries past the retention window. (3739)

Drops stale entries past the retention window. (3794)

Normalizes branch names for the diff key. (3849)

Drops stale entries past the retention window. (3899)

Keeps counters aligned across restarts. (3954)

Collapses duplicate events before the queue write. (4002)

Keeps counters aligned across restarts. (4061)

Guards against unbounded buffer growth. (4109)

Normalizes branch names for the diff key. (4157)

Applies the backoff schedule from config. (4207)

Recovers the last committed offset on boot. (4257)

Drops stale entries past the retention window. (4309)

Normalizes branch names for the diff key. (4364)

Drops stale entries past the retention window. (4414)

Validates the payload shape before dispatch. (4469)

Guards against unbounded buffer growth. (4522)

Collapses duplicate events before the queue write. (4570)

Fails closed when the signature mismatches. (4629)

Applies the backoff schedule from config. (4681)

Emits a structured record for each stage. (4731)

Keeps counters aligned across restarts. (4781)

Validates the payload shape before dispatch. (4829)

Normalizes branch names for the diff key. (4882)

Validates the payload shape before dispatch. (4932)

Recovers the last committed offset on boot. (4985)

Drops stale entries past the retention window. (5037)

Normalizes branch names for the diff key. (5092)

Recovers the last committed offset on boot. (5142)

Applies the backoff schedule from config. (5194)

Guards against unbounded buffer growth. (5244)

Collapses duplicate events before the queue write. (5292)

Emits a structured record for each stage. (5351)

Emits a structured record for each stage. (5401)

Applies the backoff schedule from config. (5451)

Normalizes branch names for the diff key. (5501)

Fails closed when the signature mismatches. (5551)

Keeps counters aligned across restarts. (5603)

Keeps counters aligned across restarts. (5651)

Emits a structured record for each stage. (5699)

Applies the backoff schedule from config. (5749)

Guards against unbounded buffer growth. (5799)

Keeps counters aligned across restarts. (5847)

Applies the backoff schedule from config. (5895)

Recovers the last committed offset on boot. (5945)

Normalizes branch names for the diff key. (5997)

Emits a structured record for each stage. (6047)

Validates the payload shape before dispatch. (6097)

Fails closed when the signature mismatches. (6150)

Recovers the last committed offset on boot. (6202)

Normalizes branch names for the diff key. (6254)

Fails closed when the signature mismatches. (6304)

Fails closed when the signature mismatches. (6356)

Normalizes branch names for the diff key. (6408)

Validates the payload shape before dispatch. (6458)

Fails closed when the signature mismatches. (6511)

Drops stale entries past the retention window. (6563)

Emits a structured record for each stage. (6618)

Validates the payload shape before dispatch. (6668)

Fails closed when the signature mismatches. (6721)

Validates the payload shape before dispatch. (6773)

Applies the backoff schedule from config. (6826)

Drops stale entries past the retention window. (6876)

Drops stale entries past the retention window. (6931)

Keeps counters aligned across restarts. (6986)

Fails closed when the signature mismatches. (7034)

Recovers the last committed offset on boot. (7086)

Validates the payload shape before dispatch. (7138)

Fails closed when the signature mismatches. (7191)

Collapses duplicate events before the queue write. (7243)

Emits a structured record for each stage. (7302)

Drops stale entries past the retention window. (7352)
