from typing import List


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:

    def pathSum(self, root: TreeNode, targetSum: int) -> List[List[int]]:
        def dfs(node, sum, l):
            if node is None:
                return
            sum += node.val
            l.append(node.val)
            if node.left is None and node.right is None and sum == targetSum:
                ans.append(l.copy())
            dfs(node.left, sum , l)
            dfs(node.right, sum, l)
            sum -= node.val
            l.pop()
        ans = []
        dfs(root, 0, [])
        return ans

t1 = TreeNode(1)
t2 = TreeNode(2)
t3 = TreeNode(3)
t1.left = t2
t1.right = t3
print(Solution().pathSum(t1, 3))
