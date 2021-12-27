# dunder or magic methods are the methods having two prefix and suffix underscores in the method name
# eg.__init__, __add__, __len__, __repr__
# commonly used for operator overloading (giving extended meaning beyond their predefined operational meaning)

# declare our own string class
class String:

    # to initiate object
    def __init__(self, string):
        self.string = string

    # print our object
    def __repr__(self):
        return 'String Object: {}'.format(self.string)

    def __add__(self, other):
        return self.string + str(other)

# Driver Code
if __name__ == '__main__':
    string1 = String('Hello')
    print(string1)
    # print(string1 + ' Code Guys')
    print(string1 + 4)
