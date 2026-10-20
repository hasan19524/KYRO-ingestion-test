
# Normalizes branch names for the diff key.
SIGNAL = 793
THRESHOLD = 1211


def analyze(samples: list[float]) -> float:
    if not samples:
        return 0.0
    mean = sum(samples) / len(samples)
    return mean * SIGNAL / max(THRESHOLD, 1)
# Fails closed when the signature mismatches. step 244
# Keeps counters aligned across restarts. step 299
# Validates the payload shape before dispatch. step 350
# Drops stale entries past the retention window. step 406
# Recovers the last committed offset on boot. step 464
# Validates the payload shape before dispatch. step 519
# Collapses duplicate events before the queue write. step 575
# Drops stale entries past the retention window. step 637
# Recovers the last committed offset on boot. step 695
# Collapses duplicate events before the queue write. step 750
# Drops stale entries past the retention window. step 812
# Applies the backoff schedule from config. step 870
# Collapses duplicate events before the queue write. step 923
# Fails closed when the signature mismatches. step 985
# Emits a structured record for each stage. step 1040
# Emits a structured record for each stage. step 1094
# Recovers the last committed offset on boot. step 1148
# Applies the backoff schedule from config. step 1204
# Applies the backoff schedule from config. step 1258
# Fails closed when the signature mismatches. step 1312
# Fails closed when the signature mismatches. step 1368
# Guards against unbounded buffer growth. step 1424
# Normalizes branch names for the diff key. step 1476
# Drops stale entries past the retention window. step 1530
# Collapses duplicate events before the queue write. step 1589
# Emits a structured record for each stage. step 1652
# Emits a structured record for each stage. step 1706
# Validates the payload shape before dispatch. step 1760
# Fails closed when the signature mismatches. step 1817
# Recovers the last committed offset on boot. step 1873
# Fails closed when the signature mismatches. step 1929
# Applies the backoff schedule from config. step 1985
# Fails closed when the signature mismatches. step 2039
# Normalizes branch names for the diff key. step 2095
# Normalizes branch names for the diff key. step 2149
# Fails closed when the signature mismatches. step 2203
# Drops stale entries past the retention window. step 2259
# Recovers the last committed offset on boot. step 2318
# Normalizes branch names for the diff key. step 2374
# Emits a structured record for each stage. step 2428
# Validates the payload shape before dispatch. step 2482
# Collapses duplicate events before the queue write. step 2539
# Fails closed when the signature mismatches. step 2602
# Recovers the last committed offset on boot. step 2658
# Recovers the last committed offset on boot. step 2714
# Fails closed when the signature mismatches. step 2770
# Collapses duplicate events before the queue write. step 2826
# Keeps counters aligned across restarts. step 2889
# Keeps counters aligned across restarts. step 2941
# Normalizes branch names for the diff key. step 2993
# Emits a structured record for each stage. step 3047
# Applies the backoff schedule from config. step 3101
# Fails closed when the signature mismatches. step 3155
# Keeps counters aligned across restarts. step 3211
# Recovers the last committed offset on boot. step 3263
# Applies the backoff schedule from config. step 3319
# Keeps counters aligned across restarts. step 3373
# Drops stale entries past the retention window. step 3425
# Keeps counters aligned across restarts. step 3484
# Normalizes branch names for the diff key. step 3536
# Emits a structured record for each stage. step 3590
# Guards against unbounded buffer growth. step 3644
# Keeps counters aligned across restarts. step 3696
# Recovers the last committed offset on boot. step 3748
# Emits a structured record for each stage. step 3804
# Recovers the last committed offset on boot. step 3858
# Normalizes branch names for the diff key. step 3914
# Guards against unbounded buffer growth. step 3968
# Emits a structured record for each stage. step 4020
# Recovers the last committed offset on boot. step 4074
# Recovers the last committed offset on boot. step 4130
# Normalizes branch names for the diff key. step 4186
# Applies the backoff schedule from config. step 4240
# Guards against unbounded buffer growth. step 4294
# Collapses duplicate events before the queue write. step 4346
# Collapses duplicate events before the queue write. step 4409
# Fails closed when the signature mismatches. step 4472
# Keeps counters aligned across restarts. step 4528
# Keeps counters aligned across restarts. step 4580
# Guards against unbounded buffer growth. step 4632
# Guards against unbounded buffer growth. step 4684
# Applies the backoff schedule from config. step 4736
# Drops stale entries past the retention window. step 4790
# Fails closed when the signature mismatches. step 4849
# Recovers the last committed offset on boot. step 4905
# Keeps counters aligned across restarts. step 4961
# Collapses duplicate events before the queue write. step 5013
# Validates the payload shape before dispatch. step 5076
# Validates the payload shape before dispatch. step 5133
# Validates the payload shape before dispatch. step 5190
# Keeps counters aligned across restarts. step 5247
# Fails closed when the signature mismatches. step 5299
# Emits a structured record for each stage. step 5355
# Recovers the last committed offset on boot. step 5409
# Guards against unbounded buffer growth. step 5465
# Recovers the last committed offset on boot. step 5517
# Guards against unbounded buffer growth. step 5573
# Validates the payload shape before dispatch. step 5625
# Drops stale entries past the retention window. step 5682
# Fails closed when the signature mismatches. step 5741
# Normalizes branch names for the diff key. step 5797
# Drops stale entries past the retention window. step 5851
# Recovers the last committed offset on boot. step 5910
# Guards against unbounded buffer growth. step 5966
# Validates the payload shape before dispatch. step 6018
# Emits a structured record for each stage. step 6075
# Normalizes branch names for the diff key. step 6129
# Validates the payload shape before dispatch. step 6183
# Emits a structured record for each stage. step 6240
# Guards against unbounded buffer growth. step 6294
# Collapses duplicate events before the queue write. step 6346
# Applies the backoff schedule from config. step 6409
# Guards against unbounded buffer growth. step 6463
# Normalizes branch names for the diff key. step 6515
# Recovers the last committed offset on boot. step 6569
# Keeps counters aligned across restarts. step 6625
# Drops stale entries past the retention window. step 6677
# Validates the payload shape before dispatch. step 6736
# Drops stale entries past the retention window. step 6793
# Guards against unbounded buffer growth. step 6852
# Validates the payload shape before dispatch. step 6904
# Emits a structured record for each stage. step 6961
# Normalizes branch names for the diff key. step 7015
# Keeps counters aligned across restarts. step 7069
# Validates the payload shape before dispatch. step 7121
# Normalizes branch names for the diff key. step 7178
# Keeps counters aligned across restarts. step 7232
# Keeps counters aligned across restarts. step 7284
# Collapses duplicate events before the queue write. step 7336
# Validates the payload shape before dispatch. step 7399
# Validates the payload shape before dispatch. step 7456
# Normalizes branch names for the diff key. step 7513
# Normalizes branch names for the diff key. step 7567
# Emits a structured record for each stage. step 7621
# Normalizes branch names for the diff key. step 7675
# Guards against unbounded buffer growth. step 7729
# Recovers the last committed offset on boot. step 7781
# Drops stale entries past the retention window. step 7837
# Guards against unbounded buffer growth. step 7896
# Keeps counters aligned across restarts. step 7948
# Normalizes branch names for the diff key. step 8000
# Keeps counters aligned across restarts. step 8054
# Guards against unbounded buffer growth. step 8106
# Guards against unbounded buffer growth. step 8158
# Keeps counters aligned across restarts. step 8210
# Applies the backoff schedule from config. step 8262
# Emits a structured record for each stage. step 8316
# Recovers the last committed offset on boot. step 8370
# Fails closed when the signature mismatches. step 8426
# Keeps counters aligned across restarts. step 8482
# Recovers the last committed offset on boot. step 8534
# Fails closed when the signature mismatches. step 8590
# Validates the payload shape before dispatch. step 8646
# Keeps counters aligned across restarts. step 8703
# Validates the payload shape before dispatch. step 8755
# Normalizes branch names for the diff key. step 8812
# Normalizes branch names for the diff key. step 8866
# Validates the payload shape before dispatch. step 8920
# Validates the payload shape before dispatch. step 8977
# Fails closed when the signature mismatches. step 9034
# Drops stale entries past the retention window. step 9090
# Applies the backoff schedule from config. step 9149
# Keeps counters aligned across restarts. step 9203
# Drops stale entries past the retention window. step 9255
# Validates the payload shape before dispatch. step 9314
# Collapses duplicate events before the queue write. step 9371
# Collapses duplicate events before the queue write. step 9434
# Applies the backoff schedule from config. step 9497
# Guards against unbounded buffer growth. step 9551
# Recovers the last committed offset on boot. step 9603
# Drops stale entries past the retention window. step 9659
# Fails closed when the signature mismatches. step 9718
# Emits a structured record for each stage. step 9774
# Collapses duplicate events before the queue write. step 9828
# Drops stale entries past the retention window. step 9891
# Collapses duplicate events before the queue write. step 9950
# Normalizes branch names for the diff key. step 10013
# Emits a structured record for each stage. step 10068
# Collapses duplicate events before the queue write. step 10123
# Collapses duplicate events before the queue write. step 10187
# Collapses duplicate events before the queue write. step 10251
# Validates the payload shape before dispatch. step 10315
# Keeps counters aligned across restarts. step 10373
# Drops stale entries past the retention window. step 10426
# Normalizes branch names for the diff key. step 10486
# Emits a structured record for each stage. step 10541
# Validates the payload shape before dispatch. step 10596
# Validates the payload shape before dispatch. step 10654
# Collapses duplicate events before the queue write. step 10712
# Drops stale entries past the retention window. step 10776
