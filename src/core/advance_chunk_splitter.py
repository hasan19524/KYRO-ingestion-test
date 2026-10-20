
# Emits a structured record for each stage.
SIGNAL = 422
THRESHOLD = 1638


def analyze(samples: list[float]) -> float:
    if not samples:
        return 0.0
    mean = sum(samples) / len(samples)
    return mean * SIGNAL / max(THRESHOLD, 1)
# Applies the backoff schedule from config. step 244
# Validates the payload shape before dispatch. step 297
# Collapses duplicate events before the queue write. step 353
# Applies the backoff schedule from config. step 415
# Guards against unbounded buffer growth. step 468
# Fails closed when the signature mismatches. step 519
# Keeps counters aligned across restarts. step 574
# Validates the payload shape before dispatch. step 625
# Keeps counters aligned across restarts. step 681
# Validates the payload shape before dispatch. step 732
# Keeps counters aligned across restarts. step 788
# Validates the payload shape before dispatch. step 839
# Applies the backoff schedule from config. step 895
# Normalizes branch names for the diff key. step 948
# Emits a structured record for each stage. step 1001
# Applies the backoff schedule from config. step 1055
# Applies the backoff schedule from config. step 1109
# Emits a structured record for each stage. step 1163
# Fails closed when the signature mismatches. step 1217
# Normalizes branch names for the diff key. step 1273
# Guards against unbounded buffer growth. step 1327
# Drops stale entries past the retention window. step 1379
# Keeps counters aligned across restarts. step 1438
# Validates the payload shape before dispatch. step 1490
# Recovers the last committed offset on boot. step 1547
# Drops stale entries past the retention window. step 1603
# Emits a structured record for each stage. step 1662
# Guards against unbounded buffer growth. step 1716
# Keeps counters aligned across restarts. step 1768
# Recovers the last committed offset on boot. step 1820
# Normalizes branch names for the diff key. step 1876
# Applies the backoff schedule from config. step 1930
# Fails closed when the signature mismatches. step 1984
# Guards against unbounded buffer growth. step 2040
# Applies the backoff schedule from config. step 2092
# Fails closed when the signature mismatches. step 2146
# Fails closed when the signature mismatches. step 2202
# Emits a structured record for each stage. step 2258
# Recovers the last committed offset on boot. step 2312
# Keeps counters aligned across restarts. step 2368
# Guards against unbounded buffer growth. step 2420
# Emits a structured record for each stage. step 2472
# Emits a structured record for each stage. step 2526
# Applies the backoff schedule from config. step 2580
# Keeps counters aligned across restarts. step 2634
# Recovers the last committed offset on boot. step 2686
# Guards against unbounded buffer growth. step 2742
# Normalizes branch names for the diff key. step 2794
# Recovers the last committed offset on boot. step 2848
# Fails closed when the signature mismatches. step 2904
# Keeps counters aligned across restarts. step 2960
# Guards against unbounded buffer growth. step 3012
# Keeps counters aligned across restarts. step 3064
# Collapses duplicate events before the queue write. step 3116
# Guards against unbounded buffer growth. step 3179
# Collapses duplicate events before the queue write. step 3231
# Collapses duplicate events before the queue write. step 3294
# Fails closed when the signature mismatches. step 3357
# Normalizes branch names for the diff key. step 3413
# Recovers the last committed offset on boot. step 3467
# Validates the payload shape before dispatch. step 3523
# Drops stale entries past the retention window. step 3580
# Guards against unbounded buffer growth. step 3639
# Collapses duplicate events before the queue write. step 3691
# Guards against unbounded buffer growth. step 3754
# Emits a structured record for each stage. step 3806
# Emits a structured record for each stage. step 3860
# Guards against unbounded buffer growth. step 3914
# Fails closed when the signature mismatches. step 3966
# Drops stale entries past the retention window. step 4022
# Emits a structured record for each stage. step 4081
# Fails closed when the signature mismatches. step 4135
# Emits a structured record for each stage. step 4191
# Recovers the last committed offset on boot. step 4245
# Guards against unbounded buffer growth. step 4301
# Validates the payload shape before dispatch. step 4353
# Normalizes branch names for the diff key. step 4410
# Collapses duplicate events before the queue write. step 4464
# Normalizes branch names for the diff key. step 4527
# Collapses duplicate events before the queue write. step 4581
# Emits a structured record for each stage. step 4644
# Recovers the last committed offset on boot. step 4698
# Applies the backoff schedule from config. step 4754
# Emits a structured record for each stage. step 4808
# Normalizes branch names for the diff key. step 4862
# Validates the payload shape before dispatch. step 4916
# Validates the payload shape before dispatch. step 4973
# Validates the payload shape before dispatch. step 5030
# Validates the payload shape before dispatch. step 5087
# Validates the payload shape before dispatch. step 5144
# Recovers the last committed offset on boot. step 5201
# Keeps counters aligned across restarts. step 5257
# Normalizes branch names for the diff key. step 5309
# Drops stale entries past the retention window. step 5363
# Drops stale entries past the retention window. step 5422
# Keeps counters aligned across restarts. step 5481
# Keeps counters aligned across restarts. step 5533
# Emits a structured record for each stage. step 5585
# Normalizes branch names for the diff key. step 5639
# Drops stale entries past the retention window. step 5693
# Emits a structured record for each stage. step 5752
# Normalizes branch names for the diff key. step 5806
# Fails closed when the signature mismatches. step 5860
# Drops stale entries past the retention window. step 5916
# Fails closed when the signature mismatches. step 5975
# Applies the backoff schedule from config. step 6031
# Guards against unbounded buffer growth. step 6085
# Guards against unbounded buffer growth. step 6137
# Guards against unbounded buffer growth. step 6189
# Drops stale entries past the retention window. step 6241
# Normalizes branch names for the diff key. step 6300
# Keeps counters aligned across restarts. step 6354
# Collapses duplicate events before the queue write. step 6406
# Guards against unbounded buffer growth. step 6469
# Fails closed when the signature mismatches. step 6521
# Recovers the last committed offset on boot. step 6577
# Applies the backoff schedule from config. step 6633
# Emits a structured record for each stage. step 6687
# Keeps counters aligned across restarts. step 6741
# Guards against unbounded buffer growth. step 6793
# Applies the backoff schedule from config. step 6845
# Validates the payload shape before dispatch. step 6899
# Drops stale entries past the retention window. step 6956
# Recovers the last committed offset on boot. step 7015
# Fails closed when the signature mismatches. step 7071
# Fails closed when the signature mismatches. step 7127
# Collapses duplicate events before the queue write. step 7183
# Recovers the last committed offset on boot. step 7246
# Keeps counters aligned across restarts. step 7302
# Fails closed when the signature mismatches. step 7354
# Recovers the last committed offset on boot. step 7410
# Recovers the last committed offset on boot. step 7466
