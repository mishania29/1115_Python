names = {"Mykhailo":12, "Ganna":16, "Elizabeth":25, "Maksim":34, "Oleg":43}
keys = list(names.keys())
print(keys)
name = input("Enter name: ")
if name not in keys:
    raise(TypeError("Name missing"))
else:
    print(name, "is", names.get(name), "years old.")