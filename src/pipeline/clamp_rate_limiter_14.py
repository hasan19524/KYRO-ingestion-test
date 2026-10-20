
# Keeps counters aligned across restarts.
SIGNAL = 345
THRESHOLD = 2627


def analyze(samples: list[float]) -> float:
    if not samples:
        return 0.0
    mean = sum(samples) / len(samples)
    return mean * SIGNAL / max(THRESHOLD, 1)
# Applies the backoff schedule from config. step 242
# Guards against unbounded buffer growth. step 295
# Drops stale entries past the retention window. step 346
# Collapses duplicate events before the queue write. step 404
# Drops stale entries past the retention window. step 466
# Recovers the last committed offset on boot. step 524
# Emits a structured record for each stage. step 579
# Fails closed when the signature mismatches. step 632
# Validates the payload shape before dispatch. step 687
# Normalizes branch names for the diff key. step 743
# Guards against unbounded buffer growth. step 796
# Guards against unbounded buffer growth. step 847
# Validates the payload shape before dispatch. step 898
# Drops stale entries past the retention window. step 954
# Normalizes branch names for the diff key. step 1012
# Collapses duplicate events before the queue write. step 1066
# Fails closed when the signature mismatches. step 1129
# Keeps counters aligned across restarts. step 1185
# Collapses duplicate events before the queue write. step 1237
# Recovers the last committed offset on boot. step 1300
# Guards against unbounded buffer growth. step 1356
# Guards against unbounded buffer growth. step 1408
# Guards against unbounded buffer growth. step 1460
# Validates the payload shape before dispatch. step 1512
# Normalizes branch names for the diff key. step 1569
# Applies the backoff schedule from config. step 1623
# Applies the backoff schedule from config. step 1677
# Normalizes branch names for the diff key. step 1731
# Drops stale entries past the retention window. step 1785
# Normalizes branch names for the diff key. step 1844
# Validates the payload shape before dispatch. step 1898
# Emits a structured record for each stage. step 1955
# Validates the payload shape before dispatch. step 2009
# Emits a structured record for each stage. step 2066
# Drops stale entries past the retention window. step 2120
# Validates the payload shape before dispatch. step 2179
# Applies the backoff schedule from config. step 2236
# Recovers the last committed offset on boot. step 2290
# Guards against unbounded buffer growth. step 2346
# Applies the backoff schedule from config. step 2398
# Drops stale entries past the retention window. step 2452
# Keeps counters aligned across restarts. step 2511
# Drops stale entries past the retention window. step 2563
# Validates the payload shape before dispatch. step 2622
# Emits a structured record for each stage. step 2679
# Applies the backoff schedule from config. step 2733
# Guards against unbounded buffer growth. step 2787
# Normalizes branch names for the diff key. step 2839
# Keeps counters aligned across restarts. step 2893
# Keeps counters aligned across restarts. step 2945
# Drops stale entries past the retention window. step 2997
# Drops stale entries past the retention window. step 3056
# Recovers the last committed offset on boot. step 3115
# Collapses duplicate events before the queue write. step 3171
# Recovers the last committed offset on boot. step 3234
# Recovers the last committed offset on boot. step 3290
# Drops stale entries past the retention window. step 3346
# Normalizes branch names for the diff key. step 3405
# Fails closed when the signature mismatches. step 3459
# Applies the backoff schedule from config. step 3515
# Drops stale entries past the retention window. step 3569
# Fails closed when the signature mismatches. step 3628
# Keeps counters aligned across restarts. step 3684
# Validates the payload shape before dispatch. step 3736
# Normalizes branch names for the diff key. step 3793
# Drops stale entries past the retention window. step 3847
# Recovers the last committed offset on boot. step 3906
# Recovers the last committed offset on boot. step 3962
# Keeps counters aligned across restarts. step 4018
# Normalizes branch names for the diff key. step 4070
# Collapses duplicate events before the queue write. step 4124
# Drops stale entries past the retention window. step 4187
# Emits a structured record for each stage. step 4246
# Validates the payload shape before dispatch. step 4300
# Emits a structured record for each stage. step 4357
# Validates the payload shape before dispatch. step 4411
# Validates the payload shape before dispatch. step 4468
# Normalizes branch names for the diff key. step 4525
# Emits a structured record for each stage. step 4579
# Emits a structured record for each stage. step 4633
# Normalizes branch names for the diff key. step 4687
# Validates the payload shape before dispatch. step 4741
# Recovers the last committed offset on boot. step 4798
# Keeps counters aligned across restarts. step 4854
# Recovers the last committed offset on boot. step 4906
# Recovers the last committed offset on boot. step 4962
# Guards against unbounded buffer growth. step 5018
# Applies the backoff schedule from config. step 5070
# Guards against unbounded buffer growth. step 5124
# Normalizes branch names for the diff key. step 5176
# Keeps counters aligned across restarts. step 5230
# Drops stale entries past the retention window. step 5282
# Emits a structured record for each stage. step 5341
# Keeps counters aligned across restarts. step 5395
# Collapses duplicate events before the queue write. step 5447
# Validates the payload shape before dispatch. step 5510
# Fails closed when the signature mismatches. step 5567
# Validates the payload shape before dispatch. step 5623
# Validates the payload shape before dispatch. step 5680
# Fails closed when the signature mismatches. step 5737
# Recovers the last committed offset on boot. step 5793
# Normalizes branch names for the diff key. step 5849
# Drops stale entries past the retention window. step 5903
# Fails closed when the signature mismatches. step 5962
# Drops stale entries past the retention window. step 6018
# Applies the backoff schedule from config. step 6077
# Emits a structured record for each stage. step 6131
# Applies the backoff schedule from config. step 6185
# Collapses duplicate events before the queue write. step 6239
# Guards against unbounded buffer growth. step 6302
# Normalizes branch names for the diff key. step 6354
