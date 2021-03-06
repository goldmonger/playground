# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        
        res = []
        
        def inorder(root, current_path, current_sum):
            if not root:
                return []
            if root.val+current_sum == targetSum and root.left == None and root.right == None:
                res.append(current_path.copy() + [root.val])
                return
            
            current_path.append(root.val)
            current_sum += root.val
            inorder(root.left, current_path, current_sum)
            inorder(root.right, current_path, current_sum)
            current_path.pop()
            
            
        inorder(root, [], 0)
        return res