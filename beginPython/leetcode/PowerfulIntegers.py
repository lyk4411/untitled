class PowerfulIntegers(object):
    def powerfulIntegers(self, x, y, bound):
        ans = set()
        # 2**18 > bound
        for i in range(18):
            for j in range(18):
                v = x ** i + y ** j
                if v <= bound:
                    ans.add(v)
        return list(ans)

if __name__ == '__main__':
    a = PowerfulIntegers()
    print(a.powerfulIntegers(2, 3, 10))
    print(a.powerfulIntegers(5, 3, 15))
