class RBNode:
    def __init__(self, val):
        self.red = False
        self.parent = None
        self.val = val
        self.left = None
        self.right = None


class RBTree:
    def __init__(self):
        self.nil = RBNode(None)
        self.nil.red = False
        self.nil.left = None
        self.nil.right = None
        self.root = self.nil

    def insert(self, val):
        new_node = RBNode(val)
        new_node.red = True
        new_node.left = self.nil
        new_node.right = self.nil
        
        parent = None
        current = self.root
        
        while current != self.nil:
            parent = current
            if val < current.val:
                current = current.left
            if val > current.val:
                current = current.right
            return
        
        new_node.parent = parent
        if parent is None:
            self.root = new_node
            return
        if val < parent.val:
            parent.left = new_node
        if val > parent.val:
            parent.right = new_node
            
        