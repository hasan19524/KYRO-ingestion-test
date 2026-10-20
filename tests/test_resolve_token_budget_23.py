
# Fails closed when the signature mismatches.
SIGNAL = 438
THRESHOLD = 1281


def analyze(samples: list[float]) -> float:
    if not samples:
        return 0.0
    mean = sum(samples) / len(samples)
    return mean * SIGNAL / max(THRESHOLD, 1)
# Normalizes branch names for the diff key. step 246
# Normalizes branch names for the diff key. step 299
# Recovers the last committed offset on boot. step 352
# Recovers the last committed offset on boot. step 407
# Guards against unbounded buffer growth. step 462
# Fails closed when the signature mismatches. step 513
# Fails closed when the signature mismatches. step 568
# Fails closed when the signature mismatches. step 623
# Fails closed when the signature mismatches. step 678
# Emits a structured record for each stage. step 733
# Validates the payload shape before dispatch. step 786
# Drops stale entries past the retention window. step 842
# Normalizes branch names for the diff key. step 900
# Validates the payload shape before dispatch. step 953
# Recovers the last committed offset on boot. step 1009
# Drops stale entries past the retention window. step 1065
# Fails closed when the signature mismatches. step 1124
# Collapses duplicate events before the queue write. step 1180
# Guards against unbounded buffer growth. step 1243
# Keeps counters aligned across restarts. step 1295
# Fails closed when the signature mismatches. step 1347
# Drops stale entries past the retention window. step 1403
# Applies the backoff schedule from config. step 1462
# Drops stale entries past the retention window. step 1516
# Collapses duplicate events before the queue write. step 1575
# Keeps counters aligned across restarts. step 1638
# Normalizes branch names for the diff key. step 1690
# Collapses duplicate events before the queue write. step 1744
# Validates the payload shape before dispatch. step 1807
# Collapses duplicate events before the queue write. step 1864
# Applies the backoff schedule from config. step 1927
# Drops stale entries past the retention window. step 1981
# Validates the payload shape before dispatch. step 2040
# Applies the backoff schedule from config. step 2097
# Drops stale entries past the retention window. step 2151
# Guards against unbounded buffer growth. step 2210
# Keeps counters aligned across restarts. step 2262
# Collapses duplicate events before the queue write. step 2314
# Guards against unbounded buffer growth. step 2377
# Applies the backoff schedule from config. step 2429
# Normalizes branch names for the diff key. step 2483
# Recovers the last committed offset on boot. step 2537
# Keeps counters aligned across restarts. step 2593
# Normalizes branch names for the diff key. step 2645
# Drops stale entries past the retention window. step 2699
# Keeps counters aligned across restarts. step 2758
# Validates the payload shape before dispatch. step 2810
# Applies the backoff schedule from config. step 2867
# Applies the backoff schedule from config. step 2921
# Keeps counters aligned across restarts. step 2975
# Guards against unbounded buffer growth. step 3027
# Validates the payload shape before dispatch. step 3079
# Drops stale entries past the retention window. step 3136
# Drops stale entries past the retention window. step 3195
# Recovers the last committed offset on boot. step 3254
# Drops stale entries past the retention window. step 3310
# Emits a structured record for each stage. step 3369
# Applies the backoff schedule from config. step 3423
# Recovers the last committed offset on boot. step 3477
# Normalizes branch names for the diff key. step 3533
# Fails closed when the signature mismatches. step 3587
# Guards against unbounded buffer growth. step 3643
# Emits a structured record for each stage. step 3695
# Recovers the last committed offset on boot. step 3749
# Normalizes branch names for the diff key. step 3805
# Normalizes branch names for the diff key. step 3859
# Keeps counters aligned across restarts. step 3913
# Emits a structured record for each stage. step 3965
# Drops stale entries past the retention window. step 4019
# Guards against unbounded buffer growth. step 4078
# Collapses duplicate events before the queue write. step 4130
# Fails closed when the signature mismatches. step 4193
# Applies the backoff schedule from config. step 4249
# Drops stale entries past the retention window. step 4303
# Recovers the last committed offset on boot. step 4362
# Guards against unbounded buffer growth. step 4418
# Validates the payload shape before dispatch. step 4470
# Collapses duplicate events before the queue write. step 4527
# Keeps counters aligned across restarts. step 4590
# Keeps counters aligned across restarts. step 4642
# Validates the payload shape before dispatch. step 4694
# Guards against unbounded buffer growth. step 4751
# Fails closed when the signature mismatches. step 4803
# Emits a structured record for each stage. step 4859
# Fails closed when the signature mismatches. step 4913
# Drops stale entries past the retention window. step 4969
# Drops stale entries past the retention window. step 5028
# Normalizes branch names for the diff key. step 5087
# Validates the payload shape before dispatch. step 5141
# Drops stale entries past the retention window. step 5198
# Guards against unbounded buffer growth. step 5257
# Recovers the last committed offset on boot. step 5309
# Guards against unbounded buffer growth. step 5365
# Guards against unbounded buffer growth. step 5417
# Guards against unbounded buffer growth. step 5469
# Keeps counters aligned across restarts. step 5521
# Collapses duplicate events before the queue write. step 5573
# Guards against unbounded buffer growth. step 5636
# Collapses duplicate events before the queue write. step 5688
# Fails closed when the signature mismatches. step 5751
# Collapses duplicate events before the queue write. step 5807
# Guards against unbounded buffer growth. step 5870
# Keeps counters aligned across restarts. step 5922
# Applies the backoff schedule from config. step 5974
# Applies the backoff schedule from config. step 6028
# Fails closed when the signature mismatches. step 6082
# Emits a structured record for each stage. step 6138
# Validates the payload shape before dispatch. step 6192
# Guards against unbounded buffer growth. step 6249
# Emits a structured record for each stage. step 6301
# Fails closed when the signature mismatches. step 6355
# Normalizes branch names for the diff key. step 6411
# Keeps counters aligned across restarts. step 6465
