class Node:
    """A node in the AVL tree."""
    
    def __init__(self, key, data):
        self.key = key
        self.data = data
        self.left = None
        self.right = None
        self.height = 1
