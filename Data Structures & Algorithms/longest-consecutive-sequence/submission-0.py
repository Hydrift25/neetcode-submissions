class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numsSet = set(nums)
        starts = []
        max = 0
        for i in nums:
            if (i-1) not in numsSet:
                starts.append(i)
        for j in starts:
            k = j
            counter = 0
            while k in numsSet:
                counter += 1
                k += 1
            if counter > max:
                max = counter
        return max
        