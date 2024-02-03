class Solution:
    def jump(self, nums: List[int]) -> int:
        def getMax(interval):
            maxIdx = maxJump = 0
            for i in range(len(interval)):
                if interval[i] + i > maxJump:
                    maxIdx = i
                    maxJump = interval[i] + i
            return maxIdx

        idx = 0
        jumps = 0
        while idx < len(nums):
            if nums[idx] == 0 or len(nums) == 1:
                break
            if nums[idx]+idx >= len(nums)-1:
                jumps += 1
                break
            else:
                jump = nums[idx]+idx
            goto = getMax(nums[idx+1:jump+1]) + 1
            idx += goto
            jumps += 1
        
        return jumps
            