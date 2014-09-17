# -*- coding: utf-8 -*-
"""
    :copyright: (c) 2014 by Openlabs Technologies & Consulting (P) Ltd.
    :license: BSD, see LICENSE for more details
"""
from trytond.model import fields, ModelSQL, ModelView

__all__ = ['Department']


class Department(ModelSQL, ModelView):
    'Department'
    __name__ = 'company.department'

    name = fields.Char("Name", required=True)
