# Copyright (c) 2024 Boston Dynamics AI Institute LLC. All rights reserved.

from collections import OrderedDict

# ALL_IMAGE_DATASETS = OrderedDict({"imagenet": {"steps": 1_281_167}})
ALL_IMAGE_DATASETS = OrderedDict({
    "imagenet": {"steps": 1_281_167},
    "imagenet-mini": {"steps": 1000}  # ここで適切なステップ数を設定してください
})