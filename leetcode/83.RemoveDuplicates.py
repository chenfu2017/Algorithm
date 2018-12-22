# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """

        cur = head

        while cur and cur.next:
            if cur.val == cur.next.val:
                cur.next = cur.next.next
            else:
                cur = cur.next
        return head

n1=ListNode(1)
n2=ListNode(2)
n3=ListNode(3)
n1.next=n2
n2.next=n3
head = Solution().deleteDuplicates(n1)
while head!=None:
    print(head.val,end='->')
    head=head.next