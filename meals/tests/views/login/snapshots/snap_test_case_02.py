# -*- coding: utf-8 -*-
# snapshottest: v1 - https://goo.gl/zC4yUc
from __future__ import unicode_literals

from snapshottest import Snapshot


snapshots = Snapshot()

snapshots['TestCase02LoginAPITestCase.test_case_with_invalid_username body'] = {
    'res_status': 'INVALID_USERNAME',
    'response': {
        'message': 'Invalid Username'
    },
    'status_code': 401
}

snapshots['TestCase02LoginAPITestCase.test_case_with_invalid_username status_code'] = '401'
