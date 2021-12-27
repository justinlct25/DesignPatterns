# cls vs self - Method Types in Python
# https://levelup.gitconnected.com/method-types-in-python-2c95d46281cd

class MethodTypes:

    #name = "Code"

    def instanceMethod(self):
        # Creates an instance attribute through keyword self
        self.lastname = "Guy"
        print(self.name)
        print(self.frontname)    
        print(self.lastname)    

    @classmethod
    def classMethod(cls):
        # access the class attribute 
        cls.name = "Lagertha"
        print(cls.name)


    @staticmethod
    def staticMethod(cls):
        cls.name = "Jack"
        print("This is a static method")

