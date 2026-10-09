# method overloading can be achieved with variable length arguments
def print_info(*args):
    for i in args:
        print(i)


print_info("Hello", "World", 123, 456.78, "VIIT", "Python")
