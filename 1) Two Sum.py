class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        length = len(nums)
        mem = {}
        for i in range(length):
            diff = target-nums[i]
            if nums[i] in mem:
                return [mem[nums[i]], i]
            else:
                mem[diff] = i
        
        return []