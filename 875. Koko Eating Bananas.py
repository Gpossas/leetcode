import math


class Solution:
    def minEatingSpeed(self, piles: list[int], h: int) -> int:
        min_k = 1
        max_k = max(piles)
        while min_k < max_k:
            middle = (min_k + max_k) >> 1
            time_to_eat_all_bananas = self.get_bananas_hour(middle, piles)

            # too slow
            if time_to_eat_all_bananas > h:
                # find a grater k in upper bound
                min_k = middle + 1
            else:
                max_k = middle
        return min_k
    
    def get_bananas_hour(self, speed_to_eat_bananas, piles):
        hours = 0
        for bananas in piles:
            bananas_per_hour = math.ceil(bananas / speed_to_eat_bananas)
            hours += bananas_per_hour
        return hours