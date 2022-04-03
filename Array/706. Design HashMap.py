class LL_Node:
    def __init__(self, key, val, nxt=None):
        self.key = key
        self.val = val
        self.next = nxt


class MyHashMap:

    def __init__(self):
        self.hashmap = [None] * 10000

    def put(self, key: int, value: int) -> None:
        k = key % 10000
        if self.hashmap[k] is None:
            self.hashmap[k] = LL_Node(key, value)
        else:
            node = self.hashmap[k]
            while node:
                if node.key == key:
                    node.val = value
                    return
                node = node.next
            node = self.hashmap[k]
            self.hashmap[k] = LL_Node(key, value, node)

    def get(self, key: int) -> int:
        k = key % 10000
        if self.hashmap[k] is None:
            return -1
        else:
            node = self.hashmap[k]
            while node:
                if node.key == key:
                    return node.val
                node = node.next
            return -1

    def remove(self, key: int) -> None:
        k = key % 10000
        if self.hashmap[k]:
            node = self.hashmap[k]
            if node.key == key:
                self.hashmap[k] = node.next
                return
            prev = node
            node = node.next
            while node:
                if node.key == key:
                    prev.next = node.next
                    return
                prev = prev.next
                node = node.next