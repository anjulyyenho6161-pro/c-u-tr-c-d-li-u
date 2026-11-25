class TreeNode:
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None
root=TreeNode('R')
NodeA=TreeNode('A')
NodeB=TreeNode('B')
NodeC=TreeNode('C')
NodeD=TreeNode('D')
NodeE=TreeNode('E')
NodeF=TreeNode('F')
NodeG=TreeNode('G')
root.left=NodeA
root.right=NodeB
NodeA.left=NodeC
NodeA.right=NodeD
NodeB.left=NodeE
NodeB.right=NodeF
NodeF.left=NodeG
def preOrderTraversal(node):
    if node is None:
        return
    print(node.data, end=", ")
    preOrderTraversal(node.left)
    preOrderTraversal(node.right)
def InOrderTraversal(node):
    if node is None:
        return
    InOrderTraversal(node.left)
    print(node.data, end=", ")
    InOrderTraversal(node.right)
def PostOrderTraversal(node):
    if node is None:
        return
    PostOrderTraversal(node.left)
    PostOrderTraversal(node.right)
    print(node.data, end=", ")
print("kết quả duyệt cây theo thứ tự trước: ")
preOrderTraversal(root)
print("\nkết quả duyệt cây theo thứ tự giữa: ")
InOrderTraversal(root)
print("\nkết quả duyệt cây theo thứ tự sau: ")
PostOrderTraversal(root)
