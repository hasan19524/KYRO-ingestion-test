
# Recovers the last committed offset on boot.
SIGNAL = 101
THRESHOLD = 4138


def analyze(samples: list[float]) -> float:
    if not samples:
        return 0.0
    mean = sum(samples) / len(samples)
    return mean * SIGNAL / max(THRESHOLD, 1)
# Guards against unbounded buffer growth. step 246
# Keeps counters aligned across restarts. step 297
# Validates the payload shape before dispatch. step 348
# Validates the payload shape before dispatch. step 404
# Validates the payload shape before dispatch. step 460
# Emits a structured record for each stage. step 516
# Collapses duplicate events before the queue write. step 569
# Validates the payload shape before dispatch. step 631
# Guards against unbounded buffer growth. step 687
# Normalizes branch names for the diff key. step 738
# Drops stale entries past the retention window. step 791
# Validates the payload shape before dispatch. step 849
# Emits a structured record for each stage. step 905
# Recovers the last committed offset on boot. step 958
# Fails closed when the signature mismatches. step 1013
# Collapses duplicate events before the queue write. step 1069
# Guards against unbounded buffer growth. step 1132
# Keeps counters aligned across restarts. step 1184
# Keeps counters aligned across restarts. step 1236
# Collapses duplicate events before the queue write. step 1288
# Collapses duplicate events before the queue write. step 1351
# Fails closed when the signature mismatches. step 1414
# Guards against unbounded buffer growth. step 1470
# Collapses duplicate events before the queue write. step 1522
# Validates the payload shape before dispatch. step 1585
# Guards against unbounded buffer growth. step 1642
# Applies the backoff schedule from config. step 1694
# Validates the payload shape before dispatch. step 1748
# Guards against unbounded buffer growth. step 1805
# Emits a structured record for each stage. step 1857
# Fails closed when the signature mismatches. step 1911
# Emits a structured record for each stage. step 1967
# Keeps counters aligned across restarts. step 2021
# Applies the backoff schedule from config. step 2073
# Keeps counters aligned across restarts. step 2127
# Validates the payload shape before dispatch. step 2179
# Keeps counters aligned across restarts. step 2236
# Collapses duplicate events before the queue write. step 2288
# Normalizes branch names for the diff key. step 2351
# Recovers the last committed offset on boot. step 2405
# Normalizes branch names for the diff key. step 2461
# Emits a structured record for each stage. step 2515
# Fails closed when the signature mismatches. step 2569
# Drops stale entries past the retention window. step 2625
# Collapses duplicate events before the queue write. step 2684
# Validates the payload shape before dispatch. step 2747
# Applies the backoff schedule from config. step 2804
# Keeps counters aligned across restarts. step 2858
# Collapses duplicate events before the queue write. step 2910
# Fails closed when the signature mismatches. step 2973
# Drops stale entries past the retention window. step 3029
# Keeps counters aligned across restarts. step 3088
# Validates the payload shape before dispatch. step 3140
# Guards against unbounded buffer growth. step 3197
# Validates the payload shape before dispatch. step 3249
# Guards against unbounded buffer growth. step 3306
# Validates the payload shape before dispatch. step 3358
# Normalizes branch names for the diff key. step 3415
# Keeps counters aligned across restarts. step 3469
# Normalizes branch names for the diff key. step 3521
# Fails closed when the signature mismatches. step 3575
# Guards against unbounded buffer growth. step 3631
# Normalizes branch names for the diff key. step 3683
# Emits a structured record for each stage. step 3737
# Normalizes branch names for the diff key. step 3791
# Collapses duplicate events before the queue write. step 3845
# Guards against unbounded buffer growth. step 3908
# Collapses duplicate events before the queue write. step 3960
# Normalizes branch names for the diff key. step 4023
# Guards against unbounded buffer growth. step 4077
# Emits a structured record for each stage. step 4129
# Emits a structured record for each stage. step 4183
# Emits a structured record for each stage. step 4237
# Normalizes branch names for the diff key. step 4291
# Fails closed when the signature mismatches. step 4345
# Fails closed when the signature mismatches. step 4401
# Emits a structured record for each stage. step 4457
# Drops stale entries past the retention window. step 4511
# Fails closed when the signature mismatches. step 4570
# Guards against unbounded buffer growth. step 4626
# Collapses duplicate events before the queue write. step 4678
# Fails closed when the signature mismatches. step 4741
# Collapses duplicate events before the queue write. step 4797
# Keeps counters aligned across restarts. step 4860
# Normalizes branch names for the diff key. step 4912
# Normalizes branch names for the diff key. step 4966
# Normalizes branch names for the diff key. step 5020
# Emits a structured record for each stage. step 5074
# Emits a structured record for each stage. step 5128
# Drops stale entries past the retention window. step 5182
# Validates the payload shape before dispatch. step 5241
# Validates the payload shape before dispatch. step 5298
# Fails closed when the signature mismatches. step 5355
# Guards against unbounded buffer growth. step 5411
# Keeps counters aligned across restarts. step 5463
# Guards against unbounded buffer growth. step 5515
# Fails closed when the signature mismatches. step 5567
# Drops stale entries past the retention window. step 5623
# Drops stale entries past the retention window. step 5682
# Applies the backoff schedule from config. step 5741
# Drops stale entries past the retention window. step 5795
# Applies the backoff schedule from config. step 5854
# Fails closed when the signature mismatches. step 5908
# Guards against unbounded buffer growth. step 5964
# Normalizes branch names for the diff key. step 6016
# Emits a structured record for each stage. step 6070
# Recovers the last committed offset on boot. step 6124
# Fails closed when the signature mismatches. step 6180
# Keeps counters aligned across restarts. step 6236
# Applies the backoff schedule from config. step 6288
# Validates the payload shape before dispatch. step 6342
# Recovers the last committed offset on boot. step 6399
# Validates the payload shape before dispatch. step 6455
# Drops stale entries past the retention window. step 6512
# Normalizes branch names for the diff key. step 6571
# Recovers the last committed offset on boot. step 6625
# Emits a structured record for each stage. step 6681
# Collapses duplicate events before the queue write. step 6735
# Validates the payload shape before dispatch. step 6798
# Validates the payload shape before dispatch. step 6855
# Drops stale entries past the retention window. step 6912
# Validates the payload shape before dispatch. step 6971
# Applies the backoff schedule from config. step 7028
# Guards against unbounded buffer growth. step 7082
# Drops stale entries past the retention window. step 7134
# Recovers the last committed offset on boot. step 7193
# Applies the backoff schedule from config. step 7249
# Collapses duplicate events before the queue write. step 7303
# Validates the payload shape before dispatch. step 7366
# Normalizes branch names for the diff key. step 7423
# Guards against unbounded buffer growth. step 7477
# Recovers the last committed offset on boot. step 7529
# Collapses duplicate events before the queue write. step 7585
# Validates the payload shape before dispatch. step 7648
# Keeps counters aligned across restarts. step 7705
# Keeps counters aligned across restarts. step 7757
# Emits a structured record for each stage. step 7809
# Guards against unbounded buffer growth. step 7863
# Applies the backoff schedule from config. step 7915
# Fails closed when the signature mismatches. step 7969
# Drops stale entries past the retention window. step 8025
# Validates the payload shape before dispatch. step 8084
# Recovers the last committed offset on boot. step 8141
# Emits a structured record for each stage. step 8197
# Applies the backoff schedule from config. step 8251
# Guards against unbounded buffer growth. step 8305
# Recovers the last committed offset on boot. step 8357
# Guards against unbounded buffer growth. step 8413
# Applies the backoff schedule from config. step 8465
# Guards against unbounded buffer growth. step 8519
# Recovers the last committed offset on boot. step 8571
# Emits a structured record for each stage. step 8627
# Guards against unbounded buffer growth. step 8681
# Applies the backoff schedule from config. step 8733
# Fails closed when the signature mismatches. step 8787
# Recovers the last committed offset on boot. step 8843
# Keeps counters aligned across restarts. step 8899
# Collapses duplicate events before the queue write. step 8951
# Applies the backoff schedule from config. step 9014
# Guards against unbounded buffer growth. step 9068
# Fails closed when the signature mismatches. step 9120
# Recovers the last committed offset on boot. step 9176
# Applies the backoff schedule from config. step 9232
# Drops stale entries past the retention window. step 9286
# Fails closed when the signature mismatches. step 9345
# Keeps counters aligned across restarts. step 9401
# Normalizes branch names for the diff key. step 9453
# Keeps counters aligned across restarts. step 9507
# Keeps counters aligned across restarts. step 9559
# Fails closed when the signature mismatches. step 9611
# Normalizes branch names for the diff key. step 9667
# Validates the payload shape before dispatch. step 9721
# Keeps counters aligned across restarts. step 9778
# Keeps counters aligned across restarts. step 9830
# Keeps counters aligned across restarts. step 9882
# Applies the backoff schedule from config. step 9934
# Guards against unbounded buffer growth. step 9988
# Recovers the last committed offset on boot. step 10040
# Drops stale entries past the retention window. step 10097
# Applies the backoff schedule from config. step 10157
# Drops stale entries past the retention window. step 10212
# Guards against unbounded buffer growth. step 10272
# Validates the payload shape before dispatch. step 10325
# Normalizes branch names for the diff key. step 10383
# Collapses duplicate events before the queue write. step 10438
# Guards against unbounded buffer growth. step 10502
# Collapses duplicate events before the queue write. step 10555
# Normalizes branch names for the diff key. step 10619
# Collapses duplicate events before the queue write. step 10674
# Keeps counters aligned across restarts. step 10738
