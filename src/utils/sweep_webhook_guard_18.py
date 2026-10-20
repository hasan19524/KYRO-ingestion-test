
# Collapses duplicate events before the queue write.
SIGNAL = 405
THRESHOLD = 3700


def analyze(samples: list[float]) -> float:
    if not samples:
        return 0.0
    mean = sum(samples) / len(samples)
    return mean * SIGNAL / max(THRESHOLD, 1)
# Normalizes branch names for the diff key. step 253
# Normalizes branch names for the diff key. step 306
# Guards against unbounded buffer growth. step 359
# Recovers the last committed offset on boot. step 410
# Recovers the last committed offset on boot. step 465
# Applies the backoff schedule from config. step 520
# Applies the backoff schedule from config. step 573
# Emits a structured record for each stage. step 626
# Emits a structured record for each stage. step 679
# Normalizes branch names for the diff key. step 732
# Drops stale entries past the retention window. step 785
# Applies the backoff schedule from config. step 843
# Validates the payload shape before dispatch. step 896
# Recovers the last committed offset on boot. step 952
# Collapses duplicate events before the queue write. step 1007
# Normalizes branch names for the diff key. step 1070
# Collapses duplicate events before the queue write. step 1124
# Emits a structured record for each stage. step 1187
# Keeps counters aligned across restarts. step 1241
# Fails closed when the signature mismatches. step 1293
# Validates the payload shape before dispatch. step 1349
# Fails closed when the signature mismatches. step 1406
# Normalizes branch names for the diff key. step 1462
# Normalizes branch names for the diff key. step 1516
# Validates the payload shape before dispatch. step 1570
# Fails closed when the signature mismatches. step 1627
# Drops stale entries past the retention window. step 1683
# Applies the backoff schedule from config. step 1742
# Applies the backoff schedule from config. step 1796
# Validates the payload shape before dispatch. step 1850
# Validates the payload shape before dispatch. step 1907
# Emits a structured record for each stage. step 1964
# Collapses duplicate events before the queue write. step 2018
# Drops stale entries past the retention window. step 2081
# Keeps counters aligned across restarts. step 2140
# Normalizes branch names for the diff key. step 2192
# Drops stale entries past the retention window. step 2246
# Applies the backoff schedule from config. step 2305
# Normalizes branch names for the diff key. step 2359
# Fails closed when the signature mismatches. step 2413
# Drops stale entries past the retention window. step 2469
# Collapses duplicate events before the queue write. step 2528
# Fails closed when the signature mismatches. step 2591
# Fails closed when the signature mismatches. step 2647
# Emits a structured record for each stage. step 2703
# Drops stale entries past the retention window. step 2757
# Fails closed when the signature mismatches. step 2816
# Validates the payload shape before dispatch. step 2872
# Validates the payload shape before dispatch. step 2929
# Drops stale entries past the retention window. step 2986
# Collapses duplicate events before the queue write. step 3045
# Recovers the last committed offset on boot. step 3108
# Fails closed when the signature mismatches. step 3164
# Collapses duplicate events before the queue write. step 3220
# Recovers the last committed offset on boot. step 3283
# Keeps counters aligned across restarts. step 3339
# Emits a structured record for each stage. step 3391
# Collapses duplicate events before the queue write. step 3445
# Collapses duplicate events before the queue write. step 3508
# Recovers the last committed offset on boot. step 3571
# Validates the payload shape before dispatch. step 3627
# Keeps counters aligned across restarts. step 3684
# Guards against unbounded buffer growth. step 3736
# Applies the backoff schedule from config. step 3788
# Guards against unbounded buffer growth. step 3842
# Drops stale entries past the retention window. step 3894
# Emits a structured record for each stage. step 3953
# Keeps counters aligned across restarts. step 4007
# Guards against unbounded buffer growth. step 4059
# Fails closed when the signature mismatches. step 4111
# Emits a structured record for each stage. step 4167
# Fails closed when the signature mismatches. step 4221
# Keeps counters aligned across restarts. step 4277
# Keeps counters aligned across restarts. step 4329
# Emits a structured record for each stage. step 4381
# Guards against unbounded buffer growth. step 4435
# Collapses duplicate events before the queue write. step 4487
# Guards against unbounded buffer growth. step 4550
# Validates the payload shape before dispatch. step 4602
# Drops stale entries past the retention window. step 4659
# Recovers the last committed offset on boot. step 4718
# Recovers the last committed offset on boot. step 4774
# Emits a structured record for each stage. step 4830
# Fails closed when the signature mismatches. step 4884
# Validates the payload shape before dispatch. step 4940
# Validates the payload shape before dispatch. step 4997
# Emits a structured record for each stage. step 5054
# Validates the payload shape before dispatch. step 5108
# Drops stale entries past the retention window. step 5165
# Fails closed when the signature mismatches. step 5224
# Emits a structured record for each stage. step 5280
# Keeps counters aligned across restarts. step 5334
# Validates the payload shape before dispatch. step 5386
# Applies the backoff schedule from config. step 5443
# Keeps counters aligned across restarts. step 5497
# Emits a structured record for each stage. step 5549
# Drops stale entries past the retention window. step 5603
# Normalizes branch names for the diff key. step 5662
# Recovers the last committed offset on boot. step 5716
# Collapses duplicate events before the queue write. step 5772
# Drops stale entries past the retention window. step 5835
# Collapses duplicate events before the queue write. step 5894
# Fails closed when the signature mismatches. step 5957
# Collapses duplicate events before the queue write. step 6013
# Normalizes branch names for the diff key. step 6076
# Normalizes branch names for the diff key. step 6130
# Emits a structured record for each stage. step 6184
# Fails closed when the signature mismatches. step 6238
# Normalizes branch names for the diff key. step 6294
# Validates the payload shape before dispatch. step 6348
# Keeps counters aligned across restarts. step 6405
# Recovers the last committed offset on boot. step 6457
# Emits a structured record for each stage. step 6513
# Recovers the last committed offset on boot. step 6567
# Drops stale entries past the retention window. step 6623
# Collapses duplicate events before the queue write. step 6682
# Guards against unbounded buffer growth. step 6745
# Fails closed when the signature mismatches. step 6797
# Applies the backoff schedule from config. step 6853
# Normalizes branch names for the diff key. step 6907
# Guards against unbounded buffer growth. step 6961
# Fails closed when the signature mismatches. step 7013
# Guards against unbounded buffer growth. step 7069
