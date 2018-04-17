class UniqueMorseCodeWords(object):
    def uniqueMorseRepresentations(self, words):
        MORSE = [".-", "-...", "-.-.", "-..", ".", "..-.", "--.",
                 "....", "..", ".---", "-.-", ".-..", "--", "-.",
                 "---", ".--.", "--.-", ".-.", "...", "-", "..-",
                 "...-", ".--", "-..-", "-.--", "--.."]

        seen = {"".join(MORSE[ord(c) - ord('a')] for c in word)
                for word in words}
        # print (seen)
        return len(seen)

if __name__ == '__main__':
    a = UniqueMorseCodeWords
    words = ["gin", "zen", "gig", "msg"]
    print(a.uniqueMorseRepresentations("1", words))