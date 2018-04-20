

class OnebitandTwobitCharacters(object):
    def isOneBitCharacter(self, bits):
        i = 0
        while i < len(bits) - 1:
            i += bits[i] + 1
        return i == len(bits) - 1

if __name__ == '__main__':
    a = OnebitandTwobitCharacters()
    print(a.isOneBitCharacter([1, 0, 0]))
    print(a.isOneBitCharacter([1, 1, 1, 0]))