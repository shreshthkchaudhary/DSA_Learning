# Tree
class Node:
    def __init__(self, data):
        self.data=data
        self.left=None
        self.right=None


# Binary Tree
class Node:
    def __init__(self, data):
        self.data=data
        self.left=None
        self.right=None
    def __init__(self):
        self.root=None
    def insert(self,data):
        new_node=Node(data)
        if self.root==None:
            self.root=new_node
            return