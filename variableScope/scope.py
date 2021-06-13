# GLOBAL variable
x = 30
def doSomething():
    # this is a LOCAL variable
    x = 10
    print(x)

# doSomething()
print(x)