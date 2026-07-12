# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        fast = head 
        slow = head
        mid = None

        while fast != None:
            if fast.next != None:
                fast = fast.next.next
            else:
                fast = fast.next
            
            mid = slow 
            slow = slow.next
        
        mid.next = None
    
        rev = slow
        prev = None

        while rev != None:
            nxt = rev.next
            rev.next = prev
            prev = rev
            rev = nxt
        
        curr1 = head 
        curr2 = prev

        dummy = ListNode()
        curr3 = dummy

        while curr1 != None and curr2 != None:
            nxt1 = curr1.next
            curr3.next = curr1 
            curr1 = nxt1
            curr3 = curr3.next

            nxt2 = curr2.next
            curr3.next = curr2 
            curr2 = nxt2
            curr3 = curr3.next

        if curr1 != None:
            curr3.next = curr1
        elif curr2 != None:
            curr3.next = curr2
        
