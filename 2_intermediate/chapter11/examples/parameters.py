# when using regular parameters, remember that order matters
def scoop_ice_cream(param1, param2, param3):
    pass


scoop_ice_cream("chocolate", "vanilla", "sprinkles")


# keyword arguments can be used to input parameter out of order
def func(p1, p2, p3):
    print(p1)  # prints 2
    print(p2)  # prints 3
    print(p3)  # prints 1


func(p3=1, p1=2, p2=3)


# keyword arguments can also be used to make parameters optional
def car(speed=100):  # if no speed is given, 100 is defaulted
    print("Car speed:", speed)


car(speed=150)  # prints "Car speed: 150"
car()  # prints "Car speed: 100"


# *args can take in an unknown number of regular parameters
def function_name(param1, *args):
    print(param1)  # prints "p1"
    print(args)  # prints (1, 2, 3, 4)


function_name("p1", 1, 2, 3, 4)


# **kwargs can take in an unknown number of keyword parameters
def function_name(param1, **kwargs):
    print(param1)  # prints "p1"
    print(kwargs)  # prints {"a":1, "b":2, "c":3}


function_name("p1", a=1, b=2, c=3)
