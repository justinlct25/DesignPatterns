# Using the __call__ method of a metaclass instead of __new__?
# https://stackoverflow.com/questions/6966772/using-the-call-method-of-a-metaclass-instead-of-new
# Explicitly inheriting from 'type' to implement metaclass in python3.x
# https://stackoverflow.com/questions/47277984/explicitly-inheriting-from-type-to-implement-metaclass-in-python3-x

class MetaCodeGuy(type):
    def __call__(cls, *a, **kw):
        print("entering __call__")
        gg = super(MetaCodeGuy, cls).__call__(*a, **kw)
        return gg

class CodeGuy(metaclass=MetaCodeGuy):
    def __new__(cls, *a, **kw):
        print("entering __new__")
        gg = super(CodeGuy, cls).__new__(cls, *a, **kw)
        return gg
    
    def __init__(self, *a, **kw):
        print("entering __init__")
        super(CodeGuy, self).__init__(*a, **kw)


if __name__ == '__main__':
    jack = CodeGuy()