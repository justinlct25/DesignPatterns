from factory import *

print(Engineer('Sam1',25,'M'))
accountant1 = Accountant('Hema1',39,'F')
print(accountant1)
print(accountant1.get_role())
admin1 = Admin('Alfred')
print(admin1)
print(admin1.get_role())

print('------factory------')
employeeFactory = EmployeeFactory()

print(employeeFactory.create('engineer','Sam2',25,'M'))

accountant2 = employeeFactory.create('accountant','Hema2',39,'F')
print(accountant2)
print(accountant2.get_role())

admin = employeeFactory.create('Admin','Supritha2',32,'F')
print(admin)
print(admin.get_role())