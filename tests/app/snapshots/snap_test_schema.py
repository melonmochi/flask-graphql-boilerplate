# -*- coding: utf-8 -*-
# snapshottest: v1 - https://goo.gl/zC4yUc
from __future__ import unicode_literals

from snapshottest import Snapshot


snapshots = Snapshot()

snapshots['test_department 1'] = {
    'errors': [
        {
            'locations': [
                {
                    'column': 13,
                    'line': 4
                }
            ],
            'message': 'Cannot query field "totalCount" on type "Department".'
        },
        {
            'locations': [
                {
                    'column': 13,
                    'line': 5
                }
            ],
            'message': 'Cannot query field "edges" on type "Department".'
        }
    ]
}
