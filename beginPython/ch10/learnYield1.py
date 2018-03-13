def flatten(nested):
    try:
        for sublist in nested:
            print("sublist:" + str(sublist))
            for element in flatten(sublist):
                yield element
            # flatten(sublist)
    except TypeError:
        # print("nested:" + nested)
        yield nested

print(list(flatten([0,[[1],2],3,4,[5,[6,7]],8])))
# a = flatten([[[1],2],3,4,[5,[6,7]],8])
# a.__next__()
