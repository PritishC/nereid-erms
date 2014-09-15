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

    designation = fields.Char("Designation", required=True, select=True)
    dob = fields.Date("Date of Birth", required=True)
    name = fields.Char("Name", required=True, select=True)
    
    _sql_constraints = [('name_not_null', 'NOT NULL(name)', 
                         'null_error'),
                        ('dob_not_null', 'NOT NULL(dob)',
                         'null_error')]
    _sql_error_messages = {'uniq_error': 'This field must be unique.',
                           'null_error': 'This field cannot be null.'}
    

class Identify(ModelSQL, ModelView):
    "Identify"
    __name__ = "employee.identify"

    pan = fields.Numeric("PAN", digits=10, required=True)
    passport = fields.Numeric("Passport Number", digits=9, required=True)
    driver_id = fields.Char("Drivers License", required=True)

    _not_nulls = [('pan_not_null', 'NOT NULL(pan)', 'null_error'),
                  ('passport_not_null', 'NOT NULL(passport)',
                   'null_error'),
                  ('driver_not_null', 'NOT NULL(driver_id)',
                   'null_error')]
    _uniques = [('pan_unique', 'UNIQUE(pan)', 'uniq_error'),
                ('passport_unique', 'UNIQUE(passport)', 'uniq_error'),
                ('driver_unique', 'UNIQUE(driver_id)', 'uniq_error')]

    _sql_constraints = [x for x in _not_nulls] + [y for y in _uniques]
    _sql_error_messages = {'uniq_error': 'This field must be unique.',
                           'null_error': 'This field must be not null.'}
