import re


def lines(file):
    for line in file:
        yield line
    # return
    yield '\n'


def blocks(file):
    print("hello world.")
    block = []
    for line in lines(file):
        if line.strip():
            block.append(line)
            # print ('block.apend {{{%s}}}') %line
        elif block:
            # print 'join(block).strip {{{%s}}}' % ''.join(block).strip()
            yield ''.join(block).strip()
            block = []

title = True

if __name__ == "__main__":
    for block in blocks(open('F:/Users/lyk/PycharmProjects/untitled/beginPython/ch20/temp_input.txt')):
        block = re.sub(r'\*(.+?)\*', r'<em>\1</em>', block)
        if title:
            print('<h1>')
            print(block)
            print('</h1>')
            title = False
        else:
            print('<p>')
            print(block)
            print('</p>')
            print('</body></html>')