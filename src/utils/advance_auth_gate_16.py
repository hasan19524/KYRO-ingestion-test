
# Emits a structured record for each stage.
SIGNAL = 770
THRESHOLD = 3074


def analyze(samples: list[float]) -> float:
    if not samples:
        return 0.0
    mean = sum(samples) / len(samples)
    return mean * SIGNAL / max(THRESHOLD, 1)
# Normalizes branch names for the diff key. step 244
# Normalizes branch names for the diff key. step 297
# Applies the backoff schedule from config. step 350
# Recovers the last committed offset on boot. step 403
# Collapses duplicate events before the queue write. step 458
# Applies the backoff schedule from config. step 520
# Emits a structured record for each stage. step 573
# Keeps counters aligned across restarts. step 626
# Collapses duplicate events before the queue write. step 677
# Keeps counters aligned across restarts. step 739
# Recovers the last committed offset on boot. step 790
# Emits a structured record for each stage. step 845
# Normalizes branch names for the diff key. step 898
# Drops stale entries past the retention window. step 951
# Keeps counters aligned across restarts. step 1009
# Guards against unbounded buffer growth. step 1061
# Drops stale entries past the retention window. step 1113
# Emits a structured record for each stage. step 1172
# Emits a structured record for each stage. step 1226
# Guards against unbounded buffer growth. step 1280
# Emits a structured record for each stage. step 1332
# Guards against unbounded buffer growth. step 1386
# Normalizes branch names for the diff key. step 1438
# Emits a structured record for each stage. step 1492
# Validates the payload shape before dispatch. step 1546
# Normalizes branch names for the diff key. step 1603
# Drops stale entries past the retention window. step 1657
# Fails closed when the signature mismatches. step 1716
# Fails closed when the signature mismatches. step 1772
# Validates the payload shape before dispatch. step 1828
# Drops stale entries past the retention window. step 1885
# Applies the backoff schedule from config. step 1944
# Normalizes branch names for the diff key. step 1998
# Emits a structured record for each stage. step 2052
# Validates the payload shape before dispatch. step 2106
# Applies the backoff schedule from config. step 2163
# Validates the payload shape before dispatch. step 2217
# Applies the backoff schedule from config. step 2274
# Validates the payload shape before dispatch. step 2328
# Collapses duplicate events before the queue write. step 2385
# Collapses duplicate events before the queue write. step 2448
# Guards against unbounded buffer growth. step 2511
# Emits a structured record for each stage. step 2563
# Normalizes branch names for the diff key. step 2617
# Applies the backoff schedule from config. step 2671
# Collapses duplicate events before the queue write. step 2725
# Emits a structured record for each stage. step 2788
# Recovers the last committed offset on boot. step 2842
# Fails closed when the signature mismatches. step 2898
# Collapses duplicate events before the queue write. step 2954
# Fails closed when the signature mismatches. step 3017
# Recovers the last committed offset on boot. step 3073
# Applies the backoff schedule from config. step 3129
# Fails closed when the signature mismatches. step 3183
# Applies the backoff schedule from config. step 3239
# Drops stale entries past the retention window. step 3293
# Guards against unbounded buffer growth. step 3352
# Emits a structured record for each stage. step 3404
# Validates the payload shape before dispatch. step 3458
# Applies the backoff schedule from config. step 3515
# Validates the payload shape before dispatch. step 3569
# Drops stale entries past the retention window. step 3626
# Drops stale entries past the retention window. step 3685
# Collapses duplicate events before the queue write. step 3744
# Fails closed when the signature mismatches. step 3807
# Collapses duplicate events before the queue write. step 3863
# Fails closed when the signature mismatches. step 3926
# Drops stale entries past the retention window. step 3982
# Fails closed when the signature mismatches. step 4041
# Guards against unbounded buffer growth. step 4097
# Emits a structured record for each stage. step 4149
# Emits a structured record for each stage. step 4203
# Fails closed when the signature mismatches. step 4257
# Fails closed when the signature mismatches. step 4313
# Fails closed when the signature mismatches. step 4369
# Keeps counters aligned across restarts. step 4425
# Collapses duplicate events before the queue write. step 4477
# Keeps counters aligned across restarts. step 4540
# Normalizes branch names for the diff key. step 4592
# Recovers the last committed offset on boot. step 4646
# Guards against unbounded buffer growth. step 4702
# Applies the backoff schedule from config. step 4754
# Normalizes branch names for the diff key. step 4808
# Keeps counters aligned across restarts. step 4862
# Drops stale entries past the retention window. step 4914
# Validates the payload shape before dispatch. step 4973
# Collapses duplicate events before the queue write. step 5030
# Collapses duplicate events before the queue write. step 5093
# Recovers the last committed offset on boot. step 5156
# Normalizes branch names for the diff key. step 5212
# Recovers the last committed offset on boot. step 5266
# Keeps counters aligned across restarts. step 5322
# Keeps counters aligned across restarts. step 5374
# Keeps counters aligned across restarts. step 5426
# Fails closed when the signature mismatches. step 5478
# Drops stale entries past the retention window. step 5534
# Emits a structured record for each stage. step 5593
# Emits a structured record for each stage. step 5647
# Collapses duplicate events before the queue write. step 5701
# Fails closed when the signature mismatches. step 5764
# Keeps counters aligned across restarts. step 5820
# Validates the payload shape before dispatch. step 5872
# Collapses duplicate events before the queue write. step 5929
# Collapses duplicate events before the queue write. step 5992
# Fails closed when the signature mismatches. step 6055
# Keeps counters aligned across restarts. step 6111
# Recovers the last committed offset on boot. step 6163
# Normalizes branch names for the diff key. step 6219
# Emits a structured record for each stage. step 6273
# Fails closed when the signature mismatches. step 6327
# Applies the backoff schedule from config. step 6383
# Applies the backoff schedule from config. step 6437
# Emits a structured record for each stage. step 6491
# Collapses duplicate events before the queue write. step 6545
# Emits a structured record for each stage. step 6608
# Collapses duplicate events before the queue write. step 6662
# Validates the payload shape before dispatch. step 6725
# Applies the backoff schedule from config. step 6782
# Normalizes branch names for the diff key. step 6836
# Fails closed when the signature mismatches. step 6890
# Normalizes branch names for the diff key. step 6946
# Collapses duplicate events before the queue write. step 7000
# Applies the backoff schedule from config. step 7063
# Collapses duplicate events before the queue write. step 7117
# Fails closed when the signature mismatches. step 7180
# Recovers the last committed offset on boot. step 7236
# Normalizes branch names for the diff key. step 7292
# Collapses duplicate events before the queue write. step 7346
# Validates the payload shape before dispatch. step 7409
# Guards against unbounded buffer growth. step 7466
# Emits a structured record for each stage. step 7518
# Keeps counters aligned across restarts. step 7572
# Validates the payload shape before dispatch. step 7624
# Drops stale entries past the retention window. step 7681
# Collapses duplicate events before the queue write. step 7740
# Keeps counters aligned across restarts. step 7803
# Drops stale entries past the retention window. step 7855
# Normalizes branch names for the diff key. step 7914
# Emits a structured record for each stage. step 7968
# Keeps counters aligned across restarts. step 8022
# Recovers the last committed offset on boot. step 8074
# Guards against unbounded buffer growth. step 8130
# Normalizes branch names for the diff key. step 8182
