class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left = right = 0
        max_length = 0
        window = set()
        while right < len(s):
            if s[right] in window:
                window.remove(s[left])
                left += 1
            else:
                window.add(s[right])
                right += 1
                max_length = max(max_length, len(window))
        return max_length