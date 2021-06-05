# need a comma
thistuple = ("apple",)
print(type(thistuple))

# NOT a tuple
thistuple = ("apple")
print(type(thistuple))

# can have multiple datatypes
tuple1 = ("abc", 34, True, 40, "male")

# immutable
location = ("north", "south")
# The following does not work. Tuples are immutable (cannot be directly changed)
# location[0] = "South"
