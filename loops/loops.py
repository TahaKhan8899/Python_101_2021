# # Purpose of a loop
jobs = ["job1", "job2", "job3", "job4", "job5", "job6", "job7"]
# print("processing " + jobs[0])
# print("processing " + jobs[1])
# print("processing " + jobs[2])
# print("processing " + jobs[3])
# print("processing " + jobs[4])

# Let's iterate the jobs with a for loop
# general syntax: for VARIABLE in ITERATOR:
for job in jobs:
    print("processing " + job)
print("this is outside the loop")

# What if we want the job number?
# Just loop over a range of numbers!
# Loop runs for 0 <= i < 5
for i in range(0, 5):
    print("job number: " + str(i))

# i is the iterator; a variable used to keep track of the number of times the code block has looped
# the loop will begin at 0 and count up to (but not including) 5
# notice x's value in the output console when printed

# specify a third number, this is the STEP
for x in range(0, 10, 2):
    print(x)

# count backwards!
for x in range(10, 0, -1):
    print(x)

# loop through characters in a string
x = "hello my name is taha"
for char in x:
    print(char)

# loop through dictionaries
scores = {"user143": 10, "player_2": 8, "user9323": 13, "3nnk92": 7}
for key in scores:
    print(key)
    print(scores[key])

# we want to print 1a 1b 1c, 2a 2b 2c .....
list1 = [1, 2, 3, 4, 5]
list2 = ['a', 'b', 'c']
for nums in list1:
    for char in list2:
        print(str(nums) + char)

# while loop with a finite counter
counter = 0
while counter < 10000:
    print("taha " + str(counter))
    counter += 1

# infinite loop with a condition
running = True
while running:
    print("yay my game is running")

# a while loop with a counter and a condition
running = True
score = 0
while running:
    if score == 10:
        # both ways stop the loop
        break
        running = False
    else:
        print(score)
        score += 1
print("game over")


# combining dictionaries
dict1 = {'Taha': 5, 'Uzair': 7, 'Sarah': 10}
dict2 = {'Abdul Rahman': 8, 'Umar': 20, 'Mark': 11}

# we basically want to do this for all the key value pairs in dict2:
dict1["Zaid"] = 2

for key in dict2:
    dict1[key] = dict2[key]
print(dict1)


