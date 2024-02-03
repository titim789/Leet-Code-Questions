class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        if len(nums) < 4:
            return []
        nums.sort()
        a = set()
        mx_3 = nums[-1] + nums[-2] + nums[-3]
        mx_2 = nums[-1] + nums[-2]
        for i in range(len(nums)):
            if (target-nums[i]) > mx_3:
                continue
            for j in range(i+1, len(nums)):
                if (target-nums[i]-nums[j]) > mx_2:
                    continue
                l = j+1
                r = len(nums)-1
                while l < r:
                    t = nums[i] + nums[j] + nums[l] + nums[r]
                    if t == target:
                        a.add((nums[i], nums[j], nums[l], nums[r]))
                        l += 1
                        r -= 1
                    elif t < target:
                        l += 1
                    else:
                        r -= 1
        a = list(a)
        
        
        return a