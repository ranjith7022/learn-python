class BSTNode:
    
    def height(self):
        if self.val is None:
            return 0
        return 1 + max((self.left.height() if self.left else 0), (self.right.height() if self.right else 0))
        # max_height_l,max_height_r = 0,0
        # if not self.val:
        #     return 0
        # if self.left:
        #     max_height_l = self.left.height()
        # if self.right:
        #     max_height_r = self.right.height()
        # return max(max_height_l, max_height_r)+1
    
    
    def search_range(self, lower_bound, upper_bound):
        values = []

        if self is None:
            return values

        # Optimized traversal: Check bounds before recursing
        if self.val > lower_bound and self.left:
            values.extend(self.left.search_range(lower_bound, upper_bound))

        if lower_bound <= self.val <= upper_bound:
            values.append(self.val)

        if self.val < upper_bound and self.right:
            values.extend(self.right.search_range(lower_bound, upper_bound))

        return values
    

    # don't touch below this line

    def exists(self, val):
        if val == self.val:
            return True

        if val < self.val:
            if self.left is None:
                return False
            return self.left.exists(val)

        if self.right is None:
            return False
        return self.right.exists(val)

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