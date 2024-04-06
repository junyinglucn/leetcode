# Solution A
class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.dict = {}
        self.l = []

    def get(self, key: int) -> int:
        if key in self.dict:
            value = self.dict[key]
            self.l.remove(key)
            self.l.insert(0, key)
        else:
            value = -1
        return value

    def put(self, key: int, value: int) -> None:
        if key in self.dict:
            self.dict[key] = value
            self.l.remove(key)
            self.l.insert(0, key)
        else:
            if len(self.dict) == self.capacity:
                oldest_key = self.l.pop()
                self.dict.pop(oldest_key)
            self.dict[key] = value
            self.l.insert(0, key)

# Solution B
class DlinkedNode:
    def __init__(self, key=0, value=0):
        self.key = key
        self.value = value
        self.prev = None

        self.next = None


class LRUCache:

    def __init__(self, capacity):
        self.cache = {}
        self.head = DlinkedNode()
        self.tail = DlinkedNode()
        self.head.next = self.tail
        self.tail.prev = self.head
        self.capacity = capacity
        self.size = 0

    def get(self, key):
        if key not in self.cache:
            return -1
        node = self.cache[key]
        self.move2head(node)
        return node.value

    def put(self, key, value):
        if key not in self.cache:
            node = DlinkedNode(key, value)
            self.cache[key] = node
            self.add2head(node)
            self.size += 1
            if self.size > self.capacity:
                removed = self.removetail()
                self.cache.pop(removed.key)
                self.size -= 1
        else:
            node = self.cache[key]
            node.value = value
            self.move2head(node)

    def add2head(self, node):
        node.prev = self.head
        node.next = self.head.next
        self.head.next.prev = node
        self.head.next = node

    def move2head(self, node):
        node.prev.next = node.next
        node.next.prev = node.prev
        self.add2head(node)

    def removetail(self):
        node = self.tail.prev
        node.prev.next = node.next
        node.next.prev = node.prev
        return node