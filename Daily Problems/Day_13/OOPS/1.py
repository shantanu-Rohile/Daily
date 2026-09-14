# 5. Binary Search Tree Class

class Node:
    def __init__(self,value):
        self.value=value
        self.left = None
        self.right=None
    def __str__(self):
        return str(self.value)


class BST:
    def __init__(self):
        self.root =None

    def insert(self,value):
        if self.root is None:
            self.root = Node(value)
        else:
            return self._insert_recursive(self.root,value)
    def _insert_recursive(self,node,value):
        if value < node.value:
            if node.left is None:
                node.left = Node(value)
            else:
                return self._insert_recursive(node.left,value)
        elif value > node.value:
            if node.right is None:
                node.right = Node(value)
            else:
                return self._insert_recursive(node.right,value)
    def search(self,value):
        return self._search_recursiv(self.root,value)
    def _search_recursiv(self,node,value):
        if node is None:
            return False
        else:
            if node.value == value:
                return True
            if value < node.value:
                return self._search_recursiv(node.left,value)
            else:
                return self._search_recursiv(node.right,value) 


bst = BST()

bst.insert(5)
bst.insert(3)
bst.insert(7)
bst.insert(2)
bst.insert(4)
bst.insert(6)
bst.insert(8)

print(bst.search(100))