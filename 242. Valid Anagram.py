class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        char_map = {}
        for char in s:
            char_map[char] = char_map.get(char, 0) + 1
        
        for char in t:
            if char not in char_map or char_map[char] <= 0:
                return False
            char_map[char] -= 1
        return True

ALPHABET_LETTERS = 26
class SolutionNoMap:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        frequency = [0] * ALPHABET_LETTERS
        for char in s:
            frequency[ord(char) - ord('a')] += 1
        
        for char in t:
            frequency[ord(char) - ord('a')] -= 1
            if frequency[ord(char) - ord('a')] < 0:
                return False
        return True