class LemonadeChange(object):
    def lemonadeChange(self, bills):
        num5 = 0
        num10 = 0
        for i in range(len(bills)):
            if bills[i] == 5:
                num5 += 1
            else:
                if bills[i] == 20:
                    while bills[i] > 10 and num10 > 0:
                        bills[i] -= 10
                        num10 -= 1
                    while bills[i] > 5 and num5 > 0:
                        bills[i] -= 5
                        num5 -= 1
                    if bills[i] > 5:
                        return False
                else:
                    while bills[i] > 5 and num5 > 0:
                        bills[i] -= 5
                        num5 -= 1

                    if bills[i] > 5:
                        return False
                    num10 += 1
        return True
if __name__ == '__main__':
    a = LemonadeChange()
    print(a.lemonadeChange([5, 5, 5, 10, 20]))
    print(a.lemonadeChange([5, 5, 10]))
    print(a.lemonadeChange([5, 5, 10, 10, 20]))
