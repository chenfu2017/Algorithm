# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        cur, prev = head, None
        while cur:
            cur.next, prev, cur = prev, cur, cur.next
        return prev


n = ListNode(0)
head = n
for i in range(1, 5):
    m = ListNode(i)
    n.next = m
    n = m
p = Solution().reverseList(head)

while p != None:
    print(p.val)
    p = p.next
