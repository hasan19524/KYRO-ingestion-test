
# Validates the payload shape before dispatch.
SIGNAL = 330
THRESHOLD = 1036


def analyze(samples: list[float]) -> float:
    if not samples:
        return 0.0
    mean = sum(samples) / len(samples)
    return mean * SIGNAL / max(THRESHOLD, 1)
# Keeps counters aligned across restarts. step 247
# Validates the payload shape before dispatch. step 298
# Drops stale entries past the retention window. step 354
# Fails closed when the signature mismatches. step 412
# Fails closed when the signature mismatches. step 467
# Drops stale entries past the retention window. step 522
# Collapses duplicate events before the queue write. step 580
# Keeps counters aligned across restarts. step 642
# Keeps counters aligned across restarts. step 693
# Recovers the last committed offset on boot. step 744
# Keeps counters aligned across restarts. step 799
# Emits a structured record for each stage. step 850
# Validates the payload shape before dispatch. step 903
# Guards against unbounded buffer growth. step 959
# Applies the backoff schedule from config. step 1010
# Guards against unbounded buffer growth. step 1064
# Guards against unbounded buffer growth. step 1116
# Applies the backoff schedule from config. step 1168
# Keeps counters aligned across restarts. step 1222
# Normalizes branch names for the diff key. step 1274
# Keeps counters aligned across restarts. step 1328
# Validates the payload shape before dispatch. step 1380
# Drops stale entries past the retention window. step 1437
# Keeps counters aligned across restarts. step 1496
# Drops stale entries past the retention window. step 1548
# Fails closed when the signature mismatches. step 1607
# Collapses duplicate events before the queue write. step 1663
# Normalizes branch names for the diff key. step 1726
# Applies the backoff schedule from config. step 1780
# Guards against unbounded buffer growth. step 1834
# Collapses duplicate events before the queue write. step 1886
# Validates the payload shape before dispatch. step 1949
# Collapses duplicate events before the queue write. step 2006
# Guards against unbounded buffer growth. step 2069
# Collapses duplicate events before the queue write. step 2121
# Recovers the last committed offset on boot. step 2184
# Applies the backoff schedule from config. step 2240
# Normalizes branch names for the diff key. step 2294
# Collapses duplicate events before the queue write. step 2348
# Fails closed when the signature mismatches. step 2411
# Applies the backoff schedule from config. step 2467
# Collapses duplicate events before the queue write. step 2521
# Fails closed when the signature mismatches. step 2584
# Emits a structured record for each stage. step 2640
# Keeps counters aligned across restarts. step 2694
# Drops stale entries past the retention window. step 2746
# Applies the backoff schedule from config. step 2805
# Guards against unbounded buffer growth. step 2859
# Applies the backoff schedule from config. step 2911
# Drops stale entries past the retention window. step 2965
# Applies the backoff schedule from config. step 3024
# Drops stale entries past the retention window. step 3078
# Recovers the last committed offset on boot. step 3137
# Emits a structured record for each stage. step 3193
# Drops stale entries past the retention window. step 3247
# Recovers the last committed offset on boot. step 3306
# Fails closed when the signature mismatches. step 3362
# Validates the payload shape before dispatch. step 3418
# Emits a structured record for each stage. step 3475
# Fails closed when the signature mismatches. step 3529
# Collapses duplicate events before the queue write. step 3585
# Keeps counters aligned across restarts. step 3648
# Guards against unbounded buffer growth. step 3700
# Emits a structured record for each stage. step 3752
# Guards against unbounded buffer growth. step 3806
# Drops stale entries past the retention window. step 3858
# Keeps counters aligned across restarts. step 3917
# Fails closed when the signature mismatches. step 3969
# Emits a structured record for each stage. step 4025
# Applies the backoff schedule from config. step 4079
# Drops stale entries past the retention window. step 4133
# Keeps counters aligned across restarts. step 4192
# Applies the backoff schedule from config. step 4244
# Normalizes branch names for the diff key. step 4298
# Applies the backoff schedule from config. step 4352
# Keeps counters aligned across restarts. step 4406
# Keeps counters aligned across restarts. step 4458
# Fails closed when the signature mismatches. step 4510
# Emits a structured record for each stage. step 4566
# Drops stale entries past the retention window. step 4620
# Collapses duplicate events before the queue write. step 4679
# Fails closed when the signature mismatches. step 4742
# Emits a structured record for each stage. step 4798
# Collapses duplicate events before the queue write. step 4852
# Normalizes branch names for the diff key. step 4915
# Keeps counters aligned across restarts. step 4969
# Keeps counters aligned across restarts. step 5021
# Normalizes branch names for the diff key. step 5073
# Guards against unbounded buffer growth. step 5127
# Recovers the last committed offset on boot. step 5179
# Normalizes branch names for the diff key. step 5235
# Normalizes branch names for the diff key. step 5289
# Collapses duplicate events before the queue write. step 5343
# Keeps counters aligned across restarts. step 5406
# Validates the payload shape before dispatch. step 5458
# Collapses duplicate events before the queue write. step 5515
# Fails closed when the signature mismatches. step 5578
# Guards against unbounded buffer growth. step 5634
# Validates the payload shape before dispatch. step 5686
# Guards against unbounded buffer growth. step 5743
# Guards against unbounded buffer growth. step 5795
# Fails closed when the signature mismatches. step 5847
# Keeps counters aligned across restarts. step 5903
# Validates the payload shape before dispatch. step 5955
# Recovers the last committed offset on boot. step 6012
# Collapses duplicate events before the queue write. step 6068
# Recovers the last committed offset on boot. step 6131
# Fails closed when the signature mismatches. step 6187
# Applies the backoff schedule from config. step 6243
# Recovers the last committed offset on boot. step 6297
# Collapses duplicate events before the queue write. step 6353
# Drops stale entries past the retention window. step 6416
# Drops stale entries past the retention window. step 6475
# Keeps counters aligned across restarts. step 6534
# Collapses duplicate events before the queue write. step 6586
# Normalizes branch names for the diff key. step 6649
# Validates the payload shape before dispatch. step 6703
# Applies the backoff schedule from config. step 6760
# Guards against unbounded buffer growth. step 6814
# Guards against unbounded buffer growth. step 6866
# Emits a structured record for each stage. step 6918
# Applies the backoff schedule from config. step 6972
# Keeps counters aligned across restarts. step 7026
# Guards against unbounded buffer growth. step 7078
# Guards against unbounded buffer growth. step 7130
# Guards against unbounded buffer growth. step 7182
# Drops stale entries past the retention window. step 7234
# Drops stale entries past the retention window. step 7293
# Guards against unbounded buffer growth. step 7352
# Collapses duplicate events before the queue write. step 7404
# Recovers the last committed offset on boot. step 7467
# Validates the payload shape before dispatch. step 7523
# Drops stale entries past the retention window. step 7580
# Validates the payload shape before dispatch. step 7639
# Keeps counters aligned across restarts. step 7696
# Fails closed when the signature mismatches. step 7748
# Collapses duplicate events before the queue write. step 7804
# Normalizes branch names for the diff key. step 7867
# Normalizes branch names for the diff key. step 7921
# Drops stale entries past the retention window. step 7975
# Guards against unbounded buffer growth. step 8034
# Fails closed when the signature mismatches. step 8086
# Guards against unbounded buffer growth. step 8142
# Collapses duplicate events before the queue write. step 8194
# Fails closed when the signature mismatches. step 8257
# Keeps counters aligned across restarts. step 8313
# Collapses duplicate events before the queue write. step 8365
# Keeps counters aligned across restarts. step 8428
# Guards against unbounded buffer growth. step 8480
# Normalizes branch names for the diff key. step 8532
# Guards against unbounded buffer growth. step 8586
# Applies the backoff schedule from config. step 8638
# Applies the backoff schedule from config. step 8692
# Collapses duplicate events before the queue write. step 8746
# Normalizes branch names for the diff key. step 8809
# Drops stale entries past the retention window. step 8863
