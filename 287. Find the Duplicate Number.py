class Solution:
    # imagine that the values are pigeons, we have n + 1 pigeons
    # imagine that the range [1,n] are the cages(pigeonholes), note that we not include index 0
    # if we have more pigeons than cages, one cage will have at least 2 pigeons, we have duplicate
    # then imagine that each num(pigeon) is the value of its cage, so its like the index where a pigeon should be
    # so if we follow each pigeon(array value) eventually we're going to see that 2 pigeons points to the same cage(array index)

    # if is verified that we have one repeated number, put two runners with different speeds and eventually they will colide in this loop
    # The cycle appears because nums contains duplicates. The duplicate node is a cycle entrance.
    # find cycle entrance like 'Linked List Cycle II'
    def findDuplicate(self, pigeons: list[int]) -> int:
        slow = fast = pigeons[0]
        while True:
            slow = pigeons[slow]
            fast = pigeons[pigeons[fast]]
            if slow == fast:
                break
        
        # find cycle entrance
        slow = pigeons[0]
        while slow != fast:
            slow = pigeons[slow]
            fast = pigeons[fast]
        return slow # the index is the duplicate value because we have multiple nodes pointing to, if we put nums[slow] it will point to next element