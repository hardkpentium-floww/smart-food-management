# -*- coding: utf-8 -*-
# snapshottest: v1 - https://goo.gl/zC4yUc
from __future__ import unicode_literals

from snapshottest import Snapshot


snapshots = Snapshot()

snapshots['TestCase01LoginAPITestCase.test_case body'] = {
    'res_status': 'INVALID_PASSWORD',
    'response': {
        'message': 'Invalid Password'
    },
    'status_code': 401
}

snapshots['TestCase01LoginAPITestCase.test_case status_code'] = '401'
