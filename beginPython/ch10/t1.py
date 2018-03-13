import copy
print([n for n in dir(copy) if not n.startswith('_')])

print(copy.__all__)

print(copy.copy.__doc__)

print("===============================================================")

print(copy.__file__)