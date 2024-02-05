class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:

        def searching(nums, target):
            length = len(nums)
            if length == 0:
                return -1
            if length == 1:
                if target <= nums[0]:
                    return 0
                else:
                    return 1
            
            if target < nums[0]:
                return 0
            elif target > nums[-1]:               return length

            mid = length//2
            l = searching(nums[:mid], target)
            r = searching(nums[mid:], target)
            print(l,r)
            if l != -1 and r != -1:
                print("in")
                return r+mid if l == mid else l
            elif l != -1:
                return l
            elif r != -1:
                return r+mid
            else:
                return mid+1
        return searching(nums, target)