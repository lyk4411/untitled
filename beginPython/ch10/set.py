from functools import reduce

mySets = []
for i in range(10):
    mySets.append(set(range(i, i + 5)))

print(mySets)

print(reduce(set.union,mySets))

# a = set(range(10))
# print(a)

# elements = [100, 200, 0, -100]
#
# # Sort from low to high.
# elements.sort()
# print(elements)


# elements = [22, 333, 0, -22, 1000]
#
# # Use a reversed, sorted view: a descending view.
# view = reversed(sorted(elements))
#
# # Display our results.
# for element in view:
#     print(element)
#
#     # An array of color names.
# colors = ["blue", "lavender", "red", "yellow"]
#
#     # Sort colors by length, in reverse (descending) order.
# for color in sorted(colors, key=lambda color: len(color), reverse=True):
#     print(color)

#
# # A dictionary with three pairs.
# furniture = {"table": 1, "chair": 2, "desk": 4}
#
# # Get sorted view of the keys.
# s = sorted(furniture.keys())
#
# # Display the sorted keys.
# for key in s:
#     print(key, furniture[key])


# class Bird:
#     def __init__(self, weight):
#         self.__weight = weight
#
#     def weight(self):
#         return self.__weight
#
#     def __repr__(self):
#         return "Bird, weight = " + str(self.__weight)
#
# # Create a list of Bird objects.
# birds = []
# birds.append(Bird(10))
# birds.append(Bird(5))
# birds.append(Bird(200))
#
# # Sort the birds by their weights.
# #birds.sort(key=Bird.weight)
# birds.sort(key=lambda b: b.weight())
# # Display sorted birds.
# for b in birds:
#     print(b)
#
# value = "boat"
#
# # Get list comprehension of characters and sort the list.
# list = [c for c in value]
# list.sort()
#
# # Join the characters together.
# result = "".join(list)
# print(result)

