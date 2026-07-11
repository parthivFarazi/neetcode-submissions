# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:

        curr1 = list1
        curr2 = list2

        dummy = ListNode()
        curr3 = dummy 
        head = dummy

        while curr1 != None and curr2 != None:
            if curr1.val <= curr2.val:
                nxt = curr1
                curr3.next = nxt
                curr1 = curr1.next
                curr3 = curr3.next
            else:
                nxt = curr2
                curr3.next = nxt
                curr2 = curr2.next
                curr3 = curr3.next
        
        if curr1 == None:
            curr3.next = curr2
        else:
            curr3.next = curr1
        
        return dummy.next
        