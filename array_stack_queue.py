class ArrayStack:
    def __init__(self, n):
        self.data = [0 for i in range(n)]
        self.i = 0
        self.size = n

    def Push(self, e):
        if self.Count()<self.size:
            self.data[self.i] = e
            self.i += 1
        else:
            raise Exception("Overflow")

    def Pop(self):
        if self.IsEmpty():
            raise Exception("Underflow")
        self.i -= 1
        return(self.data[self.i])

    def IsEmpty(self):
        return self.i==0

    def Count(self):
        return self.i
    

class ArrayQueue:
    def __init__(self, n):
        self.data = [0 for i in range(n)]
        self.f = 0 #front
        self.r = 0 #rear
        self.c = 0 #count
        self.size = n

    def Count(self):
        return self.c

    def IsEmpty(self):
        return self.c == 0

    def Enqueue(self, e):
        if self.Count() < self.size:
            self.data[self.r] = e
            self.r = (self.r + 1) % self.size
            self.c += 1
        else:
            raise Exception("Overflow")

    def Dequeue(self):
        if self.IsEmpty():
            raise Exception("Underflow")

        x = self.data[self.f]
        self.f = (self.f + 1) % self.size
        self.c -= 1
        return (x)
    
def TestQueue():
    q = ArrayQueue(5)
    q.Enqueue(5)
    q.Enqueue(7)
    q.Enqueue(8)
    q.Dequeue()
    q.Enqueue(7)
    q.Dequeue()
    q.Enqueue(15)
    q.Enqueue(25)
    print(q.data)
