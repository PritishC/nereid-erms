from trytond.model import fields
from trytond.pyson import Eval, If
from trytond.transaction import Transaction
from trytond import backend
from trytond.pool import Pool, PoolMeta

__all__ = ['Employee']
__metaclass__ = PoolMeta

STATES = {
    'readonly': ~Eval('active'),
}

DEPENDS = ['active']

class Employee:
    "Employee"
    __name__ = "company.employee"

    #party = fields.Many2One('party.party', 'Party', required=True,
    #                        select=True, states=STATES,
    #                        depends=DEPENDS)
    #company = fields.Many2One('company.company', 'Company', required=True,
    #                          select=True, states=STATES, depends=DEPENDS)
    gender = fields.Selection([
        ('male', 'M'),
        ('female', 'F'),
        ('undefined', 'N/A'),
    ], 'Gender', states=STATES, depends=DEPENDS)
    designation = fields.Char("Designation", required=True, 
                              select=True, states=STATES,
                              depends=DEPENDS)
    dob = fields.Date("Date of Birth", required=True,
                      states=STATES, depends=DEPENDS)
    pan = fields.Char("PAN", size=10, required=True,
                      states=STATES, depends=DEPENDS)
    passport = fields.Char("Passport Number", size=9, required=True,
                           states=STATES, depends=DEPENDS)
    driver_id = fields.Char("Drivers License", required=True,
                            states=STATES, depends=DEPENDS)
    active = fields.Boolean('Active')

    _sql_error_messages = {'uniq_error': 'This field must be unique.',
                           'null_error': 'This field must be not null.'}

    _unique = [('pan', 'UNIQUE(pan)',
                 _sql_error_messages['uniq_error']),
                ('passport', 'UNIQUE(passport)',
                 _sql_error_messages['uniq_error']),
                ('driver', 'UNIQUE(driver_id)',
                 _sql_error_messages['uniq_error'])]

    @classmethod
    def __setup__(cls):
        super(Employee, cls).__setup__()
        cls.party.states = STATES
        cls.party.depends = DEPENDS
        cls.company.states = STATES
        cls.company.depends = DEPENDS
        cls._sql_constraints = ([x for x in cls._unique])

    @classmethod
    def default_gender(cls):
        return 'undefined'

    @classmethod
    def default_active(cls):
        return True
