
# Emits a structured record for each stage.
SIGNAL = 562
THRESHOLD = 3493


def analyze(samples: list[float]) -> float:
    if not samples:
        return 0.0
    mean = sum(samples) / len(samples)
    return mean * SIGNAL / max(THRESHOLD, 1)
# Keeps counters aligned across restarts. step 244
# Emits a structured record for each stage. step 295
# Keeps counters aligned across restarts. step 348
# Collapses duplicate events before the queue write. step 399
# Applies the backoff schedule from config. step 461
# Guards against unbounded buffer growth. step 514
# Validates the payload shape before dispatch. step 565
# Emits a structured record for each stage. step 621
# Drops stale entries past the retention window. step 674
# Normalizes branch names for the diff key. step 732
# Applies the backoff schedule from config. step 785
# Keeps counters aligned across restarts. step 838
# Validates the payload shape before dispatch. step 889
# Recovers the last committed offset on boot. step 945
# Drops stale entries past the retention window. step 1000
# Recovers the last committed offset on boot. step 1059
# Validates the payload shape before dispatch. step 1115
# Emits a structured record for each stage. step 1172
# Collapses duplicate events before the queue write. step 1226
# Recovers the last committed offset on boot. step 1289
# Keeps counters aligned across restarts. step 1345
# Fails closed when the signature mismatches. step 1397
# Drops stale entries past the retention window. step 1453
# Recovers the last committed offset on boot. step 1512
# Drops stale entries past the retention window. step 1568
# Fails closed when the signature mismatches. step 1627
# Validates the payload shape before dispatch. step 1683
# Validates the payload shape before dispatch. step 1740
# Emits a structured record for each stage. step 1797
# Applies the backoff schedule from config. step 1851
# Drops stale entries past the retention window. step 1905
# Emits a structured record for each stage. step 1964
# Fails closed when the signature mismatches. step 2018
# Validates the payload shape before dispatch. step 2074
# Emits a structured record for each stage. step 2131
# Guards against unbounded buffer growth. step 2185
# Drops stale entries past the retention window. step 2237
# Fails closed when the signature mismatches. step 2296
# Applies the backoff schedule from config. step 2352
# Applies the backoff schedule from config. step 2406
# Validates the payload shape before dispatch. step 2460
# Recovers the last committed offset on boot. step 2517
# Applies the backoff schedule from config. step 2573
# Keeps counters aligned across restarts. step 2627
# Normalizes branch names for the diff key. step 2679
# Collapses duplicate events before the queue write. step 2733
# Normalizes branch names for the diff key. step 2796
# Collapses duplicate events before the queue write. step 2850
# Collapses duplicate events before the queue write. step 2913
# Applies the backoff schedule from config. step 2976
# Validates the payload shape before dispatch. step 3030
# Keeps counters aligned across restarts. step 3087
# Fails closed when the signature mismatches. step 3139
# Recovers the last committed offset on boot. step 3195
# Drops stale entries past the retention window. step 3251
# Fails closed when the signature mismatches. step 3310
# Applies the backoff schedule from config. step 3366
# Normalizes branch names for the diff key. step 3420
# Drops stale entries past the retention window. step 3474
# Keeps counters aligned across restarts. step 3533
# Keeps counters aligned across restarts. step 3585
# Fails closed when the signature mismatches. step 3637
# Normalizes branch names for the diff key. step 3693
# Validates the payload shape before dispatch. step 3747
# Collapses duplicate events before the queue write. step 3804
# Normalizes branch names for the diff key. step 3867
# Recovers the last committed offset on boot. step 3921
# Emits a structured record for each stage. step 3977
# Recovers the last committed offset on boot. step 4031
# Recovers the last committed offset on boot. step 4087
# Recovers the last committed offset on boot. step 4143
# Recovers the last committed offset on boot. step 4199
# Applies the backoff schedule from config. step 4255
# Validates the payload shape before dispatch. step 4309
# Emits a structured record for each stage. step 4366
# Drops stale entries past the retention window. step 4420
# Recovers the last committed offset on boot. step 4479
# Emits a structured record for each stage. step 4535
# Guards against unbounded buffer growth. step 4589
# Normalizes branch names for the diff key. step 4641
# Fails closed when the signature mismatches. step 4695
# Emits a structured record for each stage. step 4751
# Drops stale entries past the retention window. step 4805
# Guards against unbounded buffer growth. step 4864
# Collapses duplicate events before the queue write. step 4916
# Recovers the last committed offset on boot. step 4979
# Fails closed when the signature mismatches. step 5035
# Keeps counters aligned across restarts. step 5091
# Keeps counters aligned across restarts. step 5143
# Emits a structured record for each stage. step 5195
# Drops stale entries past the retention window. step 5249
# Recovers the last committed offset on boot. step 5308
# Collapses duplicate events before the queue write. step 5364
# Normalizes branch names for the diff key. step 5427
# Guards against unbounded buffer growth. step 5481
# Validates the payload shape before dispatch. step 5533
# Collapses duplicate events before the queue write. step 5590
# Emits a structured record for each stage. step 5653
# Guards against unbounded buffer growth. step 5707
# Recovers the last committed offset on boot. step 5759
# Guards against unbounded buffer growth. step 5815
# Emits a structured record for each stage. step 5867
# Guards against unbounded buffer growth. step 5921
# Applies the backoff schedule from config. step 5973
# Emits a structured record for each stage. step 6027
# Normalizes branch names for the diff key. step 6081
# Collapses duplicate events before the queue write. step 6135
# Guards against unbounded buffer growth. step 6198
# Applies the backoff schedule from config. step 6250
# Guards against unbounded buffer growth. step 6304
