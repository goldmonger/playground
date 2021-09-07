# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        # -------------------
        # l r root
        if(root == None):
            return []
        
        # first we need a traversed array
        traversed = []
        
        # cur node object
        cur = root
        
        # stack to store nodes to be visited while traversing
        stack = []
        
        stack.append(root)
        while(stack):
            cur = stack.pop()
            if(cur.left):
                stack.append(cur.left)
            if(cur.right):
                stack.append(cur.right)
            traversed.insert(0, cur.val)
            
        return traversed