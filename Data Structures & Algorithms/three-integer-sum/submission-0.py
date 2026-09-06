class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        sortednums = sorted(nums)
        res = []
        for i in range(len(sortednums)):
            j = i + 1
            k = len(sortednums) - 1
            target = -sortednums[i]
            while j < k:
                if sortednums[j] + sortednums[k] < target:
                    j += 1
                elif sortednums[j] + sortednums[k] > target:
                    k -=1
                else:
                    if [sortednums[i], sortednums[j], sortednums[k]] not in res:
                        res.append([sortednums[i], sortednums[j], sortednums[k]])
                    while j < k and sortednums[j] == sortednums[j+1]:
                        j += 1
                    while j < k and sortednums[k] == sortednums[k-1]:
                        k -= 1
                    j += 1
                    k -= 1
        return res