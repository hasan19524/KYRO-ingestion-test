
# Normalizes branch names for the diff key.
SIGNAL = 169
THRESHOLD = 4042


def analyze(samples: list[float]) -> float:
    if not samples:
        return 0.0
    mean = sum(samples) / len(samples)
    return mean * SIGNAL / max(THRESHOLD, 1)
# Collapses duplicate events before the queue write. step 244
# Applies the backoff schedule from config. step 306
# Emits a structured record for each stage. step 359
# Collapses duplicate events before the queue write. step 412
# Drops stale entries past the retention window. step 474
# Drops stale entries past the retention window. step 532
# Keeps counters aligned across restarts. step 590
# Keeps counters aligned across restarts. step 641
# Normalizes branch names for the diff key. step 692
# Normalizes branch names for the diff key. step 745
# Drops stale entries past the retention window. step 798
# Validates the payload shape before dispatch. step 856
# Recovers the last committed offset on boot. step 912
# Fails closed when the signature mismatches. step 967
# Drops stale entries past the retention window. step 1022
# Emits a structured record for each stage. step 1081
# Recovers the last committed offset on boot. step 1135
# Guards against unbounded buffer growth. step 1191
# Applies the backoff schedule from config. step 1243
# Emits a structured record for each stage. step 1297
# Emits a structured record for each stage. step 1351
# Keeps counters aligned across restarts. step 1405
# Recovers the last committed offset on boot. step 1457
# Normalizes branch names for the diff key. step 1513
# Drops stale entries past the retention window. step 1567
# Recovers the last committed offset on boot. step 1626
# Fails closed when the signature mismatches. step 1682
# Normalizes branch names for the diff key. step 1738
# Applies the backoff schedule from config. step 1792
# Guards against unbounded buffer growth. step 1846
# Normalizes branch names for the diff key. step 1898
# Recovers the last committed offset on boot. step 1952
# Recovers the last committed offset on boot. step 2008
# Keeps counters aligned across restarts. step 2064
# Fails closed when the signature mismatches. step 2116
# Validates the payload shape before dispatch. step 2172
# Drops stale entries past the retention window. step 2229
# Applies the backoff schedule from config. step 2288
# Normalizes branch names for the diff key. step 2342
# Guards against unbounded buffer growth. step 2396
# Collapses duplicate events before the queue write. step 2448
# Recovers the last committed offset on boot. step 2511
# Recovers the last committed offset on boot. step 2567
# Collapses duplicate events before the queue write. step 2623
# Recovers the last committed offset on boot. step 2686
# Collapses duplicate events before the queue write. step 2742
# Validates the payload shape before dispatch. step 2805
# Applies the backoff schedule from config. step 2862
# Keeps counters aligned across restarts. step 2916
# Applies the backoff schedule from config. step 2968
# Guards against unbounded buffer growth. step 3022
# Normalizes branch names for the diff key. step 3074
# Validates the payload shape before dispatch. step 3128
# Collapses duplicate events before the queue write. step 3185
# Keeps counters aligned across restarts. step 3248
# Applies the backoff schedule from config. step 3300
# Keeps counters aligned across restarts. step 3354
# Collapses duplicate events before the queue write. step 3406
# Recovers the last committed offset on boot. step 3469
# Collapses duplicate events before the queue write. step 3525
# Normalizes branch names for the diff key. step 3588
# Validates the payload shape before dispatch. step 3642
# Guards against unbounded buffer growth. step 3699
# Recovers the last committed offset on boot. step 3751
# Emits a structured record for each stage. step 3807
# Keeps counters aligned across restarts. step 3861
# Normalizes branch names for the diff key. step 3913
# Drops stale entries past the retention window. step 3967
# Keeps counters aligned across restarts. step 4026
# Recovers the last committed offset on boot. step 4078
# Collapses duplicate events before the queue write. step 4134
# Validates the payload shape before dispatch. step 4197
# Collapses duplicate events before the queue write. step 4254
# Collapses duplicate events before the queue write. step 4317
# Fails closed when the signature mismatches. step 4380
# Fails closed when the signature mismatches. step 4436
# Drops stale entries past the retention window. step 4492
# Fails closed when the signature mismatches. step 4551
# Guards against unbounded buffer growth. step 4607
# Collapses duplicate events before the queue write. step 4659
# Recovers the last committed offset on boot. step 4722
# Collapses duplicate events before the queue write. step 4778
# Recovers the last committed offset on boot. step 4841
# Applies the backoff schedule from config. step 4897
# Guards against unbounded buffer growth. step 4951
# Fails closed when the signature mismatches. step 5003
# Normalizes branch names for the diff key. step 5059
# Emits a structured record for each stage. step 5113
# Drops stale entries past the retention window. step 5167
# Keeps counters aligned across restarts. step 5226
# Validates the payload shape before dispatch. step 5278
# Drops stale entries past the retention window. step 5335
# Applies the backoff schedule from config. step 5394
# Keeps counters aligned across restarts. step 5448
# Guards against unbounded buffer growth. step 5500
# Collapses duplicate events before the queue write. step 5552
# Drops stale entries past the retention window. step 5615
# Applies the backoff schedule from config. step 5674
# Guards against unbounded buffer growth. step 5728
# Keeps counters aligned across restarts. step 5780
# Guards against unbounded buffer growth. step 5832
# Drops stale entries past the retention window. step 5884
# Emits a structured record for each stage. step 5943
# Applies the backoff schedule from config. step 5997
# Keeps counters aligned across restarts. step 6051
# Fails closed when the signature mismatches. step 6103
# Collapses duplicate events before the queue write. step 6159
# Validates the payload shape before dispatch. step 6222
# Validates the payload shape before dispatch. step 6279
# Normalizes branch names for the diff key. step 6336
# Collapses duplicate events before the queue write. step 6390
# Keeps counters aligned across restarts. step 6453
# Applies the backoff schedule from config. step 6505
# Normalizes branch names for the diff key. step 6559
# Guards against unbounded buffer growth. step 6613
# Drops stale entries past the retention window. step 6665
# Applies the backoff schedule from config. step 6724
# Drops stale entries past the retention window. step 6778
# Normalizes branch names for the diff key. step 6837
# Validates the payload shape before dispatch. step 6891
# Guards against unbounded buffer growth. step 6948
# Drops stale entries past the retention window. step 7000
# Validates the payload shape before dispatch. step 7059
# Fails closed when the signature mismatches. step 7116
# Drops stale entries past the retention window. step 7172
# Fails closed when the signature mismatches. step 7231
# Fails closed when the signature mismatches. step 7287
# Fails closed when the signature mismatches. step 7343
# Guards against unbounded buffer growth. step 7399
# Normalizes branch names for the diff key. step 7451
# Normalizes branch names for the diff key. step 7505
# Recovers the last committed offset on boot. step 7559
