from queue import Queue


class SystemCall(object):
    def handle(self):
        pass

class GetTid(SystemCall):
    def handle(self):
        self.task.sendval = self.task.tid
        self.sched.schedule(self.task)



class NewTask(object):
    taskid = 0
    def __init__(self,target):
        NewTask.taskid += 1
        self.tid = NewTask.taskid # Task ID
        self.target = target # Target coroutine
        self.sendval = None # Value to send
    def run(self):
        return self.target.send(self.sendval)
    def handle(self):
        tid = self.sched.new(self.target)
        self.task.sendval = tid
        self.sched.schedule(self.task)

def bar():
    while True:
        print ("I'm bar")
        yield

class KillTask(SystemCall):
    def __init__(self,tid):
        self.tid = tid
    def handle(self):
        task = self.sched.taskmap.get(self.tid,None)
        if task:
            task.target.close()
            self.task.sendval = True
        else:
            self.task.sendval = False
            self.sched.schedule(self.task)


class Scheduler(object):
    def __init__(self):
        self.ready = Queue()
        self.taskmap = {}
        self.exit_waiting = {}

    def exit(self, task):
        print("Task %d terminated" % task.tid)
        del self.taskmap[task.tid]
        for task in self.exit_waiting.pop(task.tid, []):
            self.schedule(task)

    def waitforexit(self, task, waittid):
        if waittid in self.taskmap:
            self.exit_waiting.setdefault(waittid, []).append(task)
            return True
        else:
            return False
    def new(self,target):
        newtask = NewTask(target)
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
                if isinstance(result, SystemCall):
                    result.task = task
                    result.sched = self
                    result.handle()
                    continue
            except StopIteration:
                self.exit(task)
                continue
            self.schedule(task)

def foo():
    mytid = yield GetTid()
    for i in range(5):
        print ("I'm foo", mytid)
        yield
# def main():
#     child = yield NewTask(foo()) # Launch new task
#     for i in range(5):
#         yield
#     yield KillTask(child) # Kill the task
#     print("main done")

class WaitTask(SystemCall):
    def __init__(self,tid):
        self.tid = tid
    def handle(self):
        result = self.sched.waitforexit(self.task,self.tid)
        self.task.sendval = result
        # If waiting for a non-existent task,
        # return immediately without waiting
        if not result:
            self.sched.schedule(self.task)

def main1():
    print ("Waiting for child 00000")
    child = yield NewTask(foo())
    print ("Waiting for child")
    yield WaitTask(child)
    print ("Child done")

if __name__ == '__main__':
    print("=============================")
    main1()
    print("==========================================================")
