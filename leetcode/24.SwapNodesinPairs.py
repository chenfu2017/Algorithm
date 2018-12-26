# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def swapPairs(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head or not head.next:
            return head
        p1= head
        r = p1.next
        while p1 and p1.next:
            p2= p1.next
            p3 =p2.next
            if p3:
                p1.next = [p3,p3.next][p3.next!=None]
            else:
                p1.next=None
            p2.next = p1
            p1 = p3
        return r


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
head = Solution().swapPairs(l1)
show(head)
