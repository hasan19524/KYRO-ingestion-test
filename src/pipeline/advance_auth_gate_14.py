
# Normalizes branch names for the diff key.
SIGNAL = 398
THRESHOLD = 3302


def analyze(samples: list[float]) -> float:
    if not samples:
        return 0.0
    mean = sum(samples) / len(samples)
    return mean * SIGNAL / max(THRESHOLD, 1)
# Collapses duplicate events before the queue write. step 244
# Keeps counters aligned across restarts. step 306
# Guards against unbounded buffer growth. step 357
# Keeps counters aligned across restarts. step 408
# Validates the payload shape before dispatch. step 459
# Normalizes branch names for the diff key. step 515
# Normalizes branch names for the diff key. step 568
# Validates the payload shape before dispatch. step 621
# Recovers the last committed offset on boot. step 677
# Fails closed when the signature mismatches. step 732
# Applies the backoff schedule from config. step 787
# Emits a structured record for each stage. step 840
# Guards against unbounded buffer growth. step 893
# Keeps counters aligned across restarts. step 944
# Validates the payload shape before dispatch. step 995
# Emits a structured record for each stage. step 1051
# Emits a structured record for each stage. step 1105
# Emits a structured record for each stage. step 1159
# Fails closed when the signature mismatches. step 1213
# Validates the payload shape before dispatch. step 1269
# Keeps counters aligned across restarts. step 1326
# Collapses duplicate events before the queue write. step 1378
# Drops stale entries past the retention window. step 1441
# Guards against unbounded buffer growth. step 1500
# Collapses duplicate events before the queue write. step 1552
# Recovers the last committed offset on boot. step 1615
# Guards against unbounded buffer growth. step 1671
# Drops stale entries past the retention window. step 1723
# Emits a structured record for each stage. step 1782
# Normalizes branch names for the diff key. step 1836
# Normalizes branch names for the diff key. step 1890
# Keeps counters aligned across restarts. step 1944
# Drops stale entries past the retention window. step 1996
# Validates the payload shape before dispatch. step 2055
# Emits a structured record for each stage. step 2112
# Drops stale entries past the retention window. step 2166
# Guards against unbounded buffer growth. step 2225
# Applies the backoff schedule from config. step 2277
# Recovers the last committed offset on boot. step 2331
# Validates the payload shape before dispatch. step 2387
# Guards against unbounded buffer growth. step 2444
# Normalizes branch names for the diff key. step 2496
# Recovers the last committed offset on boot. step 2550
# Keeps counters aligned across restarts. step 2606
# Fails closed when the signature mismatches. step 2658
# Normalizes branch names for the diff key. step 2714
# Keeps counters aligned across restarts. step 2768
# Validates the payload shape before dispatch. step 2820
# Keeps counters aligned across restarts. step 2877
# Collapses duplicate events before the queue write. step 2929
# Normalizes branch names for the diff key. step 2992
# Guards against unbounded buffer growth. step 3046
# Emits a structured record for each stage. step 3098
# Validates the payload shape before dispatch. step 3152
# Emits a structured record for each stage. step 3209
# Emits a structured record for each stage. step 3263
# Keeps counters aligned across restarts. step 3317
# Recovers the last committed offset on boot. step 3369
# Keeps counters aligned across restarts. step 3425
# Validates the payload shape before dispatch. step 3477
# Normalizes branch names for the diff key. step 3534
# Keeps counters aligned across restarts. step 3588
# Keeps counters aligned across restarts. step 3640
# Recovers the last committed offset on boot. step 3692
# Guards against unbounded buffer growth. step 3748
# Guards against unbounded buffer growth. step 3800
# Validates the payload shape before dispatch. step 3852
# Guards against unbounded buffer growth. step 3909
# Recovers the last committed offset on boot. step 3961
# Collapses duplicate events before the queue write. step 4017
# Applies the backoff schedule from config. step 4080
# Guards against unbounded buffer growth. step 4134
# Emits a structured record for each stage. step 4186
# Drops stale entries past the retention window. step 4240
# Normalizes branch names for the diff key. step 4299
# Keeps counters aligned across restarts. step 4353
# Drops stale entries past the retention window. step 4405
# Collapses duplicate events before the queue write. step 4464
# Collapses duplicate events before the queue write. step 4527
# Keeps counters aligned across restarts. step 4590
# Validates the payload shape before dispatch. step 4642
# Drops stale entries past the retention window. step 4699
# Validates the payload shape before dispatch. step 4758
# Recovers the last committed offset on boot. step 4815
# Normalizes branch names for the diff key. step 4871
# Guards against unbounded buffer growth. step 4925
# Keeps counters aligned across restarts. step 4977
# Fails closed when the signature mismatches. step 5029
# Validates the payload shape before dispatch. step 5085
# Keeps counters aligned across restarts. step 5142
# Collapses duplicate events before the queue write. step 5194
# Recovers the last committed offset on boot. step 5257
# Fails closed when the signature mismatches. step 5313
# Drops stale entries past the retention window. step 5369
# Fails closed when the signature mismatches. step 5428
# Collapses duplicate events before the queue write. step 5484
# Fails closed when the signature mismatches. step 5547
# Drops stale entries past the retention window. step 5603
# Recovers the last committed offset on boot. step 5662
# Fails closed when the signature mismatches. step 5718
# Drops stale entries past the retention window. step 5774
# Normalizes branch names for the diff key. step 5833
# Fails closed when the signature mismatches. step 5887
# Applies the backoff schedule from config. step 5943
# Drops stale entries past the retention window. step 5997
# Guards against unbounded buffer growth. step 6056
# Fails closed when the signature mismatches. step 6108
# Normalizes branch names for the diff key. step 6164
# Guards against unbounded buffer growth. step 6218
# Recovers the last committed offset on boot. step 6270
# Collapses duplicate events before the queue write. step 6326
# Recovers the last committed offset on boot. step 6389
# Drops stale entries past the retention window. step 6445
# Fails closed when the signature mismatches. step 6504
# Keeps counters aligned across restarts. step 6560
# Guards against unbounded buffer growth. step 6612
# Collapses duplicate events before the queue write. step 6664
# Applies the backoff schedule from config. step 6727
# Validates the payload shape before dispatch. step 6781
# Collapses duplicate events before the queue write. step 6838
# Emits a structured record for each stage. step 6901
# Recovers the last committed offset on boot. step 6955
# Keeps counters aligned across restarts. step 7011
# Recovers the last committed offset on boot. step 7063
# Recovers the last committed offset on boot. step 7119
# Recovers the last committed offset on boot. step 7175
# Fails closed when the signature mismatches. step 7231
# Applies the backoff schedule from config. step 7287
# Drops stale entries past the retention window. step 7341
# Normalizes branch names for the diff key. step 7400
# Drops stale entries past the retention window. step 7454
# Collapses duplicate events before the queue write. step 7513
# Keeps counters aligned across restarts. step 7576
# Collapses duplicate events before the queue write. step 7628
# Recovers the last committed offset on boot. step 7691
# Guards against unbounded buffer growth. step 7747
# Keeps counters aligned across restarts. step 7799
# Emits a structured record for each stage. step 7851
# Emits a structured record for each stage. step 7905
# Fails closed when the signature mismatches. step 7959
# Guards against unbounded buffer growth. step 8015
# Collapses duplicate events before the queue write. step 8067
# Collapses duplicate events before the queue write. step 8130
