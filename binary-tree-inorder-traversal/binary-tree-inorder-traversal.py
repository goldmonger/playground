# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        
        # declaring an empy list for storing the traversal
        traversal = []
        
        # stack for storing the visited pending
        stack = []
        
        # current for storing root for each iteration
        cur = root
        
        while(cur != None or stack):
            # while the cur is not null or stack has variables to be processed run
            # the first loop outer boundary
            while(cur != None):
                # first add left and run till end
                # then outside the inner loop
                stack.append(cur)
                cur = cur.left
            # here the max left is reached from previous loop
            # so the right branch is unexplored and a stack is obtained
            # we pop the node from stack which will be the left most end leaf
            # and we add to traversal to mark as visited
            # then we change to cur.right and re run outer loop as stack has elements still left
            
            cur = stack.pop()
            traversal.append(cur.val)
            cur = cur.right
            
            
        
        return traversal
            