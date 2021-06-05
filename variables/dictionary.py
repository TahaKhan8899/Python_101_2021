# Dictionary
scores = {"user143": 10, "player_2": 8, "user9323": 13, "3nnk92": 7}
print(scores["user143"])

# change an element
scores['user143'] = 20
print(scores['user143'])

# len of dict
print(len(scores))

# add items
scores['hhh'] = 123
print(scores)

# remove item
scores.pop('hhh')
print(scores)
