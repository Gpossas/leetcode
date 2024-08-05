class Solution:
    def isHappy(self, n: int) -> bool:
        fast = slow = n
        while True:
            slow = self.sum_squares_digits(slow)
            fast = self.sum_squares_digits(fast)
            fast = self.sum_squares_digits(fast)
            if fast == slow:
                break
        return True if fast == 1 else False

    def sum_squares_digits(self, n):
        sum_squares_digits = 0
        while n > 0:
            digit = n % 10
            sum_squares_digits += digit * digit
            n //= 10
        return sum_squares_digits