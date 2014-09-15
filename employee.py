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
    
