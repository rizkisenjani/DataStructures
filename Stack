class NodeS:
    def __init__(self, value):
        self.value = value
        self.prev = None


class Stack:
    def __init__(self):
        self.top = None

    def push(self, value):
        if self.top:
            new_node = NodeS(value)
            new_node.prev = self.top
            self.top = new_node
        else:
            self.top = NodeS(value)

    def empty(self):
        if self.top:
            return False
        else:
            return True

    def print_stack(self):
        node = self.top
        while not self.empty():
            print(node.value)
            if node.prev is not None:
                node = node.prev
            else:
                break

    def pop(self):
        if self.top:
            top = self.top
            self.top = self.top.prev
            return top

    def peek(self):
        if self.top is not None:
            return self.top.value
        else:
            return self.empty()
