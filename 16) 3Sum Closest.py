class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        closest = nums[0] + nums[1] + nums[2]
        nums.sort()

        for i in range(0,len(nums)-2):
            j = i+1
            k = len(nums)-1
            while j<k:
                tot = nums[i] + nums[j] + nums[k]
                if abs(tot-target) < abs(closest-target):
                    closest = tot
                if tot == target:
                    return target
                elif tot < target:
                    j+=1
                else:
                    k-=1
        return closest