class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        numsSet = {}
        for i in range(len(nums)):
            diff = target - nums[i]
            if diff in numsSet:
                if i < numsSet[diff]:
                    return [i, numsSet[diff]]
                else:
                    return [numsSet[diff], i]
            numsSet[nums[i]] = i
