'''
@author: youxinyu
@date: 2018-8-30
'''

class Node:
    def __init__(self, data, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right

    def insert(self, data):
        if self.data == None:
            self.data = data

        if data <= self.data:
            if self.left != None:
                self.left.insert(data)
            else:
                self.left = Node(data)
        else:
            if self.right != None:
                self.right.insert(data)
            else:
                self.right = Node(data)

    def contains(self, data):
        if self.data == None:
            return False
        if self.data == data:
            return True
        
        if data <= self.data:
            if self.left != None:
                if self.left.data == data:
                    print('true')
                    print(data)
                    return True
                else:
                    return self.left.contains(data)
        else:
            if self.right != None:
                if self.right.data == data:
                    return True
                else:
                    return self.right.contains(data)

    def inOrderPrint(self):
        if self.data == None:
            print('None')
        else:
            if self.left != None: self.left.inOrderPrint()
            print(self.data)
            if self.right != None: self.right.inOrderPrint()
    
    def preOrderPrint(self):
        if self == None:
            print('None')
        else:
            print(self.data)
            if self.left != None: self.left.inOrderPrint()
            if self.right != None: self.right.inOrderPrint()
    
    def postOrderPrint(self):
        if self == None:
            print('None')
        else:
            if self.left != None: self.left.inOrderPrint()
            if self.right != None: self.right.inOrderPrint()
            print(self.data)

def main():
    bst = Node(1)
    bst.insert(10)
    bst.insert(5)
    bst.insert(7)
    # print(bst.contains(5))
    bst.inOrderPrint()

if __name__ == '__main__':
    main()

