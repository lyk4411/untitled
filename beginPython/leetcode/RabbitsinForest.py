import collections


class RabbitsinForest(object):
    def numRabbits(self, answers):
        res = 0
        length = len(answers)
        if length == 0:
            return 0
        d = collections.defaultdict(int)
        for ans in answers:
            d[ans] += 1
        for n in d.keys():
            group = d.get(n) // (n + 1)
            if d.get(n) % (n + 1) == 0:
                res += group * (n + 1)
            else:
                res += (group + 1) * (n + 1)
        return res

if __name__ == '__main__':
    a = RabbitsinForest()
    print(a.numRabbits([1, 1, 2]))
    print(a.numRabbits([10, 10, 10]))
    print(a.numRabbits([1, 0, 1, 0, 0]))