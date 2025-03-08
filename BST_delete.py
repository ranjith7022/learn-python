class BSTNode:
    def delete(self, val):
        if self.val is None:
            return None

        if val < self.val:
            if self.left:
                self.left = self.left.delete(val)
            return self

        if val > self.val:
            if self.right:
                self.right = self.right.delete(val)
            return self

        # Node to delete found
        if self.right is None:
            return self.left
        if self.left is None:
            return self.right

        # Node has two children: find inorder successor (minimum of right subtree)
        min_larger_node = self.right
        while min_larger_node.left:
            min_larger_node = min_larger_node.left

        self.val = min_larger_node.val  # Copy inorder successor's value

        # Delete the inorder successor from the right subtree
        self.right = self.right.delete(min_larger_node.val)
        return self

                
            
            

    # don't touch below this line

    def __init__(self, val=None):
        self.left = None
        self.right = None
        self.val = val

    def insert(self, val):
        if not self.val:
            self.val = val
            return

        if self.val == val:
            return

        if val < self.val:
            if self.left:
                self.left.insert(val)
                return
            self.left = BSTNode(val)
            return

        if self.right:
            self.right.insert(val)
            return
        self.right = BSTNode(val)
        
