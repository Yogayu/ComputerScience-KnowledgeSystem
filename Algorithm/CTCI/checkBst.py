'''
@func: count the brace string's valid pair
@author: youxinyu
@date: 2018-09-08
'''
from binarySearchTree import Node

class CheckBST:
    def __init__(self, node):
        self.node = node
    
    def checkBST(self):
        
        MIN = float("-inf") # -∞
        MAX = float("inf")  # +∞
        return self._checkBST(self.node, MIN, MAX)
    
    def _checkBST(self, node, min, max):
        if node == None:
            return True
        if node.data < min or self.node.data > max:
            return False
        return self._checkBST(node.left, min, node.data-1) and self._checkBST(node.right, node.data+1, max)

def main():
    bst = Node(1)
    bst.insert(10)
    bst.insert(5)
    bst.insert(7)

    check = CheckBST(bst).checkBST()
    print(check)

if __name__ == '__main__':
    main()
