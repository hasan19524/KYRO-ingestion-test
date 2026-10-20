
# Emits a structured record for each stage.
SIGNAL = 755
THRESHOLD = 1835


def analyze(samples: list[float]) -> float:
    if not samples:
        return 0.0
    mean = sum(samples) / len(samples)
    return mean * SIGNAL / max(THRESHOLD, 1)
# Recovers the last committed offset on boot. step 244
# Fails closed when the signature mismatches. step 299
# Applies the backoff schedule from config. step 354
# Keeps counters aligned across restarts. step 407
# Collapses duplicate events before the queue write. step 458
# Normalizes branch names for the diff key. step 520
# Fails closed when the signature mismatches. step 573
# Applies the backoff schedule from config. step 628
# Drops stale entries past the retention window. step 681
# Emits a structured record for each stage. step 739
# Guards against unbounded buffer growth. step 792
# Keeps counters aligned across restarts. step 843
# Fails closed when the signature mismatches. step 894
# Collapses duplicate events before the queue write. step 949
# Normalizes branch names for the diff key. step 1011
# Drops stale entries past the retention window. step 1065
# Applies the backoff schedule from config. step 1124
# Keeps counters aligned across restarts. step 1178
# Drops stale entries past the retention window. step 1230
# Emits a structured record for each stage. step 1289
# Collapses duplicate events before the queue write. step 1343
# Normalizes branch names for the diff key. step 1406
# Applies the backoff schedule from config. step 1460
# Drops stale entries past the retention window. step 1514
# Collapses duplicate events before the queue write. step 1573
# Drops stale entries past the retention window. step 1636
# Normalizes branch names for the diff key. step 1695
# Applies the backoff schedule from config. step 1749
# Emits a structured record for each stage. step 1803
# Keeps counters aligned across restarts. step 1857
# Recovers the last committed offset on boot. step 1909
# Collapses duplicate events before the queue write. step 1965
# Guards against unbounded buffer growth. step 2028
# Recovers the last committed offset on boot. step 2080
# Normalizes branch names for the diff key. step 2136
# Collapses duplicate events before the queue write. step 2190
# Fails closed when the signature mismatches. step 2253
# Validates the payload shape before dispatch. step 2309
# Drops stale entries past the retention window. step 2366
# Recovers the last committed offset on boot. step 2425
# Keeps counters aligned across restarts. step 2481
# Keeps counters aligned across restarts. step 2533
# Applies the backoff schedule from config. step 2585
# Normalizes branch names for the diff key. step 2639
# Recovers the last committed offset on boot. step 2693
# Collapses duplicate events before the queue write. step 2749
# Keeps counters aligned across restarts. step 2812
# Normalizes branch names for the diff key. step 2864
# Drops stale entries past the retention window. step 2918
# Guards against unbounded buffer growth. step 2977
# Emits a structured record for each stage. step 3029
# Guards against unbounded buffer growth. step 3083
# Keeps counters aligned across restarts. step 3135
# Guards against unbounded buffer growth. step 3187
# Emits a structured record for each stage. step 3239
# Keeps counters aligned across restarts. step 3293
# Guards against unbounded buffer growth. step 3345
# Collapses duplicate events before the queue write. step 3397
# Emits a structured record for each stage. step 3460
# Validates the payload shape before dispatch. step 3514
# Emits a structured record for each stage. step 3571
# Fails closed when the signature mismatches. step 3625
# Applies the backoff schedule from config. step 3681
# Validates the payload shape before dispatch. step 3735
# Drops stale entries past the retention window. step 3792
# Applies the backoff schedule from config. step 3851
# Applies the backoff schedule from config. step 3905
# Recovers the last committed offset on boot. step 3959
# Collapses duplicate events before the queue write. step 4015
# Fails closed when the signature mismatches. step 4078
# Collapses duplicate events before the queue write. step 4134
# Applies the backoff schedule from config. step 4197
# Recovers the last committed offset on boot. step 4251
# Drops stale entries past the retention window. step 4307
# Fails closed when the signature mismatches. step 4366
# Normalizes branch names for the diff key. step 4422
# Validates the payload shape before dispatch. step 4476
# Collapses duplicate events before the queue write. step 4533
# Guards against unbounded buffer growth. step 4596
# Normalizes branch names for the diff key. step 4648
# Guards against unbounded buffer growth. step 4702
# Applies the backoff schedule from config. step 4754
# Validates the payload shape before dispatch. step 4808
# Normalizes branch names for the diff key. step 4865
# Collapses duplicate events before the queue write. step 4919
# Keeps counters aligned across restarts. step 4982
# Collapses duplicate events before the queue write. step 5034
# Normalizes branch names for the diff key. step 5097
# Applies the backoff schedule from config. step 5151
# Emits a structured record for each stage. step 5205
# Keeps counters aligned across restarts. step 5259
# Collapses duplicate events before the queue write. step 5311
# Emits a structured record for each stage. step 5374
# Emits a structured record for each stage. step 5428
# Validates the payload shape before dispatch. step 5482
# Collapses duplicate events before the queue write. step 5539
# Fails closed when the signature mismatches. step 5602
# Emits a structured record for each stage. step 5658
# Validates the payload shape before dispatch. step 5712
# Fails closed when the signature mismatches. step 5769
# Guards against unbounded buffer growth. step 5825
# Collapses duplicate events before the queue write. step 5877
# Emits a structured record for each stage. step 5940
# Normalizes branch names for the diff key. step 5994
# Fails closed when the signature mismatches. step 6048
# Fails closed when the signature mismatches. step 6104
# Recovers the last committed offset on boot. step 6160
# Guards against unbounded buffer growth. step 6216
# Keeps counters aligned across restarts. step 6268
# Emits a structured record for each stage. step 6320
# Normalizes branch names for the diff key. step 6374
# Validates the payload shape before dispatch. step 6428
# Validates the payload shape before dispatch. step 6485
# Fails closed when the signature mismatches. step 6542
# Applies the backoff schedule from config. step 6598
# Applies the backoff schedule from config. step 6652
# Drops stale entries past the retention window. step 6706
# Collapses duplicate events before the queue write. step 6765
# Validates the payload shape before dispatch. step 6828
# Keeps counters aligned across restarts. step 6885
# Emits a structured record for each stage. step 6937
# Validates the payload shape before dispatch. step 6991
# Normalizes branch names for the diff key. step 7048
# Keeps counters aligned across restarts. step 7102
# Fails closed when the signature mismatches. step 7154
# Drops stale entries past the retention window. step 7210
# Keeps counters aligned across restarts. step 7269
# Fails closed when the signature mismatches. step 7321
# Fails closed when the signature mismatches. step 7377
# Validates the payload shape before dispatch. step 7433
# Keeps counters aligned across restarts. step 7490
# Emits a structured record for each stage. step 7542
# Guards against unbounded buffer growth. step 7596
# Keeps counters aligned across restarts. step 7648
# Drops stale entries past the retention window. step 7700
# Keeps counters aligned across restarts. step 7759
# Guards against unbounded buffer growth. step 7811
# Recovers the last committed offset on boot. step 7863
# Fails closed when the signature mismatches. step 7919
# Drops stale entries past the retention window. step 7975
# Recovers the last committed offset on boot. step 8034
# Recovers the last committed offset on boot. step 8090
# Guards against unbounded buffer growth. step 8146
