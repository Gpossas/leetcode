class Solution:
    def validPalindrome(self, s: str) -> bool:
        left, right = 0, len(s) - 1
        while left < right:
            if s[left] != s[right]:
                # check if left or right substring are palindromes
                return self.is_palindrome(s, left + 1, right) or self.is_palindrome(s, left, right - 1)
            
            left += 1
            right -= 1
        return True
    
    def is_palindrome(self, s, left, right):
        while left < right:
            if s[left] != s[right]:
                return False

            left += 1
            right -= 1
        return True
    
class Solution:
    def validPalindrome(self, s: str) -> bool:
        left, right = 0, len(s) - 1
        deleted = False
        while left < right:
            if s[left] != s[right]:
                if not deleted:
                    if s[left + 1] == s[right]:
                        left += 1
                    else:
                        right -= 1
                    deleted = True
                    continue
                return False
            
            left += 1
            right -= 1
        return True
    

print(Solution().validPalindrome("aguokepatgbnvfqmgmlcupuufxoohdfpgjdmysgvhmvffcnqxjjxqncffvmhvgsymdjgpfdhooxfuupuculmgmqfvnbgtapekouga"))