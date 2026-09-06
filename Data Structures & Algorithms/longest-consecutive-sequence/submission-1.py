class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numsSet = set(nums)
        max = 0
        for i in nums:
            if (i-1) not in numsSet:
                counter = 1
                while (i+counter) in numsSet:
                    counter += 1
                if counter > max:
                    max = counter
        return max
        