class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        i = 0
        j = -1
        targetFound = False
        while not targetFound:
            sum = numbers[i] + numbers[j]
            if sum > target:
                j -= 1
            elif sum < target:
                i += 1
            else:
                targetFound = True
        return [i+1, j+1+len(numbers)]