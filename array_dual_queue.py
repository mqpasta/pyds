class ArrayDualQueue:

    def __init__(self, n):
        self.data = [0 for x in range(n)]
        self.f = 0
        self.r = 0
        self.i = len(self.data)-1

    def Push(self, e):
        self.data[self.i] = e
        self.i = self.i - 1

    def Pop(self):
        x = self.data[self.i+1]
        self.i = self.i + 1
        return(x)

    def Enqueue(self ,e):
        self.data[self.f] = e
        self.f += 1

    def Dequeue(self):
        x = self.data[self.r]
        self.r = self.r + 1
        return(x)
    
        
