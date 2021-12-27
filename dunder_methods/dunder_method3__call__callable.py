# https://stackoverflow.com/questions/9663562/what-is-the-difference-between-init-and-call
class CodeGuy: 
    # used when the class is called to initialize the instance
    def __init__(self, x, y):
        self.x = x
        self.y = y
        print("init")
    
    # called when the instance is called
    # defining a custom __call__() method in meta-class
    # allows class's instance to be called as function
    def __call__(self, x, y):
        self.x = x
        self.y = y
        print("call")
    # allows pass them to other methods/functions and call them

    def __del__(self):
        del self.x
        del self.y


if __name__ == '__main__':
    edward = CodeGuy(1,2)
    print(edward.x)

    # edward = CodeGuy(7,8)
    # print(edward.x)

    edward(7,8)
    print(edward.x)

# technically __init__ is called once by __new__ when object is created, thus initialized
# many scenarios where you want to redefine your object
# redefine the same object as if they were new