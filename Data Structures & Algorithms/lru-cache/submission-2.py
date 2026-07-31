class Node:
    def __init__(self, key, val):
        self.prev = None
        self.nxt = None
        self.key = key
        self.val = val

class LRUCache:

    def __init__(self, capacity: int):
        self.cache = {}
        self.cap = capacity
        self.right = Node(0, 0)
        self.left = Node(0, 0)

        self.right.prev = self.left
        self.left.nxt = self.right

    def insert(self, node):
        # adds it to the right
        prev = self.right.prev

        prev.nxt = node
        self.right.prev = node

        # own pointers
        node.nxt = self.right
        node.prev = prev

    def remove(self, node):
        prev = node.prev
        nxt = node.nxt

        prev.nxt = nxt
        nxt.prev = prev

        # removing current pointers
        node.prev = node.nxt = None

    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1

        node = self.cache[key]
        self.remove(node)
        self.insert(node)
        return node.val

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            node = self.cache[key]
            self.remove(node)

        node = Node(key, value)
        self.cache[key] = node

        self.insert(node)

        if len(self.cache) > self.cap:
            lru = self.left.nxt
            self.remove(lru)
            del self.cache[lru.key]
