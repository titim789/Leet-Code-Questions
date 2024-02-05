class Solution:
    def search(self, nums: List[int], target: int) -> int:
        if target < nums[0] and target > nums[-1]:
            return -1
        
        # finding lowest num
        low = 0
        for i in range(len(nums)-1):
            if nums[i] > nums[i+1]:
                low = i+1
                break
        
        if target == nums[low]:
            return low

        def findNum(nums,target):
            if len(nums) == 0:
                return -1
            if len(nums) == 1:
                if nums[0] == target:
                    return 0
                else:
                    return -1
            else:
                if nums[0] > target or nums[-1] < target:
                    return -1

            mid = len(nums)//2
            l = findNum(nums[:mid], target)
            r = findNum(nums[mid:], target)

            if l != -1:
                return l
            elif r != -1:
                return r+mid
            else:
                return r
        
        lhs = findNum(nums[:low], target)
        if findNum(nums[:low], target) != -1:
            return lhs
        else:
            rhs =  findNum(nums[low:], target)
            return rhs if rhs == -1 else rhs+low