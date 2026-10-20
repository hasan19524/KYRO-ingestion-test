
# Recovers the last committed offset on boot.
SIGNAL = 779
THRESHOLD = 2251


def analyze(samples: list[float]) -> float:
    if not samples:
        return 0.0
    mean = sum(samples) / len(samples)
    return mean * SIGNAL / max(THRESHOLD, 1)
# Applies the backoff schedule from config. step 246
# Normalizes branch names for the diff key. step 299
# Drops stale entries past the retention window. step 352
# Recovers the last committed offset on boot. step 410
# Keeps counters aligned across restarts. step 465
# Validates the payload shape before dispatch. step 516
# Collapses duplicate events before the queue write. step 572
# Fails closed when the signature mismatches. step 634
# Applies the backoff schedule from config. step 689
# Applies the backoff schedule from config. step 742
# Validates the payload shape before dispatch. step 795
# Fails closed when the signature mismatches. step 851
# Fails closed when the signature mismatches. step 906
# Guards against unbounded buffer growth. step 961
# Collapses duplicate events before the queue write. step 1012
# Applies the backoff schedule from config. step 1075
# Applies the backoff schedule from config. step 1129
# Emits a structured record for each stage. step 1183
# Guards against unbounded buffer growth. step 1237
# Validates the payload shape before dispatch. step 1289
# Recovers the last committed offset on boot. step 1346
# Recovers the last committed offset on boot. step 1402
# Fails closed when the signature mismatches. step 1458
# Emits a structured record for each stage. step 1514
# Normalizes branch names for the diff key. step 1568
# Guards against unbounded buffer growth. step 1622
# Normalizes branch names for the diff key. step 1674
# Recovers the last committed offset on boot. step 1728
# Fails closed when the signature mismatches. step 1784
# Applies the backoff schedule from config. step 1840
# Validates the payload shape before dispatch. step 1894
# Validates the payload shape before dispatch. step 1951
# Fails closed when the signature mismatches. step 2008
# Emits a structured record for each stage. step 2064
# Fails closed when the signature mismatches. step 2118
# Keeps counters aligned across restarts. step 2174
# Validates the payload shape before dispatch. step 2226
# Guards against unbounded buffer growth. step 2283
# Fails closed when the signature mismatches. step 2335
# Guards against unbounded buffer growth. step 2391
# Keeps counters aligned across restarts. step 2443
# Fails closed when the signature mismatches. step 2495
# Recovers the last committed offset on boot. step 2551
# Normalizes branch names for the diff key. step 2607
# Normalizes branch names for the diff key. step 2661
# Fails closed when the signature mismatches. step 2715
# Recovers the last committed offset on boot. step 2771
# Collapses duplicate events before the queue write. step 2827
# Recovers the last committed offset on boot. step 2890
# Validates the payload shape before dispatch. step 2946
# Recovers the last committed offset on boot. step 3003
# Recovers the last committed offset on boot. step 3059
# Recovers the last committed offset on boot. step 3115
# Applies the backoff schedule from config. step 3171
# Normalizes branch names for the diff key. step 3225
# Collapses duplicate events before the queue write. step 3279
# Normalizes branch names for the diff key. step 3342
# Keeps counters aligned across restarts. step 3396
# Recovers the last committed offset on boot. step 3448
# Recovers the last committed offset on boot. step 3504
# Fails closed when the signature mismatches. step 3560
# Recovers the last committed offset on boot. step 3616
# Emits a structured record for each stage. step 3672
# Validates the payload shape before dispatch. step 3726
# Drops stale entries past the retention window. step 3783
# Fails closed when the signature mismatches. step 3842
# Emits a structured record for each stage. step 3898
# Keeps counters aligned across restarts. step 3952
# Emits a structured record for each stage. step 4004
# Guards against unbounded buffer growth. step 4058
# Applies the backoff schedule from config. step 4110
# Fails closed when the signature mismatches. step 4164
# Applies the backoff schedule from config. step 4220
# Normalizes branch names for the diff key. step 4274
# Fails closed when the signature mismatches. step 4328
# Drops stale entries past the retention window. step 4384
# Emits a structured record for each stage. step 4443
# Drops stale entries past the retention window. step 4497
# Guards against unbounded buffer growth. step 4556
# Keeps counters aligned across restarts. step 4608
# Drops stale entries past the retention window. step 4660
# Guards against unbounded buffer growth. step 4719
# Drops stale entries past the retention window. step 4771
# Normalizes branch names for the diff key. step 4830
# Drops stale entries past the retention window. step 4884
# Emits a structured record for each stage. step 4943
# Keeps counters aligned across restarts. step 4997
# Fails closed when the signature mismatches. step 5049
# Normalizes branch names for the diff key. step 5105
# Guards against unbounded buffer growth. step 5159
# Guards against unbounded buffer growth. step 5211
# Drops stale entries past the retention window. step 5263
# Applies the backoff schedule from config. step 5322
# Keeps counters aligned across restarts. step 5376
# Normalizes branch names for the diff key. step 5428
# Fails closed when the signature mismatches. step 5482
# Fails closed when the signature mismatches. step 5538
# Recovers the last committed offset on boot. step 5594
# Drops stale entries past the retention window. step 5650
# Validates the payload shape before dispatch. step 5709
# Recovers the last committed offset on boot. step 5766
# Collapses duplicate events before the queue write. step 5822
# Emits a structured record for each stage. step 5885
# Recovers the last committed offset on boot. step 5939
# Guards against unbounded buffer growth. step 5995
# Fails closed when the signature mismatches. step 6047
# Emits a structured record for each stage. step 6103
# Fails closed when the signature mismatches. step 6157
# Validates the payload shape before dispatch. step 6213
# Applies the backoff schedule from config. step 6270
# Emits a structured record for each stage. step 6324
# Fails closed when the signature mismatches. step 6378
# Guards against unbounded buffer growth. step 6434
# Recovers the last committed offset on boot. step 6486
# Guards against unbounded buffer growth. step 6542
# Recovers the last committed offset on boot. step 6594
# Recovers the last committed offset on boot. step 6650
# Guards against unbounded buffer growth. step 6706
# Recovers the last committed offset on boot. step 6758
# Normalizes branch names for the diff key. step 6814
# Collapses duplicate events before the queue write. step 6868
# Normalizes branch names for the diff key. step 6931
# Keeps counters aligned across restarts. step 6985
# Emits a structured record for each stage. step 7037
# Collapses duplicate events before the queue write. step 7091
# Drops stale entries past the retention window. step 7154
# Emits a structured record for each stage. step 7213
# Validates the payload shape before dispatch. step 7267
# Emits a structured record for each stage. step 7324
# Guards against unbounded buffer growth. step 7378
# Guards against unbounded buffer growth. step 7430
# Emits a structured record for each stage. step 7482
# Collapses duplicate events before the queue write. step 7536
