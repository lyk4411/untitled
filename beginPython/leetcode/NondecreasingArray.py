from pip._vendor.requests.packages.urllib3.connectionpool import xrange

# 这道题给了我们一个数组，说我们最多有1次修改某个数字的机会，
# 问能不能将数组变为非递减数组。题目中给的例子太少，不能覆盖
# 所有情况，我们再来看下面三个例子：
#
# 4，2，3
# -1，4，2，3
# 2，3，3，2，4
#
# 我们通过分析上面三个例子可以发现，当我们发现后面的数字小于前
# 面的数字产生冲突后，有时候需要修改前面较大的数字(比如前两个
# 例子需要修改4)，有时候却要修改后面较小的那个数字(比如前第三个
# 例子需要修改2)，那么有什么内在规律吗？是有的，判断修改那个数
# 字其实跟再前面一个数的大小有关系，首先如果再前面的数不存在，
# 比如例子1，4前面没有数字了，我们直接修改前面的数字为当前的数
# 字2即可。而当再前面的数字存在，并且小于当前数时，比如例子2，-1
# 小于2，我们还是需要修改前面的数字4为当前数字2；如果再前面的数
# 大于当前数，比如例子3，3大于2，我们需要修改当前数2为前面的数3。
# 这是修改的情况，由于我们只有一次修改的机会，所以用一个变量cnt，
# 初始化为1，修改数字后cnt自减1，当下次再需要修改时，如果cnt已经
# 为0了，直接返回false。遍历结束后返回true，参见代码如下：
class NondecreasingArray(object):
    def checkPossibility(self, A):
        p = None
        for i in xrange(len(A) - 1):
            if A[i] > A[i+1]:
                if p is not None:
                    return False
                p = i

        return (p is None or p == 0 or p == len(A)-2 or
                A[p-1] <= A[p+1] or A[p] <= A[p+2])

if __name__ == '__main__':
    a = NondecreasingArray()
    print(a.checkPossibility([4,2,3]))
    print(a.checkPossibility([4,2,1]))
    print(a.checkPossibility([2,3,3,2,4]))
    print(a.checkPossibility([1,2,7,4,5]))
