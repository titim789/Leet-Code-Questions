# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        s=c=ListNode()
        e = []
        for i in range(len(lists)-1, -1, -1):
            if lists[i] == None:
                del lists[i]     
            
        if lists == []:
            return None
        
        def getMinIndex(lists):
            mn = mi = 10**4 + 1
            for i in range(len(lists)):
                if lists[i].val < mn:
                    mn = lists[i].val
                    mi = i
            return mi
                  
        while lists != []:
            ci = getMinIndex(lists)
            c.next = lists[ci]
            
            c = c.next
            
            lists[ci] = lists[ci].next
            
            if lists[ci] == None:
                del lists[ci]
        
        return s.next
                