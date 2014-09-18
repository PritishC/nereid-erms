# -*- coding: utf-8 -*-
"""
    :copyright: (c) 2014 by Openlabs Technologies & Consulting (P) Ltd.
    :license: GPLv3, see LICENSE for more details
"""
from trytond.pool import Pool
from employee import Employee, Designation
from company import Department


def register():
    Pool.register(
        Department,
        Designation,
        Employee,
        module='employee', type_='model'
    )
