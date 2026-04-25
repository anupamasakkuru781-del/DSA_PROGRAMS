class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
# traversal functions
#indorder (left -> root -> right)
def inorder(root):
    if root:
        inorder(root.left)
        print(root.data, end = " ")
        inorder(root.right)

#preorder(root -> root -> right)
def preorder(root):
    if root:
        print(root.data, end= " ")
        preorder(root.left)
        preorder(root.right)

#postorder(left -> right -> root)
def postorder(root):
    if root:
        postorder(root.left)
        postorder(root.right)
        print(root.data, end = " ")

def main():
    #create nodes
    root = Node(1)
    root = Node(2)
    root = Node(3)
    root = Node(4)
    root = Node(5)

    # connecting nodes
    root.left = node2
    root.right = Node3

    node2.left = node4
    node2.right = node5

    print("Inorder Traversals: ")
    inorder(root)

    print("\nPostorder Traversal: ")
    preorder(root)

    print("\nPostorder Traversal: ")
    print(root)

main()
