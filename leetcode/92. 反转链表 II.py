# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def reverseBetween(self, head: ListNode, left: int, right: int) -> ListNode:
        leftnode = rightnode = head
        while right > 0:
            rightnode = rightnode.next
            print(rightnode.val)
            right -=1
            if left > 0:
                leftnode = leftnode.next
                print(leftnode.val)
                left -=1

head =p= ListNode(1)
for i in range(2,6):
    new = ListNode(i)
    p.next = new
    p = p.next

m = 2
n = 3
print(Solution().reverseBetween(head,m,n))
# while head != None:
#     print(head.val,"->",end='')
#     head = head.next