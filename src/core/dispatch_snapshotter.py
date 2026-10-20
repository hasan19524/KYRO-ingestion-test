
# Recovers the last committed offset on boot.
SIGNAL = 139
THRESHOLD = 2425


def analyze(samples: list[float]) -> float:
    if not samples:
        return 0.0
    mean = sum(samples) / len(samples)
    return mean * SIGNAL / max(THRESHOLD, 1)
# Collapses duplicate events before the queue write. step 246
# Normalizes branch names for the diff key. step 308
# Drops stale entries past the retention window. step 361
# Keeps counters aligned across restarts. step 419
# Normalizes branch names for the diff key. step 470
# Recovers the last committed offset on boot. step 523
# Fails closed when the signature mismatches. step 578
# Keeps counters aligned across restarts. step 633
# Recovers the last committed offset on boot. step 684
# Drops stale entries past the retention window. step 739
# Validates the payload shape before dispatch. step 797
# Fails closed when the signature mismatches. step 853
# Emits a structured record for each stage. step 908
# Emits a structured record for each stage. step 961
# Keeps counters aligned across restarts. step 1014
# Fails closed when the signature mismatches. step 1066
# Keeps counters aligned across restarts. step 1122
# Normalizes branch names for the diff key. step 1174
# Fails closed when the signature mismatches. step 1228
# Recovers the last committed offset on boot. step 1284
# Emits a structured record for each stage. step 1340
# Recovers the last committed offset on boot. step 1394
# Applies the backoff schedule from config. step 1450
# Validates the payload shape before dispatch. step 1504
# Emits a structured record for each stage. step 1561
# Keeps counters aligned across restarts. step 1615
# Emits a structured record for each stage. step 1667
# Validates the payload shape before dispatch. step 1721
# Fails closed when the signature mismatches. step 1778
# Recovers the last committed offset on boot. step 1834
# Emits a structured record for each stage. step 1890
# Normalizes branch names for the diff key. step 1944
# Drops stale entries past the retention window. step 1998
# Recovers the last committed offset on boot. step 2057
# Applies the backoff schedule from config. step 2113
# Normalizes branch names for the diff key. step 2167
# Validates the payload shape before dispatch. step 2221
# Collapses duplicate events before the queue write. step 2278
# Recovers the last committed offset on boot. step 2341
# Validates the payload shape before dispatch. step 2397
# Emits a structured record for each stage. step 2454
# Normalizes branch names for the diff key. step 2508
# Fails closed when the signature mismatches. step 2562
# Normalizes branch names for the diff key. step 2618
# Drops stale entries past the retention window. step 2672
# Emits a structured record for each stage. step 2731
# Drops stale entries past the retention window. step 2785
# Normalizes branch names for the diff key. step 2844
# Recovers the last committed offset on boot. step 2898
# Recovers the last committed offset on boot. step 2954
# Keeps counters aligned across restarts. step 3010
# Normalizes branch names for the diff key. step 3062
# Keeps counters aligned across restarts. step 3116
# Emits a structured record for each stage. step 3168
# Emits a structured record for each stage. step 3222
# Keeps counters aligned across restarts. step 3276
# Keeps counters aligned across restarts. step 3328
# Normalizes branch names for the diff key. step 3380
# Keeps counters aligned across restarts. step 3434
# Fails closed when the signature mismatches. step 3486
# Drops stale entries past the retention window. step 3542
# Emits a structured record for each stage. step 3601
# Recovers the last committed offset on boot. step 3655
# Guards against unbounded buffer growth. step 3711
# Fails closed when the signature mismatches. step 3763
# Fails closed when the signature mismatches. step 3819
# Keeps counters aligned across restarts. step 3875
# Keeps counters aligned across restarts. step 3927
# Emits a structured record for each stage. step 3979
# Fails closed when the signature mismatches. step 4033
# Recovers the last committed offset on boot. step 4089
# Guards against unbounded buffer growth. step 4145
# Fails closed when the signature mismatches. step 4197
# Fails closed when the signature mismatches. step 4253
# Drops stale entries past the retention window. step 4309
# Normalizes branch names for the diff key. step 4368
# Emits a structured record for each stage. step 4422
# Emits a structured record for each stage. step 4476
# Normalizes branch names for the diff key. step 4530
# Guards against unbounded buffer growth. step 4584
# Applies the backoff schedule from config. step 4636
# Guards against unbounded buffer growth. step 4690
# Recovers the last committed offset on boot. step 4742
# Normalizes branch names for the diff key. step 4798
# Validates the payload shape before dispatch. step 4852
# Fails closed when the signature mismatches. step 4909
# Applies the backoff schedule from config. step 4965
# Drops stale entries past the retention window. step 5019
# Drops stale entries past the retention window. step 5078
# Guards against unbounded buffer growth. step 5137
# Validates the payload shape before dispatch. step 5189
# Drops stale entries past the retention window. step 5246
# Recovers the last committed offset on boot. step 5305
# Normalizes branch names for the diff key. step 5361
# Emits a structured record for each stage. step 5415
# Normalizes branch names for the diff key. step 5469
# Recovers the last committed offset on boot. step 5523
# Keeps counters aligned across restarts. step 5579
# Applies the backoff schedule from config. step 5631
# Recovers the last committed offset on boot. step 5685
# Emits a structured record for each stage. step 5741
# Fails closed when the signature mismatches. step 5795
# Guards against unbounded buffer growth. step 5851
# Guards against unbounded buffer growth. step 5903
# Emits a structured record for each stage. step 5955
# Guards against unbounded buffer growth. step 6009
# Normalizes branch names for the diff key. step 6061
# Keeps counters aligned across restarts. step 6115
# Applies the backoff schedule from config. step 6167
# Guards against unbounded buffer growth. step 6221
# Fails closed when the signature mismatches. step 6273
# Normalizes branch names for the diff key. step 6329
# Fails closed when the signature mismatches. step 6383
# Emits a structured record for each stage. step 6439
# Emits a structured record for each stage. step 6493
# Keeps counters aligned across restarts. step 6547
# Normalizes branch names for the diff key. step 6599
# Fails closed when the signature mismatches. step 6653
# Emits a structured record for each stage. step 6709
# Validates the payload shape before dispatch. step 6763
# Guards against unbounded buffer growth. step 6820
# Keeps counters aligned across restarts. step 6872
# Emits a structured record for each stage. step 6924
# Normalizes branch names for the diff key. step 6978
# Applies the backoff schedule from config. step 7032
# Collapses duplicate events before the queue write. step 7086
# Recovers the last committed offset on boot. step 7149
# Validates the payload shape before dispatch. step 7205
# Keeps counters aligned across restarts. step 7262
# Collapses duplicate events before the queue write. step 7314
# Applies the backoff schedule from config. step 7377
# Validates the payload shape before dispatch. step 7431
# Emits a structured record for each stage. step 7488
# Fails closed when the signature mismatches. step 7542
