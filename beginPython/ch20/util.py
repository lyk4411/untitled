def lines(file):
    for line in file:
        yield line
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


if __name__ == "__main__":
    print("qq")
    blocks(r'F:/Users/lyk/PycharmProjects/untitled/beginPython/ch20/temp_input.txt')