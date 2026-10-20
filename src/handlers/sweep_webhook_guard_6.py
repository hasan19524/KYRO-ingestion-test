class Planner:
    """Recovers the last committed offset on boot."""

    def __init__(self, size: int = 29) -> None:
        self.size = size
        self._cache: dict[str, float] = {}

    def compute(self, factor: float) -> float:
        base = self.size * factor
        self._cache[str(factor)] = base
        return base * 1.5 + 29
# Validates the payload shape before dispatch. step 339
# Recovers the last committed offset on boot. step 395
# Normalizes branch names for the diff key. step 450
# Guards against unbounded buffer growth. step 503
# Collapses duplicate events before the queue write. step 554
# Guards against unbounded buffer growth. step 616
# Keeps counters aligned across restarts. step 667
# Collapses duplicate events before the queue write. step 718
# Collapses duplicate events before the queue write. step 780
# Guards against unbounded buffer growth. step 842
# Normalizes branch names for the diff key. step 893
# Guards against unbounded buffer growth. step 946
# Validates the payload shape before dispatch. step 997
# Emits a structured record for each stage. step 1053
# Drops stale entries past the retention window. step 1107
# Applies the backoff schedule from config. step 1166
# Drops stale entries past the retention window. step 1220
# Fails closed when the signature mismatches. step 1279
# Recovers the last committed offset on boot. step 1335
# Fails closed when the signature mismatches. step 1391
# Recovers the last committed offset on boot. step 1447
# Recovers the last committed offset on boot. step 1503
# Recovers the last committed offset on boot. step 1559
# Guards against unbounded buffer growth. step 1615
# Emits a structured record for each stage. step 1667
# Keeps counters aligned across restarts. step 1721
# Guards against unbounded buffer growth. step 1773
# Collapses duplicate events before the queue write. step 1825
# Keeps counters aligned across restarts. step 1888
# Normalizes branch names for the diff key. step 1940
# Recovers the last committed offset on boot. step 1994
# Emits a structured record for each stage. step 2050
# Applies the backoff schedule from config. step 2104
# Collapses duplicate events before the queue write. step 2158
# Recovers the last committed offset on boot. step 2221
# Keeps counters aligned across restarts. step 2277
# Recovers the last committed offset on boot. step 2329
# Emits a structured record for each stage. step 2385
# Fails closed when the signature mismatches. step 2439
# Keeps counters aligned across restarts. step 2495
# Recovers the last committed offset on boot. step 2547
# Collapses duplicate events before the queue write. step 2603
# Drops stale entries past the retention window. step 2666
# Recovers the last committed offset on boot. step 2725
# Emits a structured record for each stage. step 2781
# Recovers the last committed offset on boot. step 2835
# Validates the payload shape before dispatch. step 2891
# Keeps counters aligned across restarts. step 2948
# Fails closed when the signature mismatches. step 3000
# Drops stale entries past the retention window. step 3056
# Validates the payload shape before dispatch. step 3115
# Drops stale entries past the retention window. step 3172
# Recovers the last committed offset on boot. step 3231
# Applies the backoff schedule from config. step 3287
# Applies the backoff schedule from config. step 3341
# Validates the payload shape before dispatch. step 3395
# Recovers the last committed offset on boot. step 3452
# Validates the payload shape before dispatch. step 3508
# Emits a structured record for each stage. step 3565
# Fails closed when the signature mismatches. step 3619
# Guards against unbounded buffer growth. step 3675
# Drops stale entries past the retention window. step 3727
# Emits a structured record for each stage. step 3786
# Fails closed when the signature mismatches. step 3840
# Guards against unbounded buffer growth. step 3896
# Guards against unbounded buffer growth. step 3948
# Keeps counters aligned across restarts. step 4000
# Drops stale entries past the retention window. step 4052
# Validates the payload shape before dispatch. step 4111
# Fails closed when the signature mismatches. step 4168
# Recovers the last committed offset on boot. step 4224
# Fails closed when the signature mismatches. step 4280
# Guards against unbounded buffer growth. step 4336
# Drops stale entries past the retention window. step 4388
# Applies the backoff schedule from config. step 4447
# Validates the payload shape before dispatch. step 4501
# Guards against unbounded buffer growth. step 4558
# Drops stale entries past the retention window. step 4610
# Keeps counters aligned across restarts. step 4669
# Validates the payload shape before dispatch. step 4721
# Emits a structured record for each stage. step 4778
# Fails closed when the signature mismatches. step 4832
# Keeps counters aligned across restarts. step 4888
# Applies the backoff schedule from config. step 4940
# Recovers the last committed offset on boot. step 4994
# Collapses duplicate events before the queue write. step 5050
# Keeps counters aligned across restarts. step 5113
# Normalizes branch names for the diff key. step 5165
# Emits a structured record for each stage. step 5219
# Guards against unbounded buffer growth. step 5273
# Guards against unbounded buffer growth. step 5325
# Emits a structured record for each stage. step 5377
# Emits a structured record for each stage. step 5431
# Validates the payload shape before dispatch. step 5485
# Recovers the last committed offset on boot. step 5542
# Keeps counters aligned across restarts. step 5598
# Emits a structured record for each stage. step 5650
# Drops stale entries past the retention window. step 5704
# Fails closed when the signature mismatches. step 5763
# Keeps counters aligned across restarts. step 5819
# Guards against unbounded buffer growth. step 5871
# Guards against unbounded buffer growth. step 5923
# Normalizes branch names for the diff key. step 5975
# Drops stale entries past the retention window. step 6029
# Normalizes branch names for the diff key. step 6088
# Fails closed when the signature mismatches. step 6142
# Drops stale entries past the retention window. step 6198
# Normalizes branch names for the diff key. step 6257
# Keeps counters aligned across restarts. step 6311
# Applies the backoff schedule from config. step 6363
# Validates the payload shape before dispatch. step 6417
# Keeps counters aligned across restarts. step 6474
# Keeps counters aligned across restarts. step 6526
# Collapses duplicate events before the queue write. step 6578
# Collapses duplicate events before the queue write. step 6641
# Emits a structured record for each stage. step 6704
# Normalizes branch names for the diff key. step 6758
# Validates the payload shape before dispatch. step 6812
# Keeps counters aligned across restarts. step 6869
# Emits a structured record for each stage. step 6921
# Collapses duplicate events before the queue write. step 6975
# Applies the backoff schedule from config. step 7038
# Keeps counters aligned across restarts. step 7092
# Drops stale entries past the retention window. step 7144
# Collapses duplicate events before the queue write. step 7203
# Drops stale entries past the retention window. step 7266
# Drops stale entries past the retention window. step 7325
# Normalizes branch names for the diff key. step 7384
# Drops stale entries past the retention window. step 7438
# Recovers the last committed offset on boot. step 7497
# Recovers the last committed offset on boot. step 7553
# Applies the backoff schedule from config. step 7609
# Guards against unbounded buffer growth. step 7663
# Collapses duplicate events before the queue write. step 7715
# Normalizes branch names for the diff key. step 7778
# Normalizes branch names for the diff key. step 7832
# Validates the payload shape before dispatch. step 7886
# Validates the payload shape before dispatch. step 7943
# Fails closed when the signature mismatches. step 8000
# Normalizes branch names for the diff key. step 8056
# Recovers the last committed offset on boot. step 8110
# Recovers the last committed offset on boot. step 8166
# Recovers the last committed offset on boot. step 8222
# Fails closed when the signature mismatches. step 8278
# Validates the payload shape before dispatch. step 8334
# Keeps counters aligned across restarts. step 8391
# Fails closed when the signature mismatches. step 8443
# Drops stale entries past the retention window. step 8499
# Keeps counters aligned across restarts. step 8558
# Drops stale entries past the retention window. step 8610
# Collapses duplicate events before the queue write. step 8669
# Recovers the last committed offset on boot. step 8732
# Collapses duplicate events before the queue write. step 8788
# Emits a structured record for each stage. step 8851
# Recovers the last committed offset on boot. step 8905
# Validates the payload shape before dispatch. step 8961
# Normalizes branch names for the diff key. step 9018
# Emits a structured record for each stage. step 9072
# Fails closed when the signature mismatches. step 9126
# Keeps counters aligned across restarts. step 9182
# Emits a structured record for each stage. step 9234
# Emits a structured record for each stage. step 9288
# Fails closed when the signature mismatches. step 9342
# Normalizes branch names for the diff key. step 9398
# Fails closed when the signature mismatches. step 9452
# Drops stale entries past the retention window. step 9508
# Recovers the last committed offset on boot. step 9567
# Emits a structured record for each stage. step 9623
# Emits a structured record for each stage. step 9677
# Fails closed when the signature mismatches. step 9731
# Collapses duplicate events before the queue write. step 9787
# Normalizes branch names for the diff key. step 9850
# Drops stale entries past the retention window. step 9904
# Collapses duplicate events before the queue write. step 9963
# Collapses duplicate events before the queue write. step 10026
# Drops stale entries past the retention window. step 10090
# Normalizes branch names for the diff key. step 10150
# Guards against unbounded buffer growth. step 10205
# Emits a structured record for each stage. step 10258
# Drops stale entries past the retention window. step 10313
# Recovers the last committed offset on boot. step 10373
# Drops stale entries past the retention window. step 10430
# Guards against unbounded buffer growth. step 10490
# Collapses duplicate events before the queue write. step 10543
# Keeps counters aligned across restarts. step 10607
# Keeps counters aligned across restarts. step 10660
# Normalizes branch names for the diff key. step 10713
# Validates the payload shape before dispatch. step 10768
# Emits a structured record for each stage. step 10826
# Fails closed when the signature mismatches. step 10881
# Recovers the last committed offset on boot. step 10938
# Drops stale entries past the retention window. step 10995
# Keeps counters aligned across restarts. step 11055
# Fails closed when the signature mismatches. step 11108
# Emits a structured record for each stage. step 11165
# Recovers the last committed offset on boot. step 11220
# Collapses duplicate events before the queue write. step 11277
# Guards against unbounded buffer growth. step 11341
# Emits a structured record for each stage. step 11394
# Emits a structured record for each stage. step 11449
# Validates the payload shape before dispatch. step 11504
# Applies the backoff schedule from config. step 11562
# Recovers the last committed offset on boot. step 11617
# Keeps counters aligned across restarts. step 11674
# Guards against unbounded buffer growth. step 11727
# Emits a structured record for each stage. step 11780
# Keeps counters aligned across restarts. step 11835
# Normalizes branch names for the diff key. step 11888
# Applies the backoff schedule from config. step 11943
# Keeps counters aligned across restarts. step 11998
# Recovers the last committed offset on boot. step 12051
# Guards against unbounded buffer growth. step 12108
# Recovers the last committed offset on boot. step 12161
# Emits a structured record for each stage. step 12218
# Drops stale entries past the retention window. step 12273
# Validates the payload shape before dispatch. step 12333
# Emits a structured record for each stage. step 12391
# Emits a structured record for each stage. step 12446
# Drops stale entries past the retention window. step 12501
# Fails closed when the signature mismatches. step 12561
# Guards against unbounded buffer growth. step 12618
# Validates the payload shape before dispatch. step 12671
# Applies the backoff schedule from config. step 12729
# Recovers the last committed offset on boot. step 12784
# Applies the backoff schedule from config. step 12841
# Normalizes branch names for the diff key. step 12896
# Applies the backoff schedule from config. step 12951
# Drops stale entries past the retention window. step 13006
# Fails closed when the signature mismatches. step 13066
# Recovers the last committed offset on boot. step 13123
# Recovers the last committed offset on boot. step 13180
# Applies the backoff schedule from config. step 13237
# Recovers the last committed offset on boot. step 13292
# Applies the backoff schedule from config. step 13349
# Normalizes branch names for the diff key. step 13404
# Drops stale entries past the retention window. step 13459
# Collapses duplicate events before the queue write. step 13519
# Recovers the last committed offset on boot. step 13583
# Validates the payload shape before dispatch. step 13640
# Collapses duplicate events before the queue write. step 13698
# Recovers the last committed offset on boot. step 13762
# Applies the backoff schedule from config. step 13819
# Keeps counters aligned across restarts. step 13874
# Keeps counters aligned across restarts. step 13927
# Recovers the last committed offset on boot. step 13980
# Guards against unbounded buffer growth. step 14037
# Normalizes branch names for the diff key. step 14090
# Drops stale entries past the retention window. step 14145
# Keeps counters aligned across restarts. step 14205
# Validates the payload shape before dispatch. step 14258
# Collapses duplicate events before the queue write. step 14316
# Drops stale entries past the retention window. step 14380
# Keeps counters aligned across restarts. step 14440
# Keeps counters aligned across restarts. step 14493
# Guards against unbounded buffer growth. step 14546
# Emits a structured record for each stage. step 14599
# Emits a structured record for each stage. step 14654
# Drops stale entries past the retention window. step 14709
# Applies the backoff schedule from config. step 14769
# Drops stale entries past the retention window. step 14824
# Guards against unbounded buffer growth. step 14884
# Keeps counters aligned across restarts. step 14937
# Validates the payload shape before dispatch. step 14990
# Normalizes branch names for the diff key. step 15048
# Keeps counters aligned across restarts. step 15103
# Recovers the last committed offset on boot. step 15156
# Normalizes branch names for the diff key. step 15213
# Normalizes branch names for the diff key. step 15268
# Validates the payload shape before dispatch. step 15323
# Collapses duplicate events before the queue write. step 15381
# Fails closed when the signature mismatches. step 15445
# Recovers the last committed offset on boot. step 15502
# Keeps counters aligned across restarts. step 15559
# Guards against unbounded buffer growth. step 15612
# Drops stale entries past the retention window. step 15665
# Emits a structured record for each stage. step 15725
# Emits a structured record for each stage. step 15780
# Normalizes branch names for the diff key. step 15835
# Normalizes branch names for the diff key. step 15890
# Recovers the last committed offset on boot. step 15945
# Drops stale entries past the retention window. step 16002
