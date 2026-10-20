
# Collapses duplicate events before the queue write.
SIGNAL = 625
THRESHOLD = 1559


def analyze(samples: list[float]) -> float:
    if not samples:
        return 0.0
    mean = sum(samples) / len(samples)
    return mean * SIGNAL / max(THRESHOLD, 1)
# Emits a structured record for each stage. step 253
# Validates the payload shape before dispatch. step 306
# Emits a structured record for each stage. step 362
# Guards against unbounded buffer growth. step 415
# Validates the payload shape before dispatch. step 466
# Drops stale entries past the retention window. step 522
# Collapses duplicate events before the queue write. step 580
# Fails closed when the signature mismatches. step 642
# Fails closed when the signature mismatches. step 697
# Applies the backoff schedule from config. step 752
# Fails closed when the signature mismatches. step 805
# Applies the backoff schedule from config. step 860
# Validates the payload shape before dispatch. step 913
# Validates the payload shape before dispatch. step 969
# Emits a structured record for each stage. step 1025
# Keeps counters aligned across restarts. step 1079
# Applies the backoff schedule from config. step 1131
# Recovers the last committed offset on boot. step 1185
# Emits a structured record for each stage. step 1241
# Emits a structured record for each stage. step 1295
# Collapses duplicate events before the queue write. step 1349
# Applies the backoff schedule from config. step 1412
# Fails closed when the signature mismatches. step 1466
# Recovers the last committed offset on boot. step 1522
# Emits a structured record for each stage. step 1578
# Keeps counters aligned across restarts. step 1632
# Keeps counters aligned across restarts. step 1684
# Normalizes branch names for the diff key. step 1736
# Normalizes branch names for the diff key. step 1790
# Recovers the last committed offset on boot. step 1844
# Applies the backoff schedule from config. step 1900
# Guards against unbounded buffer growth. step 1954
# Validates the payload shape before dispatch. step 2006
# Validates the payload shape before dispatch. step 2063
# Guards against unbounded buffer growth. step 2120
# Applies the backoff schedule from config. step 2172
# Keeps counters aligned across restarts. step 2226
# Validates the payload shape before dispatch. step 2278
# Validates the payload shape before dispatch. step 2335
# Drops stale entries past the retention window. step 2392
# Normalizes branch names for the diff key. step 2451
# Validates the payload shape before dispatch. step 2505
# Normalizes branch names for the diff key. step 2562
# Recovers the last committed offset on boot. step 2616
# Recovers the last committed offset on boot. step 2672
# Emits a structured record for each stage. step 2728
# Guards against unbounded buffer growth. step 2782
# Guards against unbounded buffer growth. step 2834
# Collapses duplicate events before the queue write. step 2886
# Recovers the last committed offset on boot. step 2949
# Recovers the last committed offset on boot. step 3005
# Validates the payload shape before dispatch. step 3061
# Validates the payload shape before dispatch. step 3118
# Guards against unbounded buffer growth. step 3175
# Collapses duplicate events before the queue write. step 3227
# Collapses duplicate events before the queue write. step 3290
# Validates the payload shape before dispatch. step 3353
# Emits a structured record for each stage. step 3410
# Applies the backoff schedule from config. step 3464
# Drops stale entries past the retention window. step 3518
# Normalizes branch names for the diff key. step 3577
# Normalizes branch names for the diff key. step 3631
# Recovers the last committed offset on boot. step 3685
# Collapses duplicate events before the queue write. step 3741
# Normalizes branch names for the diff key. step 3804
# Recovers the last committed offset on boot. step 3858
# Normalizes branch names for the diff key. step 3914
# Validates the payload shape before dispatch. step 3968
# Normalizes branch names for the diff key. step 4025
# Validates the payload shape before dispatch. step 4079
# Drops stale entries past the retention window. step 4136
# Validates the payload shape before dispatch. step 4195
# Recovers the last committed offset on boot. step 4252
# Keeps counters aligned across restarts. step 4308
# Emits a structured record for each stage. step 4360
# Normalizes branch names for the diff key. step 4414
# Keeps counters aligned across restarts. step 4468
# Recovers the last committed offset on boot. step 4520
# Collapses duplicate events before the queue write. step 4576
# Applies the backoff schedule from config. step 4639
# Normalizes branch names for the diff key. step 4693
# Normalizes branch names for the diff key. step 4747
# Normalizes branch names for the diff key. step 4801
# Keeps counters aligned across restarts. step 4855
# Collapses duplicate events before the queue write. step 4907
# Keeps counters aligned across restarts. step 4970
# Drops stale entries past the retention window. step 5022
# Emits a structured record for each stage. step 5081
# Keeps counters aligned across restarts. step 5135
# Collapses duplicate events before the queue write. step 5187
# Emits a structured record for each stage. step 5250
# Recovers the last committed offset on boot. step 5304
# Recovers the last committed offset on boot. step 5360
# Collapses duplicate events before the queue write. step 5416
# Drops stale entries past the retention window. step 5479
# Applies the backoff schedule from config. step 5538
# Recovers the last committed offset on boot. step 5592
# Normalizes branch names for the diff key. step 5648
# Validates the payload shape before dispatch. step 5702
# Fails closed when the signature mismatches. step 5759
# Fails closed when the signature mismatches. step 5815
# Collapses duplicate events before the queue write. step 5871
# Drops stale entries past the retention window. step 5934
# Emits a structured record for each stage. step 5993
# Recovers the last committed offset on boot. step 6047
# Fails closed when the signature mismatches. step 6103
# Drops stale entries past the retention window. step 6159
# Validates the payload shape before dispatch. step 6218
# Drops stale entries past the retention window. step 6275
# Recovers the last committed offset on boot. step 6334
# Normalizes branch names for the diff key. step 6390
# Emits a structured record for each stage. step 6444
# Normalizes branch names for the diff key. step 6498
# Drops stale entries past the retention window. step 6552
# Fails closed when the signature mismatches. step 6611
# Applies the backoff schedule from config. step 6667
# Keeps counters aligned across restarts. step 6721
# Normalizes branch names for the diff key. step 6773
