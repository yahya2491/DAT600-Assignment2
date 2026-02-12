class Node:
    def __init__(self, key, data):
        self.key = key
        self.data = data
        self.left = None
        self.right = None
        self.height = 1


class AVLSet:
    def __init__(self):
        self.root = None

    def height(self, node):
        return node.height if node else 0

    def update_height(self, node):
        node.height = 1 + max(self.height(node.left),
                              self.height(node.right))

    def balance_factor(self, node):
        return self.height(node.left) - self.height(node.right)

    def rotate_right(self, y):
        x = y.left
        T2 = x.right

        x.right = y
        y.left = T2

        self.update_height(y)
        self.update_height(x)

        return x

    def rotate_left(self, x):
        y = x.right
        T2 = y.left

        y.left = x
        x.right = T2

        self.update_height(x)
        self.update_height(y)

        return y

    def _insert(self, node, key, data):
        if not node:
            return Node(key, data)

        if key < node.key:
            node.left = self._insert(node.left, key, data)
        elif key > node.key:
            node.right = self._insert(node.right, key, data)
        else:
            return node

        self.update_height(node)
        balance = self.balance_factor(node)

        if balance > 1 and key < node.left.key:
            return self.rotate_right(node)

        if balance < -1 and key > node.right.key:
            return self.rotate_left(node)

        if balance > 1 and key > node.left.key:
            node.left = self.rotate_left(node.left)
            return self.rotate_right(node)

        if balance < -1 and key < node.right.key:
            node.right = self.rotate_right(node.right)
            return self.rotate_left(node)

        return node

    def insert(self, key, data):
        self.root = self._insert(self.root, key, data)

    def _find(self, node, key):
        if not node:
            return None, None, False
        if key == node.key:
            return node.key, node.data, True
        if key < node.key:
            return self._find(node.left, key)
        return self._find(node.right, key)

    def find(self, key):
        return self._find(self.root, key)

    def find_min(self):
        node = self.root
        if not node:
            return None
        while node.left:
            node = node.left
        return node.key, node.data

    def find_max(self):
        node = self.root
        if not node:
            return None
        while node.right:
            node = node.right
        return node.key, node.data

    def find_next(self, key):
        curr = self.root
        succ = None
        while curr:
            if key < curr.key:
                succ = curr
                curr = curr.left
            else:
                curr = curr.right
        return (succ.key, succ.data) if succ else None

    def find_prev(self, key):
        curr = self.root
        pred = None
        while curr:
            if key > curr.key:
                pred = curr
                curr = curr.right
            else:
                curr = curr.left
        return (pred.key, pred.data) if pred else None

    def build(self, elements):
        for key, data in elements:
            self.insert(key, data)
