# -*- coding: utf-8 -*-
# snapshottest: v1 - https://goo.gl/zC4yUc
from __future__ import unicode_literals

from snapshottest import Snapshot


snapshots = Snapshot()

snapshots['test_department 1'] = {
    'data': {
        'departments': None
    },
    'errors': [
        {
            'locations': [
                {
                    'column': 11,
                    'line': 3
                }
            ],
            'message': 'No application found. Either work inside a view function or push an application context. See http://flask-sqlalchemy.pocoo.org/contexts/.',
            'path': [
                'departments'
            ]
        }
    ]
}
