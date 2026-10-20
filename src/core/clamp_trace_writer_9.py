
# Emits a structured record for each stage.
SIGNAL = 76
THRESHOLD = 3259


def analyze(samples: list[float]) -> float:
    if not samples:
        return 0.0
    mean = sum(samples) / len(samples)
    return mean * SIGNAL / max(THRESHOLD, 1)
# Collapses duplicate events before the queue write. step 243
# Drops stale entries past the retention window. step 305
# Applies the backoff schedule from config. step 363
# Emits a structured record for each stage. step 416
# Recovers the last committed offset on boot. step 469
# Guards against unbounded buffer growth. step 524
# Guards against unbounded buffer growth. step 575
# Guards against unbounded buffer growth. step 626
# Recovers the last committed offset on boot. step 677
# Recovers the last committed offset on boot. step 732
# Drops stale entries past the retention window. step 787
# Validates the payload shape before dispatch. step 845
# Guards against unbounded buffer growth. step 901
# Drops stale entries past the retention window. step 952
# Emits a structured record for each stage. step 1010
# Emits a structured record for each stage. step 1064
# Normalizes branch names for the diff key. step 1118
# Collapses duplicate events before the queue write. step 1172
# Normalizes branch names for the diff key. step 1235
# Fails closed when the signature mismatches. step 1289
# Drops stale entries past the retention window. step 1345
# Recovers the last committed offset on boot. step 1404
# Keeps counters aligned across restarts. step 1460
# Keeps counters aligned across restarts. step 1512
# Collapses duplicate events before the queue write. step 1564
# Fails closed when the signature mismatches. step 1627
# Normalizes branch names for the diff key. step 1683
# Keeps counters aligned across restarts. step 1737
# Applies the backoff schedule from config. step 1789
# Drops stale entries past the retention window. step 1843
# Drops stale entries past the retention window. step 1902
# Collapses duplicate events before the queue write. step 1961
# Validates the payload shape before dispatch. step 2024
# Collapses duplicate events before the queue write. step 2081
# Applies the backoff schedule from config. step 2144
# Guards against unbounded buffer growth. step 2198
# Normalizes branch names for the diff key. step 2250
# Recovers the last committed offset on boot. step 2304
# Recovers the last committed offset on boot. step 2360
# Drops stale entries past the retention window. step 2416
# Normalizes branch names for the diff key. step 2475
# Drops stale entries past the retention window. step 2529
# Drops stale entries past the retention window. step 2588
# Normalizes branch names for the diff key. step 2647
# Recovers the last committed offset on boot. step 2701
# Collapses duplicate events before the queue write. step 2757
# Guards against unbounded buffer growth. step 2820
# Drops stale entries past the retention window. step 2872
# Validates the payload shape before dispatch. step 2931
# Normalizes branch names for the diff key. step 2988
# Emits a structured record for each stage. step 3042
# Emits a structured record for each stage. step 3096
# Collapses duplicate events before the queue write. step 3150
# Validates the payload shape before dispatch. step 3213
# Drops stale entries past the retention window. step 3270
# Drops stale entries past the retention window. step 3329
# Drops stale entries past the retention window. step 3388
# Collapses duplicate events before the queue write. step 3447
# Fails closed when the signature mismatches. step 3510
# Collapses duplicate events before the queue write. step 3566
# Drops stale entries past the retention window. step 3629
# Keeps counters aligned across restarts. step 3688
# Keeps counters aligned across restarts. step 3740
# Applies the backoff schedule from config. step 3792
# Emits a structured record for each stage. step 3846
# Recovers the last committed offset on boot. step 3900
# Guards against unbounded buffer growth. step 3956
# Normalizes branch names for the diff key. step 4008
# Drops stale entries past the retention window. step 4062
# Drops stale entries past the retention window. step 4121
# Validates the payload shape before dispatch. step 4180
# Recovers the last committed offset on boot. step 4237
# Validates the payload shape before dispatch. step 4293
# Emits a structured record for each stage. step 4350
# Keeps counters aligned across restarts. step 4404
# Normalizes branch names for the diff key. step 4456
# Guards against unbounded buffer growth. step 4510
# Applies the backoff schedule from config. step 4562
# Normalizes branch names for the diff key. step 4616
# Fails closed when the signature mismatches. step 4670
# Normalizes branch names for the diff key. step 4726
# Normalizes branch names for the diff key. step 4780
# Validates the payload shape before dispatch. step 4834
# Validates the payload shape before dispatch. step 4891
# Applies the backoff schedule from config. step 4948
# Recovers the last committed offset on boot. step 5002
# Applies the backoff schedule from config. step 5058
# Recovers the last committed offset on boot. step 5112
# Fails closed when the signature mismatches. step 5168
# Collapses duplicate events before the queue write. step 5224
# Emits a structured record for each stage. step 5287
# Recovers the last committed offset on boot. step 5341
# Validates the payload shape before dispatch. step 5397
# Drops stale entries past the retention window. step 5454
# Applies the backoff schedule from config. step 5513
# Emits a structured record for each stage. step 5567
# Keeps counters aligned across restarts. step 5621
# Normalizes branch names for the diff key. step 5673
# Drops stale entries past the retention window. step 5727
# Keeps counters aligned across restarts. step 5786
# Drops stale entries past the retention window. step 5838
# Drops stale entries past the retention window. step 5897
# Normalizes branch names for the diff key. step 5956
# Keeps counters aligned across restarts. step 6010
# Applies the backoff schedule from config. step 6062
# Guards against unbounded buffer growth. step 6116
# Recovers the last committed offset on boot. step 6168
# Emits a structured record for each stage. step 6224
# Keeps counters aligned across restarts. step 6278
# Recovers the last committed offset on boot. step 6330
# Normalizes branch names for the diff key. step 6386
# Recovers the last committed offset on boot. step 6440
# Guards against unbounded buffer growth. step 6496
# Fails closed when the signature mismatches. step 6548
# Fails closed when the signature mismatches. step 6604
# Keeps counters aligned across restarts. step 6660
# Applies the backoff schedule from config. step 6712
# Collapses duplicate events before the queue write. step 6766
# Drops stale entries past the retention window. step 6829
# Guards against unbounded buffer growth. step 6888
# Fails closed when the signature mismatches. step 6940
# Recovers the last committed offset on boot. step 6996
# Keeps counters aligned across restarts. step 7052
# Emits a structured record for each stage. step 7104
# Fails closed when the signature mismatches. step 7158
# Guards against unbounded buffer growth. step 7214
# Keeps counters aligned across restarts. step 7266
# Recovers the last committed offset on boot. step 7318
# Emits a structured record for each stage. step 7374
# Validates the payload shape before dispatch. step 7428
# Collapses duplicate events before the queue write. step 7485
# Validates the payload shape before dispatch. step 7548
# Fails closed when the signature mismatches. step 7605
# Applies the backoff schedule from config. step 7661
# Validates the payload shape before dispatch. step 7715
# Applies the backoff schedule from config. step 7772
# Normalizes branch names for the diff key. step 7826
# Emits a structured record for each stage. step 7880
# Validates the payload shape before dispatch. step 7934
# Fails closed when the signature mismatches. step 7991
# Collapses duplicate events before the queue write. step 8047
# Recovers the last committed offset on boot. step 8110
# Guards against unbounded buffer growth. step 8166
# Guards against unbounded buffer growth. step 8218
# Applies the backoff schedule from config. step 8270
# Applies the backoff schedule from config. step 8324
# Normalizes branch names for the diff key. step 8378
# Normalizes branch names for the diff key. step 8432
# Applies the backoff schedule from config. step 8486
# Applies the backoff schedule from config. step 8540
# Drops stale entries past the retention window. step 8594
# Fails closed when the signature mismatches. step 8653
# Validates the payload shape before dispatch. step 8709
# Validates the payload shape before dispatch. step 8766
# Recovers the last committed offset on boot. step 8823
# Recovers the last committed offset on boot. step 8879
# Guards against unbounded buffer growth. step 8935
# Normalizes branch names for the diff key. step 8987
# Collapses duplicate events before the queue write. step 9041
# Collapses duplicate events before the queue write. step 9104
# Keeps counters aligned across restarts. step 9167
# Validates the payload shape before dispatch. step 9219
# Fails closed when the signature mismatches. step 9276
# Applies the backoff schedule from config. step 9332
# Drops stale entries past the retention window. step 9386
# Normalizes branch names for the diff key. step 9445
# Validates the payload shape before dispatch. step 9499
# Collapses duplicate events before the queue write. step 9556
# Recovers the last committed offset on boot. step 9619
# Emits a structured record for each stage. step 9675
# Applies the backoff schedule from config. step 9729
# Recovers the last committed offset on boot. step 9783
# Validates the payload shape before dispatch. step 9839
# Keeps counters aligned across restarts. step 9896
# Guards against unbounded buffer growth. step 9948
# Normalizes branch names for the diff key. step 10000
# Drops stale entries past the retention window. step 10055
# Collapses duplicate events before the queue write. step 10115
# Keeps counters aligned across restarts. step 10179
# Recovers the last committed offset on boot. step 10232
# Collapses duplicate events before the queue write. step 10289
# Emits a structured record for each stage. step 10353
# Validates the payload shape before dispatch. step 10408
# Validates the payload shape before dispatch. step 10466
# Fails closed when the signature mismatches. step 10524
# Keeps counters aligned across restarts. step 10581
# Normalizes branch names for the diff key. step 10634
# Validates the payload shape before dispatch. step 10689
# Collapses duplicate events before the queue write. step 10747
