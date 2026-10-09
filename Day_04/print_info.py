# method overloading using *args
def print_info(*args):
    for i in args:
        print(i)

print_info("Hello", "world", 123, 456.78, "VIIT", "Python")
