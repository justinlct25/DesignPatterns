from singleton_borg import *


print('----singleton(normal object creation)----')
singleton1 = Singleton()
singleton2 = Singleton()
print(singleton1==singleton2)

print('----singleton(metaclass inheritance)----')
# class SingletonGG(SingletonM):pass
singletonGG = SingletonM()
singletonGG2 = SingletonM()
print(singletonGG==singletonGG2)


print('----borg----')
borg1 = IBorg()
borg2 = IBorg()
print(borg1==borg2)
print(borg1)
print(borg2)
borg1.state='new state'
print(borg1)
print(borg2)

print('----singleton state test-----') # do it manually
class SingletonA(Singleton):pass
class SingletonA1(SingletonA):pass
class SingletonB(Singleton):pass
singletonA = SingletonA()
singletonA1 = SingletonA1()
singletonB = SingletonB()
singletonA.x = 100
print(singletonA.x)
print(singletonA1.x)
print(singletonB.x)

print('----borg state test-----')
class BorgA(Borg):pass
class BorgA1(Borg):pass
class BorgB(Borg):pass
borgA = BorgA()
borgA1 = BorgA1()
borgB = BorgB()
borgA.x = 100
print(borgA.x)
print(borgA1.x)
print(borgB.x)