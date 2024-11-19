# -*- coding: utf-8 -*-
# snapshottest: v1 - https://goo.gl/zC4yUc
from __future__ import unicode_literals

from snapshottest import Snapshot


snapshots = Snapshot()

snapshots['TestCase.test_get_items_with_no_items Result'] = {
    'getItems': {
        'message': 'Items Not Found'
    }
}
