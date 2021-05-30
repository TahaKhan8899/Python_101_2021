username1 = "player1"
username2 = "player2"

#   Indexing:
#   0    1    2    3    4    5    6
#  "p"  "l"  "a"  "y"  "e"  "r"  "1"
print(username1[3])

# STRING OPERATIONS

# lower
print(username1.lower())

# len
print(len(username1))

# index of a specific character
print(username1.index('y'))

# replace 1 character with another
username1 = username1.replace('p', 'c')
print(username1)

# concatenate (combine) strings
sentence = username1 + " beat " + username2
print(sentence)

# SLICING
# Syntax: stringVariable[start:end]
# take all the letter from 2 to 5 (5 not included)

slicedName1 = username1[2:6]
print(slicedName1)

slicedName2 = username1[:4]
print(slicedName2)

slicedName3 = username1[2:]
print(slicedName3)

jumpedThing = "fence"
jumpedThing = jumpedThing[0:2] + jumpedThing[2].upper() + jumpedThing[3:]
animal = "dog"
solution = username1.upper() + " jumped over the " + jumpedThing + " and got chased by a " + animal.upper()
print(solution)
