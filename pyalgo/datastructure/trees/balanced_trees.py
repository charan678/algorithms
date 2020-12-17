from pyalgo.datastructure.trees.tree import BSTree, Node

class BalancedTree(BSTree):
    def __init__(self):
        pass

    def balance(self, root):
        pass




if __name__ == "__main__":
    print("Balanced tree")
    tree = BalancedTree()
    tree = BSTree(Node(20))
    tree.create_node(Node(10))
    tree.create_node(Node(30))
    tree.create_node(Node(40))
    tree.create_node(Node(50))
    tree.create_node(Node(5))
    tree.balance(tree.rroot())