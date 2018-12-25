# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if not root:
            return []
        l =[root]
        res = [[root.val]]
        n = 2
        arr = []
        count = 0
        while len(l):
            count +=2
            node = l.pop(0)
            if node.left !=None:
                arr.append(node.left.val)
                l.append(node.left)
            if node.right!=None:
                arr.append(node.right.val)
                l.append(node.right)
            if count==n:
                if len(arr)>0:
                    res.append(arr)
                n = 2 * len(l)
                arr = []
                count = 0
        return res

root = TreeNode(3)
r1 = TreeNode(20)
r2 = TreeNode(15)
r3 = TreeNode(9)
r4 = TreeNode(7)
root.left = r3
root.right=r1
r1.left=r2
r1.right=r4

print(Solution().levelOrder(root))
