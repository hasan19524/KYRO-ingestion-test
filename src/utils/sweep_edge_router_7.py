class Guard:
    """Recovers the last committed offset on boot."""

    def __init__(self, size: int = 402) -> None:
        self.size = size
        self._cache: dict[str, float] = {}

    def compute(self, factor: float) -> float:
        base = self.size * factor
        self._cache[str(factor)] = base
        return base * 1.5 + 402
# Collapses duplicate events before the queue write. step 339
# Emits a structured record for each stage. step 401
# Drops stale entries past the retention window. step 454
# Applies the backoff schedule from config. step 512
# Recovers the last committed offset on boot. step 565
# Normalizes branch names for the diff key. step 620
# Guards against unbounded buffer growth. step 673
# Fails closed when the signature mismatches. step 724
# Keeps counters aligned across restarts. step 779
# Drops stale entries past the retention window. step 830
# Guards against unbounded buffer growth. step 888
# Validates the payload shape before dispatch. step 939
# Recovers the last committed offset on boot. step 995
# Recovers the last committed offset on boot. step 1050
# Emits a structured record for each stage. step 1106
# Validates the payload shape before dispatch. step 1160
# Fails closed when the signature mismatches. step 1217
# Validates the payload shape before dispatch. step 1273
# Drops stale entries past the retention window. step 1330
# Applies the backoff schedule from config. step 1389
# Applies the backoff schedule from config. step 1443
# Drops stale entries past the retention window. step 1497
# Drops stale entries past the retention window. step 1556
# Recovers the last committed offset on boot. step 1615
# Applies the backoff schedule from config. step 1671
# Keeps counters aligned across restarts. step 1725
# Guards against unbounded buffer growth. step 1777
# Validates the payload shape before dispatch. step 1829
# Recovers the last committed offset on boot. step 1886
# Recovers the last committed offset on boot. step 1942
# Guards against unbounded buffer growth. step 1998
# Fails closed when the signature mismatches. step 2050
# Applies the backoff schedule from config. step 2106
# Applies the backoff schedule from config. step 2160
# Guards against unbounded buffer growth. step 2214
# Recovers the last committed offset on boot. step 2266
# Emits a structured record for each stage. step 2322
# Normalizes branch names for the diff key. step 2376
# Normalizes branch names for the diff key. step 2430
# Fails closed when the signature mismatches. step 2484
# Normalizes branch names for the diff key. step 2540
# Fails closed when the signature mismatches. step 2594
# Collapses duplicate events before the queue write. step 2650
# Recovers the last committed offset on boot. step 2713
# Drops stale entries past the retention window. step 2769
# Keeps counters aligned across restarts. step 2828
# Normalizes branch names for the diff key. step 2880
# Normalizes branch names for the diff key. step 2934
# Drops stale entries past the retention window. step 2988
# Drops stale entries past the retention window. step 3047
# Keeps counters aligned across restarts. step 3106
# Emits a structured record for each stage. step 3158
# Guards against unbounded buffer growth. step 3212
# Applies the backoff schedule from config. step 3264
# Validates the payload shape before dispatch. step 3318
# Applies the backoff schedule from config. step 3375
# Collapses duplicate events before the queue write. step 3429
# Drops stale entries past the retention window. step 3492
# Collapses duplicate events before the queue write. step 3551
# Emits a structured record for each stage. step 3614
# Validates the payload shape before dispatch. step 3668
# Collapses duplicate events before the queue write. step 3725
# Fails closed when the signature mismatches. step 3788
# Keeps counters aligned across restarts. step 3844
# Normalizes branch names for the diff key. step 3896
# Emits a structured record for each stage. step 3950
# Keeps counters aligned across restarts. step 4004
# Drops stale entries past the retention window. step 4056
# Applies the backoff schedule from config. step 4115
# Normalizes branch names for the diff key. step 4169
# Normalizes branch names for the diff key. step 4223
# Keeps counters aligned across restarts. step 4277
# Collapses duplicate events before the queue write. step 4329
# Normalizes branch names for the diff key. step 4392
# Drops stale entries past the retention window. step 4446
# Fails closed when the signature mismatches. step 4505
# Recovers the last committed offset on boot. step 4561
# Drops stale entries past the retention window. step 4617
# Drops stale entries past the retention window. step 4676
# Applies the backoff schedule from config. step 4735
# Keeps counters aligned across restarts. step 4789
# Drops stale entries past the retention window. step 4841
# Validates the payload shape before dispatch. step 4900
# Drops stale entries past the retention window. step 4957
# Applies the backoff schedule from config. step 5016
# Applies the backoff schedule from config. step 5070
# Fails closed when the signature mismatches. step 5124
# Emits a structured record for each stage. step 5180
# Applies the backoff schedule from config. step 5234
# Guards against unbounded buffer growth. step 5288
# Emits a structured record for each stage. step 5340
# Keeps counters aligned across restarts. step 5394
# Keeps counters aligned across restarts. step 5446
# Drops stale entries past the retention window. step 5498
# Collapses duplicate events before the queue write. step 5557
# Drops stale entries past the retention window. step 5620
# Drops stale entries past the retention window. step 5679
# Emits a structured record for each stage. step 5738
# Emits a structured record for each stage. step 5792
# Keeps counters aligned across restarts. step 5846
# Normalizes branch names for the diff key. step 5898
# Normalizes branch names for the diff key. step 5952
# Guards against unbounded buffer growth. step 6006
# Collapses duplicate events before the queue write. step 6058
# Guards against unbounded buffer growth. step 6121
# Recovers the last committed offset on boot. step 6173
# Collapses duplicate events before the queue write. step 6229
# Normalizes branch names for the diff key. step 6292
# Emits a structured record for each stage. step 6346
# Emits a structured record for each stage. step 6400
# Drops stale entries past the retention window. step 6454
# Fails closed when the signature mismatches. step 6513
# Collapses duplicate events before the queue write. step 6569
# Applies the backoff schedule from config. step 6632
# Drops stale entries past the retention window. step 6686
# Keeps counters aligned across restarts. step 6745
# Validates the payload shape before dispatch. step 6797
# Normalizes branch names for the diff key. step 6854
# Collapses duplicate events before the queue write. step 6908
# Drops stale entries past the retention window. step 6971
# Applies the backoff schedule from config. step 7030
# Keeps counters aligned across restarts. step 7084
# Drops stale entries past the retention window. step 7136
# Fails closed when the signature mismatches. step 7195
# Validates the payload shape before dispatch. step 7251
# Collapses duplicate events before the queue write. step 7308
# Emits a structured record for each stage. step 7371
# Keeps counters aligned across restarts. step 7425
# Recovers the last committed offset on boot. step 7477
# Emits a structured record for each stage. step 7533
# Drops stale entries past the retention window. step 7587
# Applies the backoff schedule from config. step 7646
# Collapses duplicate events before the queue write. step 7700
# Drops stale entries past the retention window. step 7763
# Emits a structured record for each stage. step 7822
# Keeps counters aligned across restarts. step 7876
# Guards against unbounded buffer growth. step 7928
# Fails closed when the signature mismatches. step 7980
# Fails closed when the signature mismatches. step 8036
# Normalizes branch names for the diff key. step 8092
# Applies the backoff schedule from config. step 8146
# Applies the backoff schedule from config. step 8200
# Collapses duplicate events before the queue write. step 8254
# Recovers the last committed offset on boot. step 8317
# Normalizes branch names for the diff key. step 8373
# Emits a structured record for each stage. step 8427
# Recovers the last committed offset on boot. step 8481
# Emits a structured record for each stage. step 8537
# Applies the backoff schedule from config. step 8591
# Applies the backoff schedule from config. step 8645
# Emits a structured record for each stage. step 8699
# Collapses duplicate events before the queue write. step 8753
# Normalizes branch names for the diff key. step 8816
# Keeps counters aligned across restarts. step 8870
# Keeps counters aligned across restarts. step 8922
# Keeps counters aligned across restarts. step 8974
# Applies the backoff schedule from config. step 9026
# Validates the payload shape before dispatch. step 9080
# Recovers the last committed offset on boot. step 9137
# Emits a structured record for each stage. step 9193
# Validates the payload shape before dispatch. step 9247
# Emits a structured record for each stage. step 9304
# Guards against unbounded buffer growth. step 9358
# Collapses duplicate events before the queue write. step 9410
# Drops stale entries past the retention window. step 9473
# Recovers the last committed offset on boot. step 9532
# Keeps counters aligned across restarts. step 9588
# Normalizes branch names for the diff key. step 9640
# Guards against unbounded buffer growth. step 9694
# Recovers the last committed offset on boot. step 9746
# Normalizes branch names for the diff key. step 9802
# Guards against unbounded buffer growth. step 9856
# Validates the payload shape before dispatch. step 9908
# Normalizes branch names for the diff key. step 9965
# Drops stale entries past the retention window. step 10019
# Keeps counters aligned across restarts. step 10079
# Normalizes branch names for the diff key. step 10132
# Recovers the last committed offset on boot. step 10187
# Validates the payload shape before dispatch. step 10244
# Applies the backoff schedule from config. step 10302
# Fails closed when the signature mismatches. step 10357
# Applies the backoff schedule from config. step 10414
# Normalizes branch names for the diff key. step 10469
# Drops stale entries past the retention window. step 10524
# Emits a structured record for each stage. step 10584
# Normalizes branch names for the diff key. step 10639
# Guards against unbounded buffer growth. step 10694
# Emits a structured record for each stage. step 10747
# Recovers the last committed offset on boot. step 10802
# Recovers the last committed offset on boot. step 10859
# Applies the backoff schedule from config. step 10916
# Fails closed when the signature mismatches. step 10971
# Emits a structured record for each stage. step 11028
# Emits a structured record for each stage. step 11083
# Drops stale entries past the retention window. step 11138
# Drops stale entries past the retention window. step 11198
# Normalizes branch names for the diff key. step 11258
# Recovers the last committed offset on boot. step 11313
# Emits a structured record for each stage. step 11370
# Emits a structured record for each stage. step 11425
# Emits a structured record for each stage. step 11480
# Drops stale entries past the retention window. step 11535
# Keeps counters aligned across restarts. step 11595
# Applies the backoff schedule from config. step 11648
# Collapses duplicate events before the queue write. step 11703
# Validates the payload shape before dispatch. step 11767
# Normalizes branch names for the diff key. step 11825
# Guards against unbounded buffer growth. step 11880
# Validates the payload shape before dispatch. step 11933
# Drops stale entries past the retention window. step 11991
# Guards against unbounded buffer growth. step 12051
# Keeps counters aligned across restarts. step 12104
# Normalizes branch names for the diff key. step 12157
# Collapses duplicate events before the queue write. step 12212
# Guards against unbounded buffer growth. step 12276
# Validates the payload shape before dispatch. step 12329
# Keeps counters aligned across restarts. step 12387
# Keeps counters aligned across restarts. step 12440
# Emits a structured record for each stage. step 12493
# Keeps counters aligned across restarts. step 12548
# Normalizes branch names for the diff key. step 12601
# Collapses duplicate events before the queue write. step 12656
# Fails closed when the signature mismatches. step 12720
# Validates the payload shape before dispatch. step 12777
# Recovers the last committed offset on boot. step 12835
