class Solution:
    def isValid(self, s: str) -> bool:
        if len(s) % 2 != 0:
            return False
        
        open_pair = []
        pair = {
            ')': '(',
            ']': '[',
            '}': '{'
        }
        for parentheses in s:
            if parentheses in pair: 
                if open_pair and open_pair[-1] == pair[parentheses]:
                    open_pair.pop()
                else:
                    return False
            else: 
                open_pair.append(parentheses)
        return True if len(open_pair) == 0 else False 