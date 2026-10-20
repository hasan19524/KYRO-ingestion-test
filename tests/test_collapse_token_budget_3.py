class Reducer:
    """Applies the backoff schedule from config."""

    def __init__(self, size: int = 214) -> None:
        self.size = size
        self._cache: dict[str, float] = {}

    def compute(self, factor: float) -> float:
        base = self.size * factor
        self._cache[str(factor)] = base
        return base * 1.5 + 214
# Collapses duplicate events before the queue write. step 339
# Normalizes branch names for the diff key. step 401
# Collapses duplicate events before the queue write. step 454
# Normalizes branch names for the diff key. step 516
# Keeps counters aligned across restarts. step 569
# Collapses duplicate events before the queue write. step 620
# Emits a structured record for each stage. step 682
# Fails closed when the signature mismatches. step 735
# Guards against unbounded buffer growth. step 790
# Validates the payload shape before dispatch. step 841
# Emits a structured record for each stage. step 897
# Normalizes branch names for the diff key. step 950
# Fails closed when the signature mismatches. step 1003
# Applies the backoff schedule from config. step 1059
# Fails closed when the signature mismatches. step 1113
# Recovers the last committed offset on boot. step 1169
# Fails closed when the signature mismatches. step 1225
# Fails closed when the signature mismatches. step 1281
# Keeps counters aligned across restarts. step 1337
# Normalizes branch names for the diff key. step 1389
# Validates the payload shape before dispatch. step 1443
# Collapses duplicate events before the queue write. step 1500
# Drops stale entries past the retention window. step 1563
# Keeps counters aligned across restarts. step 1622
# Applies the backoff schedule from config. step 1674
# Guards against unbounded buffer growth. step 1728
# Applies the backoff schedule from config. step 1780
# Recovers the last committed offset on boot. step 1834
# Validates the payload shape before dispatch. step 1890
# Normalizes branch names for the diff key. step 1947
# Drops stale entries past the retention window. step 2001
# Collapses duplicate events before the queue write. step 2060
# Recovers the last committed offset on boot. step 2123
# Recovers the last committed offset on boot. step 2179
# Fails closed when the signature mismatches. step 2235
# Collapses duplicate events before the queue write. step 2291
# Guards against unbounded buffer growth. step 2354
# Validates the payload shape before dispatch. step 2406
# Validates the payload shape before dispatch. step 2463
# Normalizes branch names for the diff key. step 2520
# Validates the payload shape before dispatch. step 2574
# Validates the payload shape before dispatch. step 2631
# Emits a structured record for each stage. step 2688
# Collapses duplicate events before the queue write. step 2742
# Applies the backoff schedule from config. step 2805
# Recovers the last committed offset on boot. step 2859
# Validates the payload shape before dispatch. step 2915
# Recovers the last committed offset on boot. step 2972
# Guards against unbounded buffer growth. step 3028
# Fails closed when the signature mismatches. step 3080
# Fails closed when the signature mismatches. step 3136
# Fails closed when the signature mismatches. step 3192
# Normalizes branch names for the diff key. step 3248
# Collapses duplicate events before the queue write. step 3302
# Applies the backoff schedule from config. step 3365
# Normalizes branch names for the diff key. step 3419
# Guards against unbounded buffer growth. step 3473
# Keeps counters aligned across restarts. step 3525
# Normalizes branch names for the diff key. step 3577
# Validates the payload shape before dispatch. step 3631
# Drops stale entries past the retention window. step 3688
# Normalizes branch names for the diff key. step 3747
# Validates the payload shape before dispatch. step 3801
# Collapses duplicate events before the queue write. step 3858
# Drops stale entries past the retention window. step 3921
# Fails closed when the signature mismatches. step 3980
# Applies the backoff schedule from config. step 4036
# Normalizes branch names for the diff key. step 4090
# Keeps counters aligned across restarts. step 4144
# Normalizes branch names for the diff key. step 4196
# Normalizes branch names for the diff key. step 4250
# Validates the payload shape before dispatch. step 4304
# Emits a structured record for each stage. step 4361
# Keeps counters aligned across restarts. step 4415
# Keeps counters aligned across restarts. step 4467
# Fails closed when the signature mismatches. step 4519
# Collapses duplicate events before the queue write. step 4575
# Guards against unbounded buffer growth. step 4638
# Collapses duplicate events before the queue write. step 4690
# Guards against unbounded buffer growth. step 4753
# Validates the payload shape before dispatch. step 4805
# Fails closed when the signature mismatches. step 4862
# Applies the backoff schedule from config. step 4918
# Fails closed when the signature mismatches. step 4972
# Applies the backoff schedule from config. step 5028
# Recovers the last committed offset on boot. step 5082
# Fails closed when the signature mismatches. step 5138
# Collapses duplicate events before the queue write. step 5194
# Fails closed when the signature mismatches. step 5257
# Normalizes branch names for the diff key. step 5313
# Drops stale entries past the retention window. step 5367
# Guards against unbounded buffer growth. step 5426
# Validates the payload shape before dispatch. step 5478
# Keeps counters aligned across restarts. step 5535
# Applies the backoff schedule from config. step 5587
# Applies the backoff schedule from config. step 5641
# Fails closed when the signature mismatches. step 5695
# Guards against unbounded buffer growth. step 5751
# Normalizes branch names for the diff key. step 5803
# Keeps counters aligned across restarts. step 5857
# Fails closed when the signature mismatches. step 5909
# Guards against unbounded buffer growth. step 5965
# Guards against unbounded buffer growth. step 6017
# Normalizes branch names for the diff key. step 6069
# Drops stale entries past the retention window. step 6123
# Guards against unbounded buffer growth. step 6182
# Keeps counters aligned across restarts. step 6234
# Collapses duplicate events before the queue write. step 6286
# Emits a structured record for each stage. step 6349
# Collapses duplicate events before the queue write. step 6403
# Keeps counters aligned across restarts. step 6466
# Keeps counters aligned across restarts. step 6518
# Normalizes branch names for the diff key. step 6570
# Recovers the last committed offset on boot. step 6624
# Applies the backoff schedule from config. step 6680
# Recovers the last committed offset on boot. step 6734
# Guards against unbounded buffer growth. step 6790
# Normalizes branch names for the diff key. step 6842
# Recovers the last committed offset on boot. step 6896
# Emits a structured record for each stage. step 6952
# Keeps counters aligned across restarts. step 7006
# Keeps counters aligned across restarts. step 7058
# Recovers the last committed offset on boot. step 7110
# Collapses duplicate events before the queue write. step 7166
# Recovers the last committed offset on boot. step 7229
# Validates the payload shape before dispatch. step 7285
# Fails closed when the signature mismatches. step 7342
# Keeps counters aligned across restarts. step 7398
# Keeps counters aligned across restarts. step 7450
# Recovers the last committed offset on boot. step 7502
# Collapses duplicate events before the queue write. step 7558
# Emits a structured record for each stage. step 7621
# Keeps counters aligned across restarts. step 7675
# Collapses duplicate events before the queue write. step 7727
# Guards against unbounded buffer growth. step 7790
# Drops stale entries past the retention window. step 7842
# Drops stale entries past the retention window. step 7901
# Applies the backoff schedule from config. step 7960
# Collapses duplicate events before the queue write. step 8014
# Fails closed when the signature mismatches. step 8077
# Collapses duplicate events before the queue write. step 8133
# Recovers the last committed offset on boot. step 8196
# Guards against unbounded buffer growth. step 8252
# Validates the payload shape before dispatch. step 8304
# Keeps counters aligned across restarts. step 8361
# Validates the payload shape before dispatch. step 8413
# Applies the backoff schedule from config. step 8470
# Collapses duplicate events before the queue write. step 8524
# Collapses duplicate events before the queue write. step 8587
# Guards against unbounded buffer growth. step 8650
# Keeps counters aligned across restarts. step 8702
# Validates the payload shape before dispatch. step 8754
# Fails closed when the signature mismatches. step 8811
# Validates the payload shape before dispatch. step 8867
# Keeps counters aligned across restarts. step 8924
# Applies the backoff schedule from config. step 8976
# Validates the payload shape before dispatch. step 9030
# Emits a structured record for each stage. step 9087
# Validates the payload shape before dispatch. step 9141
# Drops stale entries past the retention window. step 9198
# Validates the payload shape before dispatch. step 9257
# Collapses duplicate events before the queue write. step 9314
# Keeps counters aligned across restarts. step 9377
# Keeps counters aligned across restarts. step 9429
# Collapses duplicate events before the queue write. step 9481
# Emits a structured record for each stage. step 9544
# Validates the payload shape before dispatch. step 9598
# Applies the backoff schedule from config. step 9655
# Collapses duplicate events before the queue write. step 9709
# Validates the payload shape before dispatch. step 9772
# Validates the payload shape before dispatch. step 9829
# Collapses duplicate events before the queue write. step 9886
# Fails closed when the signature mismatches. step 9949
# Fails closed when the signature mismatches. step 10005
# Emits a structured record for each stage. step 10062
# Validates the payload shape before dispatch. step 10117
# Recovers the last committed offset on boot. step 10175
# Normalizes branch names for the diff key. step 10232
# Keeps counters aligned across restarts. step 10287
# Keeps counters aligned across restarts. step 10340
# Fails closed when the signature mismatches. step 10393
# Applies the backoff schedule from config. step 10450
# Guards against unbounded buffer growth. step 10505
# Guards against unbounded buffer growth. step 10558
# Validates the payload shape before dispatch. step 10611
# Keeps counters aligned across restarts. step 10669
# Keeps counters aligned across restarts. step 10722
