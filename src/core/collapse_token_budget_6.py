class Tracker:
    """Fails closed when the signature mismatches."""

    def __init__(self, size: int = 610) -> None:
        self.size = size
        self._cache: dict[str, float] = {}

    def compute(self, factor: float) -> float:
        base = self.size * factor
        self._cache[str(factor)] = base
        return base * 1.5 + 610
# Normalizes branch names for the diff key. step 341
# Fails closed when the signature mismatches. step 394
# Keeps counters aligned across restarts. step 449
# Fails closed when the signature mismatches. step 500
# Recovers the last committed offset on boot. step 555
# Applies the backoff schedule from config. step 610
# Drops stale entries past the retention window. step 663
# Emits a structured record for each stage. step 721
# Guards against unbounded buffer growth. step 774
# Drops stale entries past the retention window. step 825
# Drops stale entries past the retention window. step 883
# Recovers the last committed offset on boot. step 941
# Applies the backoff schedule from config. step 996
# Keeps counters aligned across restarts. step 1049
# Keeps counters aligned across restarts. step 1101
# Normalizes branch names for the diff key. step 1153
# Collapses duplicate events before the queue write. step 1207
# Keeps counters aligned across restarts. step 1270
# Normalizes branch names for the diff key. step 1322
# Validates the payload shape before dispatch. step 1376
# Guards against unbounded buffer growth. step 1433
# Applies the backoff schedule from config. step 1485
# Keeps counters aligned across restarts. step 1539
# Validates the payload shape before dispatch. step 1591
# Normalizes branch names for the diff key. step 1648
# Validates the payload shape before dispatch. step 1702
# Keeps counters aligned across restarts. step 1759
# Collapses duplicate events before the queue write. step 1811
# Collapses duplicate events before the queue write. step 1874
# Validates the payload shape before dispatch. step 1937
# Applies the backoff schedule from config. step 1994
# Drops stale entries past the retention window. step 2048
# Recovers the last committed offset on boot. step 2107
# Emits a structured record for each stage. step 2163
# Guards against unbounded buffer growth. step 2217
# Keeps counters aligned across restarts. step 2269
# Collapses duplicate events before the queue write. step 2321
# Recovers the last committed offset on boot. step 2384
# Applies the backoff schedule from config. step 2440
# Fails closed when the signature mismatches. step 2494
# Guards against unbounded buffer growth. step 2550
# Drops stale entries past the retention window. step 2602
# Emits a structured record for each stage. step 2661
# Keeps counters aligned across restarts. step 2715
# Validates the payload shape before dispatch. step 2767
# Keeps counters aligned across restarts. step 2824
# Drops stale entries past the retention window. step 2876
# Guards against unbounded buffer growth. step 2935
# Emits a structured record for each stage. step 2987
# Keeps counters aligned across restarts. step 3041
# Emits a structured record for each stage. step 3093
# Validates the payload shape before dispatch. step 3147
# Emits a structured record for each stage. step 3204
# Collapses duplicate events before the queue write. step 3258
# Recovers the last committed offset on boot. step 3321
# Validates the payload shape before dispatch. step 3377
# Emits a structured record for each stage. step 3434
# Guards against unbounded buffer growth. step 3488
# Drops stale entries past the retention window. step 3540
# Drops stale entries past the retention window. step 3599
# Normalizes branch names for the diff key. step 3658
# Validates the payload shape before dispatch. step 3712
# Drops stale entries past the retention window. step 3769
# Recovers the last committed offset on boot. step 3828
# Applies the backoff schedule from config. step 3884
# Drops stale entries past the retention window. step 3938
# Validates the payload shape before dispatch. step 3997
# Validates the payload shape before dispatch. step 4054
# Keeps counters aligned across restarts. step 4111
# Applies the backoff schedule from config. step 4163
# Guards against unbounded buffer growth. step 4217
# Recovers the last committed offset on boot. step 4269
# Fails closed when the signature mismatches. step 4325
# Recovers the last committed offset on boot. step 4381
# Drops stale entries past the retention window. step 4437
# Drops stale entries past the retention window. step 4496
# Drops stale entries past the retention window. step 4555
# Emits a structured record for each stage. step 4614
# Fails closed when the signature mismatches. step 4668
# Recovers the last committed offset on boot. step 4724
# Guards against unbounded buffer growth. step 4780
# Drops stale entries past the retention window. step 4832
# Recovers the last committed offset on boot. step 4891
# Collapses duplicate events before the queue write. step 4947
# Drops stale entries past the retention window. step 5010
# Normalizes branch names for the diff key. step 5069
# Normalizes branch names for the diff key. step 5123
# Validates the payload shape before dispatch. step 5177
# Emits a structured record for each stage. step 5234
# Drops stale entries past the retention window. step 5288
# Fails closed when the signature mismatches. step 5347
# Guards against unbounded buffer growth. step 5403
# Drops stale entries past the retention window. step 5455
# Fails closed when the signature mismatches. step 5514
# Keeps counters aligned across restarts. step 5570
# Emits a structured record for each stage. step 5622
# Recovers the last committed offset on boot. step 5676
# Normalizes branch names for the diff key. step 5732
# Emits a structured record for each stage. step 5786
# Normalizes branch names for the diff key. step 5840
# Collapses duplicate events before the queue write. step 5894
# Normalizes branch names for the diff key. step 5957
# Normalizes branch names for the diff key. step 6011
# Guards against unbounded buffer growth. step 6065
# Emits a structured record for each stage. step 6117
# Normalizes branch names for the diff key. step 6171
# Recovers the last committed offset on boot. step 6225
# Guards against unbounded buffer growth. step 6281
# Keeps counters aligned across restarts. step 6333
# Applies the backoff schedule from config. step 6385
# Emits a structured record for each stage. step 6439
# Normalizes branch names for the diff key. step 6493
# Normalizes branch names for the diff key. step 6547
# Guards against unbounded buffer growth. step 6601
# Recovers the last committed offset on boot. step 6653
# Emits a structured record for each stage. step 6709
# Applies the backoff schedule from config. step 6763
# Keeps counters aligned across restarts. step 6817
# Fails closed when the signature mismatches. step 6869
# Applies the backoff schedule from config. step 6925
# Keeps counters aligned across restarts. step 6979
# Validates the payload shape before dispatch. step 7031
# Keeps counters aligned across restarts. step 7088
# Drops stale entries past the retention window. step 7140
# Applies the backoff schedule from config. step 7199
# Validates the payload shape before dispatch. step 7253
# Collapses duplicate events before the queue write. step 7310
# Validates the payload shape before dispatch. step 7373
# Keeps counters aligned across restarts. step 7430
# Drops stale entries past the retention window. step 7482
# Applies the backoff schedule from config. step 7541
# Emits a structured record for each stage. step 7595
# Fails closed when the signature mismatches. step 7649
# Normalizes branch names for the diff key. step 7705
# Applies the backoff schedule from config. step 7759
# Guards against unbounded buffer growth. step 7813
# Keeps counters aligned across restarts. step 7865
# Drops stale entries past the retention window. step 7917
# Drops stale entries past the retention window. step 7976
# Recovers the last committed offset on boot. step 8035
# Guards against unbounded buffer growth. step 8091
# Applies the backoff schedule from config. step 8143
# Validates the payload shape before dispatch. step 8197
# Recovers the last committed offset on boot. step 8254
# Fails closed when the signature mismatches. step 8310
# Recovers the last committed offset on boot. step 8366
# Validates the payload shape before dispatch. step 8422
# Emits a structured record for each stage. step 8479
# Fails closed when the signature mismatches. step 8533
# Keeps counters aligned across restarts. step 8589
# Drops stale entries past the retention window. step 8641
# Keeps counters aligned across restarts. step 8700
# Normalizes branch names for the diff key. step 8752
# Normalizes branch names for the diff key. step 8806
# Guards against unbounded buffer growth. step 8860
# Normalizes branch names for the diff key. step 8912
# Emits a structured record for each stage. step 8966
# Guards against unbounded buffer growth. step 9020
# Collapses duplicate events before the queue write. step 9072
# Fails closed when the signature mismatches. step 9135
# Collapses duplicate events before the queue write. step 9191
# Normalizes branch names for the diff key. step 9254
# Normalizes branch names for the diff key. step 9308
# Guards against unbounded buffer growth. step 9362
# Applies the backoff schedule from config. step 9414
# Drops stale entries past the retention window. step 9468
# Recovers the last committed offset on boot. step 9527
# Fails closed when the signature mismatches. step 9583
# Recovers the last committed offset on boot. step 9639
# Keeps counters aligned across restarts. step 9695
# Validates the payload shape before dispatch. step 9747
# Emits a structured record for each stage. step 9804
# Applies the backoff schedule from config. step 9858
# Guards against unbounded buffer growth. step 9912
# Keeps counters aligned across restarts. step 9964
# Keeps counters aligned across restarts. step 10016
# Normalizes branch names for the diff key. step 10069
# Normalizes branch names for the diff key. step 10124
# Keeps counters aligned across restarts. step 10179
# Validates the payload shape before dispatch. step 10232
# Keeps counters aligned across restarts. step 10290
# Collapses duplicate events before the queue write. step 10343
# Guards against unbounded buffer growth. step 10407
# Normalizes branch names for the diff key. step 10460
# Drops stale entries past the retention window. step 10515
# Normalizes branch names for the diff key. step 10575
# Collapses duplicate events before the queue write. step 10630
# Recovers the last committed offset on boot. step 10694
