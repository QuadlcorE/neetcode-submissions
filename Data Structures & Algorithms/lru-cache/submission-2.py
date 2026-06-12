class Node:
    def __init__(self, key, value, next=None , prev=None):
        self.key = key
        self.value = value
        self.next = next
        self.prev = prev

class LRUCache:

    def __init__(self, capacity: int):
        # Here we need to instantiate the cache capacity and head.
        self.head = Node(key=0, value=0) 
        self.head.next = self.head.prev = self.head
        self.capacity = capacity
        self.cache = {}

    def get(self, key: int) -> int:
        # when we want to get a node we check the cache and reinsert the node in the linked list.
        if key not in self.cache:
            return -1
        node = self.cache[key]
        self.delete(node)
        self.insert(node)
        return node.value

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.delete(self.cache[key])
            # node = self.cache[key]
            # self.delete(node)
            # self.insert(node)
            # return
        node = Node(key, value)
        self.insert(node)
        self.cache[key] = node
        if len(self.cache) > self.capacity:
            del_node = self.head.prev
            self.delete(del_node)
            del self.cache[del_node.key]
    
    def insert(self, node):
        node.next = self.head.next
        node.prev = self.head
        node.next.prev = node
        self.head.next = node
    
    def delete(self, node):
        node.prev.next = node.next
        node.next.prev = node.prev