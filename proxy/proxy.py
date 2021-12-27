# https://www.geeksforgeeks.org/proxy-design-pattern/
# https://www.geeksforgeeks.org/proxy-method-python-design-patterns/

from factory import Engineer, Accountant, Admin

class EmployeeProxy(object):
    ''' Counting proxy class for Employees '''
    count = 0

    def __new__(cls, *args):
        ''' Overloaded __new__ '''
        # To keep track of counts
        instance = object.__new__(cls)
        cls.incr_count()
        return instance

    def __init__(self, employee):
        self.employee = employee

    @classmethod
    def incr_count(cls):
        ''' Increment employee count '''
        cls.count += 1

    @classmethod
    def decr_count(cls):
        ''' Decrement employee count '''
        cls.count -= 1

    @classmethod
    def get_count(cls):
        ''' Get employee count '''
        return cls.count

    def __str__(self):
        return str(self.employee)

    def __getattr__(self, name):
        ''' Redirect attributes to employee instance '''

        return getattr(self.employee, name)

    def __del__(self):
        ''' Overloaded __del__ method '''
        print("delete")
        self.decr_count()

class EmployeeProxyFactory(object):
    ''' An Employee factory class returning proxy objects'''

    @classmethod
    def create(cls, name, *args):
        ''' Factory method for creating and Employee instance '''

        name = name.lower().strip()

        if name == 'engineer':
            return EmployeeProxy(Engineer(*args))
        elif name == 'accountant':
            return EmployeeProxy(Accountant(*args))
        elif name == 'admin':
            return EmployeeProxy(Admin(*args))


class College:
    '''Resource-intensive object'''

    def studyingInCollege(self):
        print("Studying In College...")

class CollegeProxy:
    '''Less resource-intensive proxy acting as middleman'''
    '''Instantiates a College object only if there is no fee due'''

    def __init__(self):
        self.feeBalance = 1000
        self.college = None

    def studyingInCollege(self):
        print("Proxy in action. Checking to see if the balance of student is clear or not ...")
        if self.feeBalance <= 500:
            self.college = College()
            self.college.studyingInCollege()
        else:
            print("Your fee balance is greater than 500, first pay the fee")