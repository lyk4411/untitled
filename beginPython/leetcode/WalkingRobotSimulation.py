class WalkingRobotSimulation(object):
    def robotSim(self, commands, obstacles):
        dx = [0, 1, 0, -1]
        dy = [1, 0, -1, 0]
        x = y = di = 0
        obstacleSet = set(map(tuple, obstacles))
        # print(obstacleSet)
        ans = 0

        for cmd in commands:
            if cmd == -2:  # left
                di = (di - 1) % 4
            elif cmd == -1:  # right
                di = (di + 1) % 4
            else:
                for k in range(cmd):
                    if (x + dx[di], y + dy[di]) not in obstacleSet:
                        x += dx[di]
                        y += dy[di]
                        ans = max(ans, x * x + y * y)

        return ans

if __name__ == '__main__':
    a = WalkingRobotSimulation()
    print(a.robotSim([4, -1, 3],[]))
    print(a.robotSim([4, -1, 4, -2, 4], [[2, 4]]))
