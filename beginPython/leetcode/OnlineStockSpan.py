class OnlineStockSpan(object):
    def __init__(self):
        self.stack = []

    def next(self, price):
        weight = 1
        while self.stack and self.stack[-1][0] <= price:
            weight += self.stack.pop()[1]
        self.stack.append([price, weight])
        return weight

if __name__ == '__main__':
    a = OnlineStockSpan()
    print(a.next(100))
    print(a.next(80))
    print(a.next(60))
    print(a.next(70))
    print(a.next(60))
    print(a.next(75))
    print(a.next(85))
    print(a.next(90))
