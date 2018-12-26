# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def reverseKGroup(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        i = 0
        q = head
        while i<k:
            p = q.next
            p.next = q.next
            q.next = head
            head = q
            p = q
            i +=1
        return head

l1 = ListNode(1)
l2 = ListNode(2)
l3 = ListNode(3)
l4 = ListNode(4)
l5 = ListNode(5)
l6 = ListNode(6)
l1.next = l2
l2.next = l3
l3.next = l4
l4.next=l5
l5.next = l6
def show(head):
    while (head != None):
        print(head.val)
        head = head.next
head=Solution().reverseKGroup(l1,1)
show(head)


