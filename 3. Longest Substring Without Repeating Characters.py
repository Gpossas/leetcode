class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        window = set()
        max_substring = 0
        left = 0
        for right in range(len(s)):
            char = s[right]
            while char in window:
                window.remove(s[left])
                left += 1

            window.add(char)
            max_substring = max(max_substring, len(window))
        return max_substring