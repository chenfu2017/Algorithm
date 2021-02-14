# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        if not head or not head.next:
            return head
        if head.val == head.next.val:
            while head and head.next and head.val == head.next.val:
                head = head.next
            return self.deleteDuplicates(head.next)
        else:
            head.next = self.deleteDuplicates(head.next)
            return head


nd1 = ListNode(1)
nd2 = ListNode(2)
nd3 = ListNode(2)
nd4 = ListNode(4)
nd1.next = nd2
nd2.next = nd3
nd3.next = nd4
head= Solution().deleteDuplicates(nd1)
while head!=None:
    print(head.val,end='->')
    head=head.next