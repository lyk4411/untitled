from queue import Queue
from socket import socket, AF_INET, SOCK_STREAM

import select


class SystemCall(object):
    def handle(self):
        pass
class Scheduler(object):
    def __init__(self):
        self.ready = Queue()
        self.taskmap = {}
        self.exit_waiting = {}
        self.read_waiting = {}
        self.write_waiting = {}

    def waitforread(self, task, fd):
        self.read_waiting[fd] = task

    def waitforwrite(self, task, fd):
        self.write_waiting[fd] = task

    def iopoll(self, timeout):
        if self.read_waiting or self.write_waiting:
            r, w, e = select.select(self.read_waiting,
                                    self.write_waiting, [], timeout)

            for fd in r: self.schedule(self.read_waiting.pop(fd))
            for fd in w: self.schedule(self.write_waiting.pop(fd))

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

def handle_client(client,addr):
    print ("Connection from", addr)
    while True:
        data = client.recv(65536)
        if not data:
            break
        client.send(data)
    client.close()
    print ("Client closed")
    yield # Make the function a generator/coroutine
def server(port):
    print ("Server starting")
    sock = socket(AF_INET, SOCK_STREAM)
    sock.bind(("",port))
    sock.listen(5)
    while True:
        client,addr = sock.accept()
        yield NewTask(handle_client(client,addr))

def alive():
    while True:
        print ("I'm alive!")
        yield
sched = Scheduler()
sched.new(alive())
sched.new(server(45000))
sched.mainloop()