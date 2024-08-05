class Solution:
    def reverseWords(self, s: str) -> str:
        s = list(s)
        s = self.reverse_string(s, 0, len(s) - 1)
        s = self.reverse_words(s)
        s = self.trim_spaces(s)
        return ''.join(s)
        
    def reverse_string(self, s, left, right):
        while left < right:
            s[left], s[right] = s[right], s[left]
            left += 1
            right -= 1
        return s
    
    def reverse_words(self, s):
        length = len(s)
        start, end = 0, 0
        while end < length:
            while start < length and s[start] == ' ':
                start += 1
            
            end = start
            while end < length and s[end] != ' ':
                end += 1
            
            self.reverse_string(s, start, end - 1)
            start = end
        return s

    def trim_spaces(self, s):
        length = len(s)
        left, right = 0, 0
        while right < len(s):
            # find a new word/skip spaces
            while right < length and s[right] == ' ':
                right += 1
            
            # move the word to where are the blank spaces
            while right < length and s[right] != ' ':
                s[left], s[right] = s[right], s[left]
                left += 1
                right += 1

            # find a new word/skip spaces
            # we need that cuz we only add a blank space if we have another word after
            while right < length and s[right] == ' ':
                right += 1

            # add the single space
            if right < length:
                s[left] = ' '
                left += 1
                
        return s[:left]