# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if root == None:
            return None
        if root.left == None and root.right == None:
            # leaf node
            return root
        newTree = TreeNode(root.val)
        newTree.left = self.invertTree(root.right)
        newTree.right = self.invertTree(root.left)
        return newTree
        