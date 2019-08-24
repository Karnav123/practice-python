class Node:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.val = key

    def get(self):
        return self.val

    def set(self, val):
        self.val = val

    def getchildren(self):
        children = []
        if self.left is not None:
            children.append(self.left)
        if self.right is not None:
            children.append(self.right)
        return children


class BinarySearchTree:
    """
        This is a class regarding binary search tree.
    """

    def __init__(self):
        self.root = None

    def setroot(self, val):
        self.root = Node(val)

    def insert(self, val):
        if self.root is None:
            self.setroot(val)
        else:
            self.insertnode(self.root, val)

    def insertnode(self, currentnode, val):
        if val <= currentnode.val:
            if currentnode.left:
                self.insertnode(currentnode.left, val)
            else:
                currentnode.left = Node(val)
        elif val > currentnode.val:
            if currentnode.right:
                self.insertnode(currentnode.right, val)
            else:
                currentnode.right = Node(val)

    def find(self, val):
        return self.findnode(self.root, val)

    def findnode(self, currentnode, val):
        if currentnode is None:
            return False
        elif val == currentnode.val:
            return True
        elif val < currentnode.val:
            return self.findnode(currentnode.left, val)
        else:
            return self.findnode(currentnode.right, val)

    def printinorder(self, currentnode):
        if currentnode is not None:
            self.printinorder(currentnode.left)
            print(currentnode.val)
            print(" ")
            self.printinorder(currentnode.right)

    def get_tree_height(self, currentroot):
        if currentroot is None:
            return 0
        else:
            left_height = self.get_tree_height(currentroot.left)
            right_height = self.get_tree_height(currentroot.right)

        return 1 + max(left_height, right_height)

    def get_inorder_successor(self, currentnode):
        if currentnode is None:
            return None
        elif currentnode.left is None:
            return currentnode
        else:
            return self.get_inorder_successor(currentnode.left)

    def is_bst_utils(self, currentroot, min_value, max_value):
        if currentroot.val < min_value or currentroot.val >= max_value:
            return False
        elif currentroot.left and not self.is_bst_utils(currentroot.left, min_value, currentroot.val):
            return False
        elif currentroot.right and not self.is_bst_utils(currentroot.right, currentroot.val, max_value):
            return False
        return True

    def is_bst(self, currentroot):
        return self.is_bst_utils(currentroot, float("-inf"), float("inf"))

    # O(n) Time complexity
    def delete_node(self, current_node, value):
        if current_node is None:
            return current_node
        if value < current_node.val:
            if current_node.left is not None:
                current_node.left = self.delete_node(current_node.left, value)
        elif value > current_node.val:
            if current_node.right is not None:
                current_node.right = self.delete_node(current_node.right, value)
        else:
            # if the node to be deleted is a leaf node or has 
            # only one child
            if current_node.left is None : 
                temp = current_node.right  
                current_node = None 
                return temp  
            elif current_node.right is None : 
                temp = current_node.left  
                current_node = None
                return temp 
            else:   # if the node to be deleted has 2 child
                temp_node = self.get_inorder_successor(current_node.right)
                current_node.val = temp_node.val
                current_node.right = self.delete_node(current_node.right, temp_node.val)

            return current_node

    def get_minimum(self, current_node):
        if current_node.left is None:
            return current_node.val
        return self.get_minimum(current_node.left)

    def get_maximum(self, current_node):
        if current_node.right is None:
            return current_node.val
        return self.get_maximum(current_node.right)
        


def get_test_graph_1():
    dg = BinarySearchTree()
    dg.insert(6)
    dg.insert(7)
    dg.insert(8)
    dg.insert(9)
    dg.insert(10)
    dg.insert(1)
    dg.insert(2)
    dg.insert(3)
    dg.insert(4)
    dg.insert(5)

    return dg


def test_find():
    dg1 = get_test_graph_1()
    p1 = dg1.find(5)
    height = dg1.get_tree_height(dg1.root)
    insucc = dg1.get_inorder_successor(dg1.root)
    isbst = dg1.is_bst(dg1.root)
    min = dg1.get_minimum(dg1.root)
    dg1.delete_node(dg1.root, 1)
    max = dg1.get_maximum(dg1.root)
    dg1.printinorder(dg1.root)
    print(isbst)
    print(insucc.val)
    assert(p1 is True)
    assert(6 == height)


def main():
    test_find()
    print("Tests complete.")


if __name__ == "__main__":
    main()