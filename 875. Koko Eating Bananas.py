import math

class Solution:
    def minEatingSpeed(self, piles: list[int], h: int) -> int:
        min_k = 1
        max_k = max(piles)
        while min_k < max_k:
            k = (min_k + max_k) >> 1

            # too slow
            if self.hours_to_eat_all_bananas(k, piles) > h:
                # find a grater k in upper bound
                min_k = k + 1
            else:
                max_k = k
        return min_k
    
    def hours_to_eat_all_bananas(self, eating_speed, piles):
        hours = 0
        for bananas in piles:
            hours += math.ceil(bananas / eating_speed) 
        return hours


                    
                