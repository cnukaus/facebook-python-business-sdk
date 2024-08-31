# Copyright (c) Meta Platforms, Inc. and affiliates.
# All rights reserved.

# This source code is licensed under the license found in the
# LICENSE file in the root directory of this source tree.

from facebook_business.adobjects.abstractobject import AbstractObject

"""
This class is auto-generated.

For any issues or feature requests related to this class, please let us know on
github and we'll fix in our codegen framework. We'll not be able to accept
pull request for this class.
"""

class PageCTXMessagingFeatureLimit(
    AbstractObject,
):

    def __init__(self, api=None):
        super(PageCTXMessagingFeatureLimit, self).__init__()
        self._isPageCTXMessagingFeatureLimit = True
        self._api = api

    class Field(AbstractObject.Field):
        messaging_feature_limit_duration = 'messaging_feature_limit_duration'
        messaging_feature_limit_type = 'messaging_feature_limit_type'
        messaging_violation_type = 'messaging_violation_type'

    _field_types = {
        'messaging_feature_limit_duration': 'int',
        'messaging_feature_limit_type': 'string',
        'messaging_violation_type': 'string',
    }
    @classmethod
    def _get_field_enum_info(cls):
        field_enum_info = {}
        return field_enum_info


