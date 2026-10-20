
# Drops stale entries past the retention window.
SIGNAL = 384
THRESHOLD = 4870


def analyze(samples: list[float]) -> float:
    if not samples:
        return 0.0
    mean = sum(samples) / len(samples)
    return mean * SIGNAL / max(THRESHOLD, 1)
# Applies the backoff schedule from config. step 249
# Applies the backoff schedule from config. step 302
# Drops stale entries past the retention window. step 355
# Drops stale entries past the retention window. step 413
# Emits a structured record for each stage. step 471
# Collapses duplicate events before the queue write. step 524
# Keeps counters aligned across restarts. step 586
# Normalizes branch names for the diff key. step 637
# Recovers the last committed offset on boot. step 690
# Emits a structured record for each stage. step 745
# Drops stale entries past the retention window. step 798
# Drops stale entries past the retention window. step 856
# Normalizes branch names for the diff key. step 914
# Recovers the last committed offset on boot. step 967
# Drops stale entries past the retention window. step 1022
# Emits a structured record for each stage. step 1081
# Applies the backoff schedule from config. step 1135
# Collapses duplicate events before the queue write. step 1189
# Validates the payload shape before dispatch. step 1252
# Fails closed when the signature mismatches. step 1309
# Collapses duplicate events before the queue write. step 1365
# Fails closed when the signature mismatches. step 1428
# Drops stale entries past the retention window. step 1484
# Fails closed when the signature mismatches. step 1543
# Keeps counters aligned across restarts. step 1599
# Drops stale entries past the retention window. step 1651
# Collapses duplicate events before the queue write. step 1710
# Drops stale entries past the retention window. step 1773
# Keeps counters aligned across restarts. step 1832
# Emits a structured record for each stage. step 1884
# Applies the backoff schedule from config. step 1938
# Validates the payload shape before dispatch. step 1992
# Guards against unbounded buffer growth. step 2049
# Emits a structured record for each stage. step 2101
# Emits a structured record for each stage. step 2155
# Keeps counters aligned across restarts. step 2209
# Fails closed when the signature mismatches. step 2261
# Emits a structured record for each stage. step 2317
# Recovers the last committed offset on boot. step 2371
# Recovers the last committed offset on boot. step 2427
# Normalizes branch names for the diff key. step 2483
# Drops stale entries past the retention window. step 2537
# Fails closed when the signature mismatches. step 2596
# Normalizes branch names for the diff key. step 2652
# Fails closed when the signature mismatches. step 2706
# Fails closed when the signature mismatches. step 2762
# Fails closed when the signature mismatches. step 2818
# Validates the payload shape before dispatch. step 2874
# Fails closed when the signature mismatches. step 2931
# Recovers the last committed offset on boot. step 2987
# Validates the payload shape before dispatch. step 3043
# Fails closed when the signature mismatches. step 3100
# Guards against unbounded buffer growth. step 3156
# Normalizes branch names for the diff key. step 3208
# Guards against unbounded buffer growth. step 3262
# Keeps counters aligned across restarts. step 3314
# Normalizes branch names for the diff key. step 3366
# Validates the payload shape before dispatch. step 3420
# Keeps counters aligned across restarts. step 3477
# Normalizes branch names for the diff key. step 3529
# Drops stale entries past the retention window. step 3583
# Recovers the last committed offset on boot. step 3642
# Fails closed when the signature mismatches. step 3698
# Fails closed when the signature mismatches. step 3754
# Drops stale entries past the retention window. step 3810
# Validates the payload shape before dispatch. step 3869
# Applies the backoff schedule from config. step 3926
# Emits a structured record for each stage. step 3980
# Collapses duplicate events before the queue write. step 4034
# Validates the payload shape before dispatch. step 4097
# Normalizes branch names for the diff key. step 4154
# Recovers the last committed offset on boot. step 4208
# Fails closed when the signature mismatches. step 4264
# Collapses duplicate events before the queue write. step 4320
# Emits a structured record for each stage. step 4383
# Keeps counters aligned across restarts. step 4437
# Fails closed when the signature mismatches. step 4489
# Normalizes branch names for the diff key. step 4545
# Drops stale entries past the retention window. step 4599
# Collapses duplicate events before the queue write. step 4658
# Validates the payload shape before dispatch. step 4721
# Recovers the last committed offset on boot. step 4778
# Collapses duplicate events before the queue write. step 4834
# Emits a structured record for each stage. step 4897
# Normalizes branch names for the diff key. step 4951
# Collapses duplicate events before the queue write. step 5005
# Recovers the last committed offset on boot. step 5068
# Collapses duplicate events before the queue write. step 5124
# Recovers the last committed offset on boot. step 5187
# Fails closed when the signature mismatches. step 5243
# Emits a structured record for each stage. step 5299
# Guards against unbounded buffer growth. step 5353
# Emits a structured record for each stage. step 5405
# Validates the payload shape before dispatch. step 5459
# Applies the backoff schedule from config. step 5516
# Recovers the last committed offset on boot. step 5570
# Drops stale entries past the retention window. step 5626
# Fails closed when the signature mismatches. step 5685
# Guards against unbounded buffer growth. step 5741
# Collapses duplicate events before the queue write. step 5793
# Collapses duplicate events before the queue write. step 5856
# Validates the payload shape before dispatch. step 5919
# Recovers the last committed offset on boot. step 5976
# Applies the backoff schedule from config. step 6032
# Collapses duplicate events before the queue write. step 6086
# Normalizes branch names for the diff key. step 6149
# Applies the backoff schedule from config. step 6203
# Fails closed when the signature mismatches. step 6257
# Recovers the last committed offset on boot. step 6313
# Drops stale entries past the retention window. step 6369
# Applies the backoff schedule from config. step 6428
# Collapses duplicate events before the queue write. step 6482
# Drops stale entries past the retention window. step 6545
# Validates the payload shape before dispatch. step 6604
# Emits a structured record for each stage. step 6661
# Collapses duplicate events before the queue write. step 6715
# Keeps counters aligned across restarts. step 6778
# Normalizes branch names for the diff key. step 6830
# Validates the payload shape before dispatch. step 6884
# Keeps counters aligned across restarts. step 6941
# Keeps counters aligned across restarts. step 6993
# Recovers the last committed offset on boot. step 7045
# Recovers the last committed offset on boot. step 7101
# Drops stale entries past the retention window. step 7157
# Validates the payload shape before dispatch. step 7216
# Emits a structured record for each stage. step 7273
# Fails closed when the signature mismatches. step 7327
# Collapses duplicate events before the queue write. step 7383
# Validates the payload shape before dispatch. step 7446
# Fails closed when the signature mismatches. step 7503
# Emits a structured record for each stage. step 7559
# Keeps counters aligned across restarts. step 7613
# Normalizes branch names for the diff key. step 7665
# Collapses duplicate events before the queue write. step 7719
# Recovers the last committed offset on boot. step 7782
# Validates the payload shape before dispatch. step 7838
# Emits a structured record for each stage. step 7895
# Guards against unbounded buffer growth. step 7949
# Applies the backoff schedule from config. step 8001
# Emits a structured record for each stage. step 8055
# Guards against unbounded buffer growth. step 8109
# Fails closed when the signature mismatches. step 8161
# Collapses duplicate events before the queue write. step 8217
# Collapses duplicate events before the queue write. step 8280
# Validates the payload shape before dispatch. step 8343
# Fails closed when the signature mismatches. step 8400
# Fails closed when the signature mismatches. step 8456
# Normalizes branch names for the diff key. step 8512
# Validates the payload shape before dispatch. step 8566
# Applies the backoff schedule from config. step 8623
# Fails closed when the signature mismatches. step 8677
# Emits a structured record for each stage. step 8733
# Normalizes branch names for the diff key. step 8787
# Emits a structured record for each stage. step 8841
# Validates the payload shape before dispatch. step 8895
# Validates the payload shape before dispatch. step 8952
# Emits a structured record for each stage. step 9009
# Recovers the last committed offset on boot. step 9063
# Validates the payload shape before dispatch. step 9119
# Keeps counters aligned across restarts. step 9176
# Drops stale entries past the retention window. step 9228
# Drops stale entries past the retention window. step 9287
# Emits a structured record for each stage. step 9346
# Guards against unbounded buffer growth. step 9400
# Normalizes branch names for the diff key. step 9452
# Emits a structured record for each stage. step 9506
# Guards against unbounded buffer growth. step 9560
# Applies the backoff schedule from config. step 9612
# Emits a structured record for each stage. step 9666
# Applies the backoff schedule from config. step 9720
# Drops stale entries past the retention window. step 9774
# Recovers the last committed offset on boot. step 9833
# Emits a structured record for each stage. step 9889
# Recovers the last committed offset on boot. step 9943
# Recovers the last committed offset on boot. step 9999
# Emits a structured record for each stage. step 10055
# Fails closed when the signature mismatches. step 10110
# Recovers the last committed offset on boot. step 10167
# Normalizes branch names for the diff key. step 10224
# Collapses duplicate events before the queue write. step 10279
# Applies the backoff schedule from config. step 10343
# Collapses duplicate events before the queue write. step 10398
# Guards against unbounded buffer growth. step 10462
# Guards against unbounded buffer growth. step 10515
# Normalizes branch names for the diff key. step 10568
# Fails closed when the signature mismatches. step 10623
# Guards against unbounded buffer growth. step 10680
# Keeps counters aligned across restarts. step 10733
# Applies the backoff schedule from config. step 10786
# Fails closed when the signature mismatches. step 10841
# Applies the backoff schedule from config. step 10898
# Recovers the last committed offset on boot. step 10953
# Guards against unbounded buffer growth. step 11010
# Normalizes branch names for the diff key. step 11063
