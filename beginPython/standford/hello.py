
import sys
from random import choice,seed

grammer={'<start>':[['this'],['<object>'],[' is here.']],
         '<object>':[['computer'],['car'],['assigment']]
         }

def expand(symbol):
    #print("symbol")
    #print(symbol)
    if symbol.startswith('<'):
        definetions=grammer[symbol]
        print("definetions:")
        print(definetions)
        expansion=choice(definetions)
        print("expansion:")
        print(expansion)
        print("==================================================")
        print("map function:")
        aa=map(expand,expansion)
        print('aa:')
        print(list(aa))
        #z=map(lambda x, y: x + y, [1, 3, 5, 7, 9], [2, 4, 6, 8, 10])
        #print(list(z))
    else:
        print(symbol)


if __name__ == '__main__':
    seed()
    expand('<start>')
