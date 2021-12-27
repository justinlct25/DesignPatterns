import copy

# when the classes instantiated in a system are dynamic (they are specified as part of a config or can otherwise change at runtime)
# when the instances only have a few combination of initial state
# rather than keeping track of the state and instantiating an instance each time, create prototypes matching each state and clone them is more convenient
class Prototype(object):
    """ A prototype base class """
    # calls copy recursively for all objects contained in the cloned object
    # nothing is shared and each clone having its own copy
    def clone_deepcopy(self):
        return copy.deepcopy(self)

    # all objects are copied via a reference
    # fine for copying immutable objects such as strings or tuples (can't be changed)
    # problem for copying mutable objects such as lists or dictionaries
    #   (state of the instance is shared instead of being wholly owned by the instance)
    #   (any modification of a mutable in one instance will modify the same object in the cloned instances)
    def clone_shallowcopy(self):
        return copy.copy(self)

class MetaPrototype(type):

    def __init__(cls, *args):
        type.__init__(cls, *args)
        cls.clone = lambda self: copy.deepcopy(self)

# another benefit of metaclass is to allows powerful customization of class creation
# another benefit of metaclass is to combine different design pattern's behaviors
class MetaSingletonPrototype(type):

    def __init__(cls, *args):
        print(cls, "__init__ method called with args", args)
        type.__init__(cls, *args)
        cls.instance = None
        cls.clone_deepcopy = lambda self: copy.deepcopy(cls.instance)

    # singleton 
    def __call__(cls, *args, **kwargs):
        if not cls.instance:
            print(cls,"creating prototypical instance", args, kwargs)
            cls.instance = type.__call__(cls,*args,**kwargs)
        return cls.instance


# class ClassSingletonPrototype(object):
#     # singleton 
#     instance = None
#     def __new__(cls, *args, **kwargs):
#         if not cls.instance:
#             cls.instance = object.__new__(cls)
#         return cls.instance


#     def clone_deepcopy(self):
#         return copy.deepcopy(self)