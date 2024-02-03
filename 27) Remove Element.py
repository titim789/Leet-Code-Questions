class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        i = c = 0
        l = len(nums)
        while c < l:
            if nums[i] == val:
                del nums[i]
            else:
                i += 1
            c += 1
        return i+1