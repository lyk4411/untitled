class VowelSpellchecker(object):
    def spellchecker(self, wordlist, queries):
        def devowel(word):
            return "".join('*' if c in 'aeiou' else c
                           for c in word)

        words_perfect = set(wordlist)
        words_cap = {}
        words_vow = {}

        for word in wordlist:
            wordlow = word.lower()
            words_cap.setdefault(wordlow, word)
            words_vow.setdefault(devowel(wordlow), word)

        def solve(query):
            if query in words_perfect:
                return query

            queryL = query.lower()
            if queryL in words_cap:
                return words_cap[queryL]

            queryLV = devowel(queryL)
            if queryLV in words_vow:
                return words_vow[queryLV]
            return ""

        return map(solve, queries)

if __name__ == '__main__':
    a = VowelSpellchecker()
    wordlist = ["KiTe", "kite", "hare", "Hare"]
    queries = ["kite", "Kite", "KiTe", "Hare", "HARE", "Hear", "hear", "keti", "keet", "keto"]
    print(list(a.spellchecker(wordlist, queries)))

    # dict = {'runoob': '菜鸟教程', 'google': 'Google 搜索'}
    #
    # print( "Value : %s" % dict.setdefault('runoob', 'aaaaaa'))
    # print("Value : %s" % dict.setdefault('Taobao', '淘宝'))
    # print( "-----------------")
    # # 该值包含 Taobao
    # for k, v in dict.items():
    #     print(   k, v)