from typing import ItemsView
from prototype import *

class Register(Prototype):
    def __init__(self, names=[]):
        self.names = names

r1 = Register(names=['amy','stu','jack'])
r2 = r1.clone_deepcopy()
r3 = r1.clone_shallowcopy()

# deepcopy
print(r1)
print(r2)
# print(r2.__class__)

# shallowcopy
print(r3)
r1.names.append('peter')
print(r1.names)
print(r2.names)
print(r3.names)

print('----prototype metaclass----')
class PrototypeM(metaclass=MetaSingletonPrototype):
    pass
class ItemCollection1(PrototypeM):
    def __init__(self, items=[]):
        self.items = items
p1=ItemCollection1(items=['apples','grapes','oranges'])
print(p1)
p2=p1.clone_deepcopy()
print(p2)
print(p1==p2)

print('----singletonprototype----')
class SingletonPrototypeM(metaclass=MetaSingletonPrototype):
    pass
class ItemCollection(SingletonPrototypeM):
    def __init__(self, items=[]):
        self.items = items

i1=ItemCollection(items=['apples','grapes','oranges'])
print(i1)
i2=i1.clone_deepcopy()
print(i2)
print(i1==i2)
i3=ItemCollection(items=['apples','grapes','mangoes'])
print(i1==i3)
print(i1.items)
print(i3.items)


print('-------')


# class ItemCollection2(ClassSingletonPrototype):
#     def __init__(self, items=[]):
#         self.items = items

# c1=ItemCollection2(items=['apples','grapes','oranges'])
# print(c1)
# c2=c1.clone_deepcopy()
# print(c2)
# print(c1==c2)
# c3=ItemCollection2(items=['apples','grapes','mangoes'])
# print(c1==c3)