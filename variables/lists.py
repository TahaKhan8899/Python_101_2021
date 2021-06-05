# access an item
serverRoom = ["user1", "user2", "user3"]
print(serverRoom[1])

# change an item. Mutable.
serverRoom[1] = "Taha"
print(serverRoom[1])

# delete an item
del(serverRoom[1])
print(serverRoom)

# pop deletes an item at an index number
serverRoom.pop(0)
print(serverRoom)

# len tells us how many variables are in our list
numberOfUsers = len(serverRoom)
print(numberOfUsers)

# append lets us add to the list
serverRoom.append("user4")
print(serverRoom)