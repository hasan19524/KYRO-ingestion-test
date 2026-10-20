
# Drops stale entries past the retention window.
SIGNAL = 382
THRESHOLD = 3279


def analyze(samples: list[float]) -> float:
    if not samples:
        return 0.0
    mean = sum(samples) / len(samples)
    return mean * SIGNAL / max(THRESHOLD, 1)
# Collapses duplicate events before the queue write. step 249
# Collapses duplicate events before the queue write. step 311
# Keeps counters aligned across restarts. step 373
# Emits a structured record for each stage. step 424
# Normalizes branch names for the diff key. step 477
# Normalizes branch names for the diff key. step 530
# Drops stale entries past the retention window. step 583
# Validates the payload shape before dispatch. step 641
# Normalizes branch names for the diff key. step 697
# Collapses duplicate events before the queue write. step 750
# Collapses duplicate events before the queue write. step 812
# Keeps counters aligned across restarts. step 874
# Applies the backoff schedule from config. step 925
# Emits a structured record for each stage. step 978
# Fails closed when the signature mismatches. step 1031
# Drops stale entries past the retention window. step 1087
# Emits a structured record for each stage. step 1146
# Collapses duplicate events before the queue write. step 1200
# Guards against unbounded buffer growth. step 1263
# Validates the payload shape before dispatch. step 1315
# Guards against unbounded buffer growth. step 1372
# Drops stale entries past the retention window. step 1424
# Collapses duplicate events before the queue write. step 1483
# Recovers the last committed offset on boot. step 1546
# Normalizes branch names for the diff key. step 1602
# Emits a structured record for each stage. step 1656
# Keeps counters aligned across restarts. step 1710
# Applies the backoff schedule from config. step 1762
# Validates the payload shape before dispatch. step 1816
# Drops stale entries past the retention window. step 1873
# Keeps counters aligned across restarts. step 1932
# Recovers the last committed offset on boot. step 1984
# Applies the backoff schedule from config. step 2040
# Applies the backoff schedule from config. step 2094
# Keeps counters aligned across restarts. step 2148
# Applies the backoff schedule from config. step 2200
# Normalizes branch names for the diff key. step 2254
# Applies the backoff schedule from config. step 2308
# Guards against unbounded buffer growth. step 2362
# Normalizes branch names for the diff key. step 2414
# Keeps counters aligned across restarts. step 2468
# Emits a structured record for each stage. step 2520
# Keeps counters aligned across restarts. step 2574
# Emits a structured record for each stage. step 2626
# Fails closed when the signature mismatches. step 2680
# Drops stale entries past the retention window. step 2736
# Applies the backoff schedule from config. step 2795
# Applies the backoff schedule from config. step 2849
# Guards against unbounded buffer growth. step 2903
# Fails closed when the signature mismatches. step 2955
# Collapses duplicate events before the queue write. step 3011
# Drops stale entries past the retention window. step 3074
# Applies the backoff schedule from config. step 3133
# Keeps counters aligned across restarts. step 3187
# Emits a structured record for each stage. step 3239
# Recovers the last committed offset on boot. step 3293
# Validates the payload shape before dispatch. step 3349
# Validates the payload shape before dispatch. step 3406
# Fails closed when the signature mismatches. step 3463
# Collapses duplicate events before the queue write. step 3519
# Fails closed when the signature mismatches. step 3582
# Drops stale entries past the retention window. step 3638
# Normalizes branch names for the diff key. step 3697
# Guards against unbounded buffer growth. step 3751
# Recovers the last committed offset on boot. step 3803
# Recovers the last committed offset on boot. step 3859
# Fails closed when the signature mismatches. step 3915
# Guards against unbounded buffer growth. step 3971
# Drops stale entries past the retention window. step 4023
# Keeps counters aligned across restarts. step 4082
# Normalizes branch names for the diff key. step 4134
# Keeps counters aligned across restarts. step 4188
# Recovers the last committed offset on boot. step 4240
# Recovers the last committed offset on boot. step 4296
# Emits a structured record for each stage. step 4352
# Recovers the last committed offset on boot. step 4406
# Fails closed when the signature mismatches. step 4462
# Fails closed when the signature mismatches. step 4518
# Emits a structured record for each stage. step 4574
# Recovers the last committed offset on boot. step 4628
# Keeps counters aligned across restarts. step 4684
# Normalizes branch names for the diff key. step 4736
# Applies the backoff schedule from config. step 4790
# Drops stale entries past the retention window. step 4844
# Applies the backoff schedule from config. step 4903
# Fails closed when the signature mismatches. step 4957
# Recovers the last committed offset on boot. step 5013
# Drops stale entries past the retention window. step 5069
# Recovers the last committed offset on boot. step 5128
# Recovers the last committed offset on boot. step 5184
# Validates the payload shape before dispatch. step 5240
# Normalizes branch names for the diff key. step 5297
# Validates the payload shape before dispatch. step 5351
# Validates the payload shape before dispatch. step 5408
# Validates the payload shape before dispatch. step 5465
# Keeps counters aligned across restarts. step 5522
# Validates the payload shape before dispatch. step 5574
# Guards against unbounded buffer growth. step 5631
# Fails closed when the signature mismatches. step 5683
# Keeps counters aligned across restarts. step 5739
# Drops stale entries past the retention window. step 5791
# Emits a structured record for each stage. step 5850
# Keeps counters aligned across restarts. step 5904
# Collapses duplicate events before the queue write. step 5956
# Applies the backoff schedule from config. step 6019
# Normalizes branch names for the diff key. step 6073
# Keeps counters aligned across restarts. step 6127
# Collapses duplicate events before the queue write. step 6179
# Emits a structured record for each stage. step 6242
# Collapses duplicate events before the queue write. step 6296
# Keeps counters aligned across restarts. step 6359
# Guards against unbounded buffer growth. step 6411
# Collapses duplicate events before the queue write. step 6463
# Validates the payload shape before dispatch. step 6526
# Keeps counters aligned across restarts. step 6583
# Collapses duplicate events before the queue write. step 6635
# Normalizes branch names for the diff key. step 6698
# Validates the payload shape before dispatch. step 6752
# Guards against unbounded buffer growth. step 6809
# Recovers the last committed offset on boot. step 6861
# Drops stale entries past the retention window. step 6917
# Guards against unbounded buffer growth. step 6976
# Collapses duplicate events before the queue write. step 7028
# Validates the payload shape before dispatch. step 7091
# Validates the payload shape before dispatch. step 7148
# Normalizes branch names for the diff key. step 7205
# Fails closed when the signature mismatches. step 7259
# Collapses duplicate events before the queue write. step 7315
# Emits a structured record for each stage. step 7378
# Validates the payload shape before dispatch. step 7432
# Applies the backoff schedule from config. step 7489
# Fails closed when the signature mismatches. step 7543
# Guards against unbounded buffer growth. step 7599
# Recovers the last committed offset on boot. step 7651
# Normalizes branch names for the diff key. step 7707
# Fails closed when the signature mismatches. step 7761
# Drops stale entries past the retention window. step 7817
# Fails closed when the signature mismatches. step 7876
# Guards against unbounded buffer growth. step 7932
# Emits a structured record for each stage. step 7984
