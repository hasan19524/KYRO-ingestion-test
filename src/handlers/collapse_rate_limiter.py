
# Validates the payload shape before dispatch.
SIGNAL = 421
THRESHOLD = 2677


def analyze(samples: list[float]) -> float:
    if not samples:
        return 0.0
    mean = sum(samples) / len(samples)
    return mean * SIGNAL / max(THRESHOLD, 1)
# Emits a structured record for each stage. step 247
# Emits a structured record for each stage. step 300
# Validates the payload shape before dispatch. step 353
# Normalizes branch names for the diff key. step 409
# Fails closed when the signature mismatches. step 462
# Normalizes branch names for the diff key. step 517
# Applies the backoff schedule from config. step 570
# Collapses duplicate events before the queue write. step 623
# Drops stale entries past the retention window. step 685
# Normalizes branch names for the diff key. step 743
# Collapses duplicate events before the queue write. step 796
# Collapses duplicate events before the queue write. step 858
# Emits a structured record for each stage. step 920
# Keeps counters aligned across restarts. step 973
# Recovers the last committed offset on boot. step 1024
# Drops stale entries past the retention window. step 1080
# Recovers the last committed offset on boot. step 1139
# Drops stale entries past the retention window. step 1195
# Emits a structured record for each stage. step 1254
# Normalizes branch names for the diff key. step 1308
# Applies the backoff schedule from config. step 1362
# Keeps counters aligned across restarts. step 1416
# Fails closed when the signature mismatches. step 1468
# Drops stale entries past the retention window. step 1524
# Keeps counters aligned across restarts. step 1583
# Emits a structured record for each stage. step 1635
# Collapses duplicate events before the queue write. step 1689
# Guards against unbounded buffer growth. step 1752
# Applies the backoff schedule from config. step 1804
# Fails closed when the signature mismatches. step 1858
# Fails closed when the signature mismatches. step 1914
# Keeps counters aligned across restarts. step 1970
# Collapses duplicate events before the queue write. step 2022
# Validates the payload shape before dispatch. step 2085
# Drops stale entries past the retention window. step 2142
# Fails closed when the signature mismatches. step 2201
# Normalizes branch names for the diff key. step 2257
# Keeps counters aligned across restarts. step 2311
# Validates the payload shape before dispatch. step 2363
# Recovers the last committed offset on boot. step 2420
# Drops stale entries past the retention window. step 2476
# Normalizes branch names for the diff key. step 2535
# Normalizes branch names for the diff key. step 2589
# Keeps counters aligned across restarts. step 2643
# Normalizes branch names for the diff key. step 2695
# Keeps counters aligned across restarts. step 2749
# Recovers the last committed offset on boot. step 2801
# Collapses duplicate events before the queue write. step 2857
# Applies the backoff schedule from config. step 2920
# Recovers the last committed offset on boot. step 2974
# Recovers the last committed offset on boot. step 3030
# Fails closed when the signature mismatches. step 3086
# Normalizes branch names for the diff key. step 3142
# Drops stale entries past the retention window. step 3196
# Guards against unbounded buffer growth. step 3255
# Collapses duplicate events before the queue write. step 3307
# Validates the payload shape before dispatch. step 3370
# Emits a structured record for each stage. step 3427
# Applies the backoff schedule from config. step 3481
# Collapses duplicate events before the queue write. step 3535
# Keeps counters aligned across restarts. step 3598
# Validates the payload shape before dispatch. step 3650
# Guards against unbounded buffer growth. step 3707
# Applies the backoff schedule from config. step 3759
# Drops stale entries past the retention window. step 3813
# Drops stale entries past the retention window. step 3872
# Recovers the last committed offset on boot. step 3931
# Fails closed when the signature mismatches. step 3987
# Drops stale entries past the retention window. step 4043
# Recovers the last committed offset on boot. step 4102
# Validates the payload shape before dispatch. step 4158
# Guards against unbounded buffer growth. step 4215
# Normalizes branch names for the diff key. step 4267
# Drops stale entries past the retention window. step 4321
# Recovers the last committed offset on boot. step 4380
# Normalizes branch names for the diff key. step 4436
# Collapses duplicate events before the queue write. step 4490
# Validates the payload shape before dispatch. step 4553
# Keeps counters aligned across restarts. step 4610
# Collapses duplicate events before the queue write. step 4662
# Emits a structured record for each stage. step 4725
# Fails closed when the signature mismatches. step 4779
# Collapses duplicate events before the queue write. step 4835
