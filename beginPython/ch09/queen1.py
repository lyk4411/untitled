def conflict(state,nextx):
    '定义冲突函数,state为元组，nextx为下一个皇后的水平位置，nexty为下一个皇后的垂直位置'
    nexty = len(state)
    for i in range(nexty):
        if abs(state[i]-nextx) in (0,nexty-i):#若下一个皇后和前面的皇后列相同或者在一条对角线上，则冲突
            return True
    return False

def queens(num,state=()):
    '八皇后问题，这里num表示规模'
    if num == 8:
        print(state)

    for pos in list(range(8)):
        if not conflict(state,pos):#位置不冲突
            queens(num + 1,state + (pos,))





queens(0,())
# print(list(queens(5)))
# print(list(queens(6)))
# print(list(queens(7)))
# print(list(queens(8)))