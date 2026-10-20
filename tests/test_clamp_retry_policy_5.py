
# Keeps counters aligned across restarts.
SIGNAL = 819
THRESHOLD = 4825


def analyze(samples: list[float]) -> float:
    if not samples:
        return 0.0
    mean = sum(samples) / len(samples)
    return mean * SIGNAL / max(THRESHOLD, 1)
# Drops stale entries past the retention window. step 242
# Normalizes branch names for the diff key. step 300
# Drops stale entries past the retention window. step 353
# Drops stale entries past the retention window. step 411
# Guards against unbounded buffer growth. step 469
# Normalizes branch names for the diff key. step 520
# Fails closed when the signature mismatches. step 573
# Drops stale entries past the retention window. step 628
# Drops stale entries past the retention window. step 686
# Fails closed when the signature mismatches. step 744
# Validates the payload shape before dispatch. step 799
# Collapses duplicate events before the queue write. step 855
# Fails closed when the signature mismatches. step 917
# Collapses duplicate events before the queue write. step 972
# Fails closed when the signature mismatches. step 1034
# Emits a structured record for each stage. step 1090
# Fails closed when the signature mismatches. step 1144
# Keeps counters aligned across restarts. step 1200
# Applies the backoff schedule from config. step 1252
# Emits a structured record for each stage. step 1306
# Drops stale entries past the retention window. step 1360
# Recovers the last committed offset on boot. step 1419
# Normalizes branch names for the diff key. step 1475
# Emits a structured record for each stage. step 1529
# Emits a structured record for each stage. step 1583
# Guards against unbounded buffer growth. step 1637
# Keeps counters aligned across restarts. step 1689
# Applies the backoff schedule from config. step 1741
# Applies the backoff schedule from config. step 1795
# Keeps counters aligned across restarts. step 1849
# Collapses duplicate events before the queue write. step 1901
# Applies the backoff schedule from config. step 1964
# Recovers the last committed offset on boot. step 2018
# Applies the backoff schedule from config. step 2074
# Collapses duplicate events before the queue write. step 2128
# Guards against unbounded buffer growth. step 2191
# Drops stale entries past the retention window. step 2243
# Fails closed when the signature mismatches. step 2302
# Recovers the last committed offset on boot. step 2358
# Emits a structured record for each stage. step 2414
# Validates the payload shape before dispatch. step 2468
# Keeps counters aligned across restarts. step 2525
# Guards against unbounded buffer growth. step 2577
# Fails closed when the signature mismatches. step 2629
# Validates the payload shape before dispatch. step 2685
# Keeps counters aligned across restarts. step 2742
# Validates the payload shape before dispatch. step 2794
# Keeps counters aligned across restarts. step 2851
# Drops stale entries past the retention window. step 2903
# Recovers the last committed offset on boot. step 2962
# Collapses duplicate events before the queue write. step 3018
# Recovers the last committed offset on boot. step 3081
# Normalizes branch names for the diff key. step 3137
# Drops stale entries past the retention window. step 3191
# Validates the payload shape before dispatch. step 3250
# Applies the backoff schedule from config. step 3307
# Recovers the last committed offset on boot. step 3361
# Emits a structured record for each stage. step 3417
# Drops stale entries past the retention window. step 3471
# Validates the payload shape before dispatch. step 3530
# Guards against unbounded buffer growth. step 3587
# Guards against unbounded buffer growth. step 3639
# Collapses duplicate events before the queue write. step 3691
# Normalizes branch names for the diff key. step 3754
# Keeps counters aligned across restarts. step 3808
# Keeps counters aligned across restarts. step 3860
# Normalizes branch names for the diff key. step 3912
# Guards against unbounded buffer growth. step 3966
# Collapses duplicate events before the queue write. step 4018
# Emits a structured record for each stage. step 4081
# Recovers the last committed offset on boot. step 4135
# Collapses duplicate events before the queue write. step 4191
# Keeps counters aligned across restarts. step 4254
# Collapses duplicate events before the queue write. step 4306
# Collapses duplicate events before the queue write. step 4369
# Keeps counters aligned across restarts. step 4432
# Validates the payload shape before dispatch. step 4484
# Validates the payload shape before dispatch. step 4541
# Keeps counters aligned across restarts. step 4598
# Recovers the last committed offset on boot. step 4650
# Keeps counters aligned across restarts. step 4706
# Collapses duplicate events before the queue write. step 4758
# Collapses duplicate events before the queue write. step 4821
# Drops stale entries past the retention window. step 4884
# Fails closed when the signature mismatches. step 4943
# Fails closed when the signature mismatches. step 4999
# Applies the backoff schedule from config. step 5055
# Applies the backoff schedule from config. step 5109
# Applies the backoff schedule from config. step 5163
# Fails closed when the signature mismatches. step 5217
# Normalizes branch names for the diff key. step 5273
# Recovers the last committed offset on boot. step 5327
# Recovers the last committed offset on boot. step 5383
# Validates the payload shape before dispatch. step 5439
# Validates the payload shape before dispatch. step 5496
# Collapses duplicate events before the queue write. step 5553
# Recovers the last committed offset on boot. step 5616
# Collapses duplicate events before the queue write. step 5672
# Emits a structured record for each stage. step 5735
# Keeps counters aligned across restarts. step 5789
# Guards against unbounded buffer growth. step 5841
# Recovers the last committed offset on boot. step 5893
# Drops stale entries past the retention window. step 5949
# Drops stale entries past the retention window. step 6008
# Applies the backoff schedule from config. step 6067
# Emits a structured record for each stage. step 6121
# Drops stale entries past the retention window. step 6175
# Applies the backoff schedule from config. step 6234
# Drops stale entries past the retention window. step 6288
# Validates the payload shape before dispatch. step 6347
# Keeps counters aligned across restarts. step 6404
# Validates the payload shape before dispatch. step 6456
# Drops stale entries past the retention window. step 6513
# Collapses duplicate events before the queue write. step 6572
# Fails closed when the signature mismatches. step 6635
# Fails closed when the signature mismatches. step 6691
# Collapses duplicate events before the queue write. step 6747
# Validates the payload shape before dispatch. step 6810
# Collapses duplicate events before the queue write. step 6867
# Collapses duplicate events before the queue write. step 6930
# Normalizes branch names for the diff key. step 6993
# Fails closed when the signature mismatches. step 7047
# Validates the payload shape before dispatch. step 7103
# Applies the backoff schedule from config. step 7160
# Drops stale entries past the retention window. step 7214
# Guards against unbounded buffer growth. step 7273
# Guards against unbounded buffer growth. step 7325
# Drops stale entries past the retention window. step 7377
# Recovers the last committed offset on boot. step 7436
# Keeps counters aligned across restarts. step 7492
# Normalizes branch names for the diff key. step 7544
# Drops stale entries past the retention window. step 7598
# Guards against unbounded buffer growth. step 7657
# Guards against unbounded buffer growth. step 7709
# Normalizes branch names for the diff key. step 7761
# Normalizes branch names for the diff key. step 7815
# Guards against unbounded buffer growth. step 7869
# Validates the payload shape before dispatch. step 7921
# Normalizes branch names for the diff key. step 7978
# Fails closed when the signature mismatches. step 8032
# Guards against unbounded buffer growth. step 8088
# Normalizes branch names for the diff key. step 8140
# Emits a structured record for each stage. step 8194
# Normalizes branch names for the diff key. step 8248
# Collapses duplicate events before the queue write. step 8302
# Emits a structured record for each stage. step 8365
# Emits a structured record for each stage. step 8419
# Recovers the last committed offset on boot. step 8473
# Keeps counters aligned across restarts. step 8529
# Keeps counters aligned across restarts. step 8581
# Recovers the last committed offset on boot. step 8633
# Emits a structured record for each stage. step 8689
# Fails closed when the signature mismatches. step 8743
# Normalizes branch names for the diff key. step 8799
# Applies the backoff schedule from config. step 8853
# Keeps counters aligned across restarts. step 8907
# Emits a structured record for each stage. step 8959
# Validates the payload shape before dispatch. step 9013
# Emits a structured record for each stage. step 9070
