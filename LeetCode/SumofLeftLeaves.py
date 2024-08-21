# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:
        if not root :
            return 0
        def is_leaf(node) :
            return node and not node.left and not node.right
        
        total_sum = 0
        
        if root.left and is_leaf(root.left) :
            total_sum += root.left.val
        
        total_sum += self.sumOfLeftLeaves(root.left)
        total_sum += self.sumOfLeftLeaves(root.right)

        return total_sum
        