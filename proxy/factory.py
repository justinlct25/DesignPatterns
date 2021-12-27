

class Employee:

    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender

    def get_role(self):
        pass

    def __str__(self):
        return "{} - {}, {} years old {}".format(self.__class__.__name__, self.name, self.age, self.gender)

class Engineer(Employee):
    def get_role(self):
        return "engineering"

class Accountant(Employee):
    def get_role(self):
        return "accountant"

class Admin(Employee):
    def get_role(self):
        return "administration"

# implements instance creation via a single method / entry point, which is useful to abstract away the creation of instances
# reduce wrongly creating instances of related classes to another class
# provides a convenient way for the client (user) of a class to provide a single entry point to create instances of classess and subclasses
class EmployeeFactory(object):

    @classmethod
    def create(cls, name, *args):
        name = name.lower().strip()
        if name == 'engineer':
            return Engineer(*args)
        elif name == 'accountant':
            return Accountant(*args)
        elif name == 'admin':
            return Admin(*args)


