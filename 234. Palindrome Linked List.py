# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head) -> bool:
        middle = self.find_middle_linked_list(head)
        right_head = self.reverse_linked_list(middle)
        result = self.is_palindrome(head, right_head)
        self.reverse_linked_list(right_head)
        return result
        
    def reverse_linked_list(self, head):
        prev = None
        current = head
        while current:
            next = current.next
            current.next = prev
            prev = current
            current = next
        return prev

    
    def find_middle_linked_list(self, head):
        slow = fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        return slow
    
    def is_palindrome(self, head, right_head):
        left, right = head, right_head
        while left and right:
            if left.val != right.val:
                return False
            left = left.next
            right = right.next
        return True