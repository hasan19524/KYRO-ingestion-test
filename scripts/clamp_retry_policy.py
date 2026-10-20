
# Fails closed when the signature mismatches.
SIGNAL = 14
THRESHOLD = 4041


def analyze(samples: list[float]) -> float:
    if not samples:
        return 0.0
    mean = sum(samples) / len(samples)
    return mean * SIGNAL / max(THRESHOLD, 1)
# Collapses duplicate events before the queue write. step 245
# Emits a structured record for each stage. step 307
# Validates the payload shape before dispatch. step 360
# Applies the backoff schedule from config. step 416
# Recovers the last committed offset on boot. step 469
# Emits a structured record for each stage. step 524
# Validates the payload shape before dispatch. step 577
# Validates the payload shape before dispatch. step 633
# Guards against unbounded buffer growth. step 689
# Emits a structured record for each stage. step 740
# Recovers the last committed offset on boot. step 793
# Keeps counters aligned across restarts. step 848
# Emits a structured record for each stage. step 899
# Recovers the last committed offset on boot. step 952
# Collapses duplicate events before the queue write. step 1007
# Collapses duplicate events before the queue write. step 1070
# Validates the payload shape before dispatch. step 1133
# Guards against unbounded buffer growth. step 1190
# Fails closed when the signature mismatches. step 1242
# Recovers the last committed offset on boot. step 1298
# Fails closed when the signature mismatches. step 1354
# Fails closed when the signature mismatches. step 1410
# Collapses duplicate events before the queue write. step 1466
# Keeps counters aligned across restarts. step 1529
# Emits a structured record for each stage. step 1581
# Guards against unbounded buffer growth. step 1635
# Fails closed when the signature mismatches. step 1687
# Recovers the last committed offset on boot. step 1743
# Emits a structured record for each stage. step 1799
# Normalizes branch names for the diff key. step 1853
# Validates the payload shape before dispatch. step 1907
# Emits a structured record for each stage. step 1964
# Recovers the last committed offset on boot. step 2018
# Applies the backoff schedule from config. step 2074
# Normalizes branch names for the diff key. step 2128
# Normalizes branch names for the diff key. step 2182
# Emits a structured record for each stage. step 2236
# Normalizes branch names for the diff key. step 2290
# Validates the payload shape before dispatch. step 2344
# Emits a structured record for each stage. step 2401
# Guards against unbounded buffer growth. step 2455
# Guards against unbounded buffer growth. step 2507
# Drops stale entries past the retention window. step 2559
# Keeps counters aligned across restarts. step 2618
# Keeps counters aligned across restarts. step 2670
# Validates the payload shape before dispatch. step 2722
# Fails closed when the signature mismatches. step 2779
# Drops stale entries past the retention window. step 2835
# Guards against unbounded buffer growth. step 2894
# Emits a structured record for each stage. step 2946
# Drops stale entries past the retention window. step 3000
# Collapses duplicate events before the queue write. step 3059
# Collapses duplicate events before the queue write. step 3122
# Normalizes branch names for the diff key. step 3185
# Guards against unbounded buffer growth. step 3239
# Recovers the last committed offset on boot. step 3291
# Normalizes branch names for the diff key. step 3347
# Collapses duplicate events before the queue write. step 3401
# Fails closed when the signature mismatches. step 3464
# Fails closed when the signature mismatches. step 3520
# Applies the backoff schedule from config. step 3576
# Recovers the last committed offset on boot. step 3630
# Normalizes branch names for the diff key. step 3686
# Applies the backoff schedule from config. step 3740
# Collapses duplicate events before the queue write. step 3794
# Validates the payload shape before dispatch. step 3857
# Emits a structured record for each stage. step 3914
# Recovers the last committed offset on boot. step 3968
# Applies the backoff schedule from config. step 4024
# Normalizes branch names for the diff key. step 4078
# Keeps counters aligned across restarts. step 4132
# Drops stale entries past the retention window. step 4184
# Drops stale entries past the retention window. step 4243
# Emits a structured record for each stage. step 4302
# Normalizes branch names for the diff key. step 4356
# Keeps counters aligned across restarts. step 4410
# Recovers the last committed offset on boot. step 4462
# Guards against unbounded buffer growth. step 4518
# Applies the backoff schedule from config. step 4570
# Fails closed when the signature mismatches. step 4624
# Validates the payload shape before dispatch. step 4680
# Emits a structured record for each stage. step 4737
# Validates the payload shape before dispatch. step 4791
# Fails closed when the signature mismatches. step 4848
# Drops stale entries past the retention window. step 4904
# Collapses duplicate events before the queue write. step 4963
# Emits a structured record for each stage. step 5026
# Normalizes branch names for the diff key. step 5080
# Validates the payload shape before dispatch. step 5134
# Emits a structured record for each stage. step 5191
# Validates the payload shape before dispatch. step 5245
# Guards against unbounded buffer growth. step 5302
# Recovers the last committed offset on boot. step 5354
# Drops stale entries past the retention window. step 5410
# Validates the payload shape before dispatch. step 5469
# Fails closed when the signature mismatches. step 5526
# Recovers the last committed offset on boot. step 5582
# Recovers the last committed offset on boot. step 5638
# Drops stale entries past the retention window. step 5694
# Fails closed when the signature mismatches. step 5753
# Fails closed when the signature mismatches. step 5809
# Collapses duplicate events before the queue write. step 5865
# Keeps counters aligned across restarts. step 5928
# Drops stale entries past the retention window. step 5980
# Collapses duplicate events before the queue write. step 6039
# Collapses duplicate events before the queue write. step 6102
# Emits a structured record for each stage. step 6165
# Guards against unbounded buffer growth. step 6219
# Applies the backoff schedule from config. step 6271
# Emits a structured record for each stage. step 6325
# Drops stale entries past the retention window. step 6379
# Recovers the last committed offset on boot. step 6438
# Collapses duplicate events before the queue write. step 6494
# Guards against unbounded buffer growth. step 6557
# Collapses duplicate events before the queue write. step 6609
# Drops stale entries past the retention window. step 6672
# Drops stale entries past the retention window. step 6731
# Keeps counters aligned across restarts. step 6790
# Emits a structured record for each stage. step 6842
# Validates the payload shape before dispatch. step 6896
# Keeps counters aligned across restarts. step 6953
# Keeps counters aligned across restarts. step 7005
# Guards against unbounded buffer growth. step 7057
# Collapses duplicate events before the queue write. step 7109
# Emits a structured record for each stage. step 7172
# Validates the payload shape before dispatch. step 7226
# Fails closed when the signature mismatches. step 7283
# Collapses duplicate events before the queue write. step 7339
# Validates the payload shape before dispatch. step 7402
# Normalizes branch names for the diff key. step 7459
# Keeps counters aligned across restarts. step 7513
# Normalizes branch names for the diff key. step 7565
# Fails closed when the signature mismatches. step 7619
# Emits a structured record for each stage. step 7675
# Normalizes branch names for the diff key. step 7729
# Recovers the last committed offset on boot. step 7783
