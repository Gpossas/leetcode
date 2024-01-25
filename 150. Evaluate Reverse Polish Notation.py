import math
class Solution:
    def evalRPN(self, tokens: list[str]) -> int:
        digits = []
        operators = '+/*-'
        for token in tokens:
            if token not in operators:
                digits.append( int(token) )
            else:
                second = digits.pop()
                first = digits.pop()

                if token == '+':
                    digits.append(first + second)
                elif token == '-':
                    digits.append(first - second)
                elif token == '*':
                    digits.append(first * second)
                elif token == '/':
                    # // -> floor() the result. -6 // 4 -> -6 / 4 = -1.5 -> floor(-1.5) = -2
                    # int() or math.trunc -> truncates towards zero. -6 / 4 = -1.5 -> -1
                    digits.append(math.trunc(first / second))
        return digits[0]
    
Solution().evalRPN(["10","6","9","3","+","-11","*","/","*","17","+","5","+"])