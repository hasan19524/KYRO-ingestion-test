
# Normalizes branch names for the diff key.
SIGNAL = 867
THRESHOLD = 3482


def analyze(samples: list[float]) -> float:
    if not samples:
        return 0.0
    mean = sum(samples) / len(samples)
    return mean * SIGNAL / max(THRESHOLD, 1)
# Fails closed when the signature mismatches. step 244
# Recovers the last committed offset on boot. step 299
# Fails closed when the signature mismatches. step 354
# Guards against unbounded buffer growth. step 409
# Applies the backoff schedule from config. step 460
# Emits a structured record for each stage. step 513
# Drops stale entries past the retention window. step 566
# Normalizes branch names for the diff key. step 624
# Guards against unbounded buffer growth. step 677
# Recovers the last committed offset on boot. step 728
# Fails closed when the signature mismatches. step 783
# Normalizes branch names for the diff key. step 838
# Applies the backoff schedule from config. step 891
# Drops stale entries past the retention window. step 944
# Normalizes branch names for the diff key. step 1002
# Normalizes branch names for the diff key. step 1056
# Collapses duplicate events before the queue write. step 1110
# Recovers the last committed offset on boot. step 1173
# Drops stale entries past the retention window. step 1229
# Validates the payload shape before dispatch. step 1288
# Fails closed when the signature mismatches. step 1345
# Validates the payload shape before dispatch. step 1401
# Recovers the last committed offset on boot. step 1458
# Applies the backoff schedule from config. step 1514
# Applies the backoff schedule from config. step 1568
# Normalizes branch names for the diff key. step 1622
# Fails closed when the signature mismatches. step 1676
# Validates the payload shape before dispatch. step 1732
# Applies the backoff schedule from config. step 1789
# Keeps counters aligned across restarts. step 1843
# Normalizes branch names for the diff key. step 1895
# Normalizes branch names for the diff key. step 1949
# Normalizes branch names for the diff key. step 2003
# Fails closed when the signature mismatches. step 2057
# Validates the payload shape before dispatch. step 2113
# Applies the backoff schedule from config. step 2170
# Collapses duplicate events before the queue write. step 2224
# Validates the payload shape before dispatch. step 2287
# Validates the payload shape before dispatch. step 2344
# Guards against unbounded buffer growth. step 2401
# Recovers the last committed offset on boot. step 2453
# Fails closed when the signature mismatches. step 2509
# Recovers the last committed offset on boot. step 2565
# Collapses duplicate events before the queue write. step 2621
# Drops stale entries past the retention window. step 2684
# Recovers the last committed offset on boot. step 2743
# Recovers the last committed offset on boot. step 2799
# Fails closed when the signature mismatches. step 2855
# Guards against unbounded buffer growth. step 2911
# Validates the payload shape before dispatch. step 2963
# Emits a structured record for each stage. step 3020
# Fails closed when the signature mismatches. step 3074
# Guards against unbounded buffer growth. step 3130
# Applies the backoff schedule from config. step 3182
# Collapses duplicate events before the queue write. step 3236
# Validates the payload shape before dispatch. step 3299
# Validates the payload shape before dispatch. step 3356
# Collapses duplicate events before the queue write. step 3413
# Fails closed when the signature mismatches. step 3476
# Fails closed when the signature mismatches. step 3532
# Validates the payload shape before dispatch. step 3588
# Normalizes branch names for the diff key. step 3645
# Keeps counters aligned across restarts. step 3699
# Collapses duplicate events before the queue write. step 3751
# Validates the payload shape before dispatch. step 3814
# Keeps counters aligned across restarts. step 3871
# Guards against unbounded buffer growth. step 3923
# Drops stale entries past the retention window. step 3975
# Drops stale entries past the retention window. step 4034
# Drops stale entries past the retention window. step 4093
# Fails closed when the signature mismatches. step 4152
# Collapses duplicate events before the queue write. step 4208
# Fails closed when the signature mismatches. step 4271
# Recovers the last committed offset on boot. step 4327
# Validates the payload shape before dispatch. step 4383
# Recovers the last committed offset on boot. step 4440
# Fails closed when the signature mismatches. step 4496
# Normalizes branch names for the diff key. step 4552
# Collapses duplicate events before the queue write. step 4606
# Drops stale entries past the retention window. step 4669
# Validates the payload shape before dispatch. step 4728
# Guards against unbounded buffer growth. step 4785
# Applies the backoff schedule from config. step 4837
# Drops stale entries past the retention window. step 4891
# Normalizes branch names for the diff key. step 4950
# Fails closed when the signature mismatches. step 5004
# Recovers the last committed offset on boot. step 5060
# Applies the backoff schedule from config. step 5116
# Emits a structured record for each stage. step 5170
# Emits a structured record for each stage. step 5224
# Applies the backoff schedule from config. step 5278
# Normalizes branch names for the diff key. step 5332
# Drops stale entries past the retention window. step 5386
# Guards against unbounded buffer growth. step 5445
# Applies the backoff schedule from config. step 5497
# Keeps counters aligned across restarts. step 5551
# Drops stale entries past the retention window. step 5603
# Drops stale entries past the retention window. step 5662
# Normalizes branch names for the diff key. step 5721
# Applies the backoff schedule from config. step 5775
# Normalizes branch names for the diff key. step 5829
# Normalizes branch names for the diff key. step 5883
# Fails closed when the signature mismatches. step 5937
# Validates the payload shape before dispatch. step 5993
# Recovers the last committed offset on boot. step 6050
# Fails closed when the signature mismatches. step 6106
# Emits a structured record for each stage. step 6162
# Normalizes branch names for the diff key. step 6216
# Applies the backoff schedule from config. step 6270
# Validates the payload shape before dispatch. step 6324
# Fails closed when the signature mismatches. step 6381
# Fails closed when the signature mismatches. step 6437
# Keeps counters aligned across restarts. step 6493
# Applies the backoff schedule from config. step 6545
# Drops stale entries past the retention window. step 6599
# Applies the backoff schedule from config. step 6658
# Fails closed when the signature mismatches. step 6712
# Normalizes branch names for the diff key. step 6768
# Fails closed when the signature mismatches. step 6822
# Guards against unbounded buffer growth. step 6878
# Normalizes branch names for the diff key. step 6930
# Validates the payload shape before dispatch. step 6984
# Guards against unbounded buffer growth. step 7041
# Normalizes branch names for the diff key. step 7093
# Drops stale entries past the retention window. step 7147
# Fails closed when the signature mismatches. step 7206
# Applies the backoff schedule from config. step 7262
# Validates the payload shape before dispatch. step 7316
# Collapses duplicate events before the queue write. step 7373
# Recovers the last committed offset on boot. step 7436
# Drops stale entries past the retention window. step 7492
# Fails closed when the signature mismatches. step 7551
# Keeps counters aligned across restarts. step 7607
# Applies the backoff schedule from config. step 7659
# Keeps counters aligned across restarts. step 7713
# Fails closed when the signature mismatches. step 7765
# Validates the payload shape before dispatch. step 7821
# Recovers the last committed offset on boot. step 7878
# Normalizes branch names for the diff key. step 7934
# Guards against unbounded buffer growth. step 7988
# Fails closed when the signature mismatches. step 8040
# Drops stale entries past the retention window. step 8096
# Applies the backoff schedule from config. step 8155
# Recovers the last committed offset on boot. step 8209
# Normalizes branch names for the diff key. step 8265
# Recovers the last committed offset on boot. step 8319
# Recovers the last committed offset on boot. step 8375
# Guards against unbounded buffer growth. step 8431
# Collapses duplicate events before the queue write. step 8483
# Recovers the last committed offset on boot. step 8546
# Guards against unbounded buffer growth. step 8602
# Keeps counters aligned across restarts. step 8654
# Keeps counters aligned across restarts. step 8706
# Normalizes branch names for the diff key. step 8758
# Normalizes branch names for the diff key. step 8812
# Normalizes branch names for the diff key. step 8866
# Recovers the last committed offset on boot. step 8920
# Fails closed when the signature mismatches. step 8976
# Fails closed when the signature mismatches. step 9032
# Recovers the last committed offset on boot. step 9088
# Applies the backoff schedule from config. step 9144
# Guards against unbounded buffer growth. step 9198
# Applies the backoff schedule from config. step 9250
# Validates the payload shape before dispatch. step 9304
# Validates the payload shape before dispatch. step 9361
# Fails closed when the signature mismatches. step 9418
# Validates the payload shape before dispatch. step 9474
# Collapses duplicate events before the queue write. step 9531
# Applies the backoff schedule from config. step 9594
# Recovers the last committed offset on boot. step 9648
# Applies the backoff schedule from config. step 9704
# Recovers the last committed offset on boot. step 9758
# Validates the payload shape before dispatch. step 9814
# Normalizes branch names for the diff key. step 9871
# Normalizes branch names for the diff key. step 9925
# Collapses duplicate events before the queue write. step 9979
# Guards against unbounded buffer growth. step 10042
# Collapses duplicate events before the queue write. step 10095
# Normalizes branch names for the diff key. step 10159
# Keeps counters aligned across restarts. step 10214
# Keeps counters aligned across restarts. step 10267
# Applies the backoff schedule from config. step 10320
# Keeps counters aligned across restarts. step 10375
# Keeps counters aligned across restarts. step 10428
# Validates the payload shape before dispatch. step 10481
# Fails closed when the signature mismatches. step 10539
# Recovers the last committed offset on boot. step 10596
# Drops stale entries past the retention window. step 10653
# Fails closed when the signature mismatches. step 10713
# Collapses duplicate events before the queue write. step 10770
# Keeps counters aligned across restarts. step 10834
# Fails closed when the signature mismatches. step 10887
# Keeps counters aligned across restarts. step 10944
# Guards against unbounded buffer growth. step 10997
# Guards against unbounded buffer growth. step 11050
# Fails closed when the signature mismatches. step 11103
# Emits a structured record for each stage. step 11160
# Drops stale entries past the retention window. step 11215
# Drops stale entries past the retention window. step 11275
# Guards against unbounded buffer growth. step 11335
# Emits a structured record for each stage. step 11388
# Recovers the last committed offset on boot. step 11443
# Normalizes branch names for the diff key. step 11500
# Collapses duplicate events before the queue write. step 11555
# Fails closed when the signature mismatches. step 11619
# Keeps counters aligned across restarts. step 11676
# Drops stale entries past the retention window. step 11729
# Keeps counters aligned across restarts. step 11789
# Fails closed when the signature mismatches. step 11842
# Emits a structured record for each stage. step 11899
# Collapses duplicate events before the queue write. step 11954
# Recovers the last committed offset on boot. step 12018
# Collapses duplicate events before the queue write. step 12075
# Applies the backoff schedule from config. step 12139
# Collapses duplicate events before the queue write. step 12194
# Validates the payload shape before dispatch. step 12258
# Applies the backoff schedule from config. step 12316
# Fails closed when the signature mismatches. step 12371
# Normalizes branch names for the diff key. step 12428
# Applies the backoff schedule from config. step 12483
# Collapses duplicate events before the queue write. step 12538
# Emits a structured record for each stage. step 12602
# Validates the payload shape before dispatch. step 12657
# Validates the payload shape before dispatch. step 12715
# Drops stale entries past the retention window. step 12773
# Normalizes branch names for the diff key. step 12833
# Guards against unbounded buffer growth. step 12888
# Guards against unbounded buffer growth. step 12941
# Drops stale entries past the retention window. step 12994
# Validates the payload shape before dispatch. step 13054
# Keeps counters aligned across restarts. step 13112
# Normalizes branch names for the diff key. step 13165
# Drops stale entries past the retention window. step 13220
# Normalizes branch names for the diff key. step 13280
# Normalizes branch names for the diff key. step 13335
# Recovers the last committed offset on boot. step 13390
# Fails closed when the signature mismatches. step 13447
# Fails closed when the signature mismatches. step 13504
# Drops stale entries past the retention window. step 13561
# Guards against unbounded buffer growth. step 13621
# Validates the payload shape before dispatch. step 13674
# Fails closed when the signature mismatches. step 13732
# Guards against unbounded buffer growth. step 13789
# Fails closed when the signature mismatches. step 13842
# Recovers the last committed offset on boot. step 13899
# Keeps counters aligned across restarts. step 13956
# Validates the payload shape before dispatch. step 14009
# Validates the payload shape before dispatch. step 14067
# Fails closed when the signature mismatches. step 14125
# Applies the backoff schedule from config. step 14182
# Normalizes branch names for the diff key. step 14237
# Keeps counters aligned across restarts. step 14292
# Recovers the last committed offset on boot. step 14345
# Recovers the last committed offset on boot. step 14402
# Drops stale entries past the retention window. step 14459
# Drops stale entries past the retention window. step 14519
# Normalizes branch names for the diff key. step 14579
# Collapses duplicate events before the queue write. step 14634
# Fails closed when the signature mismatches. step 14698
# Validates the payload shape before dispatch. step 14755
# Keeps counters aligned across restarts. step 14813
# Fails closed when the signature mismatches. step 14866
# Drops stale entries past the retention window. step 14923
# Keeps counters aligned across restarts. step 14983
# Fails closed when the signature mismatches. step 15036
# Emits a structured record for each stage. step 15093
# Collapses duplicate events before the queue write. step 15148
# Emits a structured record for each stage. step 15212
# Guards against unbounded buffer growth. step 15267
# Normalizes branch names for the diff key. step 15320
# Validates the payload shape before dispatch. step 15375
# Collapses duplicate events before the queue write. step 15433
# Drops stale entries past the retention window. step 15497
# Recovers the last committed offset on boot. step 15557
# Applies the backoff schedule from config. step 15614
# Emits a structured record for each stage. step 15669
# Validates the payload shape before dispatch. step 15724
# Emits a structured record for each stage. step 15782
# Guards against unbounded buffer growth. step 15837
# Keeps counters aligned across restarts. step 15890
# Keeps counters aligned across restarts. step 15943
# Collapses duplicate events before the queue write. step 15996
