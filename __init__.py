from trytond.pool import Pool
from employee import Employee


def register():
    Pool.register(
        Employee,
        module='employee', type_='model'
    )
