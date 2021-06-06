# Purpose of a loop
jobs = ["job1", "job2", "job3", "job4", "job5"]
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
x = "hello"
for char in x:
    print(char)