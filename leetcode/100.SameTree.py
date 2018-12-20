# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def isSameTree(self, p, q):
        """
        :type p: TreeNode
        :type q: TreeNode
        :rtype: bool
        """
        if (p is None and q is None):
            return True
        if (p is not None and q is not None):
            return p.val == q.val and self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)
        return False


n1 = TreeNode(0)
n2 = TreeNode(1)
n3 = TreeNode(2)
n1.left = n2
n1.right = n3
n4 = TreeNode(0)
n5 = TreeNode(1)
n6 = TreeNode(2)
n4.left = n5
n4.right = n6
print(Solution().isSameTree(n1, n4))
