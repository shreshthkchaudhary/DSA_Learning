# User define datatype
# linkdlist

class node:
    def __init__(self, data):
        self.data=data
        self.next=None
        

a1=node("hi")
print(a1.data)
