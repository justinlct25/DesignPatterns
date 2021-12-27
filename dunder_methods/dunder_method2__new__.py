# https://stackoverflow.com/questions/100003/what-are-metaclasses-in-python
# tuple is a comma-separated sequence of items, which comma-separated 
class UppercaseTuple(tuple):

    # __new__ method is executed first before __init__
    # method that creates the object and returns it
    # intercept and modify the arguments before the immutable object is created
    # return value of __new__ is usually an instance of the class
    # allows subclasses of immutable types to customize instance creation
    def __new__(cls, iterable):
        upper_iterable = (s.upper() for s in iterable)
        return super().__new__(cls, upper_iterable)

    # __init__ is called after the object has been created
    # so as to initialize it with attributes
    # just initialized the object passed as parameters
    # def __init__(self, iterable):
    #     print(f'init {iterable}')
    #     for i, arg in enumerate(iterable):
    #         self[i] = arg.upper()

# Driver Code
if __name__ == '__main__':
    codeGuys = UppercaseTuple(["hi","code guys"])
    print(codeGuys)

