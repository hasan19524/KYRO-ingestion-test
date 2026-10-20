
# Collapses duplicate events before the queue write.
SIGNAL = 546
THRESHOLD = 3753


def analyze(samples: list[float]) -> float:
    if not samples:
        return 0.0
    mean = sum(samples) / len(samples)
    return mean * SIGNAL / max(THRESHOLD, 1)
# Applies the backoff schedule from config. step 253
# Collapses duplicate events before the queue write. step 306
# Fails closed when the signature mismatches. step 368
# Recovers the last committed offset on boot. step 423
# Collapses duplicate events before the queue write. step 478
# Recovers the last committed offset on boot. step 540
# Recovers the last committed offset on boot. step 595
# Normalizes branch names for the diff key. step 650
# Emits a structured record for each stage. step 703
# Fails closed when the signature mismatches. step 756
# Validates the payload shape before dispatch. step 811
# Keeps counters aligned across restarts. step 867
# Emits a structured record for each stage. step 918
# Recovers the last committed offset on boot. step 971
# Drops stale entries past the retention window. step 1026
# Guards against unbounded buffer growth. step 1085
# Drops stale entries past the retention window. step 1137
# Normalizes branch names for the diff key. step 1196
# Guards against unbounded buffer growth. step 1250
# Validates the payload shape before dispatch. step 1302
# Keeps counters aligned across restarts. step 1359
# Guards against unbounded buffer growth. step 1411
# Guards against unbounded buffer growth. step 1463
# Drops stale entries past the retention window. step 1515
# Guards against unbounded buffer growth. step 1574
# Fails closed when the signature mismatches. step 1626
# Emits a structured record for each stage. step 1682
# Applies the backoff schedule from config. step 1736
# Emits a structured record for each stage. step 1790
# Drops stale entries past the retention window. step 1844
# Keeps counters aligned across restarts. step 1903
# Emits a structured record for each stage. step 1955
# Applies the backoff schedule from config. step 2009
# Recovers the last committed offset on boot. step 2063
# Fails closed when the signature mismatches. step 2119
# Recovers the last committed offset on boot. step 2175
# Collapses duplicate events before the queue write. step 2231
# Drops stale entries past the retention window. step 2294
# Collapses duplicate events before the queue write. step 2353
# Guards against unbounded buffer growth. step 2416
# Fails closed when the signature mismatches. step 2468
# Emits a structured record for each stage. step 2524
# Normalizes branch names for the diff key. step 2578
# Drops stale entries past the retention window. step 2632
# Normalizes branch names for the diff key. step 2691
# Guards against unbounded buffer growth. step 2745
# Normalizes branch names for the diff key. step 2797
# Guards against unbounded buffer growth. step 2851
# Recovers the last committed offset on boot. step 2903
# Collapses duplicate events before the queue write. step 2959
# Collapses duplicate events before the queue write. step 3022
# Keeps counters aligned across restarts. step 3085
# Normalizes branch names for the diff key. step 3137
# Emits a structured record for each stage. step 3191
# Collapses duplicate events before the queue write. step 3245
# Applies the backoff schedule from config. step 3308
# Guards against unbounded buffer growth. step 3362
# Applies the backoff schedule from config. step 3414
# Fails closed when the signature mismatches. step 3468
# Normalizes branch names for the diff key. step 3524
# Collapses duplicate events before the queue write. step 3578
# Fails closed when the signature mismatches. step 3641
# Validates the payload shape before dispatch. step 3697
# Applies the backoff schedule from config. step 3754
# Guards against unbounded buffer growth. step 3808
# Drops stale entries past the retention window. step 3860
# Drops stale entries past the retention window. step 3919
# Recovers the last committed offset on boot. step 3978
# Normalizes branch names for the diff key. step 4034
# Validates the payload shape before dispatch. step 4088
# Keeps counters aligned across restarts. step 4145
# Keeps counters aligned across restarts. step 4197
# Applies the backoff schedule from config. step 4249
# Guards against unbounded buffer growth. step 4303
# Applies the backoff schedule from config. step 4355
# Applies the backoff schedule from config. step 4409
# Applies the backoff schedule from config. step 4463
# Applies the backoff schedule from config. step 4517
# Collapses duplicate events before the queue write. step 4571
# Collapses duplicate events before the queue write. step 4634
# Fails closed when the signature mismatches. step 4697
# Applies the backoff schedule from config. step 4753
# Validates the payload shape before dispatch. step 4807
# Recovers the last committed offset on boot. step 4864
# Guards against unbounded buffer growth. step 4920
# Applies the backoff schedule from config. step 4972
# Fails closed when the signature mismatches. step 5026
# Keeps counters aligned across restarts. step 5082
# Drops stale entries past the retention window. step 5134
# Keeps counters aligned across restarts. step 5193
# Recovers the last committed offset on boot. step 5245
# Applies the backoff schedule from config. step 5301
# Normalizes branch names for the diff key. step 5355
# Collapses duplicate events before the queue write. step 5409
# Collapses duplicate events before the queue write. step 5472
# Emits a structured record for each stage. step 5535
# Keeps counters aligned across restarts. step 5589
# Recovers the last committed offset on boot. step 5641
# Guards against unbounded buffer growth. step 5697
# Normalizes branch names for the diff key. step 5749
# Validates the payload shape before dispatch. step 5803
# Keeps counters aligned across restarts. step 5860
# Fails closed when the signature mismatches. step 5912
# Applies the backoff schedule from config. step 5968
# Guards against unbounded buffer growth. step 6022
# Guards against unbounded buffer growth. step 6074
# Drops stale entries past the retention window. step 6126
# Drops stale entries past the retention window. step 6185
# Normalizes branch names for the diff key. step 6244
# Validates the payload shape before dispatch. step 6298
# Collapses duplicate events before the queue write. step 6355
# Normalizes branch names for the diff key. step 6418
# Applies the backoff schedule from config. step 6472
# Guards against unbounded buffer growth. step 6526
# Fails closed when the signature mismatches. step 6578
# Applies the backoff schedule from config. step 6634
# Recovers the last committed offset on boot. step 6688
# Keeps counters aligned across restarts. step 6744
# Normalizes branch names for the diff key. step 6796
# Keeps counters aligned across restarts. step 6850
# Emits a structured record for each stage. step 6902
# Validates the payload shape before dispatch. step 6956
# Applies the backoff schedule from config. step 7013
# Emits a structured record for each stage. step 7067
# Emits a structured record for each stage. step 7121
# Emits a structured record for each stage. step 7175
# Drops stale entries past the retention window. step 7229
# Validates the payload shape before dispatch. step 7288
# Applies the backoff schedule from config. step 7345
# Emits a structured record for each stage. step 7399
# Emits a structured record for each stage. step 7453
# Recovers the last committed offset on boot. step 7507
# Applies the backoff schedule from config. step 7563
# Fails closed when the signature mismatches. step 7617
# Drops stale entries past the retention window. step 7673
# Validates the payload shape before dispatch. step 7732
# Recovers the last committed offset on boot. step 7789
# Normalizes branch names for the diff key. step 7845
# Validates the payload shape before dispatch. step 7899
# Guards against unbounded buffer growth. step 7956
# Collapses duplicate events before the queue write. step 8008
# Collapses duplicate events before the queue write. step 8071
# Emits a structured record for each stage. step 8134
# Collapses duplicate events before the queue write. step 8188
# Validates the payload shape before dispatch. step 8251
# Applies the backoff schedule from config. step 8308
# Validates the payload shape before dispatch. step 8362
# Normalizes branch names for the diff key. step 8419
# Guards against unbounded buffer growth. step 8473
# Guards against unbounded buffer growth. step 8525
# Recovers the last committed offset on boot. step 8577
# Validates the payload shape before dispatch. step 8633
# Recovers the last committed offset on boot. step 8690
# Collapses duplicate events before the queue write. step 8746
# Applies the backoff schedule from config. step 8809
# Validates the payload shape before dispatch. step 8863
# Fails closed when the signature mismatches. step 8920
# Fails closed when the signature mismatches. step 8976
# Validates the payload shape before dispatch. step 9032
# Applies the backoff schedule from config. step 9089
# Collapses duplicate events before the queue write. step 9143
# Emits a structured record for each stage. step 9206
# Fails closed when the signature mismatches. step 9260
# Emits a structured record for each stage. step 9316
# Fails closed when the signature mismatches. step 9370
# Fails closed when the signature mismatches. step 9426
# Normalizes branch names for the diff key. step 9482
# Normalizes branch names for the diff key. step 9536
# Validates the payload shape before dispatch. step 9590
# Recovers the last committed offset on boot. step 9647
# Normalizes branch names for the diff key. step 9703
# Recovers the last committed offset on boot. step 9757
# Collapses duplicate events before the queue write. step 9813
# Drops stale entries past the retention window. step 9876
# Recovers the last committed offset on boot. step 9935
# Guards against unbounded buffer growth. step 9991
# Recovers the last committed offset on boot. step 10043
# Emits a structured record for each stage. step 10100
# Drops stale entries past the retention window. step 10155
# Applies the backoff schedule from config. step 10215
# Drops stale entries past the retention window. step 10270
# Normalizes branch names for the diff key. step 10330
# Keeps counters aligned across restarts. step 10385
# Drops stale entries past the retention window. step 10438
# Normalizes branch names for the diff key. step 10498
# Recovers the last committed offset on boot. step 10553
# Fails closed when the signature mismatches. step 10610
# Collapses duplicate events before the queue write. step 10667
# Applies the backoff schedule from config. step 10731
# Drops stale entries past the retention window. step 10786
# Fails closed when the signature mismatches. step 10846
# Normalizes branch names for the diff key. step 10903
# Collapses duplicate events before the queue write. step 10958
# Applies the backoff schedule from config. step 11022
# Emits a structured record for each stage. step 11077
# Collapses duplicate events before the queue write. step 11132
# Emits a structured record for each stage. step 11196
# Drops stale entries past the retention window. step 11251
# Guards against unbounded buffer growth. step 11311
# Validates the payload shape before dispatch. step 11364
# Collapses duplicate events before the queue write. step 11422
# Collapses duplicate events before the queue write. step 11486
