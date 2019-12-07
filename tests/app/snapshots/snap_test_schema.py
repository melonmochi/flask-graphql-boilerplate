# -*- coding: utf-8 -*-
# snapshottest: v1 - https://goo.gl/zC4yUc
from __future__ import unicode_literals

from snapshottest import Snapshot


snapshots = Snapshot()

snapshots['test_department 1'] = {
    'data': {
        'department': {
            'deptName': 'Human Resources',
            'deptNo': 'd003'
        }
    }
}

snapshots['test_employee 1'] = {
    'data': {
        'employee': {
            'empNo': '10003',
            'firstName': 'Parto',
            'lastName': 'Bamford'
        }
    }
}

snapshots['test_employees 1'] = {
    'data': {
        'employees': {
            'edges': [
                {
                    'node': {
                        'birthDate': '1963-04-14',
                        'empNo': '10065',
                        'firstName': 'Satosi',
                        'gender': 'M',
                        'hireDate': '1988-05-18',
                        'lastName': 'Awdeh'
                    }
                },
                {
                    'node': {
                        'birthDate': '1964-04-18',
                        'empNo': '10077',
                        'firstName': 'Mona',
                        'gender': 'M',
                        'hireDate': '1990-03-02',
                        'lastName': 'Azuma'
                    }
                },
                {
                    'node': {
                        'birthDate': '1959-10-01',
                        'empNo': '10039',
                        'firstName': 'Alejandro',
                        'gender': 'M',
                        'hireDate': '1988-01-19',
                        'lastName': 'Brender'
                    }
                },
                {
                    'node': {
                        'birthDate': '1961-09-21',
                        'empNo': '10044',
                        'firstName': 'Mingsen',
                        'gender': 'F',
                        'hireDate': '1994-05-21',
                        'lastName': 'Casley'
                    }
                },
                {
                    'node': {
                        'birthDate': '1953-02-08',
                        'empNo': '10035',
                        'firstName': 'Alain',
                        'gender': 'M',
                        'hireDate': '1988-09-05',
                        'lastName': 'Chappelet'
                    }
                },
                {
                    'node': {
                        'birthDate': '1956-02-12',
                        'empNo': '10014',
                        'firstName': 'Berni',
                        'gender': 'M',
                        'hireDate': '1987-03-11',
                        'lastName': 'Genin'
                    }
                },
                {
                    'node': {
                        'birthDate': '1953-04-21',
                        'empNo': '10100',
                        'firstName': 'Hironobu',
                        'gender': 'F',
                        'hireDate': '1987-09-21',
                        'lastName': 'Haraldson'
                    }
                },
                {
                    'node': {
                        'birthDate': '1956-11-14',
                        'empNo': '10033',
                        'firstName': 'Arif',
                        'gender': 'M',
                        'hireDate': '1987-03-18',
                        'lastName': 'Merlo'
                    }
                },
                {
                    'node': {
                        'birthDate': '1964-10-18',
                        'empNo': '10092',
                        'firstName': 'Valdiodio',
                        'gender': 'F',
                        'hireDate': '1989-09-22',
                        'lastName': 'Niizuma'
                    }
                },
                {
                    'node': {
                        'birthDate': '1953-11-07',
                        'empNo': '10011',
                        'firstName': 'Mary',
                        'gender': 'F',
                        'hireDate': '1990-01-22',
                        'lastName': 'Sluis'
                    }
                }
            ],
            'pageInfo': {
                'endCursor': 'YXJyYXljb25uZWN0aW9uOjk=',
                'hasNextPage': True,
                'hasPreviousPage': False,
                'startCursor': 'YXJyYXljb25uZWN0aW9uOjA='
            },
            'totalCount': 11
        }
    }
}

