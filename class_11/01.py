# Tree
class Node:
    def __init__(self, data):
        self.data=data
        self.left=None
        self.right=None


# Binary Tree
class Node:
    def __init__(self, data):
        self.data=data      # Member Variable
        self.left=None      # Member Variable
        self.right=None     # Member Variable
    def __init__(self):
        self.root=None
    def insert(self,data):
        new_node=Node(data)

        #   for first Node
        if self.root==None:
            self.root=new_node
            return
        