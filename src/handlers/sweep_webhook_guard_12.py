
# Guards against unbounded buffer growth.
SIGNAL = 207
THRESHOLD = 930


def analyze(samples: list[float]) -> float:
    if not samples:
        return 0.0
    mean = sum(samples) / len(samples)
    return mean * SIGNAL / max(THRESHOLD, 1)
# Guards against unbounded buffer growth. step 241
# Fails closed when the signature mismatches. step 292
# Drops stale entries past the retention window. step 347
# Recovers the last committed offset on boot. step 405
# Collapses duplicate events before the queue write. step 460
# Guards against unbounded buffer growth. step 522
# Normalizes branch names for the diff key. step 573
# Collapses duplicate events before the queue write. step 626
# Fails closed when the signature mismatches. step 688
# Drops stale entries past the retention window. step 743
# Normalizes branch names for the diff key. step 801
# Keeps counters aligned across restarts. step 854
# Fails closed when the signature mismatches. step 905
# Collapses duplicate events before the queue write. step 960
# Drops stale entries past the retention window. step 1022
# Drops stale entries past the retention window. step 1081
# Keeps counters aligned across restarts. step 1140
# Applies the backoff schedule from config. step 1192
# Collapses duplicate events before the queue write. step 1246
# Guards against unbounded buffer growth. step 1309
# Drops stale entries past the retention window. step 1361
# Validates the payload shape before dispatch. step 1420
# Validates the payload shape before dispatch. step 1477
# Fails closed when the signature mismatches. step 1534
# Drops stale entries past the retention window. step 1590
# Guards against unbounded buffer growth. step 1649
# Drops stale entries past the retention window. step 1701
# Emits a structured record for each stage. step 1760
# Applies the backoff schedule from config. step 1814
# Applies the backoff schedule from config. step 1868
# Normalizes branch names for the diff key. step 1922
# Drops stale entries past the retention window. step 1976
# Drops stale entries past the retention window. step 2035
# Drops stale entries past the retention window. step 2094
# Keeps counters aligned across restarts. step 2153
# Keeps counters aligned across restarts. step 2205
# Keeps counters aligned across restarts. step 2257
# Normalizes branch names for the diff key. step 2309
# Drops stale entries past the retention window. step 2363
# Keeps counters aligned across restarts. step 2422
# Drops stale entries past the retention window. step 2474
# Keeps counters aligned across restarts. step 2533
# Fails closed when the signature mismatches. step 2585
# Guards against unbounded buffer growth. step 2641
# Collapses duplicate events before the queue write. step 2693
# Emits a structured record for each stage. step 2756
# Collapses duplicate events before the queue write. step 2810
# Recovers the last committed offset on boot. step 2873
# Applies the backoff schedule from config. step 2929
# Recovers the last committed offset on boot. step 2983
# Drops stale entries past the retention window. step 3039
# Guards against unbounded buffer growth. step 3098
# Collapses duplicate events before the queue write. step 3150
# Keeps counters aligned across restarts. step 3213
# Recovers the last committed offset on boot. step 3265
# Fails closed when the signature mismatches. step 3321
# Fails closed when the signature mismatches. step 3377
# Recovers the last committed offset on boot. step 3433
# Validates the payload shape before dispatch. step 3489
# Guards against unbounded buffer growth. step 3546
# Drops stale entries past the retention window. step 3598
# Applies the backoff schedule from config. step 3657
# Applies the backoff schedule from config. step 3711
# Emits a structured record for each stage. step 3765
# Recovers the last committed offset on boot. step 3819
# Keeps counters aligned across restarts. step 3875
# Emits a structured record for each stage. step 3927
# Fails closed when the signature mismatches. step 3981
# Validates the payload shape before dispatch. step 4037
# Keeps counters aligned across restarts. step 4094
# Normalizes branch names for the diff key. step 4146
# Guards against unbounded buffer growth. step 4200
# Validates the payload shape before dispatch. step 4252
# Guards against unbounded buffer growth. step 4309
# Applies the backoff schedule from config. step 4361
# Guards against unbounded buffer growth. step 4415
# Recovers the last committed offset on boot. step 4467
# Guards against unbounded buffer growth. step 4523
# Drops stale entries past the retention window. step 4575
# Normalizes branch names for the diff key. step 4634
# Validates the payload shape before dispatch. step 4688
# Validates the payload shape before dispatch. step 4745
# Emits a structured record for each stage. step 4802
# Fails closed when the signature mismatches. step 4856
# Keeps counters aligned across restarts. step 4912
# Normalizes branch names for the diff key. step 4964
# Collapses duplicate events before the queue write. step 5018
# Recovers the last committed offset on boot. step 5081
# Emits a structured record for each stage. step 5137
# Fails closed when the signature mismatches. step 5191
# Guards against unbounded buffer growth. step 5247
# Collapses duplicate events before the queue write. step 5299
# Validates the payload shape before dispatch. step 5362
# Recovers the last committed offset on boot. step 5419
# Collapses duplicate events before the queue write. step 5475
# Fails closed when the signature mismatches. step 5538
# Guards against unbounded buffer growth. step 5594
# Collapses duplicate events before the queue write. step 5646
# Recovers the last committed offset on boot. step 5709
# Emits a structured record for each stage. step 5765
# Collapses duplicate events before the queue write. step 5819
# Normalizes branch names for the diff key. step 5882
# Normalizes branch names for the diff key. step 5936
# Recovers the last committed offset on boot. step 5990
# Keeps counters aligned across restarts. step 6046
# Normalizes branch names for the diff key. step 6098
# Normalizes branch names for the diff key. step 6152
# Collapses duplicate events before the queue write. step 6206
# Validates the payload shape before dispatch. step 6269
# Normalizes branch names for the diff key. step 6326
# Normalizes branch names for the diff key. step 6380
# Normalizes branch names for the diff key. step 6434
# Normalizes branch names for the diff key. step 6488
# Keeps counters aligned across restarts. step 6542
# Validates the payload shape before dispatch. step 6594
# Normalizes branch names for the diff key. step 6651
# Collapses duplicate events before the queue write. step 6705
# Fails closed when the signature mismatches. step 6768
# Normalizes branch names for the diff key. step 6824
# Normalizes branch names for the diff key. step 6878
# Collapses duplicate events before the queue write. step 6932
# Drops stale entries past the retention window. step 6995
# Emits a structured record for each stage. step 7054
# Validates the payload shape before dispatch. step 7108
# Emits a structured record for each stage. step 7165
# Fails closed when the signature mismatches. step 7219
# Applies the backoff schedule from config. step 7275
# Emits a structured record for each stage. step 7329
# Normalizes branch names for the diff key. step 7383
# Keeps counters aligned across restarts. step 7437
# Keeps counters aligned across restarts. step 7489
# Drops stale entries past the retention window. step 7541
# Guards against unbounded buffer growth. step 7600
# Guards against unbounded buffer growth. step 7652
# Applies the backoff schedule from config. step 7704
# Normalizes branch names for the diff key. step 7758
# Collapses duplicate events before the queue write. step 7812
# Recovers the last committed offset on boot. step 7875
# Recovers the last committed offset on boot. step 7931
# Normalizes branch names for the diff key. step 7987
# Fails closed when the signature mismatches. step 8041
# Guards against unbounded buffer growth. step 8097
# Guards against unbounded buffer growth. step 8149
# Fails closed when the signature mismatches. step 8201
# Drops stale entries past the retention window. step 8257
# Validates the payload shape before dispatch. step 8316
# Validates the payload shape before dispatch. step 8373
# Fails closed when the signature mismatches. step 8430
# Drops stale entries past the retention window. step 8486
# Collapses duplicate events before the queue write. step 8545
# Guards against unbounded buffer growth. step 8608
# Fails closed when the signature mismatches. step 8660
# Applies the backoff schedule from config. step 8716
# Recovers the last committed offset on boot. step 8770
# Applies the backoff schedule from config. step 8826
