# using a binary search tree
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
    def __str__(self):
        children = f"{str(self.left)} , {str(self.right)}"
        return f"Val={self.val} children=[{children}]"

def findNodeAndParent(node, num, parent=None):
    if not node:
        return None, None  # Base case: return None if node doesn't exist
    
    if node.val == num:
        return node, parent  # Found the node, return it with its parent

    # Recursively check left and right subtrees
    l, r = None, None
    if node.left:
        l = findNodeAndParent(node.left, num, node)
    if node.right and not l:  # Only search right if not found on the left
        r = findNodeAndParent(node.right, num, node)
    
    return l or r  # Return the first non-None result
    
# min heap
class MinHeapBST:
    def __init__(self):
        self.root = TreeNode(None)
    
    def add(self, n):
        # first val
        if self.root.val == None:
            self.root.val = n
        # adding smallest
        elif n <= self.root.val:
            newNode = TreeNode(n)
            newNode.left = self.root
            self.root = newNode
        # adding val bigger than root
        else:
            p = self.root
            while p.right and p.left:
                p = p.right
            if p.right:
                p.left = TreeNode(n)
            else:
                p.right = TreeNode(n)
    
    def getMin(self):
        return self.root.val
    
    def remove(self, num):
        node, parent = findNodeAndParent(self.root, num)
        
        if not node:
            return
        
        # if we are removing the root
        if not parent:
            # no children
            if not node.left and not node.right:
                self.root = TreeNode(None)
            # two children
            elif node.left and node.right:
                if node.left.val <= node.right.val:
                    self.root = node.left
                    self.addEverything(node.right)
                else:
                    self.root = node.right
                    self.addEverything(node.left)
            # one child
            else:
                if node.left:
                    self.root = node.left
                else:
                    self.root = node.right
            return
        
        side = ""
        if parent.left == node:
            side = "left"
        else:
            side = "right"
        
        # no children so can just remove it
        if not node.left and not node.right:
            if side == "left":
                parent.left = None
            else:
                parent.right = None

        # two children so pick lesser and that is new child and add everything in larger back into the heap
        elif node.left and node.right:
            leftval = node.left.val
            rightval = node.right.val
            if leftval <= rightval:
                if side == "left":
                    parent.left = node.left
                else:
                    parent.right = node.left
                self.addEverything(node.right)
            else:
                if side == "left":
                    parent.left = node.right
                else:
                    parent.right = node.right
                self.addEverything(node.right)
        # one child
        else:
            if node.left:
                if side == "left":
                    parent.left = node.left
                else:
                    parent.right = node.left
            else:
                if side == "left":
                    parent.left = node.right
                else:
                    parent.right = node.right
    
    # adds everything in subtree back into heap
    def addEverything(self, node):
        self.add(node.val)
        if node.left:
            self.addEverything(node.left)
        if node.right:
            self.addEverything(node.right)

    def __str__(self):
        return str(self.root)

class MinHeap:
    def __init__(self):
        self.heap = []
    
    def add(self, n):
        """Insert element while maintaining heap property of val of parent is less than or equal to val of children"""
        self.heap.append(n)
        self._bubble_up(len(self.heap) - 1)

    def getMin(self):
        """Get min element at root of heap"""
        if not self.heap:
            return None
        return self.heap[0]
    
    def remove(self, n):
        """remove specific val and maintains heap property"""
        if not self.heap:
            return None
        try:
            index = self.heap.index(n)
        except ValueError:
            return None
        
        last_val = self.heap.pop()

        if index < len(self.heap):
            self.heap[index] = last_val

            # decide bubble up or heapify down
            parent = (index - 1) // 2
            if index > 0 and self.heap[index] < self.heap[parent]:
                self._bubble_up(index)
            else:
                self._heapify_down(index)

    def _bubble_up(self, index):
        """bubble up smaller vals to maintain heap property"""
        parent = (index - 1) // 2
        while index > 0 and self.heap[parent] > self.heap[index]:
            # swap parent and child
            self.heap[index], self.heap[parent] = self.heap[parent], self.heap[index]
            index = parent
            parent = (index - 1) // 2
        
    def _heapify_down(self, index):
        """bubble down an index if it's too big to maintain heap property"""
        size = len(self.heap)
        while True:
            left = 2 * index + 1
            right = 2 * index + 2
            smallest = index

            if left < size and self.heap[left] < self.heap[index]:
                smallest = left
            if right < size and self.heap[right] < self.heap[index]:
                smallest = right
            if smallest == index:
                break
            
            # swap smaller value to be higher in the tree
            self.heap[index], self.heap[smallest] = self.heap[smallest], self.heap[index]
            index = smallest
    
    def __str__(self):
        return str(self.heap)
        
        
h = MinHeap()
h.add(3)
h.add(2)
h.add(5)
h.add(6)
h.add(1)
h.add(45)
print(h)
h.remove(3)
print(h)
h.remove(2)
print(h)
print("---------------------------------------")
t = MinHeap()
t.add(4)
t.add(9)
print(t.getMin())
t.remove(4)
print(t.getMin())
print("---------------------------------------")

heap = MinHeap()
operations = [
    (1, 286789035),
    (1, 255653921),
    (1, 274310529),
    (1, 494521015),
    (3, None),         # Get min
    (2, 255653921),    # Remove 255653921
    (2, 286789035),    # Remove 286789035
    (3, None),         # Get min
    (1, 236295092),
    (1, 254828111),
    (2, 254828111),    # Remove 254828111
    (1, 465995753),
    (1, 85886315),
    (1, 7959587),
    (1, 20842598),
    (2, 7959587),      # Remove 7959587
    (3, None),         # Get min
    (1, -51159108),
    (3, None),         # Get min
    (2, -51159108),    # Remove -51159108
    (3, None),         # Get min
    (1, 789534713),
]

for op, val in operations:
    if op == 1:
        heap.add(val)
    elif op == 2:
        heap.remove(val)
    elif op == 3:
        print(heap.getMin()) 