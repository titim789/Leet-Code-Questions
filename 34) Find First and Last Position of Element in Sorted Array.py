class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        def findNum(nums, target):
            length = len(nums)
            if length == 0:
                return [-1,-1]
            if length == 1:
                if nums[0] == target:
                    return [0,0]
                else:
                    return [-1,-1]
            
            if target < nums[0] or target > nums[-1]:
                return [-1,-1]
            
            mid = length//2
            l = findNum(nums[:mid], target)
            r = findNum(nums[mid:], target)

            if l != [-1,-1] and r != [-1,-1]: #change here for findlast
                return [l[0],r[1]+mid]
            elif l != [-1,-1]:
                return l
            elif r != [-1,-1]:
                return [r[0]+mid, r[1]+mid]
            else:
                return [-1,-1]

        return findNum(nums,target)

        