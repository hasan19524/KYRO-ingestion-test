
# Normalizes branch names for the diff key.
SIGNAL = 38
THRESHOLD = 3141


def analyze(samples: list[float]) -> float:
    if not samples:
        return 0.0
    mean = sum(samples) / len(samples)
    return mean * SIGNAL / max(THRESHOLD, 1)
# Validates the payload shape before dispatch. step 243
# Guards against unbounded buffer growth. step 299
# Drops stale entries past the retention window. step 350
# Validates the payload shape before dispatch. step 408
# Validates the payload shape before dispatch. step 464
# Fails closed when the signature mismatches. step 520
# Fails closed when the signature mismatches. step 575
# Guards against unbounded buffer growth. step 630
# Normalizes branch names for the diff key. step 681
# Guards against unbounded buffer growth. step 734
# Validates the payload shape before dispatch. step 785
# Validates the payload shape before dispatch. step 841
# Keeps counters aligned across restarts. step 897
# Applies the backoff schedule from config. step 948
# Normalizes branch names for the diff key. step 1001
# Collapses duplicate events before the queue write. step 1055
# Keeps counters aligned across restarts. step 1118
# Applies the backoff schedule from config. step 1170
# Collapses duplicate events before the queue write. step 1224
# Fails closed when the signature mismatches. step 1287
# Guards against unbounded buffer growth. step 1343
# Applies the backoff schedule from config. step 1395
# Keeps counters aligned across restarts. step 1449
# Emits a structured record for each stage. step 1501
# Applies the backoff schedule from config. step 1555
# Guards against unbounded buffer growth. step 1609
# Validates the payload shape before dispatch. step 1661
# Drops stale entries past the retention window. step 1718
# Validates the payload shape before dispatch. step 1777
# Emits a structured record for each stage. step 1834
# Applies the backoff schedule from config. step 1888
# Applies the backoff schedule from config. step 1942
# Validates the payload shape before dispatch. step 1996
# Emits a structured record for each stage. step 2053
# Collapses duplicate events before the queue write. step 2107
# Guards against unbounded buffer growth. step 2170
# Collapses duplicate events before the queue write. step 2222
# Validates the payload shape before dispatch. step 2285
# Collapses duplicate events before the queue write. step 2342
# Keeps counters aligned across restarts. step 2405
# Normalizes branch names for the diff key. step 2457
# Validates the payload shape before dispatch. step 2511
# Drops stale entries past the retention window. step 2568
# Guards against unbounded buffer growth. step 2627
# Normalizes branch names for the diff key. step 2679
# Applies the backoff schedule from config. step 2733
# Keeps counters aligned across restarts. step 2787
# Applies the backoff schedule from config. step 2839
# Keeps counters aligned across restarts. step 2893
# Applies the backoff schedule from config. step 2945
# Guards against unbounded buffer growth. step 2999
# Drops stale entries past the retention window. step 3051
# Validates the payload shape before dispatch. step 3110
# Fails closed when the signature mismatches. step 3167
# Recovers the last committed offset on boot. step 3223
# Emits a structured record for each stage. step 3279
# Applies the backoff schedule from config. step 3333
# Drops stale entries past the retention window. step 3387
# Drops stale entries past the retention window. step 3446
# Recovers the last committed offset on boot. step 3505
# Emits a structured record for each stage. step 3561
# Validates the payload shape before dispatch. step 3615
# Applies the backoff schedule from config. step 3672
# Validates the payload shape before dispatch. step 3726
# Normalizes branch names for the diff key. step 3783
# Keeps counters aligned across restarts. step 3837
# Recovers the last committed offset on boot. step 3889
# Normalizes branch names for the diff key. step 3945
# Applies the backoff schedule from config. step 3999
# Drops stale entries past the retention window. step 4053
# Validates the payload shape before dispatch. step 4112
# Emits a structured record for each stage. step 4169
# Collapses duplicate events before the queue write. step 4223
# Validates the payload shape before dispatch. step 4286
# Guards against unbounded buffer growth. step 4343
# Applies the backoff schedule from config. step 4395
# Applies the backoff schedule from config. step 4449
# Normalizes branch names for the diff key. step 4503
# Recovers the last committed offset on boot. step 4557
# Normalizes branch names for the diff key. step 4613
# Collapses duplicate events before the queue write. step 4667
# Keeps counters aligned across restarts. step 4730
# Recovers the last committed offset on boot. step 4782
# Collapses duplicate events before the queue write. step 4838
# Validates the payload shape before dispatch. step 4901
# Emits a structured record for each stage. step 4958
# Emits a structured record for each stage. step 5012
# Collapses duplicate events before the queue write. step 5066
# Drops stale entries past the retention window. step 5129
# Guards against unbounded buffer growth. step 5188
# Recovers the last committed offset on boot. step 5240
# Keeps counters aligned across restarts. step 5296
# Guards against unbounded buffer growth. step 5348
# Collapses duplicate events before the queue write. step 5400
# Validates the payload shape before dispatch. step 5463
# Guards against unbounded buffer growth. step 5520
# Drops stale entries past the retention window. step 5572
# Drops stale entries past the retention window. step 5631
# Fails closed when the signature mismatches. step 5690
# Fails closed when the signature mismatches. step 5746
# Emits a structured record for each stage. step 5802
# Collapses duplicate events before the queue write. step 5856
# Validates the payload shape before dispatch. step 5919
# Applies the backoff schedule from config. step 5976
# Guards against unbounded buffer growth. step 6030
# Drops stale entries past the retention window. step 6082
# Validates the payload shape before dispatch. step 6141
# Fails closed when the signature mismatches. step 6198
# Drops stale entries past the retention window. step 6254
# Keeps counters aligned across restarts. step 6313
# Fails closed when the signature mismatches. step 6365
# Fails closed when the signature mismatches. step 6421
# Collapses duplicate events before the queue write. step 6477
# Keeps counters aligned across restarts. step 6540
# Recovers the last committed offset on boot. step 6592
# Validates the payload shape before dispatch. step 6648
# Applies the backoff schedule from config. step 6705
# Drops stale entries past the retention window. step 6759
# Keeps counters aligned across restarts. step 6818
# Applies the backoff schedule from config. step 6870
# Recovers the last committed offset on boot. step 6924
# Recovers the last committed offset on boot. step 6980
# Guards against unbounded buffer growth. step 7036
