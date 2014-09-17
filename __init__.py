# -*- coding: utf-8 -*-
"""
    :copyright: (c) 2014 by Openlabs Technologies & Consulting (P) Limited
    :license: BSD, see LICENSE for more details.
"""
from trytond.pool import Pool
from employee import Employee
from department import Designation, Department


def register():
    Pool.register(
        Department,
        Designation,
        Employee,
        module='employee', type_='model'
    )
