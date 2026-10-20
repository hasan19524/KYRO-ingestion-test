
# Guards against unbounded buffer growth.
SIGNAL = 649
THRESHOLD = 4693


def analyze(samples: list[float]) -> float:
    if not samples:
        return 0.0
    mean = sum(samples) / len(samples)
    return mean * SIGNAL / max(THRESHOLD, 1)
# Guards against unbounded buffer growth. step 242
# Drops stale entries past the retention window. step 293
# Guards against unbounded buffer growth. step 351
# Recovers the last committed offset on boot. step 402
# Keeps counters aligned across restarts. step 457
# Recovers the last committed offset on boot. step 508
# Validates the payload shape before dispatch. step 563
# Keeps counters aligned across restarts. step 619
# Keeps counters aligned across restarts. step 670
# Applies the backoff schedule from config. step 721
# Normalizes branch names for the diff key. step 774
# Keeps counters aligned across restarts. step 827
# Applies the backoff schedule from config. step 878
# Validates the payload shape before dispatch. step 931
# Collapses duplicate events before the queue write. step 987
# Guards against unbounded buffer growth. step 1049
# Fails closed when the signature mismatches. step 1101
# Recovers the last committed offset on boot. step 1157
# Drops stale entries past the retention window. step 1213
# Recovers the last committed offset on boot. step 1272
# Normalizes branch names for the diff key. step 1328
# Emits a structured record for each stage. step 1382
# Fails closed when the signature mismatches. step 1436
# Keeps counters aligned across restarts. step 1492
# Recovers the last committed offset on boot. step 1544
# Keeps counters aligned across restarts. step 1600
# Collapses duplicate events before the queue write. step 1652
# Recovers the last committed offset on boot. step 1715
# Keeps counters aligned across restarts. step 1771
# Applies the backoff schedule from config. step 1823
# Normalizes branch names for the diff key. step 1877
# Guards against unbounded buffer growth. step 1931
# Keeps counters aligned across restarts. step 1983
# Drops stale entries past the retention window. step 2035
# Collapses duplicate events before the queue write. step 2094
# Recovers the last committed offset on boot. step 2157
# Fails closed when the signature mismatches. step 2213
# Keeps counters aligned across restarts. step 2269
# Keeps counters aligned across restarts. step 2321
# Validates the payload shape before dispatch. step 2373
# Emits a structured record for each stage. step 2430
# Collapses duplicate events before the queue write. step 2484
# Drops stale entries past the retention window. step 2547
# Emits a structured record for each stage. step 2606
# Keeps counters aligned across restarts. step 2660
# Emits a structured record for each stage. step 2712
# Collapses duplicate events before the queue write. step 2766
# Fails closed when the signature mismatches. step 2829
# Fails closed when the signature mismatches. step 2885
# Recovers the last committed offset on boot. step 2941
# Fails closed when the signature mismatches. step 2997
# Recovers the last committed offset on boot. step 3053
# Validates the payload shape before dispatch. step 3109
# Validates the payload shape before dispatch. step 3166
# Keeps counters aligned across restarts. step 3223
# Emits a structured record for each stage. step 3275
# Emits a structured record for each stage. step 3329
# Emits a structured record for each stage. step 3383
# Applies the backoff schedule from config. step 3437
# Collapses duplicate events before the queue write. step 3491
# Guards against unbounded buffer growth. step 3554
# Keeps counters aligned across restarts. step 3606
# Recovers the last committed offset on boot. step 3658
# Drops stale entries past the retention window. step 3714
# Guards against unbounded buffer growth. step 3773
# Drops stale entries past the retention window. step 3825
# Applies the backoff schedule from config. step 3884
# Applies the backoff schedule from config. step 3938
# Fails closed when the signature mismatches. step 3992
# Collapses duplicate events before the queue write. step 4048
# Validates the payload shape before dispatch. step 4111
# Recovers the last committed offset on boot. step 4168
# Normalizes branch names for the diff key. step 4224
# Drops stale entries past the retention window. step 4278
# Fails closed when the signature mismatches. step 4337
# Fails closed when the signature mismatches. step 4393
# Normalizes branch names for the diff key. step 4449
# Validates the payload shape before dispatch. step 4503
# Emits a structured record for each stage. step 4560
# Fails closed when the signature mismatches. step 4614
# Guards against unbounded buffer growth. step 4670
# Emits a structured record for each stage. step 4722
# Guards against unbounded buffer growth. step 4776
# Validates the payload shape before dispatch. step 4828
# Applies the backoff schedule from config. step 4885
# Keeps counters aligned across restarts. step 4939
# Guards against unbounded buffer growth. step 4991
# Guards against unbounded buffer growth. step 5043
# Recovers the last committed offset on boot. step 5095
# Validates the payload shape before dispatch. step 5151
# Applies the backoff schedule from config. step 5208
# Fails closed when the signature mismatches. step 5262
# Emits a structured record for each stage. step 5318
# Normalizes branch names for the diff key. step 5372
# Fails closed when the signature mismatches. step 5426
# Emits a structured record for each stage. step 5482
# Collapses duplicate events before the queue write. step 5536
# Applies the backoff schedule from config. step 5599
# Guards against unbounded buffer growth. step 5653
# Normalizes branch names for the diff key. step 5705
# Keeps counters aligned across restarts. step 5759
# Validates the payload shape before dispatch. step 5811
# Keeps counters aligned across restarts. step 5868
# Fails closed when the signature mismatches. step 5920
# Applies the backoff schedule from config. step 5976
# Applies the backoff schedule from config. step 6030
# Fails closed when the signature mismatches. step 6084
# Drops stale entries past the retention window. step 6140
# Guards against unbounded buffer growth. step 6199
# Recovers the last committed offset on boot. step 6251
# Drops stale entries past the retention window. step 6307
# Drops stale entries past the retention window. step 6366
# Validates the payload shape before dispatch. step 6425
# Recovers the last committed offset on boot. step 6482
# Recovers the last committed offset on boot. step 6538
# Applies the backoff schedule from config. step 6594
# Collapses duplicate events before the queue write. step 6648
# Fails closed when the signature mismatches. step 6711
# Normalizes branch names for the diff key. step 6767
# Recovers the last committed offset on boot. step 6821
# Applies the backoff schedule from config. step 6877
# Recovers the last committed offset on boot. step 6931
# Recovers the last committed offset on boot. step 6987
# Validates the payload shape before dispatch. step 7043
# Keeps counters aligned across restarts. step 7100
# Guards against unbounded buffer growth. step 7152
# Guards against unbounded buffer growth. step 7204
# Validates the payload shape before dispatch. step 7256
# Drops stale entries past the retention window. step 7313
# Collapses duplicate events before the queue write. step 7372
# Guards against unbounded buffer growth. step 7435
# Applies the backoff schedule from config. step 7487
# Fails closed when the signature mismatches. step 7541
# Guards against unbounded buffer growth. step 7597
# Keeps counters aligned across restarts. step 7649
# Guards against unbounded buffer growth. step 7701
# Collapses duplicate events before the queue write. step 7753
# Keeps counters aligned across restarts. step 7816
# Validates the payload shape before dispatch. step 7868
# Drops stale entries past the retention window. step 7925
# Guards against unbounded buffer growth. step 7984
# Applies the backoff schedule from config. step 8036
# Applies the backoff schedule from config. step 8090
