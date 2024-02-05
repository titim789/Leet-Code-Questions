# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        end = ListNode()
        def getLength(curr):
            count = 0
            while curr != None:
                count += 1
                bef = curr
                curr = curr.next
            if count == 0:
                return 0    
            bef.next = head
            return count
        
        length = getLength(head)
        if length == 0: return None
        rot = k % length
        count = length-rot
        curr = head
        print(length, rot)
        while count > 1:
            print(curr.val)
            curr = curr.next
            count -= 1
        head = curr.next
        curr.next = None
        
        return head

        