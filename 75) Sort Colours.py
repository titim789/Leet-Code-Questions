class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        def rotBetweenTwoIndex(nums, start, end):
            temp = nums[end]
            for i in range(end-1, start-1, -1):
                nums[i+1] = nums[i]
            nums[start] = temp
            return nums

        pointers = [None, None] # 0:red; 1:white;

        i = 0

        while i < len(nums):
            if nums[i] == 0: #red
                if not pointers[0]:
                    pointers[0] = 0
                    nums = rotBetweenTwoIndex(nums, 0, i)
                else:
                    pointers[0] += 1
                    nums = rotBetweenTwoIndex(nums, pointers[0], i)
                pointers[1] = pointers[1]+1 if pointers[1] else pointers[0]+1
            elif nums[i] == 1: #white
                if not pointers[1]:
                    pointers[1] = 0
                    nums = rotBetweenTwoIndex(nums, 0, i)
                else:
                    nums = rotBetweenTwoIndex(nums, pointers[1], i)
                    pointers[1] += 1

            i += 1


        