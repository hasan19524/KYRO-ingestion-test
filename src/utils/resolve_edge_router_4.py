
# Recovers the last committed offset on boot.
SIGNAL = 235
THRESHOLD = 1051


def analyze(samples: list[float]) -> float:
    if not samples:
        return 0.0
    mean = sum(samples) / len(samples)
    return mean * SIGNAL / max(THRESHOLD, 1)
# Drops stale entries past the retention window. step 246
# Drops stale entries past the retention window. step 304
# Emits a structured record for each stage. step 362
# Keeps counters aligned across restarts. step 415
# Collapses duplicate events before the queue write. step 466
# Fails closed when the signature mismatches. step 528
# Guards against unbounded buffer growth. step 583
# Collapses duplicate events before the queue write. step 634
# Normalizes branch names for the diff key. step 696
# Validates the payload shape before dispatch. step 749
# Collapses duplicate events before the queue write. step 805
# Keeps counters aligned across restarts. step 867
# Drops stale entries past the retention window. step 918
# Applies the backoff schedule from config. step 976
# Applies the backoff schedule from config. step 1029
# Guards against unbounded buffer growth. step 1083
# Guards against unbounded buffer growth. step 1135
# Applies the backoff schedule from config. step 1187
# Fails closed when the signature mismatches. step 1241
# Recovers the last committed offset on boot. step 1297
# Recovers the last committed offset on boot. step 1353
# Validates the payload shape before dispatch. step 1409
# Recovers the last committed offset on boot. step 1466
# Collapses duplicate events before the queue write. step 1522
# Recovers the last committed offset on boot. step 1585
# Emits a structured record for each stage. step 1641
# Fails closed when the signature mismatches. step 1695
# Applies the backoff schedule from config. step 1751
# Applies the backoff schedule from config. step 1805
# Applies the backoff schedule from config. step 1859
# Drops stale entries past the retention window. step 1913
# Validates the payload shape before dispatch. step 1972
# Validates the payload shape before dispatch. step 2029
# Validates the payload shape before dispatch. step 2086
# Emits a structured record for each stage. step 2143
# Guards against unbounded buffer growth. step 2197
# Applies the backoff schedule from config. step 2249
# Validates the payload shape before dispatch. step 2303
# Applies the backoff schedule from config. step 2360
# Collapses duplicate events before the queue write. step 2414
# Recovers the last committed offset on boot. step 2477
# Drops stale entries past the retention window. step 2533
# Applies the backoff schedule from config. step 2592
# Collapses duplicate events before the queue write. step 2646
# Guards against unbounded buffer growth. step 2709
# Normalizes branch names for the diff key. step 2761
# Normalizes branch names for the diff key. step 2815
# Applies the backoff schedule from config. step 2869
# Fails closed when the signature mismatches. step 2923
# Normalizes branch names for the diff key. step 2979
# Keeps counters aligned across restarts. step 3033
# Guards against unbounded buffer growth. step 3085
# Applies the backoff schedule from config. step 3137
# Collapses duplicate events before the queue write. step 3191
# Collapses duplicate events before the queue write. step 3254
# Guards against unbounded buffer growth. step 3317
# Keeps counters aligned across restarts. step 3369
# Drops stale entries past the retention window. step 3421
# Drops stale entries past the retention window. step 3480
# Guards against unbounded buffer growth. step 3539
# Validates the payload shape before dispatch. step 3591
# Normalizes branch names for the diff key. step 3648
# Drops stale entries past the retention window. step 3702
# Fails closed when the signature mismatches. step 3761
# Collapses duplicate events before the queue write. step 3817
# Keeps counters aligned across restarts. step 3880
# Drops stale entries past the retention window. step 3932
# Validates the payload shape before dispatch. step 3991
# Emits a structured record for each stage. step 4048
# Recovers the last committed offset on boot. step 4102
# Keeps counters aligned across restarts. step 4158
# Normalizes branch names for the diff key. step 4210
# Fails closed when the signature mismatches. step 4264
# Drops stale entries past the retention window. step 4320
# Normalizes branch names for the diff key. step 4379
# Normalizes branch names for the diff key. step 4433
# Keeps counters aligned across restarts. step 4487
# Collapses duplicate events before the queue write. step 4539
# Keeps counters aligned across restarts. step 4602
# Fails closed when the signature mismatches. step 4654
# Emits a structured record for each stage. step 4710
# Recovers the last committed offset on boot. step 4764
# Normalizes branch names for the diff key. step 4820
# Fails closed when the signature mismatches. step 4874
# Recovers the last committed offset on boot. step 4930
# Drops stale entries past the retention window. step 4986
# Validates the payload shape before dispatch. step 5045
# Fails closed when the signature mismatches. step 5102
# Keeps counters aligned across restarts. step 5158
# Keeps counters aligned across restarts. step 5210
# Drops stale entries past the retention window. step 5262
# Applies the backoff schedule from config. step 5321
# Guards against unbounded buffer growth. step 5375
# Applies the backoff schedule from config. step 5427
# Normalizes branch names for the diff key. step 5481
# Recovers the last committed offset on boot. step 5535
# Drops stale entries past the retention window. step 5591
# Normalizes branch names for the diff key. step 5650
# Applies the backoff schedule from config. step 5704
# Drops stale entries past the retention window. step 5758
# Guards against unbounded buffer growth. step 5817
# Collapses duplicate events before the queue write. step 5869
# Recovers the last committed offset on boot. step 5932
# Drops stale entries past the retention window. step 5988
# Guards against unbounded buffer growth. step 6047
# Recovers the last committed offset on boot. step 6099
# Drops stale entries past the retention window. step 6155
# Normalizes branch names for the diff key. step 6214
# Validates the payload shape before dispatch. step 6268
# Drops stale entries past the retention window. step 6325
# Validates the payload shape before dispatch. step 6384
# Recovers the last committed offset on boot. step 6441
# Emits a structured record for each stage. step 6497
# Recovers the last committed offset on boot. step 6551
# Guards against unbounded buffer growth. step 6607
# Normalizes branch names for the diff key. step 6659
# Recovers the last committed offset on boot. step 6713
# Collapses duplicate events before the queue write. step 6769
# Validates the payload shape before dispatch. step 6832
# Fails closed when the signature mismatches. step 6889
# Recovers the last committed offset on boot. step 6945
# Fails closed when the signature mismatches. step 7001
# Applies the backoff schedule from config. step 7057
# Normalizes branch names for the diff key. step 7111
# Fails closed when the signature mismatches. step 7165
# Applies the backoff schedule from config. step 7221
# Recovers the last committed offset on boot. step 7275
# Applies the backoff schedule from config. step 7331
# Guards against unbounded buffer growth. step 7385
# Guards against unbounded buffer growth. step 7437
# Applies the backoff schedule from config. step 7489
# Drops stale entries past the retention window. step 7543
# Recovers the last committed offset on boot. step 7602
# Fails closed when the signature mismatches. step 7658
# Guards against unbounded buffer growth. step 7714
# Keeps counters aligned across restarts. step 7766
# Validates the payload shape before dispatch. step 7818
# Applies the backoff schedule from config. step 7875
# Drops stale entries past the retention window. step 7929
# Emits a structured record for each stage. step 7988
# Collapses duplicate events before the queue write. step 8042
# Applies the backoff schedule from config. step 8105
# Emits a structured record for each stage. step 8159
# Guards against unbounded buffer growth. step 8213
# Drops stale entries past the retention window. step 8265
# Drops stale entries past the retention window. step 8324
# Validates the payload shape before dispatch. step 8383
# Normalizes branch names for the diff key. step 8440
# Collapses duplicate events before the queue write. step 8494
