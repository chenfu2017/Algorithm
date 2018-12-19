# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        if l1==None and l2==None:
            return None
        if l2 == None:
            return l1
        if l1 ==None:
            return l2
        pre1= cur1 = l1
        pre2 = cur2 = l2
        while pre1!=None:
            cur1 = pre1.next
            cur2 = pre2.next
            if pre1.val >= pre2.val and (cur2==None or pre1.val < cur2.val):
                pre2.next = pre1
                pre2 = pre1
                pre1.next = cur2
                pre1 = cur1
            else:
                if pre2==l2 and pre1.val < pre2.val:
                    pre1.next = l2
                    l2 = pre1
                    pre1 = cur1
                    pre2 = l2
                else:
                    pre2 = pre2.next
        return l2

def show(head):
    while (head != None):
        print(head.val)
        head = head.next
l1 = ListNode(1)
l2 = ListNode(2)
l3 = ListNode(4)
l4 = ListNode(1)
l5 = ListNode(3)
l6 = ListNode(5)
l1.next = l2
l2.next = l3
l4.next = l5
l5.next = l6
head = Solution().mergeTwoLists(l1,l6)
show(head)
