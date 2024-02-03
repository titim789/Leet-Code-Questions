class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        c= i = 0
        l = len(nums)
        while c < l-1:
            if nums[i] == nums[i+1]:
                del nums[i]
            else:
                i += 1
            c += 1
        return len(nums)