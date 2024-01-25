import heapq
class SolutionMaxHeap:
    def topKFrequent(self, nums: list[int], k: int) -> list[int]:
        # O(N)
        frequency = {}
        for num in nums:
            frequency[num] = frequency.get(num, 0) + 1

        # O(N), N is the number of different numbers
        max_heap = [(-val, key) for key, val in frequency.items()]
        heapq.heapify(max_heap)

        # O(K log N) -> popping k times from a heap of size N
        result = []
        while k:
            result.append(heapq.heappop(max_heap)[1])
            k -= 1
        return result

class SolutionMinHeap:
    def topKFrequent(self, nums: list[int], k: int) -> list[int]:
        # O(N)
        frequency = {}
        for num in nums:
            frequency[num] = frequency.get(num, 0) + 1
        
        # O(N log K)
        min_heap = []
        for key, priority in frequency.items():
            if len(min_heap) < k:
                heapq.heappush(min_heap, (priority, key))
            elif priority > min_heap[0][0]:
                heapq.heappushpop(min_heap, (priority, key))
        
        return [value for priority, value in min_heap]

class SolutionBucketSort:
    def topKFrequent(self, nums: list[int], k: int) -> list[int]:
        # O(N)
        frequency = {}
        max_frequency = 0
        for num in nums:
            frequency[num] = frequency.get(num, 0) + 1
            max_frequency = max(max_frequency, frequency[num])
        
        # index: frequency
        # value: list of values with frequency = index
        count = [[] for _ in range(max_frequency + 1)]
        for key, freq in frequency.items():
            count[freq].append(key)

        # O(k)
        result = []
        for items in reversed(count):
            for item in items:
                result.append(item)
                k -= 1
                if not k: return result

class SolutionQuickSelect:
    def topKFrequent(self, nums: list[int], k: int) -> list[int]:
        # O(N)
        frequency = {}
        for num in nums:
            frequency[num] = frequency.get(num, 0) + 1
        
        values = [key for key in frequency]
        return self.quick_select(values, k, frequency)

    def quick_select(self, A, k, frequency): 
        left, right = 0, len(A) - 1  
        while left < right:
            partition_index = self.partition(left, right, A, frequency)
            if partition_index < k:
                left = partition_index - 1
            elif partition_index + 1:
                right = partition_index + 1
            else:
                return A[k:]

    def partition(self, left, right, nums, frequency):
        # TODO: PROBLEM WITH FREQUENCY KEY == 0
        pivot = frequency[right]
        pivot_index = left
        while left < right:
            while left < right and frequency.get(right, 0) > pivot:
                right -= 1
            while left < right and frequency.get(left, pivot+1) <= pivot:
                left += 1
            nums[right], nums[left] = nums[left], nums[right]
        nums[left], nums[pivot_index] = nums[pivot_index], nums[left]
        return right
    
print(SolutionMaxHeap().topKFrequent([1,1,1,2,2,3], 2))
print(SolutionMinHeap().topKFrequent([1,1,1,2,2,3], 2))
print(SolutionBucketSort().topKFrequent([1,1,1,2,2,3,7,7], 3))
print(SolutionQuickSelect().topKFrequent([1,1,1,2,2,3,7,7], 3))