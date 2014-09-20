# -*- coding: utf-8 -*-
"""
    tests/test_views_depends.py

    :copyright: (C) 2014 by Openlabs Technologies & Consulting (P) Limited
    :license: BSD, see LICENSE for more details.
"""
import sys
import os
DIR = os.path.abspath(os.path.normpath(os.path.join(
    __file__, '..', '..', '..', '..', '..', 'trytond'
)))
if os.path.isdir(DIR):
    sys.path.insert(0, os.path.dirname(DIR))
import unittest

import trytond.tests.test_tryton
from trytond.transaction import Transaction
from trytond.tests.test_tryton import (
    test_view, test_depends, POOL, DB_NAME, USER, CONTEXT
)


class TestViewsDepends(unittest.TestCase):
    '''
    Test views and depends
    '''

    def setUp(self):
        """
        Set up data used in the tests.
        this method is called before each test function execution.
        """
        trytond.tests.test_tryton.install_module('employee')
        self.Party = POOL.get('party.party')
        self.Company = POOL.get('company.company')
        self.Department = POOL.get('company.department')
        self.Designation = POOL.get('employee.designation')
        self.Employee = POOL.get('company.employee')
        self.Currency = POOL.get('currency.currency')

    def setup_basics(self):
        """
        Set up some basic models.
        """
        self.currency, = self.Currency.create([{
            'name': 'US Dollar',
            'code': 'USD',
            'symbol': '$',
        }])
        self.party, = self.Party.create([{'name': 'Openlabs'}])
        self.party_emp, = self.Party.create([{'name': 'Pritish C'}])
        self.company, = self.Company.create([{
            'party': self.party.id,
            'currency': self.currency.id,
        }])

    def _populate_department(self):
        """
        Create department and designations.
        """
        self.department, = self.Department.create([{
            'name': 'IT',
            'company': self.company.id
        }])
        self.desig1, = self.Designation.create([{
            'name': 'Sr Software Developer',
            'department': self.department.id
        }])
        self.desig2, = self.Designation.create([{
            'name': 'Software Dev Trainee',
            'department': self.department.id
        }])

    def _create_employee(self):
        """
        Set up a dummy Employee
        """
        self.employee, = self.Employee.create([{
            'party': self.party_emp.id,
            'company': self.company.id,
            'gender': 'male',
            'designation': self.desig2.id,
            'department': self.department.id,
            'dob': '1992-08-08',
            'pan': '1234567891',
            'passport': '123456789',
            'driver_id': 'ABCD1234',
        }])

    def test0005views(self):
        '''
        Test views.
        '''
        test_view('employee')

    def test0006depends(self):
        '''
        Test depends.
        '''
        test_depends()

    def test0010employee_creation(self):
        """
        Test dummy employee
        """
        import datetime
        with Transaction().start(DB_NAME, USER, CONTEXT):
            self.setup_basics()
            self._populate_department()
            self._create_employee()

            test_tuple = 'party.party,' + str(self.party_emp.id)
            self.assertEquals(str(self.employee.party), test_tuple)

            test_tuple = 'company.company,' + str(self.company.id)
            self.assertEquals(str(self.employee.company), test_tuple)

            self.assertEquals(self.employee.gender, 'male')
            self.assertEquals(self.employee.dob, datetime.date(1992, 8, 8))
            self.assertEquals(self.employee.pan, '1234567891')
            self.assertEquals(self.employee.passport, '123456789')
            self.assertEquals(self.employee.driver_id, 'ABCD1234')

            test_tuple = 'company.department,' + str(self.department.id)
            self.assertEquals(str(self.employee.department), test_tuple)

            test_tuple = 'employee.designation,' + str(self.desig2.id)
            self.assertEquals(str(self.employee.designation), test_tuple)

    def test0015employee_uniqueness(self):
        """
        Cannot create employee with exactly same details
        """
        from trytond.error import UserError
        with Transaction().start(DB_NAME, USER, CONTEXT):
            self.setup_basics()
            self._populate_department()
            self._create_employee()

            with self.assertRaises(UserError):
                self._create_employee()


def suite():
    """
    Define suite
    """
    test_suite = trytond.tests.test_tryton.suite()
    test_suite.addTests(
        unittest.TestLoader().loadTestsFromTestCase(TestViewsDepends)
    )
    return test_suite

if __name__ == '__main__':
    unittest.TextTestRunner(verbosity=2).run(suite())
