class MostProfitAssigningWork(object):
    def maxProfitAssignment(self, difficulty, profit, worker):
        jobs = list(zip(difficulty, profit))
        jobs.sort()
        ans = i = best = 0
        for skill in sorted(worker):
            while i < len(jobs) and skill >= jobs[i][0]:
                best = max(best, jobs[i][1])
                i += 1
            ans += best
        return ans

if __name__ == '__main__':
    a = MostProfitAssigningWork()
    print(a.maxProfitAssignment(difficulty = [2,4,6,8,10], profit = [10,20,30,40,50], worker = [4,5,6,7]))