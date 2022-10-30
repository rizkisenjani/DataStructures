class NodeQ:
    def __init__(self, value):
        self.value = value
        self.next = None


class Queue:
    def __init__(self):
        self.head = None
        self.tail = None

    def add(self, value):
        if self.head:
            self.tail.next = NodeQ(value)
            self.tail = self.tail.next
        else:
            self.head = self.tail = NodeQ(value)

    def empty(self):
        if self.head:
            return False
        else:
            return True

    def pop(self):
        if self.head:
            head = self.head
            self.head = self.head.next
            return head.value

    def print_q(self):
        node = self.head
        while not self.empty():
            print(node.value)
            if node.next is not None:
                node = node.next
            else:
                break
