from trytond.model import ModelView, ModelSQL, fields
from trytond.pyson import Eval, If
from trytond.transaction import Transaction
from trytond import backend
from trytond.pool import Pool

__all__ = ['Employee']

class Employee(ModelSQL, ModelView):
    "Employee"
    __name__ = "employee.employee"
    ID = fields.Integer()
    name = fields.Char("Name")

Pool.register(Employee)
