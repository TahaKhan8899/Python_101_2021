def sayHello(fname, lname):
    print("Hi " + fname + " " + lname)


# sayHello("Taha", "Khan")


def addNumbers(a, b):
    sum = a + b
    return sum


# answer1 = addNumbers(2, 3)
# answer2 = addNumbers(4, 7)
# answer3 = addNumbers(10, 76)
# print(answer1)
# print(answer2)
# print(answer3)

def areaOfRect(l, w):
    return l * w

# area1 = areaOfRect(2, 4)
# print(area1)

def printNums():
    for x in range(-10, 0):
        print(x)

# printNums()

def userSum():
    userNum = int(input("enter a number: "))
    sum = 0
    for num in range(1, userNum+1):
        sum += num

    return sum

sum1 = userSum()
print(sum1)
