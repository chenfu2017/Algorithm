# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        flag = False
        value = l1.val + l2.val
        if value > 9:
            c = ListNode(value - 10)
            flag = True
        else:
            c = ListNode(value)
        q = c
        while l1.next != None or l2.next != None:
            if l1.next == None:
                l1 = ListNode(0)
            else:
                l1 = l1.next
            if l2.next == None:
                l2 = ListNode(0)
            else:
                l2 = l2.next
            value = l1.val + l2.val
            if flag:
                value += 1
                flag = False
            if value > 9:
                p = ListNode(value - 10)
                flag = True
            else:
                p = ListNode(value)
            c.next = p
            c = p
        if flag:
            m = ListNode(1)
            c.next=m
        return q


a = ListNode(9)
b = ListNode(9)
c = ListNode(1)
a.next = b
# e = ListNode(5)
# f = ListNode(6)
# g = ListNode(4)
# e.next = f
# f.next = g
l = (Solution().addTwoNumbers(c, a))
while l != None:
    print(l.val)
    l = l.next
