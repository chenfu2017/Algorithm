# Definition for singly-linked list.
import heapq
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
    #     n = len(lists)
    #     if n==0:
    #         return None
    #     while n > 1 :
    #         k = (n + 1) // 2
    #         for i in range(n//2):
    #             lists[i] = self.mergeTwoLists(lists[i], lists[i + k])
    #         n = k
    #     return lists[0]
    #
    # def mergeTwoLists(self, l1, l2):
    #     """
    #     :type l1: ListNode
    #     :type l2: ListNode
    #     :rtype: ListNode
    #     """
    #     if l1==None and l2==None:
    #         return None
    #     if l2 == None:
    #         return l1
    #     if l1 ==None:
    #         return l2
    #     pre1= cur1 = l1
    #     pre2 = cur2 = l2
    #     while pre1!=None:
    #         cur1 = pre1.next
    #         cur2 = pre2.next
    #         if pre1.val >= pre2.val and (cur2==None or pre1.val < cur2.val):
    #             pre2.next = pre1
    #             pre2 = pre1
    #             pre1.next = cur2
    #             pre1 = cur1
    #         else:
    #             if pre2==l2 and pre1.val < pre2.val:
    #                 pre1.next = l2
    #                 l2 = pre1
    #                 pre1 = cur1
    #                 pre2 = l2
    #             else:
    #                 pre2 = pre2.next
    #     return l2
        if not len(lists):
            return None
        heap = []
        n = len(lists)
        for i in range(n):
            if lists[i] != None:
                heapq.heappush(heap, (lists[i].val, i))
        p = q = ListNode(-1)
        while len(heap) > 0:
            n = heapq.heappop(heap)
            value = n[0]
            index = n[1]
            r = ListNode(value)
            q.next = r
            q = r
            if lists[index].next != None:
                lists[index] = lists[index].next
                heapq.heappush(heap, (lists[index].val, index))
        return p.next

def show(head):
    while (head != None):
        print(head.val)
        head = head.next
l1 = ListNode(1)
l2 = ListNode(2)
l3 = ListNode(3)
l4 = ListNode(4)
l5 = ListNode(5)
l6 = ListNode(6)
l1.next = l2
l3.next = l4
l5.next = l6
list =[l1,l3,l5]
head = Solution().mergeKLists(list)
show(head)