# class - Python executes it and creates an object(instance)
class ObjectCreator(object):
    pass

if __name__ == '__main__':

    # normal type usage
    print('----normal usage of type----')
    print(type(1))
    print(type("1"))
    print(type(ObjectCreator))
    print(type(ObjectCreator()))

    print('----type as the metaclass of all types----')
    age = 35
    print(age.__class__)
    print(age.__class__.__class__)

    cls = "cls"
    print(cls.__class__)
    print(cls.__class__.__class__)












# https://stackoverflow.com/questions/52327384/why-metaclass-should-inherit-from-type


# another completely different ability - create classes with the description of a class as parameters
    # type(name, base, attrs)
    #   name - class name
    #   base - tuple of the parent class (for inheritance, can be empty)
    #   attrs - dictionary containing attributes names and values


    # class CodeGuysClass(object):
    #   pass 

    # above class can be created manually by the following
    codeguy = type('CodeGuysClass',(),{})
    # class code(codeguy):
    #     pass

    # print(codeguy)
    # print('-------sss')



    def echo_bar(self):
        print(self.bar)

    # class Foo(object):
    #     bar = True
    Foo = type('Foo', (), {'bar':True})
    # class FooChild(Foo):
    #     def echo_bar(self):
    #       print(self.bar)
    FooChild = type('FooChild',(Foo,),{'echo_bar': echo_bar})

    # print(FooChild)
    # print(FooChild.bar)
    fooChild = FooChild()
    # fooChild.echo_bar()


    # type is in fact a built-in metaclass Python uses
    # used by Python to create all classess behind the scenes
    # base class for all class objects in Python3