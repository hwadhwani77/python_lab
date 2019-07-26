class Queue:
    def __init__(self, capacity):
        self.front = self.size = 0
        self.rear = capacity - 1
        self.Q = [None]*capacity
        self.capacity = capacity
    def isFull(self):
        return self.size == self.capacity
    def isEmpty(self):
        return self.size == 0
    def Enqueue(self, item):
        if self.isFull():
            print("Full")
            return 
        print(self.rear)
        self.rear = (self.rear + 1) % (self.capacity)
        self.Q[self.rear] = item
        self.size += 1
        print("%s enqueued" %str(item))
        print(self.Q, self.rear, self.front)
    def Dequeue(self):
        if(self.isEmpty()):
            print("Empty")
            return
        print("Dequeued item %s" %str(self.Q[self.front]))
        self.Q[self.front] = None
        self.front = (self.front + 1) % (self.capacity)
        self.size -= 1
        print(self.Q, self.rear, self.front)

q1 = Queue(5)
q1.Enqueue(1)
q1.Enqueue(2)
q1.Enqueue(3)
q1.Enqueue(4)
q1.Enqueue(5)
q1.Enqueue(6)

q1.Dequeue()
q1.Dequeue()

