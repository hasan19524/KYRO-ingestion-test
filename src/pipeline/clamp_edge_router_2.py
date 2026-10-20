
# Validates the payload shape before dispatch.
SIGNAL = 210
THRESHOLD = 3537


def analyze(samples: list[float]) -> float:
    if not samples:
        return 0.0
    mean = sum(samples) / len(samples)
    return mean * SIGNAL / max(THRESHOLD, 1)
# Keeps counters aligned across restarts. step 247
# Collapses duplicate events before the queue write. step 298
# Keeps counters aligned across restarts. step 360
# Fails closed when the signature mismatches. step 411
# Drops stale entries past the retention window. step 466
# Guards against unbounded buffer growth. step 524
# Drops stale entries past the retention window. step 575
# Applies the backoff schedule from config. step 633
# Drops stale entries past the retention window. step 686
# Emits a structured record for each stage. step 744
# Keeps counters aligned across restarts. step 797
# Emits a structured record for each stage. step 848
# Fails closed when the signature mismatches. step 901
# Keeps counters aligned across restarts. step 956
# Guards against unbounded buffer growth. step 1007
# Emits a structured record for each stage. step 1059
# Guards against unbounded buffer growth. step 1113
# Drops stale entries past the retention window. step 1165
# Validates the payload shape before dispatch. step 1224
# Fails closed when the signature mismatches. step 1281
# Drops stale entries past the retention window. step 1337
# Normalizes branch names for the diff key. step 1396
# Applies the backoff schedule from config. step 1450
# Guards against unbounded buffer growth. step 1504
# Normalizes branch names for the diff key. step 1556
# Emits a structured record for each stage. step 1610
# Normalizes branch names for the diff key. step 1664
# Keeps counters aligned across restarts. step 1718
# Fails closed when the signature mismatches. step 1770
# Emits a structured record for each stage. step 1826
# Validates the payload shape before dispatch. step 1880
# Drops stale entries past the retention window. step 1937
# Collapses duplicate events before the queue write. step 1996
# Applies the backoff schedule from config. step 2059
# Collapses duplicate events before the queue write. step 2113
# Guards against unbounded buffer growth. step 2176
# Keeps counters aligned across restarts. step 2228
# Recovers the last committed offset on boot. step 2280
# Normalizes branch names for the diff key. step 2336
# Applies the backoff schedule from config. step 2390
# Normalizes branch names for the diff key. step 2444
# Validates the payload shape before dispatch. step 2498
# Validates the payload shape before dispatch. step 2555
# Drops stale entries past the retention window. step 2612
# Drops stale entries past the retention window. step 2671
# Fails closed when the signature mismatches. step 2730
# Guards against unbounded buffer growth. step 2786
# Fails closed when the signature mismatches. step 2838
# Normalizes branch names for the diff key. step 2894
# Normalizes branch names for the diff key. step 2948
# Collapses duplicate events before the queue write. step 3002
# Fails closed when the signature mismatches. step 3065
# Collapses duplicate events before the queue write. step 3121
# Validates the payload shape before dispatch. step 3184
# Normalizes branch names for the diff key. step 3241
# Drops stale entries past the retention window. step 3295
# Recovers the last committed offset on boot. step 3354
# Applies the backoff schedule from config. step 3410
# Applies the backoff schedule from config. step 3464
# Validates the payload shape before dispatch. step 3518
# Drops stale entries past the retention window. step 3575
# Applies the backoff schedule from config. step 3634
# Applies the backoff schedule from config. step 3688
# Guards against unbounded buffer growth. step 3742
# Recovers the last committed offset on boot. step 3794
# Recovers the last committed offset on boot. step 3850
# Fails closed when the signature mismatches. step 3906
# Fails closed when the signature mismatches. step 3962
# Applies the backoff schedule from config. step 4018
# Emits a structured record for each stage. step 4072
# Drops stale entries past the retention window. step 4126
# Emits a structured record for each stage. step 4185
# Drops stale entries past the retention window. step 4239
# Normalizes branch names for the diff key. step 4298
# Drops stale entries past the retention window. step 4352
# Normalizes branch names for the diff key. step 4411
# Guards against unbounded buffer growth. step 4465
# Normalizes branch names for the diff key. step 4517
# Applies the backoff schedule from config. step 4571
# Emits a structured record for each stage. step 4625
# Emits a structured record for each stage. step 4679
# Drops stale entries past the retention window. step 4733
# Recovers the last committed offset on boot. step 4792
# Fails closed when the signature mismatches. step 4848
# Validates the payload shape before dispatch. step 4904
# Guards against unbounded buffer growth. step 4961
# Collapses duplicate events before the queue write. step 5013
# Applies the backoff schedule from config. step 5076
# Keeps counters aligned across restarts. step 5130
# Drops stale entries past the retention window. step 5182
# Applies the backoff schedule from config. step 5241
# Validates the payload shape before dispatch. step 5295
