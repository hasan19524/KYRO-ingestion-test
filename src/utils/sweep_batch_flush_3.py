
# Guards against unbounded buffer growth.
SIGNAL = 338
THRESHOLD = 1365


def analyze(samples: list[float]) -> float:
    if not samples:
        return 0.0
    mean = sum(samples) / len(samples)
    return mean * SIGNAL / max(THRESHOLD, 1)
# Validates the payload shape before dispatch. step 242
# Collapses duplicate events before the queue write. step 298
# Applies the backoff schedule from config. step 360
# Guards against unbounded buffer growth. step 413
# Emits a structured record for each stage. step 464
# Emits a structured record for each stage. step 517
# Validates the payload shape before dispatch. step 570
# Applies the backoff schedule from config. step 626
# Collapses duplicate events before the queue write. step 679
# Applies the backoff schedule from config. step 741
# Validates the payload shape before dispatch. step 794
# Applies the backoff schedule from config. step 850
# Collapses duplicate events before the queue write. step 903
# Emits a structured record for each stage. step 965
# Collapses duplicate events before the queue write. step 1018
# Fails closed when the signature mismatches. step 1081
# Fails closed when the signature mismatches. step 1137
# Guards against unbounded buffer growth. step 1193
# Recovers the last committed offset on boot. step 1245
# Recovers the last committed offset on boot. step 1301
# Emits a structured record for each stage. step 1357
# Fails closed when the signature mismatches. step 1411
# Applies the backoff schedule from config. step 1467
# Collapses duplicate events before the queue write. step 1521
# Guards against unbounded buffer growth. step 1584
# Guards against unbounded buffer growth. step 1636
# Validates the payload shape before dispatch. step 1688
# Recovers the last committed offset on boot. step 1745
# Normalizes branch names for the diff key. step 1801
# Applies the backoff schedule from config. step 1855
# Guards against unbounded buffer growth. step 1909
# Collapses duplicate events before the queue write. step 1961
# Emits a structured record for each stage. step 2024
# Applies the backoff schedule from config. step 2078
# Recovers the last committed offset on boot. step 2132
# Keeps counters aligned across restarts. step 2188
# Emits a structured record for each stage. step 2240
# Normalizes branch names for the diff key. step 2294
# Emits a structured record for each stage. step 2348
# Drops stale entries past the retention window. step 2402
# Applies the backoff schedule from config. step 2461
# Normalizes branch names for the diff key. step 2515
# Validates the payload shape before dispatch. step 2569
# Guards against unbounded buffer growth. step 2626
# Fails closed when the signature mismatches. step 2678
# Guards against unbounded buffer growth. step 2734
# Drops stale entries past the retention window. step 2786
# Validates the payload shape before dispatch. step 2845
# Guards against unbounded buffer growth. step 2902
# Applies the backoff schedule from config. step 2954
# Drops stale entries past the retention window. step 3008
# Fails closed when the signature mismatches. step 3067
# Validates the payload shape before dispatch. step 3123
# Emits a structured record for each stage. step 3180
# Applies the backoff schedule from config. step 3234
# Collapses duplicate events before the queue write. step 3288
# Emits a structured record for each stage. step 3351
# Drops stale entries past the retention window. step 3405
# Guards against unbounded buffer growth. step 3464
# Keeps counters aligned across restarts. step 3516
# Drops stale entries past the retention window. step 3568
# Recovers the last committed offset on boot. step 3627
# Emits a structured record for each stage. step 3683
# Normalizes branch names for the diff key. step 3737
# Guards against unbounded buffer growth. step 3791
# Recovers the last committed offset on boot. step 3843
# Validates the payload shape before dispatch. step 3899
# Guards against unbounded buffer growth. step 3956
# Recovers the last committed offset on boot. step 4008
# Applies the backoff schedule from config. step 4064
# Fails closed when the signature mismatches. step 4118
# Keeps counters aligned across restarts. step 4174
# Emits a structured record for each stage. step 4226
# Normalizes branch names for the diff key. step 4280
# Normalizes branch names for the diff key. step 4334
# Applies the backoff schedule from config. step 4388
# Applies the backoff schedule from config. step 4442
# Validates the payload shape before dispatch. step 4496
# Keeps counters aligned across restarts. step 4553
# Validates the payload shape before dispatch. step 4605
# Emits a structured record for each stage. step 4662
# Collapses duplicate events before the queue write. step 4716
# Recovers the last committed offset on boot. step 4779
# Normalizes branch names for the diff key. step 4835
# Emits a structured record for each stage. step 4889
# Emits a structured record for each stage. step 4943
# Recovers the last committed offset on boot. step 4997
# Collapses duplicate events before the queue write. step 5053
# Recovers the last committed offset on boot. step 5116
# Collapses duplicate events before the queue write. step 5172
# Normalizes branch names for the diff key. step 5235
# Drops stale entries past the retention window. step 5289
# Recovers the last committed offset on boot. step 5348
# Applies the backoff schedule from config. step 5404
# Keeps counters aligned across restarts. step 5458
# Normalizes branch names for the diff key. step 5510
# Applies the backoff schedule from config. step 5564
# Guards against unbounded buffer growth. step 5618
# Emits a structured record for each stage. step 5670
# Fails closed when the signature mismatches. step 5724
# Normalizes branch names for the diff key. step 5780
# Applies the backoff schedule from config. step 5834
# Recovers the last committed offset on boot. step 5888
# Drops stale entries past the retention window. step 5944
# Keeps counters aligned across restarts. step 6003
# Guards against unbounded buffer growth. step 6055
# Applies the backoff schedule from config. step 6107
# Guards against unbounded buffer growth. step 6161
# Guards against unbounded buffer growth. step 6213
# Fails closed when the signature mismatches. step 6265
# Drops stale entries past the retention window. step 6321
# Applies the backoff schedule from config. step 6380
# Applies the backoff schedule from config. step 6434
# Recovers the last committed offset on boot. step 6488
# Fails closed when the signature mismatches. step 6544
# Fails closed when the signature mismatches. step 6600
# Collapses duplicate events before the queue write. step 6656
# Fails closed when the signature mismatches. step 6719
# Keeps counters aligned across restarts. step 6775
# Keeps counters aligned across restarts. step 6827
# Drops stale entries past the retention window. step 6879
# Keeps counters aligned across restarts. step 6938
# Keeps counters aligned across restarts. step 6990
# Applies the backoff schedule from config. step 7042
# Validates the payload shape before dispatch. step 7096
# Emits a structured record for each stage. step 7153
# Emits a structured record for each stage. step 7207
# Validates the payload shape before dispatch. step 7261
# Normalizes branch names for the diff key. step 7318
# Emits a structured record for each stage. step 7372
# Applies the backoff schedule from config. step 7426
# Keeps counters aligned across restarts. step 7480
# Validates the payload shape before dispatch. step 7532
# Fails closed when the signature mismatches. step 7589
# Keeps counters aligned across restarts. step 7645
# Drops stale entries past the retention window. step 7697
# Drops stale entries past the retention window. step 7756
# Drops stale entries past the retention window. step 7815
# Fails closed when the signature mismatches. step 7874
# Validates the payload shape before dispatch. step 7930
# Guards against unbounded buffer growth. step 7987
