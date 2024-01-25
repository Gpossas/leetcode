class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower()
        left = 0
        right = len(s) - 1
        while left < right:
            while left < right and not s[left].isalnum():
                left += 1
            while left < right and not s[right].isalnum():
                right -= 1

            if s[left] != s[right]:
                return False
            
            left += 1
            right -= 1
        return True
    
class SolutionWithoutLibraries:
    def isPalindrome(self, s: str) -> bool:
        left, right = 0, len(s) - 1
        while left < right:
            while left < right and not self.is_alphanum(s[left]):
                left += 1
            while left < right and not self.is_alphanum(s[right]):
                right -= 1
                
            if not self.is_same(s[left], s[right]):
                return False
            
            left += 1
            right -= 1
        return True
    
    def is_alphanum(self, char):
        return (
            'a' <= char <= 'z' or
            'A' <= char <= 'Z' or
            '0' <= char <= '9'
        )

    def is_same(self, char1, char2) -> bool:
        "Ignore camelcase and return if 2 chars are the same"
        LETTER_CASE_VALUE = ord('a') - ord('A')
        if 'A' <= char1 <= 'Z':
            char1 = chr(ord(char1) + LETTER_CASE_VALUE)
        if 'A' <= char2 <= 'Z':
            char2 = chr(ord(char2) + LETTER_CASE_VALUE)
        return char1 == char2

# print(Solution().isPalindrome("0P"))
# print(SolutionWithoutLibraries().isPalindrome('Aa'))
print(SolutionWithoutLibraries().isPalindrome("A man, a plan, a canal: Panama"))