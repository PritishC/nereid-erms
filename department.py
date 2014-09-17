# -*- coding: utf-8 -*-
"""
    :copyright: (c) 2014 by Openlabs Technologies & Consulting (P) Ltd.
    :license: BSD, see LICENSE for more details
"""
from trytond.model import fields, ModelSQL, ModelView


__all__ = ['Department', 'Designation']


class Department(ModelSQL, ModelView):
    'Department'
    __name__ = 'employee.department'

    name = fields.Char("Name")


class Designation(ModelSQL, ModelView):
    'Designation'
    __name__ = 'employee.designation'

    department = fields.Many2One('employee.department', 'Department')
    name = fields.Char("Name")
