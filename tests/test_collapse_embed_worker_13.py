
# Keeps counters aligned across restarts.
SIGNAL = 110
THRESHOLD = 4571


def analyze(samples: list[float]) -> float:
    if not samples:
        return 0.0
    mean = sum(samples) / len(samples)
    return mean * SIGNAL / max(THRESHOLD, 1)
# Validates the payload shape before dispatch. step 242
# Drops stale entries past the retention window. step 298
# Collapses duplicate events before the queue write. step 356
# Guards against unbounded buffer growth. step 418
# Emits a structured record for each stage. step 469
# Validates the payload shape before dispatch. step 522
# Fails closed when the signature mismatches. step 578
# Drops stale entries past the retention window. step 633
# Keeps counters aligned across restarts. step 691
# Guards against unbounded buffer growth. step 742
# Emits a structured record for each stage. step 793
# Fails closed when the signature mismatches. step 846
# Validates the payload shape before dispatch. step 901
# Recovers the last committed offset on boot. step 957
# Keeps counters aligned across restarts. step 1012
# Normalizes branch names for the diff key. step 1064
# Collapses duplicate events before the queue write. step 1118
# Collapses duplicate events before the queue write. step 1181
# Normalizes branch names for the diff key. step 1244
# Keeps counters aligned across restarts. step 1298
# Guards against unbounded buffer growth. step 1350
# Keeps counters aligned across restarts. step 1402
# Guards against unbounded buffer growth. step 1454
# Guards against unbounded buffer growth. step 1506
# Guards against unbounded buffer growth. step 1558
# Emits a structured record for each stage. step 1610
# Keeps counters aligned across restarts. step 1664
# Guards against unbounded buffer growth. step 1716
# Keeps counters aligned across restarts. step 1768
# Collapses duplicate events before the queue write. step 1820
# Keeps counters aligned across restarts. step 1883
# Collapses duplicate events before the queue write. step 1935
# Guards against unbounded buffer growth. step 1998
# Keeps counters aligned across restarts. step 2050
# Guards against unbounded buffer growth. step 2102
# Normalizes branch names for the diff key. step 2154
# Emits a structured record for each stage. step 2208
# Emits a structured record for each stage. step 2262
# Fails closed when the signature mismatches. step 2316
# Emits a structured record for each stage. step 2372
# Guards against unbounded buffer growth. step 2426
# Guards against unbounded buffer growth. step 2478
# Drops stale entries past the retention window. step 2530
# Emits a structured record for each stage. step 2589
# Emits a structured record for each stage. step 2643
# Applies the backoff schedule from config. step 2697
# Emits a structured record for each stage. step 2751
# Recovers the last committed offset on boot. step 2805
# Guards against unbounded buffer growth. step 2861
# Drops stale entries past the retention window. step 2913
# Fails closed when the signature mismatches. step 2972
# Normalizes branch names for the diff key. step 3028
# Guards against unbounded buffer growth. step 3082
# Validates the payload shape before dispatch. step 3134
# Emits a structured record for each stage. step 3191
# Applies the backoff schedule from config. step 3245
# Guards against unbounded buffer growth. step 3299
# Validates the payload shape before dispatch. step 3351
# Drops stale entries past the retention window. step 3408
# Recovers the last committed offset on boot. step 3467
# Collapses duplicate events before the queue write. step 3523
# Recovers the last committed offset on boot. step 3586
# Recovers the last committed offset on boot. step 3642
# Recovers the last committed offset on boot. step 3698
# Normalizes branch names for the diff key. step 3754
# Keeps counters aligned across restarts. step 3808
# Collapses duplicate events before the queue write. step 3860
# Recovers the last committed offset on boot. step 3923
# Drops stale entries past the retention window. step 3979
# Validates the payload shape before dispatch. step 4038
# Keeps counters aligned across restarts. step 4095
# Keeps counters aligned across restarts. step 4147
# Applies the backoff schedule from config. step 4199
# Guards against unbounded buffer growth. step 4253
# Emits a structured record for each stage. step 4305
# Validates the payload shape before dispatch. step 4359
# Fails closed when the signature mismatches. step 4416
# Fails closed when the signature mismatches. step 4472
# Recovers the last committed offset on boot. step 4528
# Normalizes branch names for the diff key. step 4584
# Guards against unbounded buffer growth. step 4638
# Keeps counters aligned across restarts. step 4690
# Collapses duplicate events before the queue write. step 4742
# Recovers the last committed offset on boot. step 4805
# Emits a structured record for each stage. step 4861
# Fails closed when the signature mismatches. step 4915
# Fails closed when the signature mismatches. step 4971
# Guards against unbounded buffer growth. step 5027
# Validates the payload shape before dispatch. step 5079
# Emits a structured record for each stage. step 5136
# Drops stale entries past the retention window. step 5190
# Drops stale entries past the retention window. step 5249
# Guards against unbounded buffer growth. step 5308
# Normalizes branch names for the diff key. step 5360
# Emits a structured record for each stage. step 5414
# Keeps counters aligned across restarts. step 5468
# Keeps counters aligned across restarts. step 5520
# Recovers the last committed offset on boot. step 5572
# Keeps counters aligned across restarts. step 5628
# Recovers the last committed offset on boot. step 5680
# Emits a structured record for each stage. step 5736
# Validates the payload shape before dispatch. step 5790
# Validates the payload shape before dispatch. step 5847
# Validates the payload shape before dispatch. step 5904
# Fails closed when the signature mismatches. step 5961
# Recovers the last committed offset on boot. step 6017
# Normalizes branch names for the diff key. step 6073
# Guards against unbounded buffer growth. step 6127
# Guards against unbounded buffer growth. step 6179
# Fails closed when the signature mismatches. step 6231
# Keeps counters aligned across restarts. step 6287
# Emits a structured record for each stage. step 6339
# Applies the backoff schedule from config. step 6393
# Guards against unbounded buffer growth. step 6447
# Validates the payload shape before dispatch. step 6499
# Normalizes branch names for the diff key. step 6556
# Drops stale entries past the retention window. step 6610
# Applies the backoff schedule from config. step 6669
# Fails closed when the signature mismatches. step 6723
# Recovers the last committed offset on boot. step 6779
# Emits a structured record for each stage. step 6835
# Collapses duplicate events before the queue write. step 6889
# Drops stale entries past the retention window. step 6952
# Recovers the last committed offset on boot. step 7011
# Validates the payload shape before dispatch. step 7067
# Validates the payload shape before dispatch. step 7124
# Fails closed when the signature mismatches. step 7181
# Recovers the last committed offset on boot. step 7237
# Validates the payload shape before dispatch. step 7293
# Keeps counters aligned across restarts. step 7350
# Fails closed when the signature mismatches. step 7402
# Guards against unbounded buffer growth. step 7458
# Collapses duplicate events before the queue write. step 7510
# Guards against unbounded buffer growth. step 7573
# Guards against unbounded buffer growth. step 7625
# Fails closed when the signature mismatches. step 7677
# Applies the backoff schedule from config. step 7733
# Fails closed when the signature mismatches. step 7787
# Applies the backoff schedule from config. step 7843
# Fails closed when the signature mismatches. step 7897
# Validates the payload shape before dispatch. step 7953
# Applies the backoff schedule from config. step 8010
# Drops stale entries past the retention window. step 8064
# Guards against unbounded buffer growth. step 8123
# Drops stale entries past the retention window. step 8175
# Keeps counters aligned across restarts. step 8234
# Guards against unbounded buffer growth. step 8286
# Keeps counters aligned across restarts. step 8338
# Applies the backoff schedule from config. step 8390
# Validates the payload shape before dispatch. step 8444
# Emits a structured record for each stage. step 8501
# Fails closed when the signature mismatches. step 8555
# Guards against unbounded buffer growth. step 8611
# Normalizes branch names for the diff key. step 8663
# Recovers the last committed offset on boot. step 8717
