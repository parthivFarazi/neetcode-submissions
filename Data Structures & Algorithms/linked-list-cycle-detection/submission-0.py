# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        fast = head
        slow = head

        while fast != None:
            if fast.next != None:
                fast = fast.next.next
            else:
                fast = fast.next
            
            slow = slow.next

            if fast == slow and fast != None:
                return True
        return False