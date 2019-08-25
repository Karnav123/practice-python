import queue

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

class BinaryTree:
    def __init__(self):
        self.root = None
    
    def set_root(self, val):
        self.root = Node(val)

    def insert(self, val):
        if self.root is None:
            self.set_root(val)
        else:
            self.insert_node(self.root, val)

    def insert_node(self, current_node, val):
        temp = current_node
        q = queue.Queue()
        q.put(temp)
        while not q.empty():
            node = q.get()
            if node.left is None:
                node.left = Node(val)
                break
            else:
                q.put(node.left)
            if node.right is None:
                node.right = Node(val)
                break
            else:
                q.put(node.right)

    def printinorder(self, currentnode):
        if currentnode is not None:
            self.printinorder(currentnode.left)
            print(currentnode.val)
            print(" ")
            self.printinorder(currentnode.right)

    def find(self, currentnode, val):
        if currentnode is None:
            return currentnode
        q = queue.Queue()
        q.put(currentnode)
        while not q.empty():
            temp_node = q.get()
            if temp_node.val == val:
                return temp_node
            if temp_node.left is not None:
                q.put(temp_node.left)
            if temp_node.right is not None:
                q.put(temp_node.right)



def get_test_btree_1():
    bt = BinaryTree()
    bt.insert(6)
    bt.insert(7)
    bt.insert(8)
    bt.insert(9)
    bt.insert(10)
    bt.insert(1)
    bt.insert(2)
    bt.insert(3)
    bt.insert(4)
    bt.insert(5)

    return bt


def test_find():
    bt1 = get_test_btree_1()
    bt1.printinorder(bt1.root)
    f = bt1.find(bt1.root, 2)
    print(f.val)


def main():
    test_find()
    print("Tests complete.")


if __name__ == "__main__":
    main()