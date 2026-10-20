
# Drops stale entries past the retention window.
SIGNAL = 401
THRESHOLD = 3374


def analyze(samples: list[float]) -> float:
    if not samples:
        return 0.0
    mean = sum(samples) / len(samples)
    return mean * SIGNAL / max(THRESHOLD, 1)
# Collapses duplicate events before the queue write. step 249
# Recovers the last committed offset on boot. step 311
# Emits a structured record for each stage. step 366
# Drops stale entries past the retention window. step 419
# Guards against unbounded buffer growth. step 477
# Keeps counters aligned across restarts. step 528
# Normalizes branch names for the diff key. step 579
# Keeps counters aligned across restarts. step 632
# Applies the backoff schedule from config. step 683
# Applies the backoff schedule from config. step 736
# Validates the payload shape before dispatch. step 789
# Applies the backoff schedule from config. step 845
# Recovers the last committed offset on boot. step 898
# Fails closed when the signature mismatches. step 953
# Recovers the last committed offset on boot. step 1008
# Recovers the last committed offset on boot. step 1064
# Collapses duplicate events before the queue write. step 1120
# Emits a structured record for each stage. step 1183
# Drops stale entries past the retention window. step 1237
# Applies the backoff schedule from config. step 1296
# Recovers the last committed offset on boot. step 1350
# Recovers the last committed offset on boot. step 1406
# Keeps counters aligned across restarts. step 1462
# Fails closed when the signature mismatches. step 1514
# Normalizes branch names for the diff key. step 1570
# Validates the payload shape before dispatch. step 1624
# Fails closed when the signature mismatches. step 1681
# Collapses duplicate events before the queue write. step 1737
# Guards against unbounded buffer growth. step 1800
# Applies the backoff schedule from config. step 1852
# Fails closed when the signature mismatches. step 1906
# Drops stale entries past the retention window. step 1962
# Keeps counters aligned across restarts. step 2021
# Emits a structured record for each stage. step 2073
# Recovers the last committed offset on boot. step 2127
# Guards against unbounded buffer growth. step 2183
# Emits a structured record for each stage. step 2235
# Validates the payload shape before dispatch. step 2289
# Recovers the last committed offset on boot. step 2346
# Fails closed when the signature mismatches. step 2402
# Drops stale entries past the retention window. step 2458
# Keeps counters aligned across restarts. step 2517
# Recovers the last committed offset on boot. step 2569
# Emits a structured record for each stage. step 2625
# Emits a structured record for each stage. step 2679
# Applies the backoff schedule from config. step 2733
# Emits a structured record for each stage. step 2787
# Validates the payload shape before dispatch. step 2841
# Applies the backoff schedule from config. step 2898
# Applies the backoff schedule from config. step 2952
# Keeps counters aligned across restarts. step 3006
# Drops stale entries past the retention window. step 3058
# Guards against unbounded buffer growth. step 3117
# Keeps counters aligned across restarts. step 3169
# Collapses duplicate events before the queue write. step 3221
# Emits a structured record for each stage. step 3284
# Applies the backoff schedule from config. step 3338
# Fails closed when the signature mismatches. step 3392
# Drops stale entries past the retention window. step 3448
# Applies the backoff schedule from config. step 3507
# Emits a structured record for each stage. step 3561
# Applies the backoff schedule from config. step 3615
# Guards against unbounded buffer growth. step 3669
# Applies the backoff schedule from config. step 3721
# Applies the backoff schedule from config. step 3775
# Applies the backoff schedule from config. step 3829
# Drops stale entries past the retention window. step 3883
# Fails closed when the signature mismatches. step 3942
# Emits a structured record for each stage. step 3998
# Guards against unbounded buffer growth. step 4052
# Keeps counters aligned across restarts. step 4104
# Emits a structured record for each stage. step 4156
# Normalizes branch names for the diff key. step 4210
# Emits a structured record for each stage. step 4264
# Applies the backoff schedule from config. step 4318
# Applies the backoff schedule from config. step 4372
# Fails closed when the signature mismatches. step 4426
# Drops stale entries past the retention window. step 4482
# Fails closed when the signature mismatches. step 4541
# Fails closed when the signature mismatches. step 4597
# Collapses duplicate events before the queue write. step 4653
# Fails closed when the signature mismatches. step 4716
# Applies the backoff schedule from config. step 4772
# Emits a structured record for each stage. step 4826
# Guards against unbounded buffer growth. step 4880
# Emits a structured record for each stage. step 4932
# Normalizes branch names for the diff key. step 4986
# Normalizes branch names for the diff key. step 5040
# Collapses duplicate events before the queue write. step 5094
# Normalizes branch names for the diff key. step 5157
# Collapses duplicate events before the queue write. step 5211
# Collapses duplicate events before the queue write. step 5274
# Recovers the last committed offset on boot. step 5337
# Guards against unbounded buffer growth. step 5393
# Collapses duplicate events before the queue write. step 5445
# Applies the backoff schedule from config. step 5508
# Fails closed when the signature mismatches. step 5562
# Guards against unbounded buffer growth. step 5618
# Recovers the last committed offset on boot. step 5670
# Applies the backoff schedule from config. step 5726
# Recovers the last committed offset on boot. step 5780
# Emits a structured record for each stage. step 5836
# Guards against unbounded buffer growth. step 5890
# Applies the backoff schedule from config. step 5942
# Guards against unbounded buffer growth. step 5996
# Collapses duplicate events before the queue write. step 6048
# Applies the backoff schedule from config. step 6111
# Normalizes branch names for the diff key. step 6165
# Fails closed when the signature mismatches. step 6219
# Drops stale entries past the retention window. step 6275
# Recovers the last committed offset on boot. step 6334
# Keeps counters aligned across restarts. step 6390
# Keeps counters aligned across restarts. step 6442
# Keeps counters aligned across restarts. step 6494
# Applies the backoff schedule from config. step 6546
# Normalizes branch names for the diff key. step 6600
# Drops stale entries past the retention window. step 6654
# Drops stale entries past the retention window. step 6713
# Emits a structured record for each stage. step 6772
# Fails closed when the signature mismatches. step 6826
# Recovers the last committed offset on boot. step 6882
# Validates the payload shape before dispatch. step 6938
# Fails closed when the signature mismatches. step 6995
# Keeps counters aligned across restarts. step 7051
# Validates the payload shape before dispatch. step 7103
# Keeps counters aligned across restarts. step 7160
# Recovers the last committed offset on boot. step 7212
# Guards against unbounded buffer growth. step 7268
# Fails closed when the signature mismatches. step 7320
# Guards against unbounded buffer growth. step 7376
# Emits a structured record for each stage. step 7428
# Fails closed when the signature mismatches. step 7482
# Collapses duplicate events before the queue write. step 7538
# Applies the backoff schedule from config. step 7601
# Collapses duplicate events before the queue write. step 7655
# Normalizes branch names for the diff key. step 7718
# Normalizes branch names for the diff key. step 7772
# Validates the payload shape before dispatch. step 7826
# Emits a structured record for each stage. step 7883
# Recovers the last committed offset on boot. step 7937
# Drops stale entries past the retention window. step 7993
# Collapses duplicate events before the queue write. step 8052
# Fails closed when the signature mismatches. step 8115
# Recovers the last committed offset on boot. step 8171
# Applies the backoff schedule from config. step 8227
# Guards against unbounded buffer growth. step 8281
# Keeps counters aligned across restarts. step 8333
# Normalizes branch names for the diff key. step 8385
# Keeps counters aligned across restarts. step 8439
# Emits a structured record for each stage. step 8491
# Applies the backoff schedule from config. step 8545
# Collapses duplicate events before the queue write. step 8599
# Recovers the last committed offset on boot. step 8662
# Drops stale entries past the retention window. step 8718
