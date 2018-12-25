# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def zigzagLevelOrder(self, root):
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
        flag = True
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
                    if flag:
                        arr.reverse()
                    res.append(arr)
                    flag =not flag
                n = 2 * len(l)
                arr = []
                count = 0
        return res

root = TreeNode(1)
r1 = TreeNode(2)
r2 = TreeNode(3)
r3 = TreeNode(4)
r4 = TreeNode(5)
root.left = r1
root.right=r2
r2.left=r3
r2.right=r4

print(Solution().zigzagLevelOrder(root))
