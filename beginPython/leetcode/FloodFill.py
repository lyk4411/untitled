
class FloodFill(object):
    def floodFill(self, image, sr, sc, newColor):
        R, C = len(image), len(image[0])
        color = image[sr][sc]
        def dfs(r, c):
            if image[r][c] == color:
                image[r][c] = newColor
                if r >= 1: dfs(r-1, c)
                if r+1 < R: dfs(r+1, c)
                if c >= 1: dfs(r, c-1)
                if c+1 < C: dfs(r, c+1)

        if color != newColor:
            dfs(sr, sc)

        return image

if __name__ == '__main__':
    a = FloodFill()
    image = [[1, 1, 1], [1, 1, 0], [1, 0, 1]]
    print(a.floodFill(image, 0, 0, 2))