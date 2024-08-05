class Solution:
    def findRepeatedDnaSequences(self, s: str) -> list[str]:
        SEQUENCE_LENGTH = 10 - 1 # subtract 1 cuz we're using index
        left, right = 0, 0
        repeated_sequences = set()
        visited_sequences = set()

        while right < len(s):
            if right - left < SEQUENCE_LENGTH:
                right += 1
            else:
                subsequence = s[left:right + 1]
                if subsequence in visited_sequences:
                    repeated_sequences.add( subsequence )
                
                visited_sequences.add( subsequence )
                left += 1
            
        return repeated_sequences