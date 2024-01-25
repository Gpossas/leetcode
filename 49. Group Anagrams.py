class Solution:
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        anagrams = {}
        for string in strs:
            frequency = [0] * 26
            for char in string:
                frequency[ord(char) - ord('a')] += 1

            anagram = tuple(frequency)

            if not anagram in anagrams:
                anagrams[anagram] = []
            anagrams[anagram].append(string)
        return list(anagrams.values())