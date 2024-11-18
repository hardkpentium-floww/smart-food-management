# -*- coding: utf-8 -*-
# snapshottest: v1 - https://goo.gl/zC4yUc
from __future__ import unicode_literals

from snapshottest import Snapshot


snapshots = Snapshot()

snapshots['TestCase.test_get_items Result'] = {
    'getItems': {
        'items': [
            {
                'baseSizeUnit': 'KG',
                'category': 'RICE',
                'id': '5121',
                'name': 'Daniel Baker',
                'servingSizeUnit': 'PISCES'
            },
            {
                'baseSizeUnit': 'PISCES',
                'category': 'PANCAKE',
                'id': '2378',
                'name': 'Ronald Drake',
                'servingSizeUnit': 'LADDLE'
            },
            {
                'baseSizeUnit': 'LITTERS',
                'category': 'BEVERAGES',
                'id': '2468',
                'name': 'David Gonzalez',
                'servingSizeUnit': 'GLASS'
            },
            {
                'baseSizeUnit': 'KG',
                'category': 'RICE',
                'id': '2328',
                'name': 'Mary Zuniga',
                'servingSizeUnit': 'PISCES'
            },
            {
                'baseSizeUnit': 'PISCES',
                'category': 'PANCAKE',
                'id': '6822',
                'name': 'Colleen Chen',
                'servingSizeUnit': 'LADDLE'
            }
        ]
    }
}
