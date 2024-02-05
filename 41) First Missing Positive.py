class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        nums = list(set(nums))
        nums.sort()
        c = 1
        for i in range(len(nums)):
            if nums[i] <= 0:
                continue
            elif c == nums[i]:
                c += 1
            else:
                return c
        return c   