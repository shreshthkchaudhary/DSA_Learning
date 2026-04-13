# Tree
class Node:
    def __init__(self, data):
        self.data=data      # Member Variable
        self.left=None      # Member Variable
        self.right=None     # Member Variable


# Binary Tree
    def __init__(self):
        self.root=None
    def insert(self,data):
        new_node=Node(data)

        #   for first Node
        if self.root==None:
            self.root=new_node
            return
        
        #   for Node after first Node
        queue=[]
        queue.append(root)
            while queue:
                temp = queue.pop(0)
                if temp.left==None:
                    temp.left=new_node
                    return
                elif temp.right==None:
                    temp.right=new_node
                    return
                else queue.append(temp.left)
        

        def insert(node, data):
            if node is None:
                return TreeNode(data)
            else:
                if data < node.data:
                    node.left = insert(node.left, data)
                elif data > node.data:
                    node.right = insert(node.right, data)
            return node