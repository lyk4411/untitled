class BoatstoSavePeople(object):
    def numRescueBoats(self, people, limit):
        people.sort()
        i, j = 0, len(people) - 1
        ans = 0
        while i <= j:
            ans += 1
            if people[i] + people[j] <= limit:
                i += 1
            j -= 1
        return ans

if __name__ == '__main__':
    a = BoatstoSavePeople()
    print(a.numRescueBoats(people = [1,2 ], limit = 3))
    print(a.numRescueBoats(people = [3, 2, 2, 1], limit = 3))
