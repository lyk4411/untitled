class GroupsofSpecialEquivalentStrings(object):
    def numSpecialEquivGroups(self, A):
        def count(word):
            ans = [0] * 52
            for i, letter in enumerate(word):
                ans[ord(letter) - ord('a') + 26 * (i % 2)] += 1
            return tuple(ans)

        # print({count(word) for word in A})
        return len({count(word) for word in A})

if __name__ == '__main__':
    a = GroupsofSpecialEquivalentStrings()
    print(a.numSpecialEquivGroups(["a", "b", "c", "a", "c", "c"]))
    print(a.numSpecialEquivGroups(["aa","bb","ab","ba"]))
    print(a.numSpecialEquivGroups(["abc","acb","bac","bca","cab","cba"]))
    print(a.numSpecialEquivGroups(["abcd","cdab","adcb","cbad"]))
