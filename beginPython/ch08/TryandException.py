try:
    x = 1
    y = 0
    print
    x / y
except (ZeroDivisionError, TypeError) as e:
    print (e)



try:
    x = 1
    y = "0"
    print
    x / y
except (ZeroDivisionError, TypeError) as e:
    print (e)