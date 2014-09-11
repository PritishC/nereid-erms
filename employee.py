from trytond.model import ModelView, ModelSQL, fields
from trytond.pyson import Eval, If
from trytond.transaction import Transaction
from trytond import backend
from trytond.pool import Pool

__all__ = ['Employee']

class Employee(ModelSQL, ModelView):
    "Employee"
    __name__ = "employee.employee"
    name = fields.Char("Name", required=True, select=True)
    phone = fields.Integer("Phone Number", size=10, required=True, select=True)
    designation = fields.Char("Designation", required=True, select=True)
    address = fields.Text("Address", required=True, select=True)
