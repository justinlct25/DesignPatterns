# a class must provide a way for all its instances to share the same initial state
# the class must be extensible by inheritance without breaking the pattern
# singleton ensures just a single actual instance at a specific memory location which is accessible via a well-known access point
# eg. used in other patterns (factory, prototype, facade), state, global variables, logging (writing the same logging file by multi-thread logging)
class Singleton(object):
    instann = None
    
    def __new__(cls):
        if cls.instann == None:
            cls.instann = object.__new__(cls)
        return cls.instann


# inherit from the Python built-in class 'type'
class MetaSingleton(type):

    def __init__(cls, *args): 
        print(cls, "__init method called with args", args)
        # type.__init__(cls, *args)
        cls.instance = None
    
    # custom __call__() method in the meta-class allows the class's instance to be called as a function
    # invoked when an instance of a class is used as a callable
    # class itself is an instance of this metaclass, this would be called first before __new__() in the child class
    def __call__(cls, *args, **kwargs):
        if not cls.instance:
            print(cls, "creating instance", args, kwargs)
            cls.instance = type.__call__(cls, *args, **kwargs)
        return cls.instance

class SingletonM(metaclass=MetaSingleton):
    pass

# metaclass benefit
# can create any number of new top-level classes which get the Singleton behavior via metaclass
#   instead of inheriting the top-level class Singleton to obtain the behavior
# using metaclass can be more flexible and respect to class hierarchies


# borg

class Borg(object):

    __shared_state = {}
    def __init__(self):
        self.__dict__ = self.__shared_state


class IBorg(Borg):

    def __init__(self):
        Borg.__init__(self)
        self.state = 'old state'

    def __str__(self):
        return self.state
