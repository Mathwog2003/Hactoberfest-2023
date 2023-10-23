# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def mergeKLists(self, lists):
        q, h = len(lists), []
        for i in range(q):
            if lists[i]:
                heapq.heappush(h, (lists[i].val, i, lists[i]))
        
        rhead = rtail = ListNode(0)
        
        while h:
            i, n = heapq.heappop(h)[1:]
            rtail.next = n
            rtail = rtail.next
            if n.next:
                heapq.heappush(h, (n.next.val, i, n.next))
                
        return rhead.next
