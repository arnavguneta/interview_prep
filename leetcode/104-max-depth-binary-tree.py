# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        depth = 0
        stack = [(root, 1)]
        while stack:
            cur_node, cur_depth = stack.pop()
            if cur_node:
                depth = max(depth, cur_depth)
                stack.append((cur_node.left,cur_depth+1))
                stack.append((cur_node.right,cur_depth+1))
        return depth

        