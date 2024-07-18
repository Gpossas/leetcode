# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        dummy = ListNode('dummy', head)

        ahead = dummy
        while ahead and n: # prevent iterate overflow if n > list length
            ahead = ahead.next
            n -= 1
        
        current = dummy
        while ahead and ahead.next:
            current = current.next
            ahead = ahead.next
        
        current.next = current.next.next
        return dummy.next