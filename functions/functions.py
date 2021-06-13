# Simplest function
def sayHello():
    print("hi!")


# We need to call functions AFTER we define them (defined above)
sayHello()


# function with parameters
def sayHelloTo(fname, lname):
    print("Hi " + fname + " " + lname)


sayHelloTo("taha", "khan")


# Function with parameters and a returns value
def addNumbers(a, b):
    sum = a + b
    return sum


answer1 = addNumbers(2, 3)

# They can be called multiple times with different PARAMETERS
# This is nice because we don't need to keep re-writing the code for adding numbers, we write it ONCE in our function
# and call that function whenever we want
answer2 = addNumbers(5, 10)
answer3 = addNumbers(2, 15)
print(answer1)
print(answer2)
print(answer3)

# try this #1
def areaRect(l, w):
    return l * w


# try this #2:
def printNums():
    for i in range(-10, 0):
        print(i)


# Try this #3:
def userSum():
    userNum = int(input("enter a number: "))
    sum = 0
    for x in range(1, userNum + 1):
        sum += x
    return sum


result = userSum()
print(result)
