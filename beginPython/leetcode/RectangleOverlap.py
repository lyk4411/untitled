class RectangleOverlap(object):
    def isRectangleOverlap(self, rec1, rec2):
        return not (rec1[2] <= rec2[0] or  # left
                    rec1[3] <= rec2[1] or  # bottom
                    rec1[0] >= rec2[2] or  # right
                    rec1[1] >= rec2[3])  # top

if __name__ == '__main__':
    a = RectangleOverlap()
    print(a.isRectangleOverlap([0,0,2,2], [1,1,3,3]))
    print(a.isRectangleOverlap([0,0,1,1], rec2 = [1,0,2,1]))