class Solution:
    def generateParenthesis(self, n: int) -> list[str]:
        result = []
        self.backtracking(0, 0, [], n, result)
        return result
        
    
    def backtracking(self, open_parentheses, closed_parentheses, candidates, n, result):
        if len(candidates) == n * 2:
            candidate = ''.join(candidates)
            result.append(candidate)
            return
        
        if open_parentheses < n:
            candidates.append('(')
            self.backtracking(open_parentheses + 1, closed_parentheses, candidates, n, result)
            candidates.pop()
        if open_parentheses > closed_parentheses:
            candidates.append(')')
            self.backtracking(open_parentheses, closed_parentheses + 1, candidates, n, result)
            candidates.pop()

print(Solution().generateParenthesis(3))