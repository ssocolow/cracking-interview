# singly linked list implementation of queue
# storing tail so can efficiently add to queue

class ListNode:
    def __init__(self, val):
        self.next = None
        self.val = val

class Queue:
    def __init__(self):
        self.head = ListNode("start")
        self.tail = ListNode("end")
        self.head.next = self.tail
    
    def enqueue(self, item):
        self.tail.next = ListNode(item)
        self.tail = self.tail.next
    
    def dequeue(self):
        ret = self.head.val
        self.head = self.head.next
        return ret
    
    def __str__(self):
        ret = ""
        p = self.head
        while p:
            ret += f"{p.val} - "
            p = p.next
        return ret
    
q = Queue()
q.enqueue('a')
q.enqueue('b')
q.enqueue('c')
q.enqueue('d')
print(q)
print(q.dequeue())
print(q.dequeue())
print(q)