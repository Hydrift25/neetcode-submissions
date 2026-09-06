class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        ans = []
        itemCounts = defaultdict(int)
        for num in nums:
            itemCounts[num] += 1
        buckets = [[] for _ in range(len(nums) + 1)]
        for num in itemCounts:
            buckets[itemCounts[num]].append(num)
        i = 0
        while i < len(buckets):
            for j in buckets[-i-1]:
                ans.append(j)
                if len(ans) >= k:
                    return ans
            i += 1
            