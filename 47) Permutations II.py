class Solution(object):
    def permuteUnique(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        def backtrack(arr, ds, res, hashmap):
            if len(ds) == len(arr):
                if ds[:] not in res:
                    res.append(ds[:])
                return

            for i in range(len(arr)):
                if hashmap[i] == 1:
                    continue
                hashmap[i] = 1
                ds.append(arr[i])
                backtrack(arr, ds, res, hashmap)
                ds.pop()
                hashmap[i] = 0

        res = []
        hashmap = [0]*len(nums)
        backtrack(nums, [], res, hashmap)
        return res