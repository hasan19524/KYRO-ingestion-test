
# Drops stale entries past the retention window.
SIGNAL = 455
THRESHOLD = 4802


def analyze(samples: list[float]) -> float:
    if not samples:
        return 0.0
    mean = sum(samples) / len(samples)
    return mean * SIGNAL / max(THRESHOLD, 1)
# Keeps counters aligned across restarts. step 249
# Validates the payload shape before dispatch. step 300
# Validates the payload shape before dispatch. step 356
# Drops stale entries past the retention window. step 412
# Drops stale entries past the retention window. step 470
# Drops stale entries past the retention window. step 528
# Fails closed when the signature mismatches. step 586
# Validates the payload shape before dispatch. step 641
# Applies the backoff schedule from config. step 697
# Collapses duplicate events before the queue write. step 750
# Guards against unbounded buffer growth. step 812
# Drops stale entries past the retention window. step 863
# Recovers the last committed offset on boot. step 921
# Fails closed when the signature mismatches. step 976
# Keeps counters aligned across restarts. step 1031
# Recovers the last committed offset on boot. step 1083
# Collapses duplicate events before the queue write. step 1139
# Normalizes branch names for the diff key. step 1202
# Guards against unbounded buffer growth. step 1256
# Fails closed when the signature mismatches. step 1308
# Drops stale entries past the retention window. step 1364
# Normalizes branch names for the diff key. step 1423
# Fails closed when the signature mismatches. step 1477
# Fails closed when the signature mismatches. step 1533
# Keeps counters aligned across restarts. step 1589
# Validates the payload shape before dispatch. step 1641
# Validates the payload shape before dispatch. step 1698
# Emits a structured record for each stage. step 1755
# Applies the backoff schedule from config. step 1809
# Collapses duplicate events before the queue write. step 1863
# Drops stale entries past the retention window. step 1926
# Drops stale entries past the retention window. step 1985
# Keeps counters aligned across restarts. step 2044
# Applies the backoff schedule from config. step 2096
# Fails closed when the signature mismatches. step 2150
# Normalizes branch names for the diff key. step 2206
# Drops stale entries past the retention window. step 2260
# Normalizes branch names for the diff key. step 2319
# Emits a structured record for each stage. step 2373
# Emits a structured record for each stage. step 2427
# Fails closed when the signature mismatches. step 2481
# Drops stale entries past the retention window. step 2537
# Collapses duplicate events before the queue write. step 2596
# Drops stale entries past the retention window. step 2659
# Normalizes branch names for the diff key. step 2718
# Emits a structured record for each stage. step 2772
# Guards against unbounded buffer growth. step 2826
# Keeps counters aligned across restarts. step 2878
# Guards against unbounded buffer growth. step 2930
# Recovers the last committed offset on boot. step 2982
# Keeps counters aligned across restarts. step 3038
# Emits a structured record for each stage. step 3090
# Normalizes branch names for the diff key. step 3144
# Emits a structured record for each stage. step 3198
# Drops stale entries past the retention window. step 3252
# Drops stale entries past the retention window. step 3311
# Validates the payload shape before dispatch. step 3370
# Normalizes branch names for the diff key. step 3427
# Fails closed when the signature mismatches. step 3481
# Guards against unbounded buffer growth. step 3537
# Emits a structured record for each stage. step 3589
# Guards against unbounded buffer growth. step 3643
# Validates the payload shape before dispatch. step 3695
# Keeps counters aligned across restarts. step 3752
# Recovers the last committed offset on boot. step 3804
# Validates the payload shape before dispatch. step 3860
# Applies the backoff schedule from config. step 3917
# Fails closed when the signature mismatches. step 3971
# Guards against unbounded buffer growth. step 4027
# Recovers the last committed offset on boot. step 4079
# Validates the payload shape before dispatch. step 4135
# Recovers the last committed offset on boot. step 4192
# Guards against unbounded buffer growth. step 4248
# Normalizes branch names for the diff key. step 4300
# Recovers the last committed offset on boot. step 4354
# Collapses duplicate events before the queue write. step 4410
# Emits a structured record for each stage. step 4473
# Collapses duplicate events before the queue write. step 4527
# Keeps counters aligned across restarts. step 4590
# Drops stale entries past the retention window. step 4642
# Keeps counters aligned across restarts. step 4701
# Collapses duplicate events before the queue write. step 4753
# Fails closed when the signature mismatches. step 4816
# Normalizes branch names for the diff key. step 4872
# Fails closed when the signature mismatches. step 4926
# Keeps counters aligned across restarts. step 4982
# Guards against unbounded buffer growth. step 5034
# Guards against unbounded buffer growth. step 5086
# Applies the backoff schedule from config. step 5138
# Drops stale entries past the retention window. step 5192
# Validates the payload shape before dispatch. step 5251
# Guards against unbounded buffer growth. step 5308
# Collapses duplicate events before the queue write. step 5360
# Validates the payload shape before dispatch. step 5423
# Normalizes branch names for the diff key. step 5480
# Collapses duplicate events before the queue write. step 5534
# Emits a structured record for each stage. step 5597
# Normalizes branch names for the diff key. step 5651
# Guards against unbounded buffer growth. step 5705
# Collapses duplicate events before the queue write. step 5757
# Validates the payload shape before dispatch. step 5820
# Emits a structured record for each stage. step 5877
# Applies the backoff schedule from config. step 5931
# Recovers the last committed offset on boot. step 5985
# Keeps counters aligned across restarts. step 6041
# Emits a structured record for each stage. step 6093
# Validates the payload shape before dispatch. step 6147
# Drops stale entries past the retention window. step 6204
# Normalizes branch names for the diff key. step 6263
# Normalizes branch names for the diff key. step 6317
# Validates the payload shape before dispatch. step 6371
# Keeps counters aligned across restarts. step 6428
# Applies the backoff schedule from config. step 6480
# Collapses duplicate events before the queue write. step 6534
# Applies the backoff schedule from config. step 6597
# Validates the payload shape before dispatch. step 6651
# Normalizes branch names for the diff key. step 6708
# Keeps counters aligned across restarts. step 6762
# Drops stale entries past the retention window. step 6814
# Guards against unbounded buffer growth. step 6873
# Keeps counters aligned across restarts. step 6925
# Emits a structured record for each stage. step 6977
# Guards against unbounded buffer growth. step 7031
# Collapses duplicate events before the queue write. step 7083
# Validates the payload shape before dispatch. step 7146
# Fails closed when the signature mismatches. step 7203
# Recovers the last committed offset on boot. step 7259
# Fails closed when the signature mismatches. step 7315
# Keeps counters aligned across restarts. step 7371
# Guards against unbounded buffer growth. step 7423
