# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        tail = pre = cur = head
        while n > 1:
            tail = tail.next
            n = n - 1
        while tail.next != None:
            tail = tail.next
            pre = cur
            cur = pre.next
        if cur == head:
            if head.next == None:
                return []
            else:
                head = head.next
        pre.next = cur.next
        return head


l1 = ListNode(0)
l2 = ListNode(1)
l3 = ListNode(2)
l4 = ListNode(3)
l5 = ListNode(4)
l1.next = l2
l2.next = l3
l3.next = l4
l4.next = l5
head=Solution().removeNthFromEnd(l1, 3)
while(head!=None):
    print(head.val)
    head = head.next
