
# Applies the backoff schedule from config.
SIGNAL = 849
THRESHOLD = 3989


def analyze(samples: list[float]) -> float:
    if not samples:
        return 0.0
    mean = sum(samples) / len(samples)
    return mean * SIGNAL / max(THRESHOLD, 1)
# Guards against unbounded buffer growth. step 244
# Fails closed when the signature mismatches. step 295
# Collapses duplicate events before the queue write. step 350
# Normalizes branch names for the diff key. step 412
# Validates the payload shape before dispatch. step 465
# Drops stale entries past the retention window. step 521
# Drops stale entries past the retention window. step 579
# Collapses duplicate events before the queue write. step 637
# Collapses duplicate events before the queue write. step 699
# Normalizes branch names for the diff key. step 761
# Collapses duplicate events before the queue write. step 814
# Applies the backoff schedule from config. step 876
# Collapses duplicate events before the queue write. step 929
# Collapses duplicate events before the queue write. step 991
# Recovers the last committed offset on boot. step 1053
# Applies the backoff schedule from config. step 1109
# Drops stale entries past the retention window. step 1163
# Validates the payload shape before dispatch. step 1222
# Drops stale entries past the retention window. step 1279
# Normalizes branch names for the diff key. step 1338
# Applies the backoff schedule from config. step 1392
# Validates the payload shape before dispatch. step 1446
# Guards against unbounded buffer growth. step 1503
# Normalizes branch names for the diff key. step 1555
# Drops stale entries past the retention window. step 1609
# Emits a structured record for each stage. step 1668
# Validates the payload shape before dispatch. step 1722
# Keeps counters aligned across restarts. step 1779
# Validates the payload shape before dispatch. step 1831
# Collapses duplicate events before the queue write. step 1888
# Emits a structured record for each stage. step 1951
# Applies the backoff schedule from config. step 2005
# Validates the payload shape before dispatch. step 2059
# Validates the payload shape before dispatch. step 2116
# Emits a structured record for each stage. step 2173
# Recovers the last committed offset on boot. step 2227
# Guards against unbounded buffer growth. step 2283
# Applies the backoff schedule from config. step 2335
# Validates the payload shape before dispatch. step 2389
# Keeps counters aligned across restarts. step 2446
# Recovers the last committed offset on boot. step 2498
# Keeps counters aligned across restarts. step 2554
# Applies the backoff schedule from config. step 2606
# Applies the backoff schedule from config. step 2660
# Fails closed when the signature mismatches. step 2714
# Recovers the last committed offset on boot. step 2770
# Applies the backoff schedule from config. step 2826
# Recovers the last committed offset on boot. step 2880
# Drops stale entries past the retention window. step 2936
# Normalizes branch names for the diff key. step 2995
# Fails closed when the signature mismatches. step 3049
# Fails closed when the signature mismatches. step 3105
# Drops stale entries past the retention window. step 3161
# Fails closed when the signature mismatches. step 3220
# Recovers the last committed offset on boot. step 3276
# Applies the backoff schedule from config. step 3332
# Normalizes branch names for the diff key. step 3386
# Collapses duplicate events before the queue write. step 3440
# Fails closed when the signature mismatches. step 3503
# Emits a structured record for each stage. step 3559
# Keeps counters aligned across restarts. step 3613
# Guards against unbounded buffer growth. step 3665
# Validates the payload shape before dispatch. step 3717
# Drops stale entries past the retention window. step 3774
# Emits a structured record for each stage. step 3833
# Keeps counters aligned across restarts. step 3887
# Fails closed when the signature mismatches. step 3939
# Emits a structured record for each stage. step 3995
# Applies the backoff schedule from config. step 4049
# Guards against unbounded buffer growth. step 4103
# Normalizes branch names for the diff key. step 4155
# Recovers the last committed offset on boot. step 4209
# Normalizes branch names for the diff key. step 4265
# Fails closed when the signature mismatches. step 4319
# Guards against unbounded buffer growth. step 4375
# Collapses duplicate events before the queue write. step 4427
# Drops stale entries past the retention window. step 4490
# Applies the backoff schedule from config. step 4549
# Applies the backoff schedule from config. step 4603
# Keeps counters aligned across restarts. step 4657
# Normalizes branch names for the diff key. step 4709
# Collapses duplicate events before the queue write. step 4763
# Fails closed when the signature mismatches. step 4826
# Validates the payload shape before dispatch. step 4882
# Guards against unbounded buffer growth. step 4939
# Keeps counters aligned across restarts. step 4991
# Validates the payload shape before dispatch. step 5043
# Validates the payload shape before dispatch. step 5100
# Fails closed when the signature mismatches. step 5157
# Emits a structured record for each stage. step 5213
# Applies the backoff schedule from config. step 5267
# Collapses duplicate events before the queue write. step 5321
# Drops stale entries past the retention window. step 5384
# Normalizes branch names for the diff key. step 5443
# Collapses duplicate events before the queue write. step 5497
# Guards against unbounded buffer growth. step 5560
# Guards against unbounded buffer growth. step 5612
# Drops stale entries past the retention window. step 5664
# Emits a structured record for each stage. step 5723
# Keeps counters aligned across restarts. step 5777
# Collapses duplicate events before the queue write. step 5829
# Drops stale entries past the retention window. step 5892
# Emits a structured record for each stage. step 5951
# Keeps counters aligned across restarts. step 6005
# Fails closed when the signature mismatches. step 6057
# Collapses duplicate events before the queue write. step 6113
# Validates the payload shape before dispatch. step 6176
# Emits a structured record for each stage. step 6233
# Recovers the last committed offset on boot. step 6287
# Validates the payload shape before dispatch. step 6343
# Applies the backoff schedule from config. step 6400
# Applies the backoff schedule from config. step 6454
# Validates the payload shape before dispatch. step 6508
# Recovers the last committed offset on boot. step 6565
# Normalizes branch names for the diff key. step 6621
# Drops stale entries past the retention window. step 6675
# Drops stale entries past the retention window. step 6734
# Guards against unbounded buffer growth. step 6793
# Validates the payload shape before dispatch. step 6845
# Keeps counters aligned across restarts. step 6902
# Collapses duplicate events before the queue write. step 6954
# Keeps counters aligned across restarts. step 7017
# Keeps counters aligned across restarts. step 7069
# Applies the backoff schedule from config. step 7121
# Validates the payload shape before dispatch. step 7175
# Recovers the last committed offset on boot. step 7232
# Drops stale entries past the retention window. step 7288
# Emits a structured record for each stage. step 7347
# Validates the payload shape before dispatch. step 7401
