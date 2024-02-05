class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        ans = []
        candidates.sort()
        length = len(candidates)
        def dfs(cur,cur_sum,idx):
            if cur_sum > target: return
            elif cur_sum == target:
                ans.append(cur)
                return
            else:
                for i in range(idx+1, length):
                    dfs(cur+[candidates[i]], cur_sum+candidates[i], i)
        dfs([],0,-1)
        res = []
        [res.append(x) for x in ans if x not in res]
        return res