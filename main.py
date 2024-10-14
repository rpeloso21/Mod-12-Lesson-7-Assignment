class TreeNode:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None

class BinaryTree:
    def __init__(self):
        self.root = None
        self.queue = []


    def insert(self, key):
        new_node = TreeNode(key)
        if self.root == None:
            self.root = new_node
            self.queue.append(new_node)
            return
        
        front_node = self.queue[0]

        if front_node.left == None:
            front_node.left = new_node

        elif front_node.right == None:
            front_node.right = new_node
            self.queue.pop(0)

        self.queue.append(new_node)

    def in_order_traversal(self):
        self.in_order_traversal_recursive(self.root)
        print()

    def in_order_traversal_recursive(self, node):
        if node:
            self.in_order_traversal_recursive(node.left)
            print(node.key, end=" ")
            self.in_order_traversal_recursive(node.right)

    def pre_order_traversal(self):
        self.pre_order_traversal_recursive(self.root)
        print()

    def pre_order_traversal_recursive(self, node):
        if node:
            print(node.key, end=" ")
            self.pre_order_traversal_recursive(node.left)
            self.pre_order_traversal_recursive(node.right)
    
    def post_order_traversal(self):
        self.post_order_traversal_recursive(self.root)
        print()
    
    def post_order_traversal_recursive(self, node):
            self.pre_order_traversal_recursive(node.left)
            self.pre_order_traversal_recursive(node.right)        
            print(node.key, end=" ")
    


if __name__ == "__main__":

        
    tree = BinaryTree()
    tree.insert(50)
    tree.insert(30)
    tree.insert(70)
    tree.insert(40)
    tree.insert(20)
    tree.insert(60)
    tree.insert(80)

    print("In order traversal:")
    tree.in_order_traversal()

    print("Pre order traversal:")
    tree.pre_order_traversal()

    print("Post order traversal:")
    tree.post_order_traversal()

        
