#functions scope

global_b=12
def my_function():
    a=10  # local variable, within the function
    print(a)
    print(global_b)
my_function()


def f2():
    print(global_b)

my_function()
print(global_b)
f2()