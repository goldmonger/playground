# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    
    def matchTrees(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if(root == None and subRoot == None):
            return True
        if((root == None or subRoot == None) or (root.val != subRoot.val)):
            return False
        return (self.matchTrees(root.left, subRoot.left) and self.matchTrees(root.right, subRoot.right))
        
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        qu = []
        #print(root)
        qu.append(root)
        while(qu):
            cur = qu.pop(0)
            print(cur.val)
            if cur.val == subRoot.val and self.matchTrees(cur, subRoot):
                #call matcher function here
                print(cur.val)
                return True
            if(cur.right != None):
                qu.append(cur.right)
            if(cur.left != None):
                qu.append(cur.left)
        return False
        
       
        