class Node:
    def __init__(self, key=None, value=None):
        self.key, self.value = key, value
        self.prev = self.next = None

class LRUCache:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = {} # Cache maps a key->node
        self.head = Node()
        self.head.next = self.head.prev = self.head

    def delete(self, node):
        prev, nxt = node.prev, node.next
        prev.next = nxt 
        nxt.prev = prev

    def insert(self, node):
        nxt = self.head.next
        self.head.next = node
        nxt.prev = node
        node.prev, node.next = self.head, nxt

    def get(self, key: int) -> int:
        # we want to check the cache and see if key is in it
        # Do not forget to update it's position
        if key in self.cache:
            node = self.cache[key]
            self.delete(node)
            self.insert(node)
            return node.value
        return -1

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.delete(self.cache[key])
        node = Node(key, value)
        self.cache[key] = node
        self.insert(node)

        if len(self.cache) > self.capacity:
            lastNode = self.head.prev
            self.delete(lastNode)
            del self.cache[lastNode.key]
        