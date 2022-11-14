class NodeQ:
    def __init__(self, value):
        self.value = value
        self.next = None


class Queue:
    def __init__(self):
        self.first = None
        self.last = None

    def add(self, value):
        if self.first:
            self.last.next = NodeQ(value)
            self.last = self.last.next
        else:
            self.first = self.last = NodeQ(value)

    def empty(self):
        if self.first:
            return False
        else:
            return True

    def pop(self):
        if self.first:
            head = self.first
            self.first = self.first.next
            return head.value

    def print_q(self):
        node = self.first
        while not self.empty():
            print(node.value)
            if node.next:
                node = node.next
            else:
                break
