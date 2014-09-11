from trytond.pool import Pool
from .employee import *

def register():
    Pool.register(Employee,
                  module='employee', type_='model')
