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
