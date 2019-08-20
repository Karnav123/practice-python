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
    assert(p1 is True)
    assert(6 == height)


def main():
    test_find()
    print("Tests complete.")


if __name__ == "__main__":
    main()