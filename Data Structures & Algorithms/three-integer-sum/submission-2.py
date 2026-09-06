class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        sortednums = sorted(nums)
        res = []
        for i, a in enumerate(sortednums):
            if a > 0:
                break
            if i > 0 and a == sortednums[i-1]:
                continue
            j = i + 1
            k = len(sortednums) - 1
            target = -sortednums[i]
            while j < k:
                if sortednums[j] + sortednums[k] < target:
                    j += 1
                elif sortednums[j] + sortednums[k] > target:
                    k -=1
                else:
                    res.append([a, sortednums[j], sortednums[k]])
                    j += 1
                    k -= 1
                    while j < k and sortednums[j] == sortednums[j-1]:
                        j += 1
        return res