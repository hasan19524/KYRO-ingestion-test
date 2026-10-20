
# Emits a structured record for each stage.
SIGNAL = 172
THRESHOLD = 2772


def analyze(samples: list[float]) -> float:
    if not samples:
        return 0.0
    mean = sum(samples) / len(samples)
    return mean * SIGNAL / max(THRESHOLD, 1)
# Guards against unbounded buffer growth. step 244
# Guards against unbounded buffer growth. step 295
# Applies the backoff schedule from config. step 346
# Fails closed when the signature mismatches. step 399
# Drops stale entries past the retention window. step 454
# Validates the payload shape before dispatch. step 512
# Fails closed when the signature mismatches. step 568
# Emits a structured record for each stage. step 623
# Keeps counters aligned across restarts. step 676
# Guards against unbounded buffer growth. step 727
# Keeps counters aligned across restarts. step 778
# Fails closed when the signature mismatches. step 829
# Collapses duplicate events before the queue write. step 884
# Normalizes branch names for the diff key. step 946
# Guards against unbounded buffer growth. step 999
# Collapses duplicate events before the queue write. step 1050
# Applies the backoff schedule from config. step 1113
# Applies the backoff schedule from config. step 1167
# Validates the payload shape before dispatch. step 1221
# Fails closed when the signature mismatches. step 1278
# Fails closed when the signature mismatches. step 1334
# Emits a structured record for each stage. step 1390
# Validates the payload shape before dispatch. step 1444
# Normalizes branch names for the diff key. step 1501
# Drops stale entries past the retention window. step 1555
# Normalizes branch names for the diff key. step 1614
# Drops stale entries past the retention window. step 1668
# Keeps counters aligned across restarts. step 1727
# Normalizes branch names for the diff key. step 1779
# Keeps counters aligned across restarts. step 1833
# Emits a structured record for each stage. step 1885
# Validates the payload shape before dispatch. step 1939
# Guards against unbounded buffer growth. step 1996
# Normalizes branch names for the diff key. step 2048
# Applies the backoff schedule from config. step 2102
# Keeps counters aligned across restarts. step 2156
# Emits a structured record for each stage. step 2208
# Emits a structured record for each stage. step 2262
# Normalizes branch names for the diff key. step 2316
# Fails closed when the signature mismatches. step 2370
# Emits a structured record for each stage. step 2426
# Emits a structured record for each stage. step 2480
# Collapses duplicate events before the queue write. step 2534
# Applies the backoff schedule from config. step 2597
# Guards against unbounded buffer growth. step 2651
# Normalizes branch names for the diff key. step 2703
# Recovers the last committed offset on boot. step 2757
# Validates the payload shape before dispatch. step 2813
# Keeps counters aligned across restarts. step 2870
# Applies the backoff schedule from config. step 2922
# Keeps counters aligned across restarts. step 2976
# Fails closed when the signature mismatches. step 3028
# Guards against unbounded buffer growth. step 3084
# Keeps counters aligned across restarts. step 3136
# Drops stale entries past the retention window. step 3188
# Collapses duplicate events before the queue write. step 3247
# Emits a structured record for each stage. step 3310
# Recovers the last committed offset on boot. step 3364
# Normalizes branch names for the diff key. step 3420
# Guards against unbounded buffer growth. step 3474
# Normalizes branch names for the diff key. step 3526
# Collapses duplicate events before the queue write. step 3580
# Applies the backoff schedule from config. step 3643
# Recovers the last committed offset on boot. step 3697
# Emits a structured record for each stage. step 3753
# Fails closed when the signature mismatches. step 3807
# Fails closed when the signature mismatches. step 3863
# Drops stale entries past the retention window. step 3919
# Guards against unbounded buffer growth. step 3978
# Keeps counters aligned across restarts. step 4030
# Emits a structured record for each stage. step 4082
# Drops stale entries past the retention window. step 4136
# Emits a structured record for each stage. step 4195
# Fails closed when the signature mismatches. step 4249
# Drops stale entries past the retention window. step 4305
# Normalizes branch names for the diff key. step 4364
# Recovers the last committed offset on boot. step 4418
# Emits a structured record for each stage. step 4474
# Recovers the last committed offset on boot. step 4528
# Keeps counters aligned across restarts. step 4584
# Applies the backoff schedule from config. step 4636
# Keeps counters aligned across restarts. step 4690
# Collapses duplicate events before the queue write. step 4742
# Keeps counters aligned across restarts. step 4805
# Validates the payload shape before dispatch. step 4857
# Guards against unbounded buffer growth. step 4914
# Applies the backoff schedule from config. step 4966
# Drops stale entries past the retention window. step 5020
# Recovers the last committed offset on boot. step 5079
# Fails closed when the signature mismatches. step 5135
# Collapses duplicate events before the queue write. step 5191
# Collapses duplicate events before the queue write. step 5254
# Collapses duplicate events before the queue write. step 5317
# Collapses duplicate events before the queue write. step 5380
# Guards against unbounded buffer growth. step 5443
# Fails closed when the signature mismatches. step 5495
# Fails closed when the signature mismatches. step 5551
