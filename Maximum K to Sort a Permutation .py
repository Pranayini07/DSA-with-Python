class Solution:
    def sortPermutation(self, nums: List[int]) -> int:
        k = -1

        for i, num in enumerate(nums):
            if num != i:
                k &= num

        if k == -1:
            return 0
        return k
