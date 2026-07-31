class Node:
    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.prev = None
        self.next = None

class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.mymap = dict()
        self.left = Node(0,0)
        self.right = Node(0,0)
        self.left.next = self.right
        self.right.prev = self.left

    def remove(self, key):
        node = self.mymap[key]
        prev = node.prev
        next = node.next

        prev.next = next
        next.prev = prev

    
    def insert(self, node):
        prev = self.right.prev

        prev.next = node
        self.right.prev = node

        node.next = self.right
        node.prev = prev
        

    def get(self, key: int) -> int:
        if key not in self.mymap:
            return -1
        node = self.mymap[key]
        self.remove(key)
        self.insert(node)
        return node.val

    def put(self, key: int, value: int) -> None:
        node = None
        if key in self.mymap:
            node = self.mymap[key]
            self.remove(key)
            
        node = Node(key, value)

        self.mymap[key] = node
        self.insert(node)

        if len(self.mymap) > self.capacity:
            rmnode = self.left.next
            self.remove(rmnode.key)
            del self.mymap[rmnode.key]

        
        
