class FriendsOfAppropriateAges(object):
    def numFriendRequests(self, ages):
        count = [0] * 121
        for age in ages:
            count[age] += 1

        ans = 0
        for ageA, countA in enumerate(count):
            for ageB, countB in enumerate(count):
                if ageA * 0.5 + 7 >= ageB: continue
                if ageA < ageB: continue
                if ageA < 100 < ageB: continue
                ans += countA * countB
                if ageA == ageB: ans -= countA

        return ans

if __name__ == '__main__':
    a = FriendsOfAppropriateAges()
    print(a.numFriendRequests([16, 16]))
    print(a.numFriendRequests([16, 17, 18]))
    print(a.numFriendRequests([20, 30, 100, 110, 120]))

