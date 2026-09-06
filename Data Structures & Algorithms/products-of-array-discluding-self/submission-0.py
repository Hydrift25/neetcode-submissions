class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefixes = [0] * len(nums)
        suffixes = [0] * len(nums)
        product = 1
        for i in range(len(nums)):
            prefixes[i] = product
            product *= nums[i]
        product = 1
        for i in range(len(nums)):
            suffixes[-i-1] = product
            product *= nums[-i-1]
        ans = []
        for i in range(len(nums)):
            ans.append(prefixes[i] * suffixes[i])
        return ans            

