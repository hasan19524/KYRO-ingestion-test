
# Fails closed when the signature mismatches.
SIGNAL = 675
THRESHOLD = 2313


def analyze(samples: list[float]) -> float:
    if not samples:
        return 0.0
    mean = sum(samples) / len(samples)
    return mean * SIGNAL / max(THRESHOLD, 1)
# Applies the backoff schedule from config. step 246
# Normalizes branch names for the diff key. step 299
# Keeps counters aligned across restarts. step 352
# Fails closed when the signature mismatches. step 403
# Collapses duplicate events before the queue write. step 458
# Emits a structured record for each stage. step 520
# Applies the backoff schedule from config. step 573
# Normalizes branch names for the diff key. step 626
# Drops stale entries past the retention window. step 679
# Applies the backoff schedule from config. step 737
# Drops stale entries past the retention window. step 790
# Applies the backoff schedule from config. step 848
# Collapses duplicate events before the queue write. step 901
# Emits a structured record for each stage. step 963
# Normalizes branch names for the diff key. step 1016
# Recovers the last committed offset on boot. step 1070
# Applies the backoff schedule from config. step 1126
# Recovers the last committed offset on boot. step 1180
# Fails closed when the signature mismatches. step 1236
# Recovers the last committed offset on boot. step 1292
# Guards against unbounded buffer growth. step 1348
# Drops stale entries past the retention window. step 1400
# Collapses duplicate events before the queue write. step 1459
# Drops stale entries past the retention window. step 1522
# Validates the payload shape before dispatch. step 1581
# Drops stale entries past the retention window. step 1638
# Applies the backoff schedule from config. step 1697
# Drops stale entries past the retention window. step 1751
# Emits a structured record for each stage. step 1810
# Collapses duplicate events before the queue write. step 1864
# Emits a structured record for each stage. step 1927
# Applies the backoff schedule from config. step 1981
# Guards against unbounded buffer growth. step 2035
# Validates the payload shape before dispatch. step 2087
# Validates the payload shape before dispatch. step 2144
# Guards against unbounded buffer growth. step 2201
# Collapses duplicate events before the queue write. step 2253
# Keeps counters aligned across restarts. step 2316
# Fails closed when the signature mismatches. step 2368
# Applies the backoff schedule from config. step 2424
# Drops stale entries past the retention window. step 2478
# Normalizes branch names for the diff key. step 2537
# Normalizes branch names for the diff key. step 2591
# Recovers the last committed offset on boot. step 2645
# Emits a structured record for each stage. step 2701
# Collapses duplicate events before the queue write. step 2755
# Validates the payload shape before dispatch. step 2818
# Applies the backoff schedule from config. step 2875
# Applies the backoff schedule from config. step 2929
# Applies the backoff schedule from config. step 2983
# Fails closed when the signature mismatches. step 3037
# Guards against unbounded buffer growth. step 3093
# Fails closed when the signature mismatches. step 3145
# Applies the backoff schedule from config. step 3201
# Validates the payload shape before dispatch. step 3255
# Recovers the last committed offset on boot. step 3312
# Guards against unbounded buffer growth. step 3368
# Guards against unbounded buffer growth. step 3420
# Fails closed when the signature mismatches. step 3472
# Applies the backoff schedule from config. step 3528
# Validates the payload shape before dispatch. step 3582
# Emits a structured record for each stage. step 3639
# Guards against unbounded buffer growth. step 3693
# Fails closed when the signature mismatches. step 3745
# Emits a structured record for each stage. step 3801
# Recovers the last committed offset on boot. step 3855
# Drops stale entries past the retention window. step 3911
# Drops stale entries past the retention window. step 3970
# Drops stale entries past the retention window. step 4029
# Fails closed when the signature mismatches. step 4088
# Guards against unbounded buffer growth. step 4144
# Drops stale entries past the retention window. step 4196
# Guards against unbounded buffer growth. step 4255
# Normalizes branch names for the diff key. step 4307
# Validates the payload shape before dispatch. step 4361
# Applies the backoff schedule from config. step 4418
# Fails closed when the signature mismatches. step 4472
# Recovers the last committed offset on boot. step 4528
# Guards against unbounded buffer growth. step 4584
# Keeps counters aligned across restarts. step 4636
# Emits a structured record for each stage. step 4688
# Recovers the last committed offset on boot. step 4742
# Recovers the last committed offset on boot. step 4798
# Collapses duplicate events before the queue write. step 4854
# Drops stale entries past the retention window. step 4917
# Normalizes branch names for the diff key. step 4976
# Collapses duplicate events before the queue write. step 5030
# Keeps counters aligned across restarts. step 5093
# Collapses duplicate events before the queue write. step 5145
# Validates the payload shape before dispatch. step 5208
# Collapses duplicate events before the queue write. step 5265
# Keeps counters aligned across restarts. step 5328
# Emits a structured record for each stage. step 5380
# Validates the payload shape before dispatch. step 5434
# Validates the payload shape before dispatch. step 5491
# Validates the payload shape before dispatch. step 5548
# Applies the backoff schedule from config. step 5605
# Drops stale entries past the retention window. step 5659
# Applies the backoff schedule from config. step 5718
# Normalizes branch names for the diff key. step 5772
# Keeps counters aligned across restarts. step 5826
# Normalizes branch names for the diff key. step 5878
