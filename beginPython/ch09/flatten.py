from collections import deque
def flatten(nested):
    try:
        for sublist in nested:
            for element in flatten(sublist):
                yield element

    except TypeError:
        yield nested


print(list(flatten([[[1],2],3,4,[5,[6,7]],8])))
print(tuple(flatten([[[1],2],3,4,[5,[6,7]],8])))
print(deque(flatten([[[1],2],3,4,[5,[6,7]],8])))
