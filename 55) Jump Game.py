class Solution:
    def canJump(self, nums: List[int]) -> bool:
        cap = 0
        for i in nums:
            if cap < 0:
                return False
            elif i > cap:
                cap = i
            cap -= 1
        return True
        