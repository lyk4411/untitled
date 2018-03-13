def repeater(value):
    while True:
        new = (yield value)
        if new is not None:
            value = new




r = repeater(4)

print(r.__next__())
r = repeater("hello world.")
print(r.__next__())
r = repeater(42)
print(r.__next__())
print(r.__next__())

