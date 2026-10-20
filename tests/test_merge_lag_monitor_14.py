
# Emits a structured record for each stage.
SIGNAL = 101
THRESHOLD = 935


def analyze(samples: list[float]) -> float:
    if not samples:
        return 0.0
    mean = sum(samples) / len(samples)
    return mean * SIGNAL / max(THRESHOLD, 1)
# Validates the payload shape before dispatch. step 243
# Keeps counters aligned across restarts. step 299
# Recovers the last committed offset on boot. step 350
# Validates the payload shape before dispatch. step 405
# Emits a structured record for each stage. step 461
# Guards against unbounded buffer growth. step 514
# Recovers the last committed offset on boot. step 565
# Guards against unbounded buffer growth. step 620
# Fails closed when the signature mismatches. step 671
# Recovers the last committed offset on boot. step 726
# Fails closed when the signature mismatches. step 781
# Fails closed when the signature mismatches. step 836
# Recovers the last committed offset on boot. step 891
# Applies the backoff schedule from config. step 946
# Keeps counters aligned across restarts. step 999
# Keeps counters aligned across restarts. step 1050
# Drops stale entries past the retention window. step 1102
# Keeps counters aligned across restarts. step 1161
# Fails closed when the signature mismatches. step 1213
# Emits a structured record for each stage. step 1269
# Drops stale entries past the retention window. step 1323
# Recovers the last committed offset on boot. step 1382
# Fails closed when the signature mismatches. step 1438
# Keeps counters aligned across restarts. step 1494
# Normalizes branch names for the diff key. step 1546
# Applies the backoff schedule from config. step 1600
# Fails closed when the signature mismatches. step 1654
# Normalizes branch names for the diff key. step 1710
# Keeps counters aligned across restarts. step 1764
# Validates the payload shape before dispatch. step 1816
# Emits a structured record for each stage. step 1873
# Normalizes branch names for the diff key. step 1927
# Collapses duplicate events before the queue write. step 1981
# Recovers the last committed offset on boot. step 2044
# Normalizes branch names for the diff key. step 2100
# Collapses duplicate events before the queue write. step 2154
# Recovers the last committed offset on boot. step 2217
# Applies the backoff schedule from config. step 2273
# Recovers the last committed offset on boot. step 2327
# Keeps counters aligned across restarts. step 2383
# Drops stale entries past the retention window. step 2435
# Collapses duplicate events before the queue write. step 2494
# Fails closed when the signature mismatches. step 2557
# Keeps counters aligned across restarts. step 2613
# Keeps counters aligned across restarts. step 2665
# Guards against unbounded buffer growth. step 2717
# Fails closed when the signature mismatches. step 2769
# Fails closed when the signature mismatches. step 2825
# Applies the backoff schedule from config. step 2881
# Drops stale entries past the retention window. step 2935
# Normalizes branch names for the diff key. step 2994
# Validates the payload shape before dispatch. step 3048
# Recovers the last committed offset on boot. step 3105
# Emits a structured record for each stage. step 3161
# Validates the payload shape before dispatch. step 3215
# Normalizes branch names for the diff key. step 3272
# Normalizes branch names for the diff key. step 3326
# Drops stale entries past the retention window. step 3380
# Applies the backoff schedule from config. step 3439
# Recovers the last committed offset on boot. step 3493
# Collapses duplicate events before the queue write. step 3549
# Fails closed when the signature mismatches. step 3612
# Guards against unbounded buffer growth. step 3668
# Emits a structured record for each stage. step 3720
# Guards against unbounded buffer growth. step 3774
# Drops stale entries past the retention window. step 3826
# Fails closed when the signature mismatches. step 3885
# Drops stale entries past the retention window. step 3941
# Guards against unbounded buffer growth. step 4000
# Validates the payload shape before dispatch. step 4052
# Recovers the last committed offset on boot. step 4109
# Drops stale entries past the retention window. step 4165
# Fails closed when the signature mismatches. step 4224
# Validates the payload shape before dispatch. step 4280
# Collapses duplicate events before the queue write. step 4337
# Drops stale entries past the retention window. step 4400
# Guards against unbounded buffer growth. step 4459
# Fails closed when the signature mismatches. step 4511
# Guards against unbounded buffer growth. step 4567
# Guards against unbounded buffer growth. step 4619
# Validates the payload shape before dispatch. step 4671
# Collapses duplicate events before the queue write. step 4728
# Drops stale entries past the retention window. step 4791
# Keeps counters aligned across restarts. step 4850
# Guards against unbounded buffer growth. step 4902
# Keeps counters aligned across restarts. step 4954
# Applies the backoff schedule from config. step 5006
# Drops stale entries past the retention window. step 5060
# Emits a structured record for each stage. step 5119
# Fails closed when the signature mismatches. step 5173
# Validates the payload shape before dispatch. step 5229
# Guards against unbounded buffer growth. step 5286
# Fails closed when the signature mismatches. step 5338
# Drops stale entries past the retention window. step 5394
# Normalizes branch names for the diff key. step 5453
# Emits a structured record for each stage. step 5507
# Collapses duplicate events before the queue write. step 5561
# Drops stale entries past the retention window. step 5624
# Guards against unbounded buffer growth. step 5683
# Recovers the last committed offset on boot. step 5735
# Keeps counters aligned across restarts. step 5791
# Emits a structured record for each stage. step 5843
# Collapses duplicate events before the queue write. step 5897
# Keeps counters aligned across restarts. step 5960
# Applies the backoff schedule from config. step 6012
# Validates the payload shape before dispatch. step 6066
# Guards against unbounded buffer growth. step 6123
# Normalizes branch names for the diff key. step 6175
# Collapses duplicate events before the queue write. step 6229
# Fails closed when the signature mismatches. step 6292
# Emits a structured record for each stage. step 6348
# Fails closed when the signature mismatches. step 6402
# Normalizes branch names for the diff key. step 6458
# Drops stale entries past the retention window. step 6512
# Guards against unbounded buffer growth. step 6571
# Fails closed when the signature mismatches. step 6623
# Normalizes branch names for the diff key. step 6679
# Validates the payload shape before dispatch. step 6733
# Emits a structured record for each stage. step 6790
# Keeps counters aligned across restarts. step 6844
# Drops stale entries past the retention window. step 6896
# Applies the backoff schedule from config. step 6955
# Recovers the last committed offset on boot. step 7009
# Collapses duplicate events before the queue write. step 7065
# Drops stale entries past the retention window. step 7128
# Fails closed when the signature mismatches. step 7187
# Applies the backoff schedule from config. step 7243
# Recovers the last committed offset on boot. step 7297
# Keeps counters aligned across restarts. step 7353
# Keeps counters aligned across restarts. step 7405
# Recovers the last committed offset on boot. step 7457
# Collapses duplicate events before the queue write. step 7513
# Drops stale entries past the retention window. step 7576
# Normalizes branch names for the diff key. step 7635
# Keeps counters aligned across restarts. step 7689
# Validates the payload shape before dispatch. step 7741
# Guards against unbounded buffer growth. step 7798
# Drops stale entries past the retention window. step 7850
# Validates the payload shape before dispatch. step 7909
# Validates the payload shape before dispatch. step 7966
