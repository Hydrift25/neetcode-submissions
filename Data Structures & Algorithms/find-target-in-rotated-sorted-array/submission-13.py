class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums)-1
        while l < r:
            p = l + (r - l) // 2
            if nums[p] > nums[r]:
                l = p + 1
            else:
                r = p
        p = l
        
        def binary_search(left, right):
            while left <= right:
                m = left + (right - left) // 2
                if target == nums[m]:
                    return m
                elif target < nums[m]:
                    right = m - 1
                else:
                    left = m + 1
            return -1
        
        res = binary_search(0, p-1)
        if res != -1:
            return res
        return binary_search(p, len(nums)-1)