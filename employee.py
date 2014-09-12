from trytond.model import ModelView, ModelSQL, fields
from trytond.pyson import Eval, If
from trytond.transaction import Transaction
from trytond import backend
from trytond.pool import Pool

__all__ = ['Employee']

class Employee(ModelSQL, ModelView):
    "Employee"
    __name__ = "employee.employee"

    #ID = fields.Numeric("ID", digits=(4,0), required=True, select=True)
    name = fields.Char("Name", required=True, select=True)
    phone = fields.Numeric("Phone Number", digits=(10,0), required=True, select=True)
    designation = fields.Char("Designation", required=True, select=True)
    address = fields.Text("Address", required=True, select=True)
    email = fields.Char("E-Mail", required=True, select=True)
    
    @classmethod
    def __setup__(cls):
        super(Employee, cls).__setup__()
        cls._sql_constraints = [
            ('UniqueEmail', 'UNIQUE(email)', 'unique_error'),
        ]
        cls._sql_error_messages = {
            'pk_error': 'This field is a primary key, it must\
            be specified!',
            'unique_error': 'This field must be unique!',
        }

