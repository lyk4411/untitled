
class BeautifulArrangementII(object):
    def constructArray(self, n, k):
        ans = list(range(1, n - k))
        for i in range(k + 1):
            if i % 2 == 0:
                ans.append(n - k + i // 2)
            else:
                ans.append(n - i // 2)

        return ans

if __name__ == '__main__':
    a = BeautifulArrangementII()
    print(a.constructArray(3, 1))
    print(a.constructArray(8, 6))
    print(a.constructArray(18, 6))

