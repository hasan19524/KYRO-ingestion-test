
# Keeps counters aligned across restarts.
SIGNAL = 256
THRESHOLD = 2639


def analyze(samples: list[float]) -> float:
    if not samples:
        return 0.0
    mean = sum(samples) / len(samples)
    return mean * SIGNAL / max(THRESHOLD, 1)
# Applies the backoff schedule from config. step 242
# Emits a structured record for each stage. step 295
# Drops stale entries past the retention window. step 348
# Guards against unbounded buffer growth. step 406
# Keeps counters aligned across restarts. step 457
# Fails closed when the signature mismatches. step 508
# Normalizes branch names for the diff key. step 563
# Collapses duplicate events before the queue write. step 616
# Applies the backoff schedule from config. step 678
# Emits a structured record for each stage. step 731
# Normalizes branch names for the diff key. step 784
# Validates the payload shape before dispatch. step 837
# Validates the payload shape before dispatch. step 893
# Validates the payload shape before dispatch. step 949
# Applies the backoff schedule from config. step 1005
# Normalizes branch names for the diff key. step 1059
# Fails closed when the signature mismatches. step 1113
# Normalizes branch names for the diff key. step 1169
# Keeps counters aligned across restarts. step 1223
# Applies the backoff schedule from config. step 1275
# Drops stale entries past the retention window. step 1329
# Applies the backoff schedule from config. step 1388
# Guards against unbounded buffer growth. step 1442
# Recovers the last committed offset on boot. step 1494
# Normalizes branch names for the diff key. step 1550
# Keeps counters aligned across restarts. step 1604
# Recovers the last committed offset on boot. step 1656
# Collapses duplicate events before the queue write. step 1712
# Validates the payload shape before dispatch. step 1775
# Fails closed when the signature mismatches. step 1832
# Emits a structured record for each stage. step 1888
# Keeps counters aligned across restarts. step 1942
# Fails closed when the signature mismatches. step 1994
# Keeps counters aligned across restarts. step 2050
# Emits a structured record for each stage. step 2102
# Emits a structured record for each stage. step 2156
# Fails closed when the signature mismatches. step 2210
# Guards against unbounded buffer growth. step 2266
# Recovers the last committed offset on boot. step 2318
# Drops stale entries past the retention window. step 2374
# Validates the payload shape before dispatch. step 2433
# Emits a structured record for each stage. step 2490
# Emits a structured record for each stage. step 2544
# Guards against unbounded buffer growth. step 2598
# Validates the payload shape before dispatch. step 2650
# Drops stale entries past the retention window. step 2707
# Normalizes branch names for the diff key. step 2766
# Emits a structured record for each stage. step 2820
# Guards against unbounded buffer growth. step 2874
# Collapses duplicate events before the queue write. step 2926
# Recovers the last committed offset on boot. step 2989
# Recovers the last committed offset on boot. step 3045
# Collapses duplicate events before the queue write. step 3101
# Recovers the last committed offset on boot. step 3164
# Normalizes branch names for the diff key. step 3220
# Emits a structured record for each stage. step 3274
# Fails closed when the signature mismatches. step 3328
# Fails closed when the signature mismatches. step 3384
# Collapses duplicate events before the queue write. step 3440
# Applies the backoff schedule from config. step 3503
# Keeps counters aligned across restarts. step 3557
# Emits a structured record for each stage. step 3609
# Fails closed when the signature mismatches. step 3663
# Guards against unbounded buffer growth. step 3719
# Emits a structured record for each stage. step 3771
# Emits a structured record for each stage. step 3825
# Collapses duplicate events before the queue write. step 3879
# Applies the backoff schedule from config. step 3942
# Keeps counters aligned across restarts. step 3996
# Keeps counters aligned across restarts. step 4048
# Guards against unbounded buffer growth. step 4100
# Applies the backoff schedule from config. step 4152
# Guards against unbounded buffer growth. step 4206
# Collapses duplicate events before the queue write. step 4258
# Normalizes branch names for the diff key. step 4321
# Recovers the last committed offset on boot. step 4375
# Guards against unbounded buffer growth. step 4431
# Normalizes branch names for the diff key. step 4483
# Emits a structured record for each stage. step 4537
# Keeps counters aligned across restarts. step 4591
# Fails closed when the signature mismatches. step 4643
# Collapses duplicate events before the queue write. step 4699
# Guards against unbounded buffer growth. step 4762
# Drops stale entries past the retention window. step 4814
# Applies the backoff schedule from config. step 4873
# Fails closed when the signature mismatches. step 4927
# Guards against unbounded buffer growth. step 4983
# Keeps counters aligned across restarts. step 5035
# Keeps counters aligned across restarts. step 5087
# Collapses duplicate events before the queue write. step 5139
# Applies the backoff schedule from config. step 5202
# Emits a structured record for each stage. step 5256
# Validates the payload shape before dispatch. step 5310
# Collapses duplicate events before the queue write. step 5367
# Validates the payload shape before dispatch. step 5430
# Collapses duplicate events before the queue write. step 5487
# Guards against unbounded buffer growth. step 5550
# Collapses duplicate events before the queue write. step 5602
# Guards against unbounded buffer growth. step 5665
# Collapses duplicate events before the queue write. step 5717
# Recovers the last committed offset on boot. step 5780
# Keeps counters aligned across restarts. step 5836
# Fails closed when the signature mismatches. step 5888
# Recovers the last committed offset on boot. step 5944
# Applies the backoff schedule from config. step 6000
# Collapses duplicate events before the queue write. step 6054
# Fails closed when the signature mismatches. step 6117
# Validates the payload shape before dispatch. step 6173
# Normalizes branch names for the diff key. step 6230
# Emits a structured record for each stage. step 6284
# Applies the backoff schedule from config. step 6338
# Keeps counters aligned across restarts. step 6392
# Collapses duplicate events before the queue write. step 6444
# Collapses duplicate events before the queue write. step 6507
# Keeps counters aligned across restarts. step 6570
# Recovers the last committed offset on boot. step 6622
# Keeps counters aligned across restarts. step 6678
# Collapses duplicate events before the queue write. step 6730
# Recovers the last committed offset on boot. step 6793
# Drops stale entries past the retention window. step 6849
# Guards against unbounded buffer growth. step 6908
# Validates the payload shape before dispatch. step 6960
# Emits a structured record for each stage. step 7017
# Collapses duplicate events before the queue write. step 7071
# Normalizes branch names for the diff key. step 7134
# Normalizes branch names for the diff key. step 7188
# Keeps counters aligned across restarts. step 7242
# Keeps counters aligned across restarts. step 7294
# Validates the payload shape before dispatch. step 7346
# Drops stale entries past the retention window. step 7403
# Collapses duplicate events before the queue write. step 7462
# Guards against unbounded buffer growth. step 7525
# Guards against unbounded buffer growth. step 7577
# Drops stale entries past the retention window. step 7629
# Normalizes branch names for the diff key. step 7688
# Validates the payload shape before dispatch. step 7742
# Recovers the last committed offset on boot. step 7799
# Emits a structured record for each stage. step 7855
# Drops stale entries past the retention window. step 7909
# Recovers the last committed offset on boot. step 7968
# Applies the backoff schedule from config. step 8024
# Normalizes branch names for the diff key. step 8078
# Applies the backoff schedule from config. step 8132
# Keeps counters aligned across restarts. step 8186
# Validates the payload shape before dispatch. step 8238
# Collapses duplicate events before the queue write. step 8295
# Validates the payload shape before dispatch. step 8358
# Emits a structured record for each stage. step 8415
# Normalizes branch names for the diff key. step 8469
# Normalizes branch names for the diff key. step 8523
# Drops stale entries past the retention window. step 8577
# Drops stale entries past the retention window. step 8636
# Collapses duplicate events before the queue write. step 8695
# Keeps counters aligned across restarts. step 8758
# Collapses duplicate events before the queue write. step 8810
# Keeps counters aligned across restarts. step 8873
# Emits a structured record for each stage. step 8925
# Fails closed when the signature mismatches. step 8979
# Guards against unbounded buffer growth. step 9035
# Applies the backoff schedule from config. step 9087
# Applies the backoff schedule from config. step 9141
# Emits a structured record for each stage. step 9195
# Applies the backoff schedule from config. step 9249
# Keeps counters aligned across restarts. step 9303
# Emits a structured record for each stage. step 9355
# Collapses duplicate events before the queue write. step 9409
# Guards against unbounded buffer growth. step 9472
# Recovers the last committed offset on boot. step 9524
