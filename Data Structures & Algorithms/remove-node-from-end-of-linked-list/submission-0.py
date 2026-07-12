# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode()
        dummy.next = head

        slow = dummy 
        fast = dummy 

        for i in range(n):
            fast = fast.next
        
        prev = None 
        while fast != None:
            fast = fast.next
            prev = slow 
            slow = slow.next
        
        prev.next = prev.next.next

        return dummy.next