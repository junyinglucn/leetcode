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
