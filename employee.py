from trytond.model import fields
from trytond.pyson import Eval, If
from trytond.transaction import Transaction
from trytond import backend
from trytond.pool import Pool, PoolMeta

__all__ = ['Employee']
__metaclass__ = PoolMeta

class Employee:
    "Employee"
    __name__ = "company.employee"

    gender = fields.Selection([
        ('male', 'M'),
        ('female', 'F'),
        ('undefined', 'N/A'),
    ], 'Gender')
    designation = fields.Char("Designation", required=True, select=True)
    dob = fields.Date("Date of Birth", required=True)
    pan = fields.Char("PAN", required=True)
    passport = fields.Char("Passport Number", required=True)
    driver_id = fields.Char("Drivers License", required=True)

    _sql_error_messages = {'uniq_error': 'This field must be unique.',
                           'null_error': 'This field must be not null.'}

    _not_nulls = [('pan_not_null', 'NOT NULL(pan)',
                   _sql_error_messages['null_error']),
                  ('passport_not_null', 'NOT NULL(passport)',
                   _sql_error_messages['null_error']),
                  ('driver_not_null', 'NOT NULL(driver_id)',
                   _sql_error_messages['null_error']),
                  ('dob_not_null', 'NOT NULL(dob)',
                  _sql_error_messages['null_error'])]

    _uniques = [('pan_unique', 'UNIQUE(pan)',
                 _sql_error_messages['uniq_error']),
                ('passport_unique', 'UNIQUE(passport)',
                 _sql_error_messages['uniq_error']),
                ('driver_unique', 'UNIQUE(driver_id)',
                 _sql_error_messages['uniq_error'])]

    @classmethod
    def __setup__(cls):
        super(Employee, cls).__setup__()
        cls._sql_constraints = (#[x for x in cls._not_nulls] + 
                                [y for y in cls._uniques])

    @classmethod
    def default_gender(cls):
        return 'undefined'
