from queue import Queue


class NodeBST:
    def __init__(self, value):
        self.value = value
        self.right = None
        self.left = None


class BST:
    def __init__(self):
        self.root = None

    def insert(self, value):
        curr = self.root
        prev = None
        if self.root:
            while curr:
                prev = curr
                if value < curr.value:
                    curr = curr.left
                else:
                    curr = curr.right

            if value < prev.value:
                prev.left = NodeBST(value)
            elif value > prev.value:
                prev.right = NodeBST(value)
            else:
                print('Value has already existed')

        else:
            self.root = NodeBST(value)

    def print_bfs(self):
        q = Queue()
        q.add(self.root)
        while not q.empty():
            node = q.pop()
            print(node.value, end=' ')
            if node.left:
                q.add(node.left)
            if node.right:
                q.add(node.right)

    def print_leaves(self):
        q = Queue()
        q.add(self.root)
        while not q.empty():
            node = q.pop()
            if node.left:
                q.add(node.left)
            if node.right:
                q.add(node.right)
            if (node.left is None and
                    node.right is None):
                print(node.value, end=' ')

    def preorder(self, root):
        if root:
            print(root.value)
            self.preorder(root.left)
            #print(root.value, end=' ')
            self.preorder(root.right)



bst = BST()

bst.insert(8)
bst.insert(8)
bst.insert(6)
bst.insert(7)
bst.insert(11)
bst.insert(10)
bst.insert(67)

print('BFS:')
bst.print_bfs()
print('\n')
print('Leaves:')
bst.print_leaves()
print('\nDFS:')
bst.preorder(bst.root)