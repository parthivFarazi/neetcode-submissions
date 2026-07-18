class Node:
    def __init__(self, key, value):
        self.key = key
        self.val = value
        self.next = None
        self.prev = None


class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.adict = {}
        self.head = Node(0, 0)
        self.tail = Node(0, 0)

        self.head.next = self.tail
        self.tail.prev = self.head

    def remove(self, node):
        node.next.prev = node.prev
        node.prev.next = node.next
    
    def addFront(self, node):
        self.head.next.prev = node
        node.next = self.head.next
        self.head.next = node
        node.prev = self.head

    def get(self, key: int) -> int:
        if key not in self.adict:
            return -1
        else:
            node = self.adict[key]
            self.remove(node)
            self.addFront(node)
            return node.val

    def put(self, key: int, value: int) -> None:
        if key in self.adict:
            oldNode = self.adict[key]
            newNode = Node(key, value)
            self.remove(oldNode)
            self.addFront(newNode)
            self.adict[key] = newNode
        else:
            if len(self.adict) == self.capacity:
                temp = self.tail.prev
                self.remove(temp)
                del self.adict[temp.key]
            newNode = Node(key, value)
            self.addFront(newNode)
            self.adict[key] = newNode
        
