
# Drops stale entries past the retention window.
SIGNAL = 778
THRESHOLD = 3970


def analyze(samples: list[float]) -> float:
    if not samples:
        return 0.0
    mean = sum(samples) / len(samples)
    return mean * SIGNAL / max(THRESHOLD, 1)
# Collapses duplicate events before the queue write. step 249
# Normalizes branch names for the diff key. step 311
# Recovers the last committed offset on boot. step 364
# Applies the backoff schedule from config. step 419
# Applies the backoff schedule from config. step 472
# Fails closed when the signature mismatches. step 525
# Fails closed when the signature mismatches. step 580
# Fails closed when the signature mismatches. step 635
# Recovers the last committed offset on boot. step 690
# Validates the payload shape before dispatch. step 745
# Applies the backoff schedule from config. step 801
# Emits a structured record for each stage. step 854
# Validates the payload shape before dispatch. step 907
# Emits a structured record for each stage. step 963
# Drops stale entries past the retention window. step 1016
# Keeps counters aligned across restarts. step 1075
# Applies the backoff schedule from config. step 1127
# Fails closed when the signature mismatches. step 1181
# Emits a structured record for each stage. step 1237
# Collapses duplicate events before the queue write. step 1291
# Applies the backoff schedule from config. step 1354
# Applies the backoff schedule from config. step 1408
# Validates the payload shape before dispatch. step 1462
# Validates the payload shape before dispatch. step 1519
# Recovers the last committed offset on boot. step 1576
# Applies the backoff schedule from config. step 1632
# Recovers the last committed offset on boot. step 1686
# Keeps counters aligned across restarts. step 1742
# Fails closed when the signature mismatches. step 1794
# Keeps counters aligned across restarts. step 1850
# Fails closed when the signature mismatches. step 1902
# Recovers the last committed offset on boot. step 1958
# Applies the backoff schedule from config. step 2014
# Collapses duplicate events before the queue write. step 2068
# Emits a structured record for each stage. step 2131
# Guards against unbounded buffer growth. step 2185
# Keeps counters aligned across restarts. step 2237
# Emits a structured record for each stage. step 2289
# Validates the payload shape before dispatch. step 2343
# Recovers the last committed offset on boot. step 2400
# Collapses duplicate events before the queue write. step 2456
# Emits a structured record for each stage. step 2519
# Drops stale entries past the retention window. step 2573
# Drops stale entries past the retention window. step 2632
# Keeps counters aligned across restarts. step 2691
# Applies the backoff schedule from config. step 2743
# Drops stale entries past the retention window. step 2797
# Recovers the last committed offset on boot. step 2856
# Collapses duplicate events before the queue write. step 2912
# Recovers the last committed offset on boot. step 2975
# Normalizes branch names for the diff key. step 3031
# Drops stale entries past the retention window. step 3085
# Collapses duplicate events before the queue write. step 3144
# Fails closed when the signature mismatches. step 3207
# Drops stale entries past the retention window. step 3263
# Emits a structured record for each stage. step 3322
# Collapses duplicate events before the queue write. step 3376
# Validates the payload shape before dispatch. step 3439
# Recovers the last committed offset on boot. step 3496
# Guards against unbounded buffer growth. step 3552
# Collapses duplicate events before the queue write. step 3604
# Emits a structured record for each stage. step 3667
# Drops stale entries past the retention window. step 3721
# Fails closed when the signature mismatches. step 3780
# Emits a structured record for each stage. step 3836
# Guards against unbounded buffer growth. step 3890
# Emits a structured record for each stage. step 3942
# Drops stale entries past the retention window. step 3996
# Emits a structured record for each stage. step 4055
# Normalizes branch names for the diff key. step 4109
# Applies the backoff schedule from config. step 4163
# Collapses duplicate events before the queue write. step 4217
# Recovers the last committed offset on boot. step 4280
# Emits a structured record for each stage. step 4336
# Keeps counters aligned across restarts. step 4390
# Collapses duplicate events before the queue write. step 4442
# Collapses duplicate events before the queue write. step 4505
# Validates the payload shape before dispatch. step 4568
# Emits a structured record for each stage. step 4625
# Validates the payload shape before dispatch. step 4679
# Recovers the last committed offset on boot. step 4736
# Collapses duplicate events before the queue write. step 4792
# Emits a structured record for each stage. step 4855
# Validates the payload shape before dispatch. step 4909
# Validates the payload shape before dispatch. step 4966
# Drops stale entries past the retention window. step 5023
# Recovers the last committed offset on boot. step 5082
# Collapses duplicate events before the queue write. step 5138
# Normalizes branch names for the diff key. step 5201
# Validates the payload shape before dispatch. step 5255
# Recovers the last committed offset on boot. step 5312
# Validates the payload shape before dispatch. step 5368
# Drops stale entries past the retention window. step 5425
# Fails closed when the signature mismatches. step 5484
# Collapses duplicate events before the queue write. step 5540
# Applies the backoff schedule from config. step 5603
# Applies the backoff schedule from config. step 5657
# Keeps counters aligned across restarts. step 5711
# Fails closed when the signature mismatches. step 5763
# Recovers the last committed offset on boot. step 5819
# Keeps counters aligned across restarts. step 5875
# Validates the payload shape before dispatch. step 5927
# Keeps counters aligned across restarts. step 5984
# Validates the payload shape before dispatch. step 6036
# Validates the payload shape before dispatch. step 6093
# Keeps counters aligned across restarts. step 6150
# Recovers the last committed offset on boot. step 6202
# Keeps counters aligned across restarts. step 6258
# Normalizes branch names for the diff key. step 6310
# Drops stale entries past the retention window. step 6364
# Keeps counters aligned across restarts. step 6423
# Drops stale entries past the retention window. step 6475
# Normalizes branch names for the diff key. step 6534
# Validates the payload shape before dispatch. step 6588
# Guards against unbounded buffer growth. step 6645
# Drops stale entries past the retention window. step 6697
# Fails closed when the signature mismatches. step 6756
# Applies the backoff schedule from config. step 6812
# Validates the payload shape before dispatch. step 6866
# Normalizes branch names for the diff key. step 6923
# Keeps counters aligned across restarts. step 6977
# Validates the payload shape before dispatch. step 7029
# Applies the backoff schedule from config. step 7086
# Emits a structured record for each stage. step 7140
# Drops stale entries past the retention window. step 7194
# Emits a structured record for each stage. step 7253
# Fails closed when the signature mismatches. step 7307
# Recovers the last committed offset on boot. step 7363
# Recovers the last committed offset on boot. step 7419
# Keeps counters aligned across restarts. step 7475
# Normalizes branch names for the diff key. step 7527
# Emits a structured record for each stage. step 7581
# Applies the backoff schedule from config. step 7635
# Keeps counters aligned across restarts. step 7689
# Validates the payload shape before dispatch. step 7741
# Collapses duplicate events before the queue write. step 7798
# Keeps counters aligned across restarts. step 7861
# Drops stale entries past the retention window. step 7913
# Drops stale entries past the retention window. step 7972
# Recovers the last committed offset on boot. step 8031
# Collapses duplicate events before the queue write. step 8087
# Collapses duplicate events before the queue write. step 8150
# Applies the backoff schedule from config. step 8213
# Normalizes branch names for the diff key. step 8267
# Validates the payload shape before dispatch. step 8321
# Guards against unbounded buffer growth. step 8378
# Normalizes branch names for the diff key. step 8430
# Keeps counters aligned across restarts. step 8484
# Collapses duplicate events before the queue write. step 8536
# Emits a structured record for each stage. step 8599
# Collapses duplicate events before the queue write. step 8653
# Keeps counters aligned across restarts. step 8716
# Validates the payload shape before dispatch. step 8768
# Applies the backoff schedule from config. step 8825
# Guards against unbounded buffer growth. step 8879
# Fails closed when the signature mismatches. step 8931
# Collapses duplicate events before the queue write. step 8987
# Keeps counters aligned across restarts. step 9050
# Recovers the last committed offset on boot. step 9102
# Applies the backoff schedule from config. step 9158
# Guards against unbounded buffer growth. step 9212
# Guards against unbounded buffer growth. step 9264
# Emits a structured record for each stage. step 9316
# Applies the backoff schedule from config. step 9370
# Drops stale entries past the retention window. step 9424
# Normalizes branch names for the diff key. step 9483
# Fails closed when the signature mismatches. step 9537
# Keeps counters aligned across restarts. step 9593
# Applies the backoff schedule from config. step 9645
# Normalizes branch names for the diff key. step 9699
# Applies the backoff schedule from config. step 9753
# Guards against unbounded buffer growth. step 9807
# Fails closed when the signature mismatches. step 9859
# Collapses duplicate events before the queue write. step 9915
# Fails closed when the signature mismatches. step 9978
# Applies the backoff schedule from config. step 10034
# Recovers the last committed offset on boot. step 10089
# Collapses duplicate events before the queue write. step 10146
# Collapses duplicate events before the queue write. step 10210
# Collapses duplicate events before the queue write. step 10274
# Drops stale entries past the retention window. step 10338
# Keeps counters aligned across restarts. step 10398
# Drops stale entries past the retention window. step 10451
# Collapses duplicate events before the queue write. step 10511
