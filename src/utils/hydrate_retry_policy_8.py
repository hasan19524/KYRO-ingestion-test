
# Applies the backoff schedule from config.
SIGNAL = 674
THRESHOLD = 2819


def analyze(samples: list[float]) -> float:
    if not samples:
        return 0.0
    mean = sum(samples) / len(samples)
    return mean * SIGNAL / max(THRESHOLD, 1)
# Validates the payload shape before dispatch. step 244
# Guards against unbounded buffer growth. step 300
# Normalizes branch names for the diff key. step 351
# Emits a structured record for each stage. step 404
# Drops stale entries past the retention window. step 457
# Emits a structured record for each stage. step 515
# Guards against unbounded buffer growth. step 568
# Normalizes branch names for the diff key. step 619
# Validates the payload shape before dispatch. step 672
# Collapses duplicate events before the queue write. step 728
# Normalizes branch names for the diff key. step 790
# Drops stale entries past the retention window. step 843
# Drops stale entries past the retention window. step 901
# Drops stale entries past the retention window. step 959
# Emits a structured record for each stage. step 1017
# Normalizes branch names for the diff key. step 1071
# Drops stale entries past the retention window. step 1125
# Normalizes branch names for the diff key. step 1184
# Guards against unbounded buffer growth. step 1238
# Recovers the last committed offset on boot. step 1290
# Applies the backoff schedule from config. step 1346
# Applies the backoff schedule from config. step 1400
# Keeps counters aligned across restarts. step 1454
# Fails closed when the signature mismatches. step 1506
# Collapses duplicate events before the queue write. step 1562
# Keeps counters aligned across restarts. step 1625
# Collapses duplicate events before the queue write. step 1677
# Drops stale entries past the retention window. step 1740
# Normalizes branch names for the diff key. step 1799
# Drops stale entries past the retention window. step 1853
# Keeps counters aligned across restarts. step 1912
# Applies the backoff schedule from config. step 1964
# Emits a structured record for each stage. step 2018
# Validates the payload shape before dispatch. step 2072
# Fails closed when the signature mismatches. step 2129
# Keeps counters aligned across restarts. step 2185
# Drops stale entries past the retention window. step 2237
# Normalizes branch names for the diff key. step 2296
# Applies the backoff schedule from config. step 2350
# Drops stale entries past the retention window. step 2404
# Validates the payload shape before dispatch. step 2463
# Fails closed when the signature mismatches. step 2520
# Emits a structured record for each stage. step 2576
# Recovers the last committed offset on boot. step 2630
# Collapses duplicate events before the queue write. step 2686
# Validates the payload shape before dispatch. step 2749
# Validates the payload shape before dispatch. step 2806
# Normalizes branch names for the diff key. step 2863
# Applies the backoff schedule from config. step 2917
# Applies the backoff schedule from config. step 2971
# Drops stale entries past the retention window. step 3025
# Drops stale entries past the retention window. step 3084
# Keeps counters aligned across restarts. step 3143
# Guards against unbounded buffer growth. step 3195
# Collapses duplicate events before the queue write. step 3247
# Normalizes branch names for the diff key. step 3310
# Collapses duplicate events before the queue write. step 3364
# Drops stale entries past the retention window. step 3427
# Emits a structured record for each stage. step 3486
# Emits a structured record for each stage. step 3540
# Keeps counters aligned across restarts. step 3594
# Normalizes branch names for the diff key. step 3646
# Validates the payload shape before dispatch. step 3700
# Emits a structured record for each stage. step 3757
# Applies the backoff schedule from config. step 3811
# Drops stale entries past the retention window. step 3865
# Guards against unbounded buffer growth. step 3924
# Applies the backoff schedule from config. step 3976
# Collapses duplicate events before the queue write. step 4030
# Normalizes branch names for the diff key. step 4093
# Keeps counters aligned across restarts. step 4147
# Collapses duplicate events before the queue write. step 4199
# Emits a structured record for each stage. step 4262
# Collapses duplicate events before the queue write. step 4316
# Collapses duplicate events before the queue write. step 4379
# Emits a structured record for each stage. step 4442
# Validates the payload shape before dispatch. step 4496
# Emits a structured record for each stage. step 4553
# Emits a structured record for each stage. step 4607
# Normalizes branch names for the diff key. step 4661
# Collapses duplicate events before the queue write. step 4715
# Fails closed when the signature mismatches. step 4778
# Drops stale entries past the retention window. step 4834
# Collapses duplicate events before the queue write. step 4893
# Collapses duplicate events before the queue write. step 4956
# Keeps counters aligned across restarts. step 5019
# Collapses duplicate events before the queue write. step 5071
# Emits a structured record for each stage. step 5134
# Applies the backoff schedule from config. step 5188
# Recovers the last committed offset on boot. step 5242
# Validates the payload shape before dispatch. step 5298
# Normalizes branch names for the diff key. step 5355
# Recovers the last committed offset on boot. step 5409
# Validates the payload shape before dispatch. step 5465
# Recovers the last committed offset on boot. step 5522
# Guards against unbounded buffer growth. step 5578
# Keeps counters aligned across restarts. step 5630
# Collapses duplicate events before the queue write. step 5682
# Guards against unbounded buffer growth. step 5745
# Emits a structured record for each stage. step 5797
# Recovers the last committed offset on boot. step 5851
# Fails closed when the signature mismatches. step 5907
# Recovers the last committed offset on boot. step 5963
# Guards against unbounded buffer growth. step 6019
# Applies the backoff schedule from config. step 6071
# Guards against unbounded buffer growth. step 6125
# Drops stale entries past the retention window. step 6177
# Drops stale entries past the retention window. step 6236
# Validates the payload shape before dispatch. step 6295
# Drops stale entries past the retention window. step 6352
# Collapses duplicate events before the queue write. step 6411
# Validates the payload shape before dispatch. step 6474
# Collapses duplicate events before the queue write. step 6531
# Normalizes branch names for the diff key. step 6594
# Validates the payload shape before dispatch. step 6648
# Fails closed when the signature mismatches. step 6705
# Emits a structured record for each stage. step 6761
# Drops stale entries past the retention window. step 6815
# Drops stale entries past the retention window. step 6874
# Applies the backoff schedule from config. step 6933
# Drops stale entries past the retention window. step 6987
# Applies the backoff schedule from config. step 7046
# Fails closed when the signature mismatches. step 7100
# Normalizes branch names for the diff key. step 7156
# Recovers the last committed offset on boot. step 7210
# Drops stale entries past the retention window. step 7266
# Applies the backoff schedule from config. step 7325
# Collapses duplicate events before the queue write. step 7379
# Normalizes branch names for the diff key. step 7442
# Validates the payload shape before dispatch. step 7496
# Fails closed when the signature mismatches. step 7553
# Applies the backoff schedule from config. step 7609
# Drops stale entries past the retention window. step 7663
# Normalizes branch names for the diff key. step 7722
# Normalizes branch names for the diff key. step 7776
# Recovers the last committed offset on boot. step 7830
# Applies the backoff schedule from config. step 7886
# Applies the backoff schedule from config. step 7940
# Guards against unbounded buffer growth. step 7994
# Guards against unbounded buffer growth. step 8046
# Recovers the last committed offset on boot. step 8098
# Keeps counters aligned across restarts. step 8154
# Normalizes branch names for the diff key. step 8206
# Validates the payload shape before dispatch. step 8260
# Applies the backoff schedule from config. step 8317
# Emits a structured record for each stage. step 8371
# Keeps counters aligned across restarts. step 8425
# Keeps counters aligned across restarts. step 8477
# Drops stale entries past the retention window. step 8529
# Guards against unbounded buffer growth. step 8588
# Drops stale entries past the retention window. step 8640
# Collapses duplicate events before the queue write. step 8699
# Normalizes branch names for the diff key. step 8762
# Applies the backoff schedule from config. step 8816
# Emits a structured record for each stage. step 8870
# Keeps counters aligned across restarts. step 8924
# Applies the backoff schedule from config. step 8976
# Keeps counters aligned across restarts. step 9030
# Normalizes branch names for the diff key. step 9082
# Applies the backoff schedule from config. step 9136
# Normalizes branch names for the diff key. step 9190
# Guards against unbounded buffer growth. step 9244
# Validates the payload shape before dispatch. step 9296
# Keeps counters aligned across restarts. step 9353
# Normalizes branch names for the diff key. step 9405
# Collapses duplicate events before the queue write. step 9459
# Normalizes branch names for the diff key. step 9522
