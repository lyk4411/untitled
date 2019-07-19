class CarFleet(object):
    def carFleet(self, target, position, speed):
        cars = sorted(zip(position, speed))
        print(cars)
        times = [float(target - p) / s for p, s in cars]
        print(times)
        ans = 0
        while len(times) > 1:
            lead = times.pop()
            if lead < times[-1]:
                ans += 1  # if lead arrives sooner, it can't be caught
            else:
                times[-1] = lead  # else, fleet arrives at later time 'lead'

        return ans + bool(times)  # remaining car is fleet (if it exists)

if __name__ == '__main__':
    a = CarFleet()
    target = 12
    position = [10, 8, 0, 5, 3]
    speed = [2, 4, 1, 1, 3]
    print(a.carFleet(target, position, speed))