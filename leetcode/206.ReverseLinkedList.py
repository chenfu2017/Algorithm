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
        pre = None
        cur = head
        while cur:
            temp = cur.next
            cur.next = pre
            pre = cur
            cur = temp
        return pre
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
