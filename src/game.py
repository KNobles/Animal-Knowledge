class Node:
    def __init__(self, data):
        self.left = None
        self.right = None
        self.data = data

    def insert(self, data):
        if self.data is None:
            self.dat = data
        else:
            if data < self.data:
                if self.left is None:
                    self.left = Node(data)
                else:
                    self.left.insert(data)
            elif data > self.data:
                if self.right is None:
                    self.right = Node(data)
                else:
                    self.right.insert(data)


if __name__ == '__main__':

root = Node('g')
    root.insert('c')
    root.insert('a')
    root.insert('c')
    root.insert('j')
    root.insert('k')
    root.insert('l')
    root.insert('q')
    root.insert('x')
    root.insert('v')
