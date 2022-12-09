import logging

logging.basicConfig(filename='employee_log.log', level=logging.INFO,
                    format='%(levelname)s:%(asctime)s:%(message)s')


class Employee:
    """A sample Employee class"""

    def __init__(self, first, last):
        self.first = first
        self.last = last

        logging.info('Created Employee: {} - {}'.format(self.first, self.last))


emp_1 = Employee('John', 'Smith')
emp_2 = Employee('Corey', 'Schafer')
emp_3 = Employee('Jane', 'Doe')