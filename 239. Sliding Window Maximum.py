from collections import deque

class Solution:
    def maxSlidingWindow(self, nums: list[int], k: int) -> list[int]:
        max_elements_window = []
        queue = deque([])
        window_size = k - 1

        left = right = 0
        while right < len(nums):
            num = nums[right]
            max_in_window = nums[queue[0]] if queue else num

            if right - left == window_size:
                max_elements_window.append(max_elements_window if queue else num)

                if queue and queue[0] <= left:
                    queue.popleft()
                left += 1

            while queue and max_in_window < num:
                queue.popleft()
            queue.append(right)
            right += 1
        return max_elements_window


class Solution:
    def maxSlidingWindow(self, nums: list[int], k: int) -> list[int]:
        max_elements_window = []
        queue = deque([]) # store the postition(index) to invalidate numbers when left window

        for i in range(len(nums)):
            # remove unbound max
            if queue and queue[0] < i - k + 1:
                queue.popleft()

            # remove the last elements to maintain monotonically decreasing queue
            while queue and nums[queue[-1]] < nums[i]:
                queue.pop()

            queue.append(i)

            # add max when window in array bound
            if i - k + 1 >= 0:
                max_elements_window.append(nums[queue[0]])
            
        return max_elements_window