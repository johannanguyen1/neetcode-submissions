# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        curr = head 
        prev = head
        d = []
        if curr != None: 
            curr = curr.next 
        else: 
            return False
        while curr != None: 
            d.append(curr.val)
            prev = curr
            curr = curr.next 
            if curr != None: 
                if curr.val in d: 
                    return True
            else: 
                return False
        return False
            
        