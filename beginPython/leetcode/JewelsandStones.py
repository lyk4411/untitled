
class JewelsandStones(object):
    def numJewelsInStones(self, J, S):
        """
        :type J: str
        :type S: str
        :rtype: int
        """
        return sum(S.count(j) for j in J)


if __name__ == '__main__':
    a = JewelsandStones()
    J = "aA"
    S = "aAAbbbb"
    print(a.numJewelsInStones(J,S))