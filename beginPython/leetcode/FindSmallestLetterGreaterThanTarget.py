from pip._vendor.requests.packages.urllib3.connectionpool import xrange


class FindSmallestLetterGreaterThanTarget(object):
    def nextGreatestLetter(self, letters, target):
        seen = set(letters)
        for i in xrange(1, 26):
            cand = chr((ord(target) - ord('a') + i) % 26 + ord('a'))
            if cand in seen:
                return cand

if __name__ == '__main__':
    a = FindSmallestLetterGreaterThanTarget()
    letters = ["c", "f", "j"]
    print(a.nextGreatestLetter(letters, 'c'))
    print(a.nextGreatestLetter(letters, 'z'))
    print(a.nextGreatestLetter(letters, 'g'))