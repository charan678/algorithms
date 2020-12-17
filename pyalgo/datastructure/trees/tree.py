from pyalgo.datastructure.trees.node import Node

class BSTree:
    def __init__(self, node):
        self.root = node

    @property
    def rroot(self):
        return self.root

    def _add_node(self, root, new_node):
        if not root:
            return new_node
        if root.info > new_node.info:
            root.left = self._add_node(root.left, new_node)
        else:
            root.right = self._add_node(root.right, new_node)
        return root

    def create_node(self, node):
        return self._add_node(self.root, node)

    def pre_order(self, root, output=[]):
        if not root:
            return
        output.append(root.info)
        self.post_order(root.left, output)
        self.post_order(root.right, output)
        return output

    def in_order(self, root, output=[]):
        if not root:
            return
        self.post_order(root.left, output)
        output.append(root.info)
        self.post_order(root.right, output)
        return output

    def post_order(self, root, output=[]):
        if not root:
            return
        self.post_order(root.left, output)
        self.post_order(root.right, output)
        output.append(root.info)
        return output

    def traversal(self, order):
        traversal_path = []
        if order == 1:
            traversal_path = self.pre_order(self.root)
        if order == 2:
            traversal_path = self.in_order(self.root)
        if order == 3:
            traversal_path = self.post_order(self.root)
        return traversal_path

    def depth(self, root, max_val=0, index=0):
        if not root:
            return max_val
        max_val = max(max_val, index)
        max1 = self.depth(root.left,  max_val, index+1)
        max2 = self.depth(root.right, max_val, index+1)
        max_val = max(max1, max2)
        return max_val

    def traversal_level(self):
        queue = [self.root]
        while len(queue) != 0:
            node = queue[0]
            queue = queue[1:]
            if node.left != None:
                queue.append(node.left)
            if node.right != None:
                queue.append(node.right)
            print(node.info)

if __name__ == "__main__":
    tree = BSTree(Node(20))
    tree.create_node(Node(10))
    tree.create_node(Node(30))
    tree.create_node(Node(40))
    tree.create_node(Node(50))
    tree.create_node(Node(5))
    #print(tree.traversal(3))
    #print(tree.depth(tree.rroot))
    print(tree.traversal_level())
