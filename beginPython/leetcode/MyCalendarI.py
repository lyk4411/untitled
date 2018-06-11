class MyCalendarI(object):
    def __init__(self):
        self.calendar = []

    def book(self, start, end):
        for s, e in self.calendar:
            if s < end and start < e:
                return False
        self.calendar.append((start, end))
        return True

if __name__ == '__main__':
    a = MyCalendarI()
    print(a.book(10, 20))
    print(a.book(15, 20))
    print(a.book(20, 30))