class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        products = [0] * n
        prefix = 1
        for i in range(n):
            products[i] = prefix
            prefix *= nums[i]
        suffix = 1
        for i in range(n):
            products[-i-1] *= suffix
            suffix *= nums[-i-1]
        return products            