snapshots['test_employees 2'] = {
    'data': {
        'employees': {
            'edges': [
                {
                    'node': {
                        'empNo': '10001'
                    }
                },
                {
                    'node': {
                        'empNo': '10002'
                    }
                },
                {
                    'node': {
                        'empNo': '10004'
                    }
                },
                {
                    'node': {
                        'empNo': '10005'
                    }
                },
                {
                    'node': {
                        'empNo': '10006'
                    }
                },
                {
                    'node': {
                        'empNo': '10007'
                    }
                },
                {
                    'node': {
                        'empNo': '10008'
                    }
                },
                {
                    'node': {
                        'empNo': '10009'
                    }
                },
                {
                    'node': {
                        'empNo': '10010'
                    }
                },
                {
                    'node': {
                        'empNo': '10012'
                    }
                },
                {
                    'node': {
                        'empNo': '10013'
                    }
                },
                {
                    'node': {
                        'empNo': '10015'
                    }
                },
                {
                    'node': {
                        'empNo': '10016'
                    }
                },
                {
                    'node': {
                        'empNo': '10017'
                    }
                },
                {
                    'node': {
                        'empNo': '10018'
                    }
                },
                {
                    'node': {
                        'empNo': '10019'
                    }
                },
                {
                    'node': {
                        'empNo': '10021'
                    }
                },
                {
                    'node': {
                        'empNo': '10023'
                    }
                },
                {
                    'node': {
                        'empNo': '10024'
                    }
                },
                {
                    'node': {
                        'empNo': '10026'
                    }
                },
                {
                    'node': {
                        'empNo': '10027'
                    }
                },
                {
                    'node': {
                        'empNo': '10029'
                    }
                },
                {
                    'node': {
                        'empNo': '10030'
                    }
                },
                {
                    'node': {
                        'empNo': '10031'
                    }
                },
                {
                    'node': {
                        'empNo': '10032'
                    }
                },
                {
                    'node': {
                        'empNo': '10036'
                    }
                },
                {
                    'node': {
                        'empNo': '10037'
                    }
                },
                {
                    'node': {
                        'empNo': '10038'
                    }
                },
                {
                    'node': {
                        'empNo': '10040'
                    }
                },
                {
                    'node': {
                        'empNo': '10041'
                    }
                },
                {
                    'node': {
                        'empNo': '10042'
                    }
                },
                {
                    'node': {
                        'empNo': '10043'
                    }
                },
                {
                    'node': {
                        'empNo': '10045'
                    }
                },
                {
                    'node': {
                        'empNo': '10046'
                    }
                },
                {
                    'node': {
                        'empNo': '10047'
                    }
                },
                {
                    'node': {
                        'empNo': '10048'
                    }
                },
                {
                    'node': {
                        'empNo': '10049'
                    }
                },
                {
                    'node': {
                        'empNo': '10050'
                    }
                },
                {
                    'node': {
                        'empNo': '10051'
                    }
                },
                {
                    'node': {
                        'empNo': '10052'
                    }
                },
                {
                    'node': {
                        'empNo': '10053'
                    }
                },
                {
                    'node': {
                        'empNo': '10055'
                    }
                },
                {
                    'node': {
                        'empNo': '10056'
                    }
                },
                {
                    'node': {
                        'empNo': '10057'
                    }
                },
                {
                    'node': {
                        'empNo': '10058'
                    }
                },
                {
                    'node': {
                        'empNo': '10059'
                    }
                },
                {
                    'node': {
                        'empNo': '10060'
                    }
                },
                {
                    'node': {
                        'empNo': '10061'
                    }
                },
                {
                    'node': {
                        'empNo': '10062'
                    }
                },
                {
                    'node': {
                        'empNo': '10063'
                    }
                },
                {
                    'node': {
                        'empNo': '10064'
                    }
                },
                {
                    'node': {
                        'empNo': '10066'
                    }
                },
                {
                    'node': {
                        'empNo': '10068'
                    }
                },
                {
                    'node': {
                        'empNo': '10069'
                    }
                },
                {
                    'node': {
                        'empNo': '10070'
                    }
                },
                {
                    'node': {
                        'empNo': '10071'
                    }
                },
                {
                    'node': {
                        'empNo': '10072'
                    }
                },
                {
                    'node': {
                        'empNo': '10073'
                    }
                },
                {
                    'node': {
                        'empNo': '10074'
                    }
                },
                {
                    'node': {
                        'empNo': '10075'
                    }
                },
                {
                    'node': {
                        'empNo': '10076'
                    }
                },
                {
                    'node': {
                        'empNo': '10078'
                    }
                },
                {
                    'node': {
                        'empNo': '10079'
                    }
                },
                {
                    'node': {
                        'empNo': '10080'
                    }
                },
                {
                    'node': {
                        'empNo': '10081'
                    }
                },
                {
                    'node': {
                        'empNo': '10082'
                    }
                },
                {
                    'node': {
                        'empNo': '10087'
                    }
                },
                {
                    'node': {
                        'empNo': '10088'
                    }
                },
                {
                    'node': {
                        'empNo': '10089'
                    }
                },
                {
                    'node': {
                        'empNo': '10090'
                    }
                },
                {
                    'node': {
                        'empNo': '10091'
                    }
                },
                {
                    'node': {
                        'empNo': '10093'
                    }
                },
                {
                    'node': {
                        'empNo': '10094'
                    }
                },
                {
                    'node': {
                        'empNo': '10095'
                    }
                },
                {
                    'node': {
                        'empNo': '10096'
                    }
                },
                {
                    'node': {
                        'empNo': '10097'
                    }
                },
                {
                    'node': {
                        'empNo': '10098'
                    }
                },
                {
                    'node': {
                        'empNo': '10099'
                    }
                }
            ]
        }
    }
}

snapshots['test_departments 1'] = {
    'data': {
        'departments': [
            {
                'deptName': 'Marketing',
                'deptNo': 'd001'
            },
            {
                'deptName': 'Finance',
                'deptNo': 'd002'
            },
            {
                'deptName': 'Human Resources',
                'deptNo': 'd003'
            },
            {
                'deptName': 'Production',
                'deptNo': 'd004'
            },
            {
                'deptName': 'Development',
                'deptNo': 'd005'
            },
            {
                'deptName': 'Quality Management',
                'deptNo': 'd006'
            },
            {
                'deptName': 'Sales',
                'deptNo': 'd007'
            },
            {
                'deptName': 'Research',
                'deptNo': 'd008'
            },
            {
                'deptName': 'Customer Service',
                'deptNo': 'd009'
            }
        ]
    }
}
