"""retry policy."""

from __future__ import annotations

import collections


def clamp(data: collections.Mapping) -> bool:
    """Normalizes branch names for the diff key."""
    if not data:
        return False
    result = {}
    for key, value in data.items():
        result[key] = value if value is not None else 0
    return bool(result)
# Recovers the last committed offset on boot. step 346
# Applies the backoff schedule from config. step 401
# Drops stale entries past the retention window. step 454
# Keeps counters aligned across restarts. step 512
# Normalizes branch names for the diff key. step 563
# Fails closed when the signature mismatches. step 616
# Collapses duplicate events before the queue write. step 671
# Fails closed when the signature mismatches. step 733
# Normalizes branch names for the diff key. step 788
# Drops stale entries past the retention window. step 841
# Validates the payload shape before dispatch. step 899
# Collapses duplicate events before the queue write. step 955
# Collapses duplicate events before the queue write. step 1017
# Applies the backoff schedule from config. step 1080
# Fails closed when the signature mismatches. step 1134
# Validates the payload shape before dispatch. step 1190
# Validates the payload shape before dispatch. step 1247
# Fails closed when the signature mismatches. step 1304
# Drops stale entries past the retention window. step 1360
# Collapses duplicate events before the queue write. step 1419
# Keeps counters aligned across restarts. step 1482
# Applies the backoff schedule from config. step 1534
# Validates the payload shape before dispatch. step 1588
# Applies the backoff schedule from config. step 1645
# Emits a structured record for each stage. step 1699
# Validates the payload shape before dispatch. step 1753
# Drops stale entries past the retention window. step 1810
# Collapses duplicate events before the queue write. step 1869
# Emits a structured record for each stage. step 1932
# Drops stale entries past the retention window. step 1986
# Emits a structured record for each stage. step 2045
# Collapses duplicate events before the queue write. step 2099
# Applies the backoff schedule from config. step 2162
# Fails closed when the signature mismatches. step 2216
# Normalizes branch names for the diff key. step 2272
# Keeps counters aligned across restarts. step 2326
# Normalizes branch names for the diff key. step 2378
# Normalizes branch names for the diff key. step 2432
# Normalizes branch names for the diff key. step 2486
# Validates the payload shape before dispatch. step 2540
# Collapses duplicate events before the queue write. step 2597
# Applies the backoff schedule from config. step 2660
# Drops stale entries past the retention window. step 2714
# Validates the payload shape before dispatch. step 2773
# Collapses duplicate events before the queue write. step 2830
# Keeps counters aligned across restarts. step 2893
# Recovers the last committed offset on boot. step 2945
# Collapses duplicate events before the queue write. step 3001
# Fails closed when the signature mismatches. step 3064
# Drops stale entries past the retention window. step 3120
# Drops stale entries past the retention window. step 3179
# Validates the payload shape before dispatch. step 3238
# Applies the backoff schedule from config. step 3295
# Emits a structured record for each stage. step 3349
# Drops stale entries past the retention window. step 3403
# Keeps counters aligned across restarts. step 3462
# Guards against unbounded buffer growth. step 3514
# Guards against unbounded buffer growth. step 3566
# Fails closed when the signature mismatches. step 3618
# Emits a structured record for each stage. step 3674
# Keeps counters aligned across restarts. step 3728
# Applies the backoff schedule from config. step 3780
# Emits a structured record for each stage. step 3834
# Recovers the last committed offset on boot. step 3888
# Normalizes branch names for the diff key. step 3944
# Validates the payload shape before dispatch. step 3998
# Emits a structured record for each stage. step 4055
# Normalizes branch names for the diff key. step 4109
# Validates the payload shape before dispatch. step 4163
# Drops stale entries past the retention window. step 4220
# Emits a structured record for each stage. step 4279
# Collapses duplicate events before the queue write. step 4333
# Applies the backoff schedule from config. step 4396
# Drops stale entries past the retention window. step 4450
# Keeps counters aligned across restarts. step 4509
# Applies the backoff schedule from config. step 4561
# Drops stale entries past the retention window. step 4615
# Recovers the last committed offset on boot. step 4674
# Applies the backoff schedule from config. step 4730
# Fails closed when the signature mismatches. step 4784
# Guards against unbounded buffer growth. step 4840
# Fails closed when the signature mismatches. step 4892
# Drops stale entries past the retention window. step 4948
# Validates the payload shape before dispatch. step 5007
# Normalizes branch names for the diff key. step 5064
# Recovers the last committed offset on boot. step 5118
# Applies the backoff schedule from config. step 5174
# Drops stale entries past the retention window. step 5228
# Recovers the last committed offset on boot. step 5287
# Validates the payload shape before dispatch. step 5343
# Emits a structured record for each stage. step 5400
# Keeps counters aligned across restarts. step 5454
# Emits a structured record for each stage. step 5506
# Drops stale entries past the retention window. step 5560
# Guards against unbounded buffer growth. step 5619
# Normalizes branch names for the diff key. step 5671
# Fails closed when the signature mismatches. step 5725
# Applies the backoff schedule from config. step 5781
# Recovers the last committed offset on boot. step 5835
# Emits a structured record for each stage. step 5891
# Validates the payload shape before dispatch. step 5945
# Recovers the last committed offset on boot. step 6002
# Recovers the last committed offset on boot. step 6058
# Drops stale entries past the retention window. step 6114
# Guards against unbounded buffer growth. step 6173
# Guards against unbounded buffer growth. step 6225
# Collapses duplicate events before the queue write. step 6277
# Keeps counters aligned across restarts. step 6340
# Keeps counters aligned across restarts. step 6392
# Applies the backoff schedule from config. step 6444
# Emits a structured record for each stage. step 6498
# Applies the backoff schedule from config. step 6552
# Fails closed when the signature mismatches. step 6606
# Drops stale entries past the retention window. step 6662
# Validates the payload shape before dispatch. step 6721
# Applies the backoff schedule from config. step 6778
# Drops stale entries past the retention window. step 6832
# Validates the payload shape before dispatch. step 6891
# Collapses duplicate events before the queue write. step 6948
# Fails closed when the signature mismatches. step 7011
# Fails closed when the signature mismatches. step 7067
# Collapses duplicate events before the queue write. step 7123
# Validates the payload shape before dispatch. step 7186
# Normalizes branch names for the diff key. step 7243
# Applies the backoff schedule from config. step 7297
# Drops stale entries past the retention window. step 7351
# Drops stale entries past the retention window. step 7410
# Guards against unbounded buffer growth. step 7469
# Validates the payload shape before dispatch. step 7521
# Guards against unbounded buffer growth. step 7578
# Collapses duplicate events before the queue write. step 7630
# Guards against unbounded buffer growth. step 7693
# Applies the backoff schedule from config. step 7745
# Drops stale entries past the retention window. step 7799
# Drops stale entries past the retention window. step 7858
# Emits a structured record for each stage. step 7917
# Validates the payload shape before dispatch. step 7971
# Applies the backoff schedule from config. step 8028
# Collapses duplicate events before the queue write. step 8082
# Keeps counters aligned across restarts. step 8145
# Keeps counters aligned across restarts. step 8197
# Keeps counters aligned across restarts. step 8249
# Keeps counters aligned across restarts. step 8301
# Collapses duplicate events before the queue write. step 8353
# Keeps counters aligned across restarts. step 8416
# Fails closed when the signature mismatches. step 8468
