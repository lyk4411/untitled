from queue import Queue


class Task(object):
    taskid = 0
    def __init__(self,target):
        Task.taskid += 1
        self.tid = Task.taskid # Task ID
        self.target = target # Target coroutine
        self.sendval = None # Value to send
    def run(self):
        return self.target.send(self.sendval)


def foo():
    print ("Part 1")
    yield
    print ("Part 2")
    yield


# t1 = Task(foo())
#
# t1.run()
# t1.run()


class Scheduler(object):
    def __init__(self):
        self.ready = Queue()
        self.taskmap = {}

    def exit(self, task):
        print("Task %d terminated" % task.tid)
        del self.taskmap[task.tid]
    def new(self,target):
        newtask = Task(target)
        self.taskmap[newtask.tid] = newtask
        self.schedule(newtask)
        return newtask.tid
    def schedule(self,task):
       self.ready.put(task)
    def mainloop(self):
        while self.taskmap:
            task = self.ready.get()
            try:
                result = task.run()
            except StopIteration:
                self.exit(task)
                continue
            self.schedule(task)

def foo():
    for i in range(10):
        print ("I'm foo")
        yield
def bar():
    for i in range(10):
        print ("I'm bar")
        yield

sched = Scheduler()
sched.new(foo())
sched.new(bar())
sched.mainloop()