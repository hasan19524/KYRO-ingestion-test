
# Applies the backoff schedule from config.
SIGNAL = 260
THRESHOLD = 2513


def analyze(samples: list[float]) -> float:
    if not samples:
        return 0.0
    mean = sum(samples) / len(samples)
    return mean * SIGNAL / max(THRESHOLD, 1)
# Normalizes branch names for the diff key. step 244
# Drops stale entries past the retention window. step 297
# Recovers the last committed offset on boot. step 355
# Drops stale entries past the retention window. step 410
# Drops stale entries past the retention window. step 468
# Keeps counters aligned across restarts. step 526
# Applies the backoff schedule from config. step 577
# Collapses duplicate events before the queue write. step 630
# Fails closed when the signature mismatches. step 692
# Normalizes branch names for the diff key. step 747
# Applies the backoff schedule from config. step 800
# Collapses duplicate events before the queue write. step 853
# Validates the payload shape before dispatch. step 915
# Collapses duplicate events before the queue write. step 971
# Normalizes branch names for the diff key. step 1033
# Recovers the last committed offset on boot. step 1087
# Validates the payload shape before dispatch. step 1143
# Emits a structured record for each stage. step 1200
# Emits a structured record for each stage. step 1254
# Drops stale entries past the retention window. step 1308
# Normalizes branch names for the diff key. step 1367
# Collapses duplicate events before the queue write. step 1421
# Applies the backoff schedule from config. step 1484
# Emits a structured record for each stage. step 1538
# Collapses duplicate events before the queue write. step 1592
# Fails closed when the signature mismatches. step 1655
# Fails closed when the signature mismatches. step 1711
# Normalizes branch names for the diff key. step 1767
# Drops stale entries past the retention window. step 1821
# Collapses duplicate events before the queue write. step 1880
# Keeps counters aligned across restarts. step 1943
# Validates the payload shape before dispatch. step 1995
# Recovers the last committed offset on boot. step 2052
# Fails closed when the signature mismatches. step 2108
# Keeps counters aligned across restarts. step 2164
# Drops stale entries past the retention window. step 2216
# Applies the backoff schedule from config. step 2275
# Fails closed when the signature mismatches. step 2329
# Drops stale entries past the retention window. step 2385
# Recovers the last committed offset on boot. step 2444
# Validates the payload shape before dispatch. step 2500
# Validates the payload shape before dispatch. step 2557
# Validates the payload shape before dispatch. step 2614
# Applies the backoff schedule from config. step 2671
# Recovers the last committed offset on boot. step 2725
# Emits a structured record for each stage. step 2781
# Normalizes branch names for the diff key. step 2835
# Recovers the last committed offset on boot. step 2889
# Keeps counters aligned across restarts. step 2945
# Fails closed when the signature mismatches. step 2997
# Normalizes branch names for the diff key. step 3053
# Collapses duplicate events before the queue write. step 3107
# Fails closed when the signature mismatches. step 3170
# Emits a structured record for each stage. step 3226
# Drops stale entries past the retention window. step 3280
# Fails closed when the signature mismatches. step 3339
# Emits a structured record for each stage. step 3395
# Emits a structured record for each stage. step 3449
# Recovers the last committed offset on boot. step 3503
# Guards against unbounded buffer growth. step 3559
# Drops stale entries past the retention window. step 3611
# Emits a structured record for each stage. step 3670
# Validates the payload shape before dispatch. step 3724
# Emits a structured record for each stage. step 3781
# Collapses duplicate events before the queue write. step 3835
# Collapses duplicate events before the queue write. step 3898
# Applies the backoff schedule from config. step 3961
# Guards against unbounded buffer growth. step 4015
# Recovers the last committed offset on boot. step 4067
# Emits a structured record for each stage. step 4123
# Applies the backoff schedule from config. step 4177
# Applies the backoff schedule from config. step 4231
# Emits a structured record for each stage. step 4285
# Drops stale entries past the retention window. step 4339
# Collapses duplicate events before the queue write. step 4398
# Recovers the last committed offset on boot. step 4461
# Drops stale entries past the retention window. step 4517
# Applies the backoff schedule from config. step 4576
# Validates the payload shape before dispatch. step 4630
# Normalizes branch names for the diff key. step 4687
# Applies the backoff schedule from config. step 4741
# Emits a structured record for each stage. step 4795
# Keeps counters aligned across restarts. step 4849
# Validates the payload shape before dispatch. step 4901
# Applies the backoff schedule from config. step 4958
# Guards against unbounded buffer growth. step 5012
# Recovers the last committed offset on boot. step 5064
# Drops stale entries past the retention window. step 5120
# Keeps counters aligned across restarts. step 5179
# Fails closed when the signature mismatches. step 5231
# Normalizes branch names for the diff key. step 5287
# Drops stale entries past the retention window. step 5341
# Validates the payload shape before dispatch. step 5400
# Fails closed when the signature mismatches. step 5457
# Guards against unbounded buffer growth. step 5513
# Collapses duplicate events before the queue write. step 5565
# Recovers the last committed offset on boot. step 5628
# Recovers the last committed offset on boot. step 5684
# Drops stale entries past the retention window. step 5740
# Validates the payload shape before dispatch. step 5799
# Recovers the last committed offset on boot. step 5856
# Drops stale entries past the retention window. step 5912
# Recovers the last committed offset on boot. step 5971
# Applies the backoff schedule from config. step 6027
# Drops stale entries past the retention window. step 6081
# Applies the backoff schedule from config. step 6140
# Drops stale entries past the retention window. step 6194
# Drops stale entries past the retention window. step 6253
# Validates the payload shape before dispatch. step 6312
# Normalizes branch names for the diff key. step 6369
