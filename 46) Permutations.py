class Solution(object):
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        ans = []
        length = len(nums)
        def dfs(cur, idx_left):
            # print(cur, idx_left)
            if len(cur) == length:
                ans.append(cur)
                return
            for i in idx_left:
                # print(i, nums[i])
                j = idx_left.index(i)
                dfs(cur+[nums[i]], idx_left[:j]+idx_left[j+1:])

        dfs([],range(length))
        return ans