# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        s = set()
        p = head
        s.add(p.val)
        while p.next != None:
            q = p.next
            if q.val in s:
                p.next = p.next.next
                continue
            else:
                s.add(q.val)
            p = p.next
        return head


nd1 = ListNode(3)
nd2 = ListNode(2)
nd3 = ListNode(3)
nd4 = ListNode(4)
nd5= ListNode(4)
nd6 = ListNode(1)
nd7= ListNode(7)
nd8= ListNode(8)

nd1.next = nd2
nd2.next = nd3
nd3.next = nd4
nd4.next = nd5
nd5.next = nd6
nd6.next = nd7
nd7.next = nd8
head= Solution().deleteDuplicates(nd1)
while head!=None:
    print(head.val,end='->')
    head=head.next