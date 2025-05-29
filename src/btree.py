from BTrees.OOBTree import OOBTree

class BTreeWrapper:
    def __init__(self):
        self.tree = OOBTree()

    def insert(self, word):
        self.tree[word] = True  # Value can be anything

    def search(self, word):
        return word in self.tree
