class DIStringMatch(object):
    def diStringMatch(self, S):
        lo, hi = 0, len(S)
        ans = []
        for x in S:
            if x == 'I':
                ans.append(lo)
                lo += 1
            else:
                ans.append(hi)
                hi -= 1

        return ans + [lo]

if __name__ == '__main__':
    a = DIStringMatch()
    print(a.diStringMatch("IIII"))
    print(a.diStringMatch("IDID"))

