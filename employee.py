# -*- coding: utf-8 -*-
"""
    :copyright: (c) 2014 by Openlabs Technologies & Consulting (P) Ltd.
    :license: BSD, see LICENSE for more details
"""
from trytond.model import fields
from trytond.pyson import Eval
from trytond.pool import PoolMeta

__all__ = ['Employee']
__metaclass__ = PoolMeta

STATES = {
    'readonly': ~Eval('active'),
}

DEPENDS = ['active']


class Employee:
    "Employee"
    __name__ = "company.employee"

    gender = fields.Selection([
        ('male', 'M'),
        ('female', 'F'),
        ('undefined', 'N/A'),
    ], 'Gender', required=True,
        states=STATES, depends=DEPENDS)
    department = fields.Many2One(
        'employee.department', 'Department', required=True, states=STATES,
        depends=DEPENDS
    )
    designation = fields.Many2One(
        "employee.designation", "Designation", domain=[
            ('department', '=', Eval('department'))
        ], required=True, states=STATES, depends=DEPENDS.append('department')
    )
    dob = fields.Date(
        "Date of Birth", required=True, states=STATES, depends=DEPENDS
    )
    pan = fields.Char(
        "PAN", size=10, required=True, states=STATES, depends=DEPENDS
    )
    passport = fields.Char(
        "Passport Number", size=9, required=True, states=STATES,
        depends=DEPENDS
    )
    driver_id = fields.Char(
        "Drivers License", required=True, states=STATES,
        depends=DEPENDS
    )
    active = fields.Boolean('Active')

    _sql_error_messages = {
        'uniq_error': 'This field must be unique.',
        'null_error': 'This field must be not null.'
    }

    _unique = [
        ('pan', 'UNIQUE(pan)', _sql_error_messages['uniq_error']),
        ('passport', 'UNIQUE(passport)', _sql_error_messages['uniq_error']),
        ('driver', 'UNIQUE(driver_id)', _sql_error_messages['uniq_error'])
    ]

    @classmethod
    def __setup__(cls):
        super(Employee, cls).__setup__()

        cls._set_states_depends(['party', 'company'])
        cls._sql_constraints = (cls._unique)

    @classmethod
    def default_gender(cls):
        return 'male'

    @classmethod
    def default_active(cls):
        return True

    @classmethod
    def _set_states_depends(cls, arg_list):
        """
        This method takes a list of model names
        as arguments (eg: 'party') and sets their
        attributes - 'states' and 'depends' - to
        the necessary values.
        """
        for string in arg_list:
            module = getattr(cls, string)
            module.states = STATES
            module.depends = DEPENDS
