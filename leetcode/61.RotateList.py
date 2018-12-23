# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def rotateRight(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """

    def rotateRight(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        if not head:
            return None
        q = head
        i = 1
        while q.next != None:
            q = q.next
            i += 1
        q.next = head
        m = i - k % i
        if m!=i:
            while m > 0:
                q = q.next
                m -= 1
        head = q.next
        q.next = None
        return head

r = ListNode(0)
r2 =ListNode(1)
r3 =ListNode(2)
r.next =r2
r2.next=r3
q = Solution().rotateRight(r,2)
while q != None:
    print(q.val,end='->')
    q = q.next
