# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        ans_head = ListNode()
        current = ans_head
        while l1 != None or l2 != None:
            #If the next is filled means the previous digit was >= 10
            temp = current
            #if there are still digits in l1
            if l1 != None:
                temp.val += l1.val
            #if there are still digits in l2
            if l2 != None:
                temp.val += l2.val
            
            print(temp.val)
            #if the sum of the l1 and l2 digits >= 10
            if temp.val >= 10:
                temp.val -= 10
                temp_next = ListNode(1)
                temp.next = temp_next
            
            if l1 != None:
                l1 = l1.next
            if l2 != None:
                l2 = l2.next
            
            if l1 != None or l2 != None:
                if temp.next == None:
                    temp.next = ListNode()
                current = temp.next

            
        
        return ans_head