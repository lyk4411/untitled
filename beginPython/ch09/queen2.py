def conflict(state,nextx):
    '定义冲突函数,state为元组，nextx为下一个皇后的水平位置，nexty为下一个皇后的垂直位置'
    nexty = len(state)
    for i in range(nexty):
        if abs(state[i]-nextx) in (0,nexty-i):#若下一个皇后和前面的皇后列相同或者在一条对角线上，则冲突
            return True
    return False

def queens(num=8,state=()):
    '八皇后问题，这里num表示规模'
    for pos in range(num):
        if not conflict(state,pos):#位置不冲突
            # print("pos")
            # print(pos)
            if len(state) == num - 1:#若是最后一个皇后，则返回该位置
                yield (pos,)
                print("last pos:" + str(pos))

            else:#若不是最后一个皇后，则将该位置返回到state元组并传给后面的皇后
                for result in queens(num,state + (pos,)):
                    print("================")
                    print("state:" + str(state))
                    print("pos:" + str(pos,))
                    print("result:" + str(result))
                    print("================")
                    yield  (pos,) + result



print(list(queens(4)))