def code(*args):
    print(type(args))
    for arg in args:
        print(arg)

def guy(arg4, **gg):
    print(type(gg))
    for key, value in gg.items():
        print("%s == %s" % (key, value))

if __name__ == "__main__":
    code("Alfred", "Samson", "Peter")
    print("--------------------------------")
    guy("hi", senior='Edward', badminton='Samuel', musician='Peter')
