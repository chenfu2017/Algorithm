# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def hasCycle(self, head: ListNode) -> bool:
        if not head:
            return False
        fast = head.next
        slow = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                return True
        return False


nd1 = ListNode(3)
nd2 = ListNode(2)
nd3 = ListNode(0)
nd4 = ListNode(-4)
nd1.next = nd2
nd2.next = nd3
nd3.next = nd4
# nd4.next = nd2
print(Solution().hasCycle(nd1))
