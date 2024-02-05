# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        
        def removeIt(head, n):
            if head == None:
                return -1
            i = removeIt(head.next, n) + 1
            if i == n:
                head.next = head.next.next
            return i
        t=removeIt(head, n)
        if t+1==n:
            head = head.next
        return head