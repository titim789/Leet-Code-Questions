class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        ans = []
        length=len(candidates)
        def dfs(cur, cur_sum, idx):
            if cur_sum > target: return
            elif cur_sum == target:
                ans.append(cur)
                return
            for i in range(idx,length):
                dfs(cur+[candidates[i]], cur_sum + candidates[i], i)
        dfs([],0,0)
        return ans 

            