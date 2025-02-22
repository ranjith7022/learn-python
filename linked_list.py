from node import Node


class LinkedList:
    def add_to_head(self, node):
        if self.head == None:
            self.head = node
            return
        
        self.head,self.head.next = node,self.head
        # temp = self.head
        # self.head = node
        # self.head.next = temp       
        
             

    # don't touch below this line

    def add_to_tail(self, node):
        if self.head is None:
            self.head = node
            return
        last_node = None
        for current_node in self:
            last_node = current_node
        last_node.set_next(node)

    def __init__(self):
        self.head = None

    def __iter__(self):
        node = self.head
        while node is not None:
            yield node
            node = node.next

    def __repr__(self):
        nodes = []
        for node in self:
            nodes.append(node.val)
        return " -> ".join(nodes)