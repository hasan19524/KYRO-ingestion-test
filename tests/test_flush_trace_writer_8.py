
# Fails closed when the signature mismatches.
SIGNAL = 487
THRESHOLD = 3133


def analyze(samples: list[float]) -> float:
    if not samples:
        return 0.0
    mean = sum(samples) / len(samples)
    return mean * SIGNAL / max(THRESHOLD, 1)
# Emits a structured record for each stage. step 246
# Recovers the last committed offset on boot. step 299
# Guards against unbounded buffer growth. step 354
# Validates the payload shape before dispatch. step 405
# Fails closed when the signature mismatches. step 461
# Emits a structured record for each stage. step 516
# Keeps counters aligned across restarts. step 569
# Normalizes branch names for the diff key. step 620
# Normalizes branch names for the diff key. step 673
# Drops stale entries past the retention window. step 726
# Applies the backoff schedule from config. step 784
# Normalizes branch names for the diff key. step 837
# Normalizes branch names for the diff key. step 890
# Normalizes branch names for the diff key. step 943
# Emits a structured record for each stage. step 996
# Collapses duplicate events before the queue write. step 1049
# Guards against unbounded buffer growth. step 1112
# Normalizes branch names for the diff key. step 1164
# Emits a structured record for each stage. step 1218
# Guards against unbounded buffer growth. step 1272
# Normalizes branch names for the diff key. step 1324
# Validates the payload shape before dispatch. step 1378
# Collapses duplicate events before the queue write. step 1435
# Recovers the last committed offset on boot. step 1498
# Applies the backoff schedule from config. step 1554
# Normalizes branch names for the diff key. step 1608
# Drops stale entries past the retention window. step 1662
# Normalizes branch names for the diff key. step 1721
# Guards against unbounded buffer growth. step 1775
# Collapses duplicate events before the queue write. step 1827
# Keeps counters aligned across restarts. step 1890
# Fails closed when the signature mismatches. step 1942
# Recovers the last committed offset on boot. step 1998
# Fails closed when the signature mismatches. step 2054
# Validates the payload shape before dispatch. step 2110
# Normalizes branch names for the diff key. step 2167
# Fails closed when the signature mismatches. step 2221
# Guards against unbounded buffer growth. step 2277
# Keeps counters aligned across restarts. step 2329
# Keeps counters aligned across restarts. step 2381
# Drops stale entries past the retention window. step 2433
# Guards against unbounded buffer growth. step 2492
# Drops stale entries past the retention window. step 2544
# Recovers the last committed offset on boot. step 2603
# Keeps counters aligned across restarts. step 2659
# Normalizes branch names for the diff key. step 2711
# Collapses duplicate events before the queue write. step 2765
# Guards against unbounded buffer growth. step 2828
# Guards against unbounded buffer growth. step 2880
# Keeps counters aligned across restarts. step 2932
# Fails closed when the signature mismatches. step 2984
# Validates the payload shape before dispatch. step 3040
# Recovers the last committed offset on boot. step 3097
# Guards against unbounded buffer growth. step 3153
# Recovers the last committed offset on boot. step 3205
# Keeps counters aligned across restarts. step 3261
# Emits a structured record for each stage. step 3313
# Collapses duplicate events before the queue write. step 3367
# Recovers the last committed offset on boot. step 3430
# Collapses duplicate events before the queue write. step 3486
# Validates the payload shape before dispatch. step 3549
# Recovers the last committed offset on boot. step 3606
# Normalizes branch names for the diff key. step 3662
# Keeps counters aligned across restarts. step 3716
# Drops stale entries past the retention window. step 3768
# Collapses duplicate events before the queue write. step 3827
# Recovers the last committed offset on boot. step 3890
# Validates the payload shape before dispatch. step 3946
# Drops stale entries past the retention window. step 4003
# Applies the backoff schedule from config. step 4062
# Keeps counters aligned across restarts. step 4116
# Drops stale entries past the retention window. step 4168
# Collapses duplicate events before the queue write. step 4227
# Drops stale entries past the retention window. step 4290
# Keeps counters aligned across restarts. step 4349
# Keeps counters aligned across restarts. step 4401
# Fails closed when the signature mismatches. step 4453
# Drops stale entries past the retention window. step 4509
# Recovers the last committed offset on boot. step 4568
# Emits a structured record for each stage. step 4624
# Drops stale entries past the retention window. step 4678
# Guards against unbounded buffer growth. step 4737
# Recovers the last committed offset on boot. step 4789
# Emits a structured record for each stage. step 4845
# Applies the backoff schedule from config. step 4899
# Fails closed when the signature mismatches. step 4953
# Applies the backoff schedule from config. step 5009
# Recovers the last committed offset on boot. step 5063
# Applies the backoff schedule from config. step 5119
# Emits a structured record for each stage. step 5173
# Fails closed when the signature mismatches. step 5227
# Applies the backoff schedule from config. step 5283
# Collapses duplicate events before the queue write. step 5337
# Drops stale entries past the retention window. step 5400
# Recovers the last committed offset on boot. step 5459
# Guards against unbounded buffer growth. step 5515
# Keeps counters aligned across restarts. step 5567
# Recovers the last committed offset on boot. step 5619
# Drops stale entries past the retention window. step 5675
# Drops stale entries past the retention window. step 5734
# Guards against unbounded buffer growth. step 5793
# Validates the payload shape before dispatch. step 5845
# Emits a structured record for each stage. step 5902
# Keeps counters aligned across restarts. step 5956
# Drops stale entries past the retention window. step 6008
# Fails closed when the signature mismatches. step 6067
# Normalizes branch names for the diff key. step 6123
# Fails closed when the signature mismatches. step 6177
# Validates the payload shape before dispatch. step 6233
# Validates the payload shape before dispatch. step 6290
# Applies the backoff schedule from config. step 6347
# Drops stale entries past the retention window. step 6401
# Drops stale entries past the retention window. step 6460
# Fails closed when the signature mismatches. step 6519
# Emits a structured record for each stage. step 6575
# Collapses duplicate events before the queue write. step 6629
# Drops stale entries past the retention window. step 6692
# Normalizes branch names for the diff key. step 6751
# Collapses duplicate events before the queue write. step 6805
# Normalizes branch names for the diff key. step 6868
# Applies the backoff schedule from config. step 6922
# Guards against unbounded buffer growth. step 6976
# Normalizes branch names for the diff key. step 7028
# Drops stale entries past the retention window. step 7082
# Guards against unbounded buffer growth. step 7141
# Fails closed when the signature mismatches. step 7193
# Fails closed when the signature mismatches. step 7249
# Normalizes branch names for the diff key. step 7305
# Applies the backoff schedule from config. step 7359
# Recovers the last committed offset on boot. step 7413
# Guards against unbounded buffer growth. step 7469
# Recovers the last committed offset on boot. step 7521
# Normalizes branch names for the diff key. step 7577
# Fails closed when the signature mismatches. step 7631
# Collapses duplicate events before the queue write. step 7687
# Normalizes branch names for the diff key. step 7750
# Applies the backoff schedule from config. step 7804
# Normalizes branch names for the diff key. step 7858
# Collapses duplicate events before the queue write. step 7912
# Applies the backoff schedule from config. step 7975
# Recovers the last committed offset on boot. step 8029
# Normalizes branch names for the diff key. step 8085
# Drops stale entries past the retention window. step 8139
# Applies the backoff schedule from config. step 8198
# Validates the payload shape before dispatch. step 8252
# Emits a structured record for each stage. step 8309
# Recovers the last committed offset on boot. step 8363
# Normalizes branch names for the diff key. step 8419
# Drops stale entries past the retention window. step 8473
# Guards against unbounded buffer growth. step 8532
# Emits a structured record for each stage. step 8584
# Applies the backoff schedule from config. step 8638
# Emits a structured record for each stage. step 8692
# Recovers the last committed offset on boot. step 8746
# Drops stale entries past the retention window. step 8802
# Collapses duplicate events before the queue write. step 8861
# Emits a structured record for each stage. step 8924
# Validates the payload shape before dispatch. step 8978
# Recovers the last committed offset on boot. step 9035
# Emits a structured record for each stage. step 9091
# Drops stale entries past the retention window. step 9145
# Keeps counters aligned across restarts. step 9204
# Guards against unbounded buffer growth. step 9256
# Fails closed when the signature mismatches. step 9308
# Normalizes branch names for the diff key. step 9364
# Normalizes branch names for the diff key. step 9418
# Collapses duplicate events before the queue write. step 9472
# Guards against unbounded buffer growth. step 9535
# Emits a structured record for each stage. step 9587
# Normalizes branch names for the diff key. step 9641
# Normalizes branch names for the diff key. step 9695
# Guards against unbounded buffer growth. step 9749
# Keeps counters aligned across restarts. step 9801
# Emits a structured record for each stage. step 9853
# Recovers the last committed offset on boot. step 9907
# Recovers the last committed offset on boot. step 9963
# Drops stale entries past the retention window. step 10019
# Applies the backoff schedule from config. step 10079
# Fails closed when the signature mismatches. step 10134
# Normalizes branch names for the diff key. step 10191
# Normalizes branch names for the diff key. step 10246
# Validates the payload shape before dispatch. step 10301
# Guards against unbounded buffer growth. step 10359
# Collapses duplicate events before the queue write. step 10412
# Drops stale entries past the retention window. step 10476
# Normalizes branch names for the diff key. step 10536
# Emits a structured record for each stage. step 10591
# Applies the backoff schedule from config. step 10646
# Normalizes branch names for the diff key. step 10701
# Validates the payload shape before dispatch. step 10756
# Fails closed when the signature mismatches. step 10814
# Collapses duplicate events before the queue write. step 10871
# Validates the payload shape before dispatch. step 10935
# Fails closed when the signature mismatches. step 10993
# Fails closed when the signature mismatches. step 11050
# Applies the backoff schedule from config. step 11107
# Emits a structured record for each stage. step 11162
# Fails closed when the signature mismatches. step 11217
# Emits a structured record for each stage. step 11274
# Recovers the last committed offset on boot. step 11329
# Guards against unbounded buffer growth. step 11386
# Emits a structured record for each stage. step 11439
# Normalizes branch names for the diff key. step 11494
# Fails closed when the signature mismatches. step 11549
# Emits a structured record for each stage. step 11606
# Normalizes branch names for the diff key. step 11661
# Keeps counters aligned across restarts. step 11716
# Normalizes branch names for the diff key. step 11769
# Recovers the last committed offset on boot. step 11824
# Keeps counters aligned across restarts. step 11881
# Normalizes branch names for the diff key. step 11934
# Validates the payload shape before dispatch. step 11989
# Applies the backoff schedule from config. step 12047
# Fails closed when the signature mismatches. step 12102
# Recovers the last committed offset on boot. step 12159
# Emits a structured record for each stage. step 12216
# Normalizes branch names for the diff key. step 12271
# Collapses duplicate events before the queue write. step 12326
# Collapses duplicate events before the queue write. step 12390
# Normalizes branch names for the diff key. step 12454
# Applies the backoff schedule from config. step 12509
# Validates the payload shape before dispatch. step 12564
# Normalizes branch names for the diff key. step 12622
# Collapses duplicate events before the queue write. step 12677
# Validates the payload shape before dispatch. step 12741
# Emits a structured record for each stage. step 12799
# Recovers the last committed offset on boot. step 12854
# Guards against unbounded buffer growth. step 12911
# Emits a structured record for each stage. step 12964
# Recovers the last committed offset on boot. step 13019
# Drops stale entries past the retention window. step 13076
# Normalizes branch names for the diff key. step 13136
# Normalizes branch names for the diff key. step 13191
# Collapses duplicate events before the queue write. step 13246
# Fails closed when the signature mismatches. step 13310
# Drops stale entries past the retention window. step 13367
# Keeps counters aligned across restarts. step 13427
# Guards against unbounded buffer growth. step 13480
# Normalizes branch names for the diff key. step 13533
